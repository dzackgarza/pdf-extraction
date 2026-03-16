# PDF Extraction Canonical Workflow

This repo is the canonical home for Kaggle-only MinerU extraction. Local Docling and local MinerU conversion paths are intentionally out of scope.

## Compute & Quotas

### Kaggle (Primary)
- **Quota**: 30 hours of GPU time per week (on P100/T4).
- **Strategy**: This is the canonical workflow while compute time is available.
- **Cleanup**: Remote kernels and input datasets are deleted automatically after successful download to save space and maintain privacy.
- **Fallback**: If Kaggle limits are hit, fallback compute services are TBD.

### Mistral OCR (Secondary / Probe)
- **Model**: `mistral-ocr-latest`
- **Tier**: "Exploration" (Free) on La Plateforme.
- **Request Limits**: 50 MB and 1,000 pages per request.
- **Tier Limits**: Strictly for evaluation/prototyping. Throttle is ~1 request per second (RPS).
- **Usage**: Best for sparse probes or comparison. Run with `just mistral-ocr-pdf`.

## Working Rules

- **Use the justfile**: Never use ad hoc Kaggle commands or global installs.
- **Runner**: `pdf-mineru` is the active extraction runner (defined in `src/pdf_extraction/cli/mineru.py`).
- **Storage**: `outputs/kaggle-jobs/...` is the temporary local state for jobs.
- **Result**: Successfully extracted markdowns are moved next to the original PDF, and local job artifacts are trashed by default (unless `--save-artifacts` is passed).

## Primary Flow (Recipes)

Run a full remote extraction:
```bash
just kaggle-extract-pdf /abs/path/to/file.pdf
```

Math-paper default:
- Table extraction is disabled unless you opt in with `just kaggle-extract-pdf-tables /abs/path/to/file.pdf`.
- Formula extraction stays enabled by default.

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

Run a Mistral OCR probe:
```bash
just mistral-ocr-pdf /abs/path/to/file.pdf
```

## Debugging Kaggle Jobs

When asked why a Kaggle job did not finish, reconstruct the story from the existing job artifacts in this order:

1. `just kaggle-job-status <job_dir>` or `status.json` plus `manifest.json`.
2. `events.jsonl`.
3. The downloaded Kaggle notebook log in `downloads/*.log`.
4. `downloads/mineru-summary.json`.

Check before anything else:
- Did the kernel reach `complete` or `error`?
- Did the notebook produce `mineru-summary.json` and `mineru-output.zip`?
- Did the failure happen in notebook setup, Kaggle execution, output download, or MinerU itself?

## Observed Kaggle Benchmarks

- **Current Priors**: Peters-Sterk text (491 pages) on Kaggle GPU (P100) with MinerU `pipeline`.
- **Throughput**: Full-book run averaged **23.68 pages/min** (~21 minutes total).
- **Startup Overhead**: Small slices (5-10 pages) underpredict throughput (3-4 pages/min) because setup and model warmup dominate.
- **Quality Warning**: Runtime success != clean extraction. The Sterk book still required manual mathematical auditing for notation corruption (e.g., `^ { ! }` transposes).
