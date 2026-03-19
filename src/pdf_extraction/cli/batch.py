"""Batch operations for managing multiple jobs.

Provides commands for submitting, status checking, and downloading multiple jobs at once.
"""

from __future__ import annotations

import json
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

app = App(help="Batch operations for multiple jobs")

submit_group = App(name="submit", help="Submit multiple jobs")
download_group = App(name="download", help="Download multiple jobs")
status_group = App(name="status", help="Check status of multiple jobs")

app.command(submit_group)
app.command(download_group)
app.command(status_group)


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


@submit_group.command(name="all")
def submit_all(
    job_dirs: list[Path],
    kernel_prefix: str = "",
    wait: bool = False,
) -> None:
    """Submit multiple jobs to Kaggle.

    Args:
        job_dirs: List of job directories to submit
        kernel_prefix: Optional prefix for kernel names
        wait: Wait for each kernel to start running
    """
    client = KaggleClient()
    success_count = 0
    fail_count = 0

    for i, job_dir in enumerate(job_dirs):
        if not job_dir.exists():
            print(f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (not found)")
            fail_count += 1
            continue

        try:
            status = load_status(job_dir)
        except FileNotFoundError as e:
            print(f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} ({e})")
            fail_count += 1
            continue

        # Check if already submitted
        if status.local.state != JobState.PREPARED:
            print(
                f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (state: {status.local.state.value})"
            )
            continue

        # Get kernel name
        kernel_name = status.manifest.kernel_name
        if kernel_prefix and kernel_name != "unknown":
            kernel_name = f"{kernel_prefix}{kernel_name}"

        print(f"[{i + 1}/{len(job_dirs)}] Submitting: {job_dir.name}")
        print(f"  Kernel: {kernel_name}")

        try:
            # Submit kernel
            import subprocess

            cmd = ["kaggle", "kernels", "start", kernel_name, "-p", str(job_dir)]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )

            if result.returncode != 0:
                raise KaggleAPIError(
                    f"Kernel submission failed: {result.stderr.strip()}", command=cmd
                )

            # Parse kernel ref from output
            output = result.stdout.strip()
            if "https://www.kaggle.com/kernels/code/" in output:
                kernel_ref = output.split("https://www.kaggle.com/kernels/code/")[
                    -1
                ].strip()
            else:
                kernel_ref = kernel_name

            # Create remote state
            remote = RemoteJobState(
                kernel_ref=kernel_ref,
                status=KernelStatus.QUEUED,
                started_at=datetime.now(UTC),
            )

            # Transition state
            new_local = status.local.transition_to(JobState.SUBMITTED)
            new_status = status.with_remote(remote).with_local(new_local)
            save_status(new_status)

            print(f"  Kernel ref: {kernel_ref}")
            print(f"  State: {JobState.PREPARED.value} → {JobState.SUBMITTED.value}")
            success_count += 1

            if wait:
                print("  Waiting for kernel to start...")
                for _ in range(10):
                    import time

                    time.sleep(5)
                    remote = client.get_kernel_status(kernel_ref)
                    if remote.status == KernelStatus.RUNNING:
                        print("  Kernel is running!")
                        new_status = new_status.with_remote(remote)
                        save_status(new_status)
                        break
                    print(f"  Status: {remote.status.value}...")
                else:
                    print("  Still queued (use poll to continue monitoring)")

        except KaggleAPIError as e:
            print(f"  Error: {e.message}")
            new_local = status.local.transition_to(JobState.FAILED)
            new_status = status.with_local(new_local)
            save_status(new_status)
            fail_count += 1

    print(f"\nBatch submit complete: {success_count} succeeded, {fail_count} failed")


