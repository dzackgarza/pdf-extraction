set fallback := true
kaggle_jobs_dir := "outputs/kaggle-jobs"
venv_bin := ".venv/bin"

default:
  @just --list

sync:
  uv sync

test *ARGS: sync
  uv run pytest {{ARGS}}

check: lint typecheck test
  @echo "All checks passed!"

lint:
  uv run ruff check .

fmt:
  uv run ruff format .
  uv run ruff check --fix .

typecheck: sync
  uv run pyright .

kaggle-extract-pdf pdf owner='' method='auto' lang='en' backend='pipeline' device='' model_source='huggingface' poll='30' timeout='' accelerator='' enable_gpu='1' formula='1' table='' cleanup_remote='1' save_artifacts='0' virtual_vram_size='' batch_size='200': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  cmd=( "uv" "run" "pdf-mineru"
    --pdf "{{pdf}}"
    --method "{{method}}"
    --lang "{{lang}}"
    --backend "{{backend}}"
    --model-source "{{model_source}}"
    --poll-seconds "{{poll}}"
    --batch-size "{{batch_size}}" )
  if [ -n "{{owner}}" ]; then
    cmd+=( --owner "{{owner}}" )
  fi
  if [ -n "{{device}}" ]; then
    cmd+=( --device "{{device}}" )
  fi
  if [ -n "{{timeout}}" ]; then
    cmd+=( --timeout-seconds "{{timeout}}" )
  fi
  if [ -n "{{accelerator}}" ]; then
    cmd+=( --accelerator "{{accelerator}}" )
  fi
  if [ -n "{{virtual_vram_size}}" ]; then
    cmd+=( --virtual-vram-size "{{virtual_vram_size}}" )
  fi
  if [ "{{enable_gpu}}" = "1" ]; then
    cmd+=( --enable-gpu )
  else
    cmd+=( --no-enable-gpu )
  fi
  if [ "{{formula}}" = "1" ]; then
    cmd+=( --formula )
  else
    cmd+=( --no-formula )
  fi
  if [ -n "{{table}}" ]; then
    if [ "{{table}}" = "1" ]; then
      cmd+=( --table )
    else
      cmd+=( --no-table )
    fi
  fi
  if [ "{{cleanup_remote}}" = "1" ]; then
    cmd+=( --cleanup-remote )
  else
    cmd+=( --no-cleanup-remote )
  fi
  if [ "{{save_artifacts}}" = "1" ]; then
    cmd+=( --save-artifacts )
  fi
  "${cmd[@]}"

kaggle-prepare-pdf pdf owner method='auto' lang='en' backend='pipeline' device='' model_source='huggingface' accelerator='' enable_gpu='1' formula='1' table='' cleanup_remote='1' virtual_vram_size='' batch_size='200': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  cmd=( "uv" "run" "pdf-mineru"
    --pdf "{{pdf}}"
    --owner "{{owner}}"
    --prepare-only
    --method "{{method}}"
    --lang "{{lang}}"
    --backend "{{backend}}"
    --model-source "{{model_source}}"
    --batch-size "{{batch_size}}" )
  if [ -n "{{device}}" ]; then
    cmd+=( --device "{{device}}" )
  fi
  if [ -n "{{accelerator}}" ]; then
    cmd+=( --accelerator "{{accelerator}}" )
  fi
  if [ -n "{{virtual_vram_size}}" ]; then
    cmd+=( --virtual-vram-size "{{virtual_vram_size}}" )
  fi
  if [ "{{enable_gpu}}" = "1" ]; then
    cmd+=( --enable-gpu )
  else
    cmd+=( --no-enable-gpu )
  fi
  if [ "{{formula}}" = "1" ]; then
    cmd+=( --formula )
  else
    cmd+=( --no-formula )
  fi
  if [ -n "{{table}}" ]; then
    if [ "{{table}}" = "1" ]; then
      cmd+=( --table )
    else
      cmd+=( --no-table )
    fi
  fi
  if [ "{{cleanup_remote}}" = "1" ]; then
    cmd+=( --cleanup-remote )
  else
    cmd+=( --no-cleanup-remote )
  fi
  "${cmd[@]}"

kaggle-job-status job_dir:
  #!/usr/bin/env bash
  set -euxo pipefail
  jq '{phase, dataset_ref, dataset_status, kernel_ref, kernel_status, downloaded_files, markdown_path, failure}' "{{job_dir}}/status.json"
  printf '\n'
  jq '{pdf, page_count, dataset_ref, kernel_ref, downloads_dir, summary_path, bundle_path, markdown_path, remote_cleanup}' "{{job_dir}}/manifest.json"

kaggle-status job_dir refresh='false' json='false': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-status "{{job_dir}}")
  if [ "{{refresh}}" = "true" ]; then
    cmd+=(--refresh)
  fi
  if [ "{{json}}" = "true" ]; then
    cmd+=(--json-output)
  fi
  "${cmd[@]}"

kaggle-submit job_dir kernel_name='': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-submit "{{job_dir}}")
  if [ -n "{{kernel_name}}" ]; then
    cmd+=(--kernel-name "{{kernel_name}}")
  fi
  "${cmd[@]}"

