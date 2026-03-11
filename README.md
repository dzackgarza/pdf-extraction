# PDF Extraction Workflow

This repo uses `scripts/run_mineru_batched.py` as the canonical PDF to Markdown path.

Use the `just` recipes, not ad hoc `mineru` invocations:

```bash
just extract-pdf /abs/path/to/file.pdf
just launch-extract-pdf /abs/path/to/file.pdf
```

The runner always goes through the batched path. If the PDF has at most `batch_size` pages, it runs as one batch. If the PDF is larger, it splits the work into batches and rebuilds one combined markdown file as batches finish. The current default on this machine is `batch_size=120`, chosen to keep dense pages around the `5 GB` process-tree RSS target.

## Start A Run

Foreground:

```bash
just extract-pdf /abs/path/to/file.pdf
```

Background:

```bash
just launch-extract-pdf /abs/path/to/file.pdf
```

The background launcher prints:

- `job_dir=...`
- `pid=...`

Use `job_dir` as the handle for every later action.

Sterk shortcut:

```bash
just launch-sterk-mineru
```

## Manage A Long Run

Check status:

```bash
just extract-status /abs/path/to/job_dir
```

Show the current worker log:

```bash
just extract-tail /abs/path/to/job_dir
```

Show the current structured progress stream:

```bash
just extract-progress /abs/path/to/job_dir
```

Stop the supervisor cleanly:

```bash
just extract-stop /abs/path/to/job_dir
```

Resume a stopped or paused run:

```bash
just resume-extract /abs/path/to/job_dir
```

Print the combined markdown path:

```bash
just extract-markdown-path /abs/path/to/job_dir
```

## What Lives In A Job Directory

- `status.json`: current phase, current batch, and live resource snapshot
- `manifest.json`: batch plan, per-batch results, and `combined_markdown`
- `events.jsonl`: structured supervisor event log
- `run.log`: detached launcher output
- `pid`: supervisor PID for `extract-stop`
- `run.sh`: exact detached command used for the run
- `batches/<tag>/attempt-XXX/worker.log`: MinerU stdout/stderr for one batch
- `batches/<tag>/attempt-XXX/progress.jsonl`: structured progress and resource heartbeats for one batch
- `combined/<slug>.md`: concatenated markdown rebuilt after each completed batch

## Status Phases

- `starting`: supervisor started and is planning the next batch
- `running_batch`: a batch worker is active
- `paused`: the run stopped after a requested batch boundary
- `failed`: the current batch failed or was terminated
- `complete`: all batches finished and the combined markdown is final

For finished runs, `manifest.json` is the single source of truth for batch results and the final markdown path.
