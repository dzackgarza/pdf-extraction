sample_md := "fixtures/lorem.md"
sample_pdf := "artifacts/lorem.pdf"
docling_dir := "outputs/docling"
mineru_dir := "outputs/mineru"
jobs_dir := "outputs/jobs"
experiments_dir := "outputs/experiments"
sterk_pdf := "/home/dzack/pdfs/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms.pdf"
venv_bin := ".venv/bin"
default_batch_size := "120"
default_heartbeat := "10"

default:
  @just --list

sync:
  uv sync

lorem-pdf pages='1' output='artifacts/lorem.pdf': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pages="{{pages}}"
  output="{{output}}"
  mkdir -p "$(dirname "$output")"
  tmp_md="$(mktemp --suffix=.md)"
  trap 'rm -f "$tmp_md"' EXIT
  for page in $(seq 1 "$pages"); do
    printf '# Synthetic Page %s\n\n' "$page" >> "$tmp_md"
    cat "{{sample_md}}" >> "$tmp_md"
    if [ "$page" -lt "$pages" ]; then
      printf '\n\n\\newpage\n\n' >> "$tmp_md"
    fi
  done
  export PATH="$(pwd)/{{venv_bin}}:$PATH"
  pandoc "$tmp_md" --from markdown --standalone --pdf-engine=pdflatex --output "$output"
  test -s "$output"

sample-pdf:
  just lorem-pdf 1 "{{sample_pdf}}"

docling: sample-pdf
  #!/usr/bin/env bash
  set -euxo pipefail
  mkdir -p "{{docling_dir}}"
  "{{venv_bin}}/docling" "{{sample_pdf}}" --to md --no-ocr --output "{{docling_dir}}"
  docling_md="$(find "{{docling_dir}}" -name 'lorem*.md' -print -quit)"
  test -n "$docling_md"
  grep -qi "lorem ipsum" "$docling_md"

mineru: sample-pdf
  #!/usr/bin/env bash
  set -euxo pipefail
  mkdir -p "{{mineru_dir}}"
  MINERU_MODEL_SOURCE=huggingface "{{venv_bin}}/mineru" \
    -p "{{sample_pdf}}" \
    -o "{{mineru_dir}}" \
    -b pipeline \
    -m txt \
    -d cpu \
    -f false \
    -t false
  mineru_md="$(find "{{mineru_dir}}" -name 'lorem*.md' -print -quit)"
  test -n "$mineru_md"
  grep -qi "lorem ipsum" "$mineru_md"

smoke: docling mineru

extract-pdf pdf batch_size=default_batch_size method='auto' lang='en' heartbeat=default_heartbeat:
  just mineru-batched "{{pdf}}" "{{batch_size}}" "{{method}}" "{{lang}}" "{{heartbeat}}" 1 1

launch-extract-pdf pdf batch_size=default_batch_size method='auto' lang='en' heartbeat=default_heartbeat:
  just launch-mineru-batched "{{pdf}}" "{{batch_size}}" "{{method}}" "{{lang}}" "{{heartbeat}}" 1 1

resume-extract job_dir heartbeat=default_heartbeat:
  just resume-mineru-batched "{{job_dir}}" "{{heartbeat}}"

extract-status job_dir:
  #!/usr/bin/env bash
  set -euxo pipefail
  job_dir="{{job_dir}}"
  status_path="$job_dir/status.json"
  manifest_path="$job_dir/manifest.json"
  test -f "$status_path"
  jq '{phase, completed_batches, batch_count, pending_batches, current_batch, peak_rss_mb, failure}' "$status_path"
  if [ -f "$manifest_path" ]; then
    printf '\n'
    jq '{status, batch_size, page_count, selected_start_page, selected_end_page, completed_batches, pending_batches, peak_rss_mb, combined_markdown}' "$manifest_path"
  fi
  if [ -f "$job_dir/pid" ]; then
    printf '\npid=%s\n' "$(cat "$job_dir/pid")"
  fi
  printf 'job_dir=%s\n' "$job_dir"
  printf 'run_log=%s\n' "$job_dir/run.log"

extract-tail job_dir lines='40':
  #!/usr/bin/env bash
  set -euxo pipefail
  job_dir="{{job_dir}}"
  lines="{{lines}}"
  status_path="$job_dir/status.json"
  test -f "$status_path"
  batch_tag="$(jq -r '.current_batch.batch_tag // empty' "$status_path")"
  if [ -n "$batch_tag" ] && [ -d "$job_dir/batches/$batch_tag" ]; then
    attempt_dir="$(find "$job_dir/batches/$batch_tag" -mindepth 1 -maxdepth 1 -type d -name 'attempt-*' | sort | tail -n 1)"
    if [ -n "$attempt_dir" ] && [ -f "$attempt_dir/worker.log" ]; then
      tail -n "$lines" "$attempt_dir/worker.log"
      exit 0
    fi
  fi
  tail -n "$lines" "$job_dir/run.log"

