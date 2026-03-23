# PDF Extraction

Remote-first PDF-to-Markdown extraction using [MinerU](https://github.com/opendatalab/MinerU) on Kaggle GPUs.

## Quick Start

### Option 1: Local MinerU (Recommended for Small PDFs)

If you have a GPU locally, run MinerU directly:

```bash
# Install MinerU
pip install mineru[pipeline]

# Extract a PDF locally
mineru -p /path/to/document.pdf -o output_dir -b pipeline -f true -t false
```

**Requirements:**

- NVIDIA GPU with 8GB+ VRAM (16GB+ recommended)
- Python 3.10-3.12
- ~10GB disk space for models

### Option 2: Kaggle GPU (Free, No Local GPU Required)

Use this repo to run MinerU on Kaggle's free GPUs:

```bash
# Install this package
uv pip install -e .

# Extract a single PDF (GPU-accelerated on Kaggle)
pdf-mineru --pdf /absolute/path/to/document.pdf

# Or use just recipes
just kaggle-extract-pdf /absolute/path/to/document.pdf

# Extract with table parsing enabled (default: formulas only)
just kaggle-extract-pdf-tables /absolute/path/to/document.pdf

# Run a Mistral OCR probe (for comparison or sparse testing)
just mistral-ocr-pdf /absolute/path/to/document.pdf
```

Output markdown is placed next to the original PDF. Remote Kaggle resources are automatically cleaned up after successful extraction.

## Requirements

### For Local MinerU

- **NVIDIA GPU** with CUDA support (8GB+ VRAM recommended)
- **Python 3.10-3.12**
- **MinerU** installed via `pip install mineru[pipeline]`

### For Kaggle Workflow

- **Kaggle account** with API credentials configured (`~/.kaggle/kaggle.json` or env vars)
- **Python 3.12+** with [`uv`](https://github.com/astral-sh/uv) for dependency management
- **[`just`](https://github.com/casey/just)** for running recipes (optional)

## Installation

### Install This Package

```bash
# Clone and install with uv (recommended)
git clone https://github.com/dzackgarza/pdf-extraction.git
cd pdf-extraction
uv pip install -e .

# Or with pip
pip install -e .
```

This installs the `pdf-mineru` CLI entry point and all dependencies.

### Configure Kaggle API

1. Create a Kaggle account at https://www.kaggle.com
2. Go to Account → API → Create New Token
3. Download `kaggle.json` and place it at `~/.kaggle/kaggle.json`
4. Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

Alternatively, set environment variables:

```bash
export KAGGLE_USERNAME=your-username
export KAGGLE_KEY=your-api-key
```

## Workflows

### 1. Local MinerU Extraction (Direct)

For users with local GPU:

```bash
# Install MinerU
pip install mineru[pipeline]

# Basic extraction (formula parsing enabled, tables disabled)
mineru -p /path/to/document.pdf -o output_dir -b pipeline -f true -t false

# With table parsing enabled
mineru -p /path/to/document.pdf -o output_dir -b pipeline -f true -t true
```

**Key MinerU options:**

- `-p` / `--pdf`: Input PDF path
- `-o` / `--output`: Output directory
- `-b` / `--backend`: Backend (`pipeline` or `ocr`)
- `-f` / `--formula`: Enable formula parsing (`true`/`false`)
- `-t` / `--table`: Enable table parsing (`true`/`false`)
- `-l` / `--lang`: OCR language (default: `en`)
- `-d` / `--device`: Device (`cuda` or `cpu`)

### 2. Kaggle GPU Extraction (This Repo)

Uses the Kaggle script (`src/pdf_extraction/cli/mineru.py`) to run MinerU remotely:

```bash
# Using the CLI directly
pdf-mineru --pdf /path/to/document.pdf

# Using just recipe (wrapper)
just kaggle-extract-pdf /path/to/document.pdf
```

**What happens:**

1. PDF is split into batches if >200 pages
2. Each batch is uploaded to Kaggle as a private dataset
3. A GPU notebook runs MinerU on each batch (up to 2 parallel)
4. Results are downloaded, merged, and saved as `<document>.md`
5. Remote Kaggle kernels and datasets are deleted automatically
6. Local job artifacts are cleaned up (use `--save-artifacts` to keep)

**CLI Options:**

```bash
pdf-mineru --pdf /path/to/document.pdf \
  --enable-gpu false \
  --table \
  --no-formula \
  --batch-size 100 \
  --max-parallel 4 \
  --save-artifacts
```

| Option             | Default    | Description                       |
| ------------------ | ---------- | --------------------------------- |
| `--enable-gpu`     | `true`     | Request GPU (P100) on Kaggle      |
| `--table`          | `false`    | Enable table parsing              |
| `--formula`        | `true`     | Enable formula parsing            |
| `--batch-size`     | `200`      | Pages per batch                   |
| `--max-parallel`   | `2`        | Parallel GPU sessions             |
| `--save-artifacts` | `false`    | Keep local job directories        |
| `--backend`        | `pipeline` | MinerU backend                    |
| `--method`         | `auto`     | Parse method (`auto`/`txt`/`ocr`) |
| `--device`         | `cuda`     | Device for MinerU                 |

### 3. Prepare-Only Mode (Manual Control)

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

### 4. Manual Step-by-Step Workflow

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

### 5. Batch Processing

For multiple PDFs or when parallel batching is needed:

```bash
# Check batch status
just kaggle-batch-status /path/to/job1 /path/to/job2 /path/to/job3

# Merge completed extractions
just kaggle-merge-single /path/to/job1 /path/to/job2 --output merged.md
```

### 6. Mistral OCR (Alternative/Comparison)

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

### Local MinerU Flow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Your GPU   │────▶│  MinerU CLI  │────▶│  Markdown   │
│  (cuda)     │     │  (pipeline)  │     │  + Assets   │
└─────────────┘     └──────────────┘     └─────────────┘
```

### Kaggle Workflow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Local CLI  │────▶│  Kaggle API  │────▶│  GPU Kernel │
│  (pdf-mineru)│    │  (submit)    │     │  (MinerU)   │
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

| File                                  | Purpose                                       |
| ------------------------------------- | --------------------------------------------- |
| `src/pdf_extraction/cli/mineru.py`    | Main entry point (`pdf-mineru` CLI)           |
| `src/pdf_extraction/mineru/kaggle.py` | Kaggle API orchestration, notebook generation |
| `src/pdf_extraction/state_machine.py` | Job state tracking                            |
| `src/pdf_extraction/models.py`        | Pydantic data models                          |
| `pyproject.toml`                      | Package dependencies and entry points         |
| `justfile`                            | Recipe wrappers for CLI commands              |

### The Kaggle Script

The main Kaggle orchestration script is at `src/pdf_extraction/mineru/kaggle.py`. It:

1. **Prepares** a Kaggle notebook with MinerU installation and execution code
2. **Uploads** the PDF as a private Kaggle dataset
3. **Submits** the notebook to run on Kaggle GPU
4. **Polls** for completion
5. **Downloads** the extraction results
6. **Cleans up** remote resources

To run it directly (without the CLI wrapper):

```bash
python src/pdf_extraction/cli/mineru.py --pdf /path/to/document.pdf
```

Or after installation:

```bash
pdf-mineru --pdf /path/to/document.pdf
```

## Performance Benchmarks

**Peters-Sterk text (491 pages) on Kaggle P100:**

- **Throughput:** ~24 pages/min (full book, ~21 min total)
- **Small batches (5-10 pages):** ~3-4 pages/min (setup overhead dominates)
- **Parallel batching:** 2 concurrent GPU sessions by default

**Note:** Successful extraction ≠ clean output. Math notation may require manual correction (e.g., `^{!}` transposes).

## License

MIT
