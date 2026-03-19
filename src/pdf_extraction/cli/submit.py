"""Submit command for submitting prepared jobs to Kaggle.

Transitions job from PREPARED → SUBMITTED and starts kernel execution.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from cyclopts import App

from ..kaggle_client import KaggleAPIError, KaggleClient
from ..models import (
    JobManifest,
    JobState,
    JobStatus,
    KernelStatus,
    LocalJobState,
    RemoteJobState,
)

app = App(help="Submit prepared job to Kaggle")


def load_manifest(job_dir: Path) -> JobManifest:
    """Load job manifest from directory.

    Args:
        job_dir: Path to job directory

    Returns:
        JobManifest instance
    """
    manifest_file = job_dir / "manifest.json"
    if not manifest_file.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_file}")

    with open(manifest_file) as f:
        data = json.load(f)

    return JobManifest(
        job_dir=Path(data.get("job_dir", str(job_dir))),
        pdf_path=Path(data["pdf"]),
        page_range=(data.get("start_page", 1), data.get("end_page", 1)),
        kernel_name=data.get("kernel_name", "unknown"),
    )


def load_or_create_status(job_dir: Path) -> JobStatus:
    """Load existing status or create new one.

    Args:
        job_dir: Path to job directory

    Returns:
        JobStatus instance
    """
    manifest = load_manifest(job_dir)
    status_file = job_dir / "status.json"

    local_state = JobState.PREPARED
    downloaded = False
    merged = False

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

    local = LocalJobState(
        state=local_state,
        downloaded=downloaded,
        merged=merged,
    )

    return JobStatus(manifest=manifest, remote=None, local=local)


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


def submit_kernel(job_dir: Path, kernel_name: str) -> str:
    """Submit kernel to Kaggle.

    Args:
        job_dir: Path to job directory (contains kernel source)
        kernel_name: Kaggle kernel name (user/slug format)

    Returns:
        Kernel reference string

    Raises:
        KaggleAPIError: If submission fails
    """
    # Use kaggle kernels start to submit/update kernel
    cmd = ["kaggle", "kernels", "start", kernel_name, "-p", str(job_dir)]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except subprocess.TimeoutExpired:
        raise KaggleAPIError("Kernel submission timed out", command=cmd)

    if result.returncode != 0:
        raise KaggleAPIError(
            f"Kernel submission failed: {result.stderr.strip()}", command=cmd
        )

    # Parse output to get kernel ref
    # Output format: "Kernel started successfully: https://www.kaggle.com/kernels/code/..."
    output = result.stdout.strip()
    if "https://www.kaggle.com/kernels/code/" in output:
        # Extract kernel ref from URL
        url = output.split("https://www.kaggle.com/kernels/code/")[-1].strip()
        return url

    # Fallback: use the provided kernel_name
    return kernel_name


@app.command
def submit(
    job_dir: Path,
    kernel_name: str | None = None,
    wait: bool = False,
) -> None:
    """Submit a prepared job to Kaggle.

    Validates job is in PREPARED state, submits kernel, transitions to SUBMITTED.

    Args:
        job_dir: Path to job directory
        kernel_name: Kaggle kernel name (default: read from manifest)
        wait: If True, wait for kernel to start running
    """
    # Load current status
    try:
        status = load_or_create_status(job_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate state transition
    current_state = status.local.state
    if current_state != JobState.PREPARED:
        print(
            f"Error: Cannot submit job in {current_state.value} state", file=sys.stderr
        )
        print("Job must be in PREPARED state to submit", file=sys.stderr)
        sys.exit(1)

    # Get kernel name
    if not kernel_name:
        kernel_name = status.manifest.kernel_name
        if not kernel_name or kernel_name == "unknown":
            print(
                "Error: No kernel name specified and none found in manifest",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"Submitting job {job_dir.name}...")
    print(f"  Kernel: {kernel_name}")
    print(f"  Pages: {status.manifest.page_range[0]}-{status.manifest.page_range[1]}")

    try:
        # Submit kernel
        kernel_ref = submit_kernel(job_dir, kernel_name)
        print(f"  Kernel ref: {kernel_ref}")

        # Create remote state
        remote = RemoteJobState(
            kernel_ref=kernel_ref,
            status=KernelStatus.QUEUED,
            started_at=datetime.now(UTC),
        )

        # Transition state
        new_local = status.local.transition_to(JobState.SUBMITTED)
        new_status = status.with_remote(remote).with_local(new_local)

        # Save updated status
        save_status(new_status)

        print(f"  State: {JobState.PREPARED.value} → {JobState.SUBMITTED.value}")
        print("Job submitted successfully!")

        if wait:
            print("\nWaiting for kernel to start...")
            client = KaggleClient()
            import time

            for _ in range(10):  # Wait up to 50 seconds
                time.sleep(5)
                remote = client.get_kernel_status(kernel_ref)
                if remote.status == KernelStatus.RUNNING:
                    print("Kernel is now running!")
                    new_status = new_status.with_remote(remote)
                    save_status(new_status)
                    break
                print(f"  Status: {remote.status.value}...")
            else:
                print(
                    "Kernel still queued (use 'just kaggle-poll' to continue monitoring)"
                )

    except KaggleAPIError as e:
        print(f"Error: {e.message}", file=sys.stderr)
        # Transition to FAILED
        new_local = status.local.transition_to(JobState.FAILED)
        new_status = status.with_local(new_local)
        save_status(new_status)
        sys.exit(1)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