extract-progress job_dir lines='20':
  #!/usr/bin/env bash
  set -euxo pipefail
  job_dir="{{job_dir}}"
  lines="{{lines}}"
  status_path="$job_dir/status.json"
  test -f "$status_path"
  batch_tag="$(jq -r '.current_batch.batch_tag // empty' "$status_path")"
  test -n "$batch_tag"
  attempt_dir="$(find "$job_dir/batches/$batch_tag" -mindepth 1 -maxdepth 1 -type d -name 'attempt-*' | sort | tail -n 1)"
  test -n "$attempt_dir"
  progress_log="$attempt_dir/progress.jsonl"
  test -f "$progress_log"
  tail -n "$lines" "$progress_log"

extract-markdown-path job_dir:
  #!/usr/bin/env bash
  set -euxo pipefail
  jq -r '.combined_markdown' "{{job_dir}}/manifest.json"

extract-stop job_dir signal='TERM':
  #!/usr/bin/env bash
  set -euxo pipefail
  pid_path="{{job_dir}}/pid"
  test -f "$pid_path"
  pid="$(cat "$pid_path")"
  kill -s "{{signal}}" "$pid"
  printf 'pid=%s\n' "$pid"

mineru-batched pdf batch_size method='auto' lang='en' heartbeat='10' render_threads='1' min_inference_batch='1': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pdf="{{pdf}}"
  stem="$(basename "$pdf")"
  stem="${stem%.*}"
  slug="$(printf '%s' "$stem" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-')"
  slug="${slug#-}"
  slug="${slug%-}"
  ts="$(date -u +%Y%m%dT%H%M%SZ)"
  job_dir="{{jobs_dir}}/${slug}-mineru-${ts}"
  mkdir -p "$job_dir"
  cmd=( "{{venv_bin}}/python" scripts/run_mineru_batched.py \
    --pdf "$pdf" \
    --job-dir "$job_dir" \
    --method "{{method}}" \
    --batch-size "{{batch_size}}" \
    --lang "{{lang}}" \
    --heartbeat-seconds "{{heartbeat}}" \
    --render-threads "{{render_threads}}" \
    --min-inference-batch "{{min_inference_batch}}" )
  printf 'job_dir=%s\n' "$job_dir"
  "${cmd[@]}"

resume-mineru-batched job_dir heartbeat='10': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  job_dir="{{job_dir}}"
  cmd=( "{{venv_bin}}/python" scripts/run_mineru_batched.py \
    --resume-job-dir "$job_dir" \
    --heartbeat-seconds "{{heartbeat}}" )
  "${cmd[@]}"

launch-mineru-batched pdf batch_size method='auto' lang='en' heartbeat='10' render_threads='1' min_inference_batch='1': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pdf="{{pdf}}"
  stem="$(basename "$pdf")"
  stem="${stem%.*}"
  slug="$(printf '%s' "$stem" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-')"
  slug="${slug#-}"
  slug="${slug%-}"
  ts="$(date -u +%Y%m%dT%H%M%SZ)"
  job_dir="{{jobs_dir}}/${slug}-mineru-${ts}"
  mkdir -p "$job_dir"
  repo_root="$(pwd)"
  python_bin="$repo_root/{{venv_bin}}/python"
  runner_script="$repo_root/scripts/run_mineru_batched.py"
  run_script="$job_dir/run.sh"
  repo_root_q="$(printf '%q' "$repo_root")"
  python_bin_q="$(printf '%q' "$python_bin")"
  runner_script_q="$(printf '%q' "$runner_script")"
  pdf_q="$(printf '%q' "$pdf")"
  job_dir_q="$(printf '%q' "$job_dir")"
  method_q="$(printf '%q' "{{method}}")"
  batch_size_q="$(printf '%q' "{{batch_size}}")"
  lang_q="$(printf '%q' "{{lang}}")"
  heartbeat_q="$(printf '%q' "{{heartbeat}}")"
  render_threads_q="$(printf '%q' "{{render_threads}}")"
  min_inference_batch_q="$(printf '%q' "{{min_inference_batch}}")"
  {
    printf '%s\n' '#!/usr/bin/env bash'
    printf '%s\n' 'set -euo pipefail'
    printf 'cd %s\n' "$repo_root_q"
    printf 'exec %s %s \\\n' "$python_bin_q" "$runner_script_q"
    printf '  --pdf %s \\\n' "$pdf_q"
    printf '  --job-dir %s \\\n' "$job_dir_q"
    printf '  --method %s \\\n' "$method_q"
    printf '  --batch-size %s \\\n' "$batch_size_q"
    printf '  --lang %s \\\n' "$lang_q"
    printf '  --heartbeat-seconds %s \\\n' "$heartbeat_q"
    printf '  --render-threads %s \\\n' "$render_threads_q"
    printf '  --min-inference-batch %s\n' "$min_inference_batch_q"
  } > "$run_script"
  chmod +x "$run_script"
  setsid "$run_script" >"$job_dir/run.log" 2>&1 < /dev/null &
  pid=$!
  printf '%s\n' "$pid" > "$job_dir/pid"
  sleep 1
  ps -p "$pid" >/dev/null
  printf 'job_dir=%s\n' "$job_dir"
  printf 'pid=%s\n' "$pid"

