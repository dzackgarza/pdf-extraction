# PDF Extraction

Remote-first PDF-to-Markdown extraction using [MinerU](https://github.com/opendatalab/MinerU) on Kaggle GPUs.

## Quick Start

```bash
# Extract a single PDF (GPU-accelerated on Kaggle)
just kaggle-extract-pdf /absolute/path/to/document.pdf

# Extract with table parsing enabled (default: formulas only)
just kaggle-extract-pdf-tables /absolute/path/to/document.pdf

# Run a Mistral OCR probe (for comparison or sparse testing)
just mistral-ocr-pdf /absolute/path/to/document.pdf
```

Output markdown is placed next to the original PDF. Remote Kaggle resources are automatically cleaned up after successful extraction.

## Requirements

- **Kaggle account** with API credentials configured (`~/.kaggle/kaggle.json` or env vars)
- **Python 3.12+** with [`uv`](https://github.com/astral-sh/uv) for dependency management
- **[`just`](https://github.com/casey/just)** for running recipes

## Workflows

### 1. Single PDF Extraction (Recommended)

The simplest workflow handles everything automatically:

```bash
just kaggle-extract-pdf /path/to/document.pdf
```

**What happens:**

1. PDF is split into batches if >200 pages
2. Each batch is uploaded to Kaggle as a private dataset
3. A GPU notebook runs MinerU on each batch (up to 2 parallel)
4. Results are downloaded, merged, and saved as `<document>.md`
5. Remote Kaggle kernels and datasets are deleted automatically
6. Local job artifacts are cleaned up (use `--save-artifacts` to keep)

**Options:**

- `--enable-gpu=0` - Run on CPU (slower)
- `--table=1` - Enable table parsing (default: off for math papers)
- `--formula=0` - Disable formula parsing
- `--batch-size=100` - Pages per batch (default: 200)
- `--max-parallel=4` - Parallel GPU sessions (default: 2)
- `--save-artifacts=1` - Keep local job directories

### 2. Prepare-Only Mode (Manual Control)

Prepare the Kaggle bundle without submitting:

```bash
just kaggle-prepare-pdf /path/to/document.pdf your-kaggle-username
```

This creates a job directory with:

- `input-dataset/` - PDF and dataset metadata
- `kernel/` - Notebook and kernel metadata
- `manifest.json` - Job configuration
- `status.json` - Current state

Use this to inspect or modify the bundle before submission.

### 3. Manual Step-by-Step Workflow

For full control over the extraction lifecycle:

```bash
# 1. Prepare the job
just kaggle-prepare-pdf /path/to/document.pdf your-username

# 2. Submit to Kaggle
just kaggle-submit /path/to/job-directory

# 3. Poll for completion
just kaggle-poll /path/to/job-directory --interval 30

# 4. Download outputs
just kaggle-download /path/to/job-directory

# 5. Check status anytime
just kaggle-job-status /path/to/job-directory
```

### 4. Batch Processing

For multiple PDFs or when parallel batching is needed:

```bash
# Check batch status
just kaggle-batch-status /path/to/job1 /path/to/job2 /path/to/job3

# Merge completed extractions
just kaggle-merge-single /path/to/job1 /path/to/job2 --output merged.md
```

### 5. Mistral OCR (Alternative/Comparison)

Use Mistral's OCR API for comparison or when Kaggle is unavailable:

```bash
just mistral-ocr-pdf /path/to/document.pdf
```

Requires `MISTRAL_API_KEY` in your environment.

## Job Directory Structure

After extraction, job directories (in `outputs/kaggle-jobs/`) contain:

```
job-directory/
├── manifest.json          # Canonical state: paths, refs, summary
├── status.json            # Current phase and Kaggle status
├── events.jsonl           # Timestamped event log
├── downloads/
│   ├── notebook.log       # Kaggle notebook execution log
│   ├── mineru-summary.json  # MinerU run summary
│   └── mineru-output.zip    # Raw extraction bundle
└── extracted/             # Unpacked extraction (markdown + assets)
```

**Key files for debugging:**

1. `status.json` - Check `phase` and `kernel_status`
2. `events.jsonl` - Timeline of what happened
3. `downloads/*.log` - Full notebook output
4. `downloads/mineru-summary.json` - MinerU-specific errors

## Debugging Failed Jobs

```bash
# Quick status check
just kaggle-job-status /path/to/job-directory

# Refresh status from Kaggle
just kaggle-status /path/to/job-directory --refresh

# View as JSON
just kaggle-status /path/to/job-directory --json
```

**Common failure points:**

- **Dataset creation failed** - Check Kaggle API auth
- **Kernel stuck in "running"** - May need manual deletion
- **MinerU exit code != 0** - Check `mineru-summary.json` for error
- **No output files** - MinerU ran but produced nothing (corrupt PDF?)

**Cleanup orphaned resources:**

```bash
# List your Kaggle kernels
just kaggle-list-kernels

# Delete a specific kernel
just kaggle-delete-kernel your-username/kernel-slug

# Clean all local job directories
just kaggle-cleanup-local
```

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Local CLI  │────▶│  Kaggle API  │────▶│  GPU Kernel │
│  (just/uv)  │     │  (submit)    │     │  (MinerU)   │
└─────────────┘     └──────────────┘     └─────────────┘
       ▲                    │                    │
       │                    ▼                    ▼
       │            ┌──────────────┐     ┌─────────────┐
       │            │  Poll Status │     │  Generate   │
       │            └──────────────┘     │  Markdown   │
       │                                 └─────────────┘
       │                                        │
       └────────────────────────────────────────┘
                          Download
```

**Key components:**

- `src/pdf_extraction/cli/mineru.py` - Main entry point (`pdf-mineru`)
- `src/pdf_extraction/mineru/kaggle.py` - Kaggle API orchestration
- `src/pdf_extraction/state_machine.py` - Job state tracking
- `justfile` - All CLI recipes

## Performance Benchmarks

**Peters-Sterk text (491 pages) on Kaggle P100:**

- **Throughput:** ~24 pages/min (full book, ~21 min total)
- **Small batches (5-10 pages):** ~3-4 pages/min (setup overhead dominates)
- **Parallel batching:** 2 concurrent GPU sessions by default

**Note:** Successful extraction ≠ clean output. Math notation may require manual correction (e.g., `^{!}` transposes).

## License

MIT
