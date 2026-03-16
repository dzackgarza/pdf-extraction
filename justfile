kaggle_jobs_dir := "outputs/kaggle-jobs"
sterk_pdf := "/home/dzack/pdfs/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms.pdf"
venv_bin := ".venv/bin"

default:
  @just --list

sync:
  uv sync

kaggle-extract-pdf pdf owner='' method='auto' lang='en' backend='pipeline' device='' model_source='huggingface' poll='30' timeout='' accelerator='' enable_gpu='1' formula='1' table='' cleanup_remote='1' save_artifacts='0' virtual_vram_size='': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  cmd=( "uv" "run" "pdf-mineru"
    --pdf "{{pdf}}"
    --method "{{method}}"
    --lang "{{lang}}"
    --backend "{{backend}}"
    --model-source "{{model_source}}"
    --poll-seconds "{{poll}}" )
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

kaggle-prepare-pdf pdf owner method='auto' lang='en' backend='pipeline' device='' model_source='huggingface' accelerator='' enable_gpu='1' formula='1' table='' cleanup_remote='1' virtual_vram_size='': sync
  #!/usr/bin/env bash
  set -euxo pipefail
  cmd=( "uv" "run" "pdf-mineru"
    --pdf "{{pdf}}"
    --owner "{{owner}}"
    --prepare-only
    --method "{{method}}"
    --lang "{{lang}}"
    --backend "{{backend}}"
    --model-source "{{model_source}}" )
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

kaggle-markdown-path job_dir:
  #!/usr/bin/env bash
  set -euxo pipefail
  jq -r '.markdown_path' "{{job_dir}}/manifest.json"

kaggle-extract-sterk owner='' poll='30' timeout='' accelerator='' device='' enable_gpu='1' formula='1' table='' cleanup_remote='1' save_artifacts='0' virtual_vram_size='':
  just kaggle-extract-pdf "{{sterk_pdf}}" "{{owner}}" auto en pipeline "{{device}}" huggingface "{{poll}}" "{{timeout}}" "{{accelerator}}" "{{enable_gpu}}" "{{formula}}" "{{table}}" "{{cleanup_remote}}" "{{save_artifacts}}" "{{virtual_vram_size}}"

kaggle-prepare-sterk owner accelerator='' device='' enable_gpu='1' formula='1' table='' cleanup_remote='1' virtual_vram_size='':
  just kaggle-prepare-pdf "{{sterk_pdf}}" "{{owner}}" auto en pipeline "{{device}}" huggingface "{{accelerator}}" "{{enable_gpu}}" "{{formula}}" "{{table}}" "{{cleanup_remote}}" "{{virtual_vram_size}}"

kaggle-extract-pdf-tables pdf owner='' poll='30' timeout='' accelerator='' device='' enable_gpu='1' formula='1' cleanup_remote='1' save_artifacts='0' virtual_vram_size='':
  just kaggle-extract-pdf "{{pdf}}" "{{owner}}" auto en pipeline "{{device}}" huggingface "{{poll}}" "{{timeout}}" "{{accelerator}}" "{{enable_gpu}}" "{{formula}}" 1 "{{cleanup_remote}}" "{{save_artifacts}}" "{{virtual_vram_size}}"


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
