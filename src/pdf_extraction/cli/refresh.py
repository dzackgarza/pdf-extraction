"""Refresh command for updating local state from remote.

Queries Kaggle API and updates local cache without side effects.
"""

from __future__ import annotations

import json
import sys
from datetime import UTC
from pathlib import Path

from cyclopts import App

from ..kaggle_client import KaggleAPIError, KaggleClient, KernelNotFoundError
from ..models import (
    JobManifest,
    JobState,
    JobStatus,
    KernelStatus,
    LocalJobState,
    RemoteJobState,
    StaleStateWarning,
)

app = App(help="Refresh local job state from Kaggle API")


def load_status(job_dir: Path) -> JobStatus:
    """Load job status from files.

    Args:
        job_dir: Path to job directory

    Returns:
        JobStatus instance
    """
    manifest_file = job_dir / "manifest.json"
    status_file = job_dir / "status.json"

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
    kernel_ref = None

    if status_file.exists():
        with open(status_file) as f:
            data = json.load(f)

        phase = data.get("phase", "prepared")
        phase_to_state = {
            "prepared": JobState.PREPARED,
            "submitted": JobState.SUBMITTED,
            "running": JobState.RUNNING,
            "complete": JobState.COMPLETE_REMOTE,
            "downloaded": JobState.DOWNLOADED,
            "merged": JobState.MERGED,
            "failed": JobState.FAILED,
        }
        local_state = phase_to_state.get(phase, JobState.PREPARED)
        downloaded = data.get("downloaded", False)
        merged = data.get("merged", False)
        kernel_ref = data.get("kernel_ref")

    local = LocalJobState(
        state=local_state,
        downloaded=downloaded,
        merged=merged,
    )

    remote = None
    if kernel_ref:
        if status_file.exists():
            with open(status_file) as f:
                data = json.load(f)
            if data.get("kernel_status"):
                from datetime import datetime

                remote = RemoteJobState(
                    kernel_ref=kernel_ref,
                    status=KernelStatus(data["kernel_status"]),
                    query_timestamp=datetime.now(UTC),
                )

    return JobStatus(manifest=manifest, remote=remote, local=local)


def save_status(status: JobStatus) -> None:
    """Save job status to status.json.

    Args:
        status: JobStatus to save
    """
    status_file = status.manifest.job_dir / "status.json"

    data = {
        "phase": status.effective_state.value,
        "kernel_ref": status.remote.kernel_ref if status.remote else None,
        "kernel_status": status.remote.status.value if status.remote else None,
        "downloaded": status.local.downloaded,
        "merged": status.local.merged,
        "last_updated": status.local.last_updated.isoformat(),
    }

    if status.remote:
        data["started_at"] = (
            status.remote.started_at.isoformat() if status.remote.started_at else None
        )
        data["completed_at"] = (
            status.remote.completed_at.isoformat()
            if status.remote.completed_at
            else None
        )
        data["error_message"] = status.remote.error_message
        data["remote_query_time"] = status.remote.query_timestamp.isoformat()

    status_file.parent.mkdir(parents=True, exist_ok=True)
    with open(status_file, "w") as f:
        json.dump(data, f, indent=2)


@app.command
def refresh(
    job_dir: Path,
    quiet: bool = False,
) -> None:
    """Refresh local state from Kaggle API.

    Queries remote state, updates local cache, reports any changes.

    Args:
        job_dir: Path to job directory
        quiet: Only output on state change
    """
    # Load current status
    try:
        status = load_status(job_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Get kernel ref
    kernel_ref = status.remote.kernel_ref if status.remote else None
    if not kernel_ref:
        status_file = job_dir / "status.json"
        if status_file.exists():
            with open(status_file) as f:
                data = json.load(f)
            kernel_ref = data.get("kernel_ref")

    if not kernel_ref:
        print("Error: No kernel reference found", file=sys.stderr)
        sys.exit(1)

    old_state = status.effective_state
    old_remote_status = status.remote.status if status.remote else None

    # Query remote
    client = KaggleClient()
    try:
        remote = client.get_kernel_status(kernel_ref)
    except KernelNotFoundError:
        print(f"Error: Kernel not found: {kernel_ref}", file=sys.stderr)
        sys.exit(1)
    except KaggleAPIError as e:
        print(f"Error: {e.message}", file=sys.stderr)
        sys.exit(1)

    # Update status
    new_status = status.with_remote(remote)
    save_status(new_status)

    # Report changes
    new_state = new_status.effective_state
    state_changed = old_state != new_state
    status_changed = old_remote_status != remote.status if old_remote_status else True

    if not quiet or state_changed:
        print(f"Refreshed {job_dir.name}:")
        print(f"  Kernel: {kernel_ref}")
        print(f"  Remote status: {remote.status.value}")
        if state_changed:
            print(f"  State changed: {old_state.value} → {new_state.value}")
        if status.remote:
            age_min = new_status.staleness_seconds / 60
            print(f"  Queried: {age_min:.2f} min ago")

    # Warn if stale
    if new_status.is_stale:
        import warnings

        warnings.warn(StaleStateWarning(new_status.staleness_seconds), stacklevel=2)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
