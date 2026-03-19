"""Status command for querying Kaggle job state.

Remote-first status query that always checks Kaggle API before reporting.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from cyclopts import App

from ..kaggle_client import KaggleAPIError, KaggleClient, KernelNotFoundError
from ..models import (
    JobManifest,
    JobState,
    JobStatus,
    LocalJobState,
    StaleStateWarning,
)
from ..state_machine import describe_state, get_workflow_progress, is_terminal_state

app = App(help="Query and display Kaggle job status")


def load_job_status(job_dir: Path) -> JobStatus:
    """Load job status from local files.

    Args:
        job_dir: Path to job directory

    Returns:
        JobStatus with local state and manifest (remote=None)
    """
    status_file = job_dir / "status.json"
    manifest_file = job_dir / "manifest.json"

    if not manifest_file.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_file}")

    with open(manifest_file) as f:
        manifest_data = json.load(f)

    manifest = JobManifest(
        job_dir=Path(manifest_data.get("job_dir", str(job_dir))),
        pdf_path=Path(manifest_data["pdf"]),
        page_range=(
            manifest_data.get("start_page", 1),
            manifest_data.get("end_page", 1),
        ),
        kernel_name=manifest_data.get("kernel_name", "unknown"),
    )

    local_state = JobState.PREPARED
    downloaded = False
    merged = False

    if status_file.exists():
        with open(status_file) as f:
            status_data = json.load(f)

        # Map old phase field to new JobState
        phase = status_data.get("phase", "prepared")
        phase_to_state = {
            "prepared": JobState.PREPARED,
            "submitted": JobState.SUBMITTED,
            "running": JobState.RUNNING,
            "complete": JobState.COMPLETE_REMOTE,
            "downloading_output": JobState.COMPLETE_REMOTE,
            "downloaded": JobState.DOWNLOADED,
            "merged": JobState.MERGED,
            "failed": JobState.FAILED,
        }
        local_state = phase_to_state.get(phase, JobState.PREPARED)

        # Check if files were downloaded
        downloads_dir = job_dir / "downloads"
        downloaded = downloads_dir.exists() and any(downloads_dir.iterdir())

        # Check for merged output
        markdown_path = manifest_data.get("markdown_path")
        if markdown_path and Path(markdown_path).exists():
            merged = True

    local = LocalJobState(
        state=local_state,
        downloaded=downloaded,
        merged=merged,
    )

    return JobStatus(manifest=manifest, remote=None, local=local)


def save_job_status(status: JobStatus) -> None:
    """Save job status to local status.json.

    Args:
        status: Job status to save
    """
    status_file = status.manifest.job_dir / "status.json"

    # Combine remote and local state for backward compatibility
    data = {
        "phase": status.effective_state.value,
        "kernel_ref": status.remote.kernel_ref if status.remote else None,
        "kernel_status": status.remote.status.value if status.remote else None,
        "remote_query_time": status.remote.query_timestamp.isoformat()
        if status.remote
        else None,
        "downloaded": status.local.downloaded,
        "merged": status.local.merged,
        "last_updated": status.local.last_updated.isoformat(),
    }

    if status.remote:
        data["kernel_status"] = status.remote.status.value
        data["started_at"] = (
            status.remote.started_at.isoformat() if status.remote.started_at else None
        )
        data["completed_at"] = (
            status.remote.completed_at.isoformat()
            if status.remote.completed_at
            else None
        )
        data["error_message"] = status.remote.error_message

    status_file.parent.mkdir(parents=True, exist_ok=True)
    with open(status_file, "w") as f:
        json.dump(data, f, indent=2)


@app.command
def status(job_dir: Path, refresh: bool = False, json_output: bool = False) -> None:
    """Query and display job status.

    Always queries Kaggle API for remote state. Updates local cache.

    Args:
        job_dir: Path to job directory
        refresh: Force refresh even if cache is fresh
        json_output: Output as JSON instead of human-readable format
    """
    client = KaggleClient()

    # Load local state
    try:
        job_status = load_job_status(job_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    # Get kernel ref from manifest or existing status
    kernel_ref = None
    status_file = job_dir / "status.json"
    if status_file.exists():
        with open(status_file) as f:
            data = json.load(f)
            kernel_ref = data.get("kernel_ref")

    if not kernel_ref:
        print(
            "Error: No kernel reference found - job not yet submitted", file=sys.stderr
        )
        sys.exit(2)

    # Query remote state
    try:
        remote = client.get_kernel_status(kernel_ref)
        job_status = job_status.with_remote(remote)
        save_job_status(job_status)
    except KernelNotFoundError:
        print(f"Error: Kernel not found: {kernel_ref}", file=sys.stderr)
        sys.exit(2)
    except KaggleAPIError as e:
        print(f"Error querying Kaggle API: {e.message}", file=sys.stderr)
        sys.exit(2)

    # Check staleness warning
    if job_status.is_stale and not refresh:
        import warnings

        warnings.warn(StaleStateWarning(job_status.staleness_seconds), stacklevel=2)

    # Output
    if json_output:
        output = {
            "job_dir": str(job_status.manifest.job_dir),
            "pdf": str(job_status.manifest.pdf_path),
            "page_range": list(job_status.manifest.page_range),
            "page_count": job_status.manifest.page_count,
            "kernel_ref": job_status.remote.kernel_ref if job_status.remote else None,
            "remote_state": job_status.remote.status.value
            if job_status.remote
            else None,
            "local_state": job_status.effective_state.value,
            "downloaded": job_status.local.downloaded,
            "merged": job_status.local.merged,
            "is_stale": job_status.is_stale,
            "staleness_seconds": round(job_status.staleness_seconds, 1)
            if job_status.remote
            else None,
            "description": describe_state(job_status.effective_state),
            "is_terminal": is_terminal_state(job_status.effective_state),
        }
        print(json.dumps(output, indent=2))
    else:
        # Human-readable output
        current, total = get_workflow_progress(job_status.effective_state)

        print(f"\n{'=' * 60}")
        print(f"Job: {job_dir.name}")
        print(f"{'=' * 60}")
        print(f"PDF: {job_status.manifest.pdf_path.name}")
        print(
            f"Pages: {job_status.manifest.page_range[0]}-{job_status.manifest.page_range[1]} ({job_status.manifest.page_count} pages)"
        )
        print(f"Kernel: {job_status.remote.kernel_ref if job_status.remote else 'N/A'}")
        print()
        print(f"Workflow Progress: [{current}/{total}]")
        print(f"  State: {job_status.effective_state.value}")
        print(f"  Description: {describe_state(job_status.effective_state)}")
        print()
        print("Remote State (Kaggle):")
        if job_status.remote:
            print(f"  Status: {job_status.remote.status.value}")
            if job_status.remote.started_at:
                print(f"  Started: {job_status.remote.started_at}")
            if job_status.remote.completed_at:
                print(f"  Completed: {job_status.remote.completed_at}")
            if job_status.remote.error_message:
                print(f"  Error: {job_status.remote.error_message}")
            age_min = job_status.staleness_seconds / 60
            stale_marker = " ⚠️  STALE" if job_status.is_stale else ""
            print(
                f"  Queried: {job_status.remote.query_timestamp} ({age_min:.1f} min ago){stale_marker}"
            )
        else:
            print("  Not queried")
        print()
        print("Local State:")
        print(f"  Downloaded: {'Yes' if job_status.local.downloaded else 'No'}")
        print(f"  Merged: {'Yes' if job_status.local.merged else 'No'}")
        print(f"{'=' * 60}\n")

    # Exit code based on state
    if job_status.effective_state == JobState.FAILED:
        sys.exit(1)
    elif (
        is_terminal_state(job_status.effective_state)
        and job_status.effective_state != JobState.MERGED
    ):
        sys.exit(1)
    elif job_status.effective_state == JobState.MERGED:
        sys.exit(0)
    else:
        sys.exit(0)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
