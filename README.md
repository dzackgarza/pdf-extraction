# PDF Extraction Workflow

This repo is for Kaggle-only MinerU extraction. Local Docling and local MinerU conversion paths are intentionally out of scope.

Use the `just` recipes, not ad hoc Kaggle commands:

```bash
just kaggle-extract-pdf /abs/path/to/file.pdf
just kaggle-prepare-pdf /abs/path/to/file.pdf your-kaggle-username
```

## Primary Flow

Run a full remote extraction:

```bash
just kaggle-extract-pdf /abs/path/to/file.pdf
```

Math-paper default:

- table extraction is disabled unless you opt in with `just kaggle-extract-pdf-tables /abs/path/to/file.pdf`
- formula extraction stays enabled by default

```bash
just kaggle-extract-pdf-tables /abs/path/to/file.pdf
```

Prepare the local Kaggle dataset/kernel bundle without submitting it:

```bash
just kaggle-prepare-pdf /abs/path/to/file.pdf your-kaggle-username
```

Inspect a job directory:

```bash
just kaggle-job-status /abs/path/to/job_dir
```

Convenience shortcut for the Peters-Sterk text:

```bash
just kaggle-extract-sterk
```

Run a sparse Mistral OCR probe with `MISTRAL_API_KEY` loaded via `direnv`:

```bash
just mistral-ocr-pdf /abs/path/to/file.pdf 0
```

## What The Runner Does

- uploads the PDF as a private Kaggle dataset
- launches a private Kaggle notebook
- installs `mineru[pipeline]` inside the notebook
- requests GPU by default and runs MinerU in the notebook directly
- downloads `mineru-summary.json` and `mineru-output.zip` into `outputs/kaggle-jobs/...`
- extracts the bundle locally and records the markdown path in `manifest.json`
- deletes the remote kernel and input dataset after a successful download unless explicitly disabled

## Requirements

- Kaggle credentials must already be configured for the local `kaggle` Python package / CLI
- the runner honors OAuth when `KAGGLE_ENABLE_OAUTH=1`
- when GPU is enabled and no override is provided, the runner defaults to `cuda` plus Kaggle accelerator `P100`
- table extraction defaults to off for Kaggle MinerU runs; use `just kaggle-extract-pdf-tables /abs/path/to/file.pdf` to opt in

## Job Directory Layout

- `status.json`: current phase plus the latest known Kaggle refs and downloaded files
- `manifest.json`: canonical job state, summary path, bundle path, and markdown path
- `events.jsonl`: structured local event log for the Kaggle submission/download lifecycle
- `downloads/*.log`: downloaded Kaggle notebook session log
- `downloads/mineru-summary.json`: notebook-side summary of the MinerU run
- `downloads/mineru-output.zip`: downloaded extraction bundle
- `extracted/.../*.md`: extracted markdown output