mineru-resume-smoke pages='2' batch_size='1' heartbeat='2' method='txt': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pages="{{pages}}"
  batch_size="{{batch_size}}"
  heartbeat="{{heartbeat}}"
  pdf="artifacts/lorem-resume-${pages}p.pdf"
  just lorem-pdf "$pages" "$pdf"
  job_dir="{{jobs_dir}}/resume-smoke-$(date -u +%Y%m%dT%H%M%SZ)"
  mkdir -p "$job_dir"
  "{{venv_bin}}/python" scripts/run_mineru_batched.py \
    --pdf "$pdf" \
    --job-dir "$job_dir" \
    --method "{{method}}" \
    --batch-size "$batch_size" \
    --lang en \
    --heartbeat-seconds "$heartbeat" \
    --render-threads 1 \
    --min-inference-batch 1 \
    --no-formula \
    --no-table \
    --stop-after-batches 1
  "{{venv_bin}}/python" scripts/run_mineru_batched.py \
    --resume-job-dir "$job_dir" \
    --heartbeat-seconds "$heartbeat"
  jq -e '.status == "complete"' "$job_dir/manifest.json" >/dev/null
  combined_md="$(jq -r '.combined_markdown' "$job_dir/manifest.json")"
  test -s "$combined_md"
  rg -q "Synthetic Page 1" "$combined_md"
  rg -q "Synthetic Page ${pages}" "$combined_md"
  expected_batches=$(( (pages + batch_size - 1) / batch_size ))
  actual_batches="$(rg -c '^<!-- pages ' "$combined_md")"
  test "$actual_batches" -eq "$expected_batches"
  printf 'job_dir=%s\n' "$job_dir"

mineru-batch-experiment pdf batch_sizes='1,2,4' start_page='0' method='auto' heartbeat='5' render_threads='1' min_inference_batch='1': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pdf="{{pdf}}"
  stem="$(basename "$pdf")"
  stem="${stem%.*}"
  slug="$(printf '%s' "$stem" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-')"
  slug="${slug#-}"
  slug="${slug%-}"
  ts="$(date -u +%Y%m%dT%H%M%SZ)"
  experiment_dir="{{experiments_dir}}/${slug}-batch-profile-${ts}"
  mkdir -p "$experiment_dir"
  "{{venv_bin}}/python" scripts/profile_mineru_batch_sizes.py \
    --pdf "$pdf" \
    --experiment-dir "$experiment_dir" \
    --batch-sizes "{{batch_sizes}}" \
    --start-page "{{start_page}}" \
    --method "{{method}}" \
    --lang en \
    --heartbeat-seconds "{{heartbeat}}" \
    --render-threads "{{render_threads}}" \
    --min-inference-batch "{{min_inference_batch}}" \
    --model-source huggingface
  printf 'experiment_dir=%s\n' "$experiment_dir"
  cat "$experiment_dir/summary.md"

lorem-batch-experiment pages='4' batch_sizes='1,2,4' start_page='0' method='txt' heartbeat='5': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  pdf="artifacts/lorem-batch-profile-${pages}p.pdf"
  just lorem-pdf "{{pages}}" "$pdf"
  just mineru-batch-experiment "$pdf" "{{batch_sizes}}" "{{start_page}}" "{{method}}" "{{heartbeat}}" 1 1

extract-sterk batch_size=default_batch_size heartbeat=default_heartbeat:
  just extract-pdf "{{sterk_pdf}}" "{{batch_size}}" auto en "{{heartbeat}}"

launch-sterk-mineru batch_size=default_batch_size heartbeat=default_heartbeat:
  just launch-extract-pdf "{{sterk_pdf}}" "{{batch_size}}" auto en "{{heartbeat}}"
