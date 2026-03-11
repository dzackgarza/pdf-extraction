sample_md := "fixtures/lorem.md"
sample_pdf := "artifacts/lorem.pdf"
docling_dir := "outputs/docling"
mineru_dir := "outputs/mineru"
jobs_dir := "outputs/jobs"
experiments_dir := "outputs/experiments"
sterk_pdf := "/home/dzack/pdfs/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms.pdf"
venv_bin := ".venv/bin"

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
  cmd=( nohup "{{venv_bin}}/python" scripts/run_mineru_batched.py \
    --pdf "$pdf" \
    --job-dir "$job_dir" \
    --method "{{method}}" \
    --batch-size "{{batch_size}}" \
    --lang "{{lang}}" \
    --heartbeat-seconds "{{heartbeat}}" \
    --render-threads "{{render_threads}}" \
    --min-inference-batch "{{min_inference_batch}}" )
  "${cmd[@]}" >"$job_dir/run.log" 2>&1 &
  pid=$!
  printf '%s\n' "$pid" > "$job_dir/pid"
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

launch-sterk-mineru batch_size heartbeat='10':
  just launch-mineru-batched "{{sterk_pdf}}" "{{batch_size}}" auto en "{{heartbeat}}" 1 1
