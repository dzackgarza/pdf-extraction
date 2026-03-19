"""Merge command for combining multiple batch outputs.

Merges markdown files from multiple downloaded jobs into a single output.
Transitions DOWNLOADED → MERGED.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from cyclopts import App

from ..models import JobManifest, JobState, JobStatus, LocalJobState

app = App(help="Merge multiple batch outputs into single markdown")


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


def find_markdown_files(job_dir: Path) -> list[Path]:
    """Find all markdown files in job directory.

    Args:
        job_dir: Path to job directory

    Returns:
        List of markdown file paths
    """
    downloads_dir = job_dir / "downloads"
    if not downloads_dir.exists():
        return []

    md_files = []
    for p in downloads_dir.rglob("*.md"):
        if p.is_file():
            md_files.append(p)

    return sorted(md_files)


def merge_markdown_files(md_files: list[Path], output_path: Path) -> int:
    """Merge multiple markdown files into single output.

    Args:
        md_files: List of markdown files to merge
        output_path: Destination path for merged output

    Returns:
        Total number of lines written
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total_lines = 0
    with open(output_path, "w") as out:
        for i, md_file in enumerate(md_files):
            if i > 0:
                out.write("\n\n")  # Add separator between files

            with open(md_file) as f:
                content = f.read()
                out.write(content)
                total_lines += content.count("\n") + 1

    return total_lines


@app.command
def merge(
    job_dirs: list[Path],
    output: Path | None = None,
    dry_run: bool = False,
) -> None:
    """Merge multiple batch outputs into single markdown.

    All jobs must be in DOWNLOADED state. Creates merged output and updates state.

    Args:
        job_dirs: List of job directories to merge (in order)
        output: Output path for merged markdown (default: first job's manifest markdown_path)
        dry_run: Show what would be merged without writing
    """
    if len(job_dirs) < 2:
        print("Error: Need at least 2 job directories to merge", file=sys.stderr)
        sys.exit(1)

    # Load all job statuses
    statuses = []
    for job_dir in job_dirs:
        if not job_dir.exists():
            print(f"Error: Job directory not found: {job_dir}", file=sys.stderr)
            sys.exit(1)

        try:
            status = load_status(job_dir)
            statuses.append(status)
        except FileNotFoundError as e:
            print(f"Error loading {job_dir.name}: {e}", file=sys.stderr)
            sys.exit(1)

    # Validate all jobs are downloaded
    for status in statuses:
        if not status.local.downloaded:
            print(
                f"Error: Job {status.manifest.job_dir.name} not downloaded (state: {status.effective_state.value})",
                file=sys.stderr,
            )
            print("All jobs must be downloaded before merging", file=sys.stderr)
            sys.exit(1)

    # Find markdown files in each job
    all_md_files = []
    for i, status in enumerate(statuses):
        md_files = find_markdown_files(status.manifest.job_dir)
        if not md_files:
            print(
                f"Warning: No markdown files found in {status.manifest.job_dir.name}",
                file=sys.stderr,
            )
        all_md_files.extend(md_files)
        print(f"Job {i + 1}: {status.manifest.job_dir.name}")
        print(
            f"  Pages: {status.manifest.page_range[0]}-{status.manifest.page_range[1]}"
        )
        print(f"  Markdown files: {len(md_files)}")

    if not all_md_files:
        print("Error: No markdown files found to merge", file=sys.stderr)
        sys.exit(1)

    # Determine output path
    if output is None:
        # Use first job's manifest markdown_path if available
        first_manifest = statuses[0].manifest
        output = first_manifest.job_dir / "merged" / "output.md"

    print(f"\nMerging {len(all_md_files)} markdown files into:")
    print(f"  {output}")

    if dry_run:
        print("\nDry run - not writing output")
        return

    # Perform merge
    total_lines = merge_markdown_files(all_md_files, output)
    print(f"\nMerged {total_lines} lines")

    # Update status for all jobs
    for status in statuses:
        new_local = status.local.transition_to(JobState.MERGED).mark_merged(output)
        new_status = status.with_local(new_local)
        save_status(new_status)
        print(f"Updated {status.manifest.job_dir.name}: DOWNLOADED → MERGED")

    print("\nMerge complete!")


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
