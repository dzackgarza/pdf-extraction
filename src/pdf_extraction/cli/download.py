"""Download command for retrieving completed kernel output.

Downloads output files from Kaggle and transitions COMPLETE_REMOTE → DOWNLOADED.
"""

from __future__ import annotations

import json
import sys
from datetime import UTC
from pathlib import Path
from zipfile import ZipFile

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

app = App(help="Download completed kernel output from Kaggle")


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
        # Try to load remote state from status
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


def extract_mineru_summary(zip_path: Path, dest_dir: Path) -> Path | None:
    """Extract mineru-summary.json from zip if present.

    Args:
        zip_path: Path to mineru-output.zip
        dest_dir: Destination directory

    Returns:
        Path to extracted summary or None
    """
    try:
        with ZipFile(zip_path) as zf:
            # Look for mineru-summary.json in root or nested
            for name in zf.namelist():
                if name.endswith("mineru-summary.json"):
                    zf.extract(name, dest_dir)
                    return dest_dir / name
    except KeyError:
        pass
    return None


@app.command
def download(
    job_dir: Path,
    force: bool = False,
    extract_zip: bool = True,
) -> None:
    """Download kernel output from Kaggle.

    Validates kernel is complete, downloads output files, transitions to DOWNLOADED.

    Args:
        job_dir: Path to job directory
        force: Force download even if already downloaded
        extract_zip: Extract mineru-output.zip if present
    """
    # Load current status
    try:
        status = load_status(job_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if already downloaded
    downloads_dir = job_dir / "downloads"
    if downloads_dir.exists() and any(downloads_dir.iterdir()) and not force:
        print(f"Warning: Output already downloaded to {downloads_dir}")
        print("Use --force to re-download")
        if status.local.downloaded:
            print("Local state already marks as downloaded")
            return
        # Continue to update state even if files exist

    # Get kernel ref
    kernel_ref = status.remote.kernel_ref if status.remote else None
    if not kernel_ref:
        # Try to get from status.json
        status_file = job_dir / "status.json"
        if status_file.exists():
            with open(status_file) as f:
                data = json.load(f)
            kernel_ref = data.get("kernel_ref")

    if not kernel_ref:
        print(
            "Error: No kernel reference found - job not yet submitted", file=sys.stderr
        )
        sys.exit(1)

    # Query remote state first
    client = KaggleClient()
    try:
        remote = client.get_kernel_status(kernel_ref)
    except KernelNotFoundError:
        print(f"Error: Kernel not found: {kernel_ref}", file=sys.stderr)
        sys.exit(1)
    except KaggleAPIError as e:
        print(f"Error querying kernel status: {e.message}", file=sys.stderr)
        sys.exit(1)

    # Validate kernel is complete
    if remote.status != KernelStatus.COMPLETE:
        print(
            f"Error: Kernel is not complete (status: {remote.status.value})",
            file=sys.stderr,
        )
        print("Wait for kernel to complete before downloading", file=sys.stderr)
        sys.exit(1)

    print(f"Downloading output for {job_dir.name}...")
    print(f"  Kernel: {kernel_ref}")
    print(f"  Remote status: {remote.status.value}")

    # Download output
    try:
        files = client.download_output(kernel_ref, downloads_dir)
        print(f"  Downloaded {len(files)} files to {downloads_dir}")

        # Extract zip if present
        zip_path = downloads_dir / "mineru-output.zip"
        if zip_path.exists() and extract_zip:
            print(f"  Extracting {zip_path.name}...")
            with ZipFile(zip_path) as zf:
                zf.extractall(downloads_dir)
            extracted_count = sum(1 for _ in (downloads_dir).rglob("*") if _.is_file())
            print(f"  Extracted {extracted_count} files from zip")

        # Look for mineru-summary.json
        summary_path = None
        for p in downloads_dir.rglob("mineru-summary.json"):
            summary_path = p
            break

        if summary_path:
            print(f"  Found mineru-summary.json: {summary_path}")
        else:
            print("  Warning: mineru-summary.json not found")

        # Update status - transition to DOWNLOADED
        from ..models import JobState

        new_local = status.local.transition_to(JobState.DOWNLOADED).mark_downloaded()
        new_status = status.with_remote(remote).with_local(new_local)
        save_status(new_status)

        print(
            f"  State: {status.effective_state.value} → {new_status.effective_state.value}"
        )
        print("Download complete!")

    except KaggleAPIError as e:
        print(f"Error downloading output: {e.message}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