@status_group.command(name="all")
def status_all(
    job_dirs: list[Path],
    json_output: bool = False,
) -> None:
    """Check status of multiple jobs.

    Args:
        job_dirs: List of job directories to check
        json_output: Output as JSON
    """
    client = KaggleClient()
    results = []

    for i, job_dir in enumerate(job_dirs):
        if not job_dir.exists():
            results.append(
                {
                    "job_dir": str(job_dir),
                    "error": "Directory not found",
                }
            )
            continue

        try:
            status = load_status(job_dir)
        except FileNotFoundError as e:
            results.append(
                {
                    "job_dir": str(job_dir),
                    "error": str(e),
                }
            )
            continue

        # Query remote
        kernel_ref = status.remote.kernel_ref if status.remote else None
        if not kernel_ref:
            status_file = job_dir / "status.json"
            if status_file.exists():
                with open(status_file) as f:
                    data = json.load(f)
                kernel_ref = data.get("kernel_ref")

        if kernel_ref:
            try:
                remote = client.get_kernel_status(kernel_ref)
                status = status.with_remote(remote)
                save_status(status)
            except (KernelNotFoundError, KaggleAPIError):
                pass

        results.append(
            {
                "job_dir": str(job_dir),
                "job_name": job_dir.name,
                "page_range": list(status.manifest.page_range),
                "kernel_ref": status.remote.kernel_ref if status.remote else None,
                "remote_status": status.remote.status.value if status.remote else None,
                "local_state": status.effective_state.value,
                "downloaded": status.local.downloaded,
                "merged": status.local.merged,
            }
        )

    if json_output:
        print(json.dumps(results, indent=2))
    else:
        # Table format
        print(
            f"{'Job':<50} {'Pages':<15} {'Remote':<12} {'Local':<20} {'Downloaded':<10}"
        )
        print("-" * 107)
        for r in results:
            if "error" in r:
                print(
                    f"{r['job_name']:<50} {'-':<15} {'-':<12} {'ERROR':<20} {'-':<10}"
                )
                print(f"  Error: {r['error']}")
            else:
                pages = f"{r['page_range'][0]}-{r['page_range'][1]}"
                remote = r["remote_status"] or "-"
                local = r["local_state"]
                downloaded = "Yes" if r["downloaded"] else "No"
                print(
                    f"{r['job_name']:<50} {pages:<15} {remote:<12} {local:<20} {downloaded:<10}"
                )


@download_group.command(name="all")
def download_all(
    job_dirs: list[Path],
    force: bool = False,
) -> None:
    """Download output from multiple completed jobs.

    Args:
        job_dirs: List of job directories to download
        force: Force download even if already downloaded
    """
    client = KaggleClient()
    success_count = 0
    fail_count = 0
    skip_count = 0

    for i, job_dir in enumerate(job_dirs):
        if not job_dir.exists():
            print(f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (not found)")
            fail_count += 1
            continue

        try:
            status = load_status(job_dir)
        except FileNotFoundError as e:
            print(f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} ({e})")
            fail_count += 1
            continue

        # Check if already downloaded
        downloads_dir = job_dir / "downloads"
        if downloads_dir.exists() and any(downloads_dir.iterdir()) and not force:
            print(
                f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (already downloaded)"
            )
            skip_count += 1
            # Still update state
            if not status.local.downloaded:
                new_local = status.local.mark_downloaded()
                new_status = status.with_local(new_local)
                save_status(new_status)
            continue

        # Get kernel ref
        kernel_ref = status.remote.kernel_ref if status.remote else None
        if not kernel_ref:
            status_file = job_dir / "status.json"
            if status_file.exists():
                with open(status_file) as f:
                    data = json.load(f)
                kernel_ref = data.get("kernel_ref")

        if not kernel_ref:
            print(f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (no kernel ref)")
            fail_count += 1
            continue

        # Query remote
        try:
            remote = client.get_kernel_status(kernel_ref)
        except (KernelNotFoundError, KaggleAPIError) as e:
            print(f"[{i + 1}/{len(job_dirs)}] Error: {job_dir.name} ({e})")
            fail_count += 1
            continue

        # Check if complete
        if remote.status != KernelStatus.COMPLETE:
            print(
                f"[{i + 1}/{len(job_dirs)}] Skip: {job_dir.name} (status: {remote.status.value})"
            )
            skip_count += 1
            continue

        print(f"[{i + 1}/{len(job_dirs)}] Downloading: {job_dir.name}")

        try:
            files = client.download_output(kernel_ref, downloads_dir)
            print(f"  Downloaded {len(files)} files")

            # Update state
            new_local = status.local.transition_to(
                JobState.DOWNLOADED
            ).mark_downloaded()
            new_status = status.with_remote(remote).with_local(new_local)
            save_status(new_status)

            success_count += 1

        except KaggleAPIError as e:
            print(f"  Error: {e.message}")
            fail_count += 1

    print(
        f"\nBatch download complete: {success_count} succeeded, {fail_count} failed, {skip_count} skipped"
    )


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