kaggle-download job_dir force='false': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-download "{{job_dir}}")
  if [ "{{force}}" = "true" ]; then
    cmd+=(--force)
  fi
  "${cmd[@]}"

kaggle-refresh job_dir quiet='false': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-refresh "{{job_dir}}")
  if [ "{{quiet}}" = "true" ]; then
    cmd+=(--quiet)
  fi
  "${cmd[@]}"

kaggle-markdown-path job_dir:
  #!/usr/bin/env bash
  set -euxo pipefail
  jq -r '.markdown_path' "{{job_dir}}/manifest.json"

kaggle-download-output job_dir: sync
  #!/usr/bin/env bash
  set -euxo pipefail
  kernel_ref=$(jq -r '.kernel_ref' "{{job_dir}}/status.json")
  uv run kaggle kernels output "$kernel_ref" -p "{{job_dir}}/downloads/"

kaggle-list-kernels: sync
  #!/usr/bin/env bash
  set -euo pipefail
  uv run kaggle kernels list --csv

kaggle-delete-kernel kernel_ref: sync
  #!/usr/bin/env bash
  set -euo pipefail
  uv run kaggle kernels delete "$kernel_ref"

kaggle-cleanup-local:
  #!/usr/bin/env bash
  set -euo pipefail
  echo "Removing all local Kaggle job directories..."
  find outputs/kaggle-jobs -mindepth 1 -delete 2>/dev/null || true
  mkdir -p outputs/kaggle-jobs
  echo "Cleaning tmp-batches..."
  find outputs/tmp-batches -mindepth 1 -delete 2>/dev/null || true
  mkdir -p outputs/tmp-batches
  echo "Cleanup complete"

cleanup-logs:
  #!/usr/bin/env bash
  set -euo pipefail
  echo "Cleaning up log files and test artifacts..."
  find . -maxdepth 1 -name "*.log" -type f -delete
  find . -maxdepth 1 -name "*_pid.txt" -type f -delete
  find . -maxdepth 1 -name "test_*.md" -type f -delete
  find . -maxdepth 1 -name "test_*.pdf" -type f -delete
  [ -d test_5pages_assets ] && find test_5pages_assets -type f -delete
  [ -d test_5pages_assets ] && rmdir test_5pages_assets 2>/dev/null || true
  echo "Cleanup complete"

# CLI testing helpers
cli-status-help: sync
  uv run pdf-status --help

cli-submit-help: sync
  uv run pdf-submit --help

cli-download-help: sync
  uv run pdf-download --help

cli-refresh-help: sync
  uv run pdf-refresh --help

cli-merge-help: sync
  uv run pdf-merge --help

cli-poll-help: sync
  uv run pdf-poll --help

cli-batch-help: sync
  uv run pdf-batch --help

# New CLI commands - simplified single job versions
kaggle-merge-single job_dir1 job_dir2 output='' dry_run='false': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-merge merge "{{job_dir1}}" "{{job_dir2}}")
  if [ -n "{{output}}" ]; then
    cmd+=(--output "{{output}}")
  fi
  if [ "{{dry_run}}" = "true" ]; then
    cmd+=(--dry-run)
  fi
  "${cmd[@]}"

kaggle-poll job_dir interval='30' timeout='' quiet='false': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-poll poll "{{job_dir}}")
  cmd+=(--interval "{{interval}}")
  if [ -n "{{timeout}}" ]; then
    cmd+=(--timeout "{{timeout}}")
  fi
  if [ "{{quiet}}" = "true" ]; then
    cmd+=(--quiet)
  fi
  "${cmd[@]}"

kaggle-batch-status json='false' job_dir1='' job_dir2='' job_dir3='' job_dir4='' job_dir5='': sync
  #!/usr/bin/env bash
  set -euo pipefail
  cmd=(uv run pdf-batch status all)
  for dir in {{job_dir1}} {{job_dir2}} {{job_dir3}} {{job_dir4}} {{job_dir5}}; do
    [ -n "$dir" ] && cmd+=("$dir")
  done
  if [ "{{json}}" = "true" ]; then
    cmd+=(--json-output)
  fi
  "${cmd[@]}"

kaggle-extract-pdf-cpu pdf owner='' method='auto' lang='en' backend='pipeline' device='cpu' model_source='huggingface' poll='30' timeout='' accelerator='' cleanup_remote='1' save_artifacts='0' batch_size='200': sync
  just kaggle-extract-pdf "{{pdf}}" "{{owner}}" "{{method}}" "{{lang}}" "{{backend}}" "{{device}}" "{{model_source}}" "{{poll}}" "{{timeout}}" "{{accelerator}}" 0 1 0 "{{cleanup_remote}}" "{{save_artifacts}}" "" "{{batch_size}}"


mistral-ocr-pdf pdf pages='' table_format='' output_dir='':
  #!/usr/bin/env bash
  set -euxo pipefail
  cmd=( direnv exec . uv run pdf-mistral
    --pdf "{{pdf}}" )
  if [ -n "{{pages}}" ]; then
    cmd+=( --pages "{{pages}}" )
  fi
  if [ -n "{{table_format}}" ]; then
    cmd+=( --table-format "{{table_format}}" )
  fi
  if [ -n "{{output_dir}}" ]; then
    cmd+=( --output-dir "{{output_dir}}" )
  fi
  "${cmd[@]}"
