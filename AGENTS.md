# PDF Extraction - Agent Guidelines

This document provides operational context for agents working in this repository. For user-facing documentation, see [README.md](README.md).

## Scope

- **In scope:** Kaggle-based MinerU extraction (remote GPU)
- **Out of scope:** Local Docling, local MinerU, alternative extraction backends

## Compute Quotas

### Kaggle (Primary)

- **Weekly GPU quota:** 30 hours (P100/T4)
- **Automatic cleanup:** Remote kernels and datasets deleted after successful download
- **Fallback:** TBD when quota exhausted

### Mistral OCR (Probe/Comparison Only)

- **Model:** `mistral-ocr-latest`
- **Limits:** 50 MB, 1,000 pages per request; ~1 RPS throttle
- **Use case:** Sparse probes, quality comparison

## Debugging Workflow

When a Kaggle job fails, investigate in this order:

1. **Status check:** `just kaggle-job-status <job_dir>` or read `status.json` + `manifest.json`
2. **Event timeline:** Read `events.jsonl` for phase transitions
3. **Notebook logs:** Check `downloads/*.log` for execution output
4. **MinerU summary:** Inspect `downloads/mineru-summary.json` for specific errors

**Key questions:**

- Kernel phase: `complete` or `error`?
- Did MinerU produce `mineru-summary.json` and `mineru-output.zip`?
- Failure point: setup, execution, download, or MinerU itself?

## Performance Priors

- **Peters-Sterk (491 pages, P100):** ~24 pages/min (~21 min total)
- **Small batches (5-10 pages):** ~3-4 pages/min (setup overhead dominates)
- **Quality note:** Successful run ≠ clean output; math notation may need manual audit

## Environment

- **Runner:** `pdf-mineru` (entry point: `src/pdf_extraction/cli/mineru.py`)
- **Job storage:** `outputs/kaggle-jobs/` (temporary, cleaned by default)
- **Output:** Markdown placed next to source PDF
- **Auth:** Kaggle API via `~/.kaggle/kaggle.json` or env vars; Mistral via `MISTRAL_API_KEY`
