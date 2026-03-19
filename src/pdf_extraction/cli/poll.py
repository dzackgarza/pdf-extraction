"""Poll command for monitoring long-running Kaggle jobs.

Continuously queries kernel status until completion or timeout.
"""

from __future__ import annotations

import json
import sys
import time
from datetime import UTC, datetime
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
)

app = App(help="Monitor long-running Kaggle kernel execution")


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
def poll(
    job_dir: Path,
    interval: int = 30,
    timeout: int | None = None,
    quiet: bool = False,
) -> None:
    """Monitor kernel execution until completion.

    Continuously queries Kaggle API and updates local state.
    Exits when kernel completes, errors, or timeout is reached.

    Args:
        job_dir: Path to job directory
        interval: Polling interval in seconds (default: 30)
        timeout: Maximum time to wait in seconds (None = infinite)
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

    client = KaggleClient()
    start_time = time.time()
    last_status = None
    last_state = status.effective_state

    if not quiet:
        print(f"Polling {job_dir.name}...")
        print(f"  Kernel: {kernel_ref}")
        print(f"  Interval: {interval}s")
        if timeout:
            print(f"  Timeout: {timeout}s")
        print()

    try:
        while True:
            # Check timeout
            if timeout and (time.time() - start_time) > timeout:
                print(
                    f"Timeout after {int(time.time() - start_time)}s", file=sys.stderr
                )
                sys.exit(1)

            # Query remote
            try:
                remote = client.get_kernel_status(kernel_ref)
            except KernelNotFoundError:
                print(f"Error: Kernel not found: {kernel_ref}", file=sys.stderr)
                sys.exit(1)
            except KaggleAPIError as e:
                print(f"API error: {e.message}", file=sys.stderr)
                time.sleep(interval)
                continue

            # Update status
            status = status.with_remote(remote)
            save_status(status)

            # Check for state change
            current_state = status.effective_state
            status_changed = last_status != remote.status
            state_changed = last_state != current_state

            if not quiet or status_changed:
                timestamp = datetime.now().strftime("%H:%M:%S")
                if status_changed:
                    print(f"[{timestamp}] {remote.status.value}")

                if state_changed:
                    print(
                        f"[{timestamp}] State: {last_state.value} → {current_state.value}"
                    )

            # Check terminal states
            if remote.status == KernelStatus.COMPLETE:
                if not quiet:
                    print(f"\nKernel completed after {int(time.time() - start_time)}s")
                # Transition to COMPLETE_REMOTE if not already downloaded
                if not status.local.downloaded:
                    new_local = status.local.transition_to(JobState.COMPLETE_REMOTE)
                    status = status.with_local(new_local)
                    save_status(status)
                sys.exit(0)

            elif remote.status in (KernelStatus.ERROR, KernelStatus.CANCELLED):
                print(
                    f"\nKernel failed with status: {remote.status.value}",
                    file=sys.stderr,
                )
                if remote.error_message:
                    print(f"Error: {remote.error_message}", file=sys.stderr)
                # Transition to FAILED
                new_local = status.local.transition_to(JobState.FAILED)
                status = status.with_local(new_local)
                save_status(status)
                sys.exit(1)

            # Update tracking
            last_status = remote.status
            last_state = current_state

            # Wait for next poll
            time.sleep(interval)

    except KeyboardInterrupt:
        print(f"\nInterrupted after {int(time.time() - start_time)}s")
        print(f"Last status: {last_status.value if last_status else 'unknown'}")
        sys.exit(130)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
