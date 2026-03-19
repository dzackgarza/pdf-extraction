"""Pydantic models for PDF extraction job state management.

This module defines the canonical data models for tracking Kaggle extraction jobs.
All state tracking flows through these models - they are the Single Source of Truth.
"""

from __future__ import annotations

from datetime import UTC, datetime
from enum import Enum
from pathlib import Path
from typing import Self

from pydantic import BaseModel, ConfigDict, Field


class JobState(str, Enum):
    """Explicit state machine for extraction jobs.

    States represent the canonical workflow progression. Transitions must be
    explicit - no automatic state changes.

    State flow:
        prepared → submitted → running → complete_remote → downloaded → merged
                                                          ↘ failed ↗
    """

    PREPARED = "prepared"
    SUBMITTED = "submitted"
    RUNNING = "running"
    COMPLETE_REMOTE = "complete_remote"
    DOWNLOADED = "downloaded"
    MERGED = "merged"
    FAILED = "failed"


class KernelStatus(str, Enum):
    """Kaggle kernel execution status (from remote API).

    These values come directly from Kaggle API and are not under our control.
    """

    QUEUED = "queued"
    RUNNING = "running"
    COMPLETE = "complete"
    ERROR = "error"
    CANCELLED = "cancelled"


class RemoteJobState(BaseModel):
    """State queried from Kaggle API (remote truth).

    This is refreshed on every `kaggle-status` call. Never cached without timestamp.
    """

    model_config = ConfigDict(strict=True, frozen=True, extra="forbid")

    kernel_ref: str = Field(
        ..., description="Kaggle kernel reference (user/kernel-slug)"
    )
    status: KernelStatus = Field(..., description="Current kernel status from Kaggle")
    started_at: datetime | None = Field(
        None, description="Kernel start time (Kaggle time)"
    )
    completed_at: datetime | None = Field(
        None, description="Kernel completion time (Kaggle time)"
    )
    error_message: str | None = Field(
        None, description="Error message if status is ERROR"
    )
    query_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="When this state was queried from Kaggle",
    )

    @property
    def is_complete(self) -> bool:
        """True if kernel finished successfully."""
        return self.status == KernelStatus.COMPLETE

    @property
    def is_failed(self) -> bool:
        """True if kernel failed or was cancelled."""
        return self.status in (KernelStatus.ERROR, KernelStatus.CANCELLED)

    @property
    def is_running(self) -> bool:
        """True if kernel is still executing."""
        return self.status in (KernelStatus.QUEUED, KernelStatus.RUNNING)


class LocalJobState(BaseModel):
    """Local workflow state (our orchestration).

    Tracks what we've done with the job locally. Independent of remote state.
    """

    model_config = ConfigDict(strict=True, frozen=True, extra="forbid")

    state: JobState = Field(..., description="Current local workflow state")
    downloaded: bool = Field(
        False, description="True if output files downloaded locally"
    )
    merged: bool = Field(
        False, description="True if this job was merged into a combined output"
    )
    merge_target: Path | None = Field(
        None, description="Path to merged output if merged=True"
    )
    last_updated: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="When local state was last modified",
    )

    def transition_to(self, new_state: JobState) -> Self:
        """Create new state with updated state and timestamp."""
        return self.model_copy(
            update={
                "state": new_state,
                "last_updated": datetime.now(UTC),
            }
        )

    def mark_downloaded(self) -> Self:
        """Mark as downloaded."""
        return self.model_copy(
            update={
                "downloaded": True,
                "last_updated": datetime.now(UTC),
            }
        )

    def mark_merged(self, target: Path) -> Self:
        """Mark as merged into target."""
        return self.model_copy(
            update={
                "merged": True,
                "merge_target": target,
                "last_updated": datetime.now(UTC),
            }
        )


class JobManifest(BaseModel):
    """Job configuration and metadata (immutable after creation).

    Created when job is prepared, never modified.
    """

    model_config = ConfigDict(strict=True, frozen=True)

    job_dir: Path = Field(..., description="Absolute path to job directory")
    pdf_path: Path = Field(..., description="Source PDF file path")
    page_range: tuple[int, int] = Field(
        ..., description="Page range (start, end) inclusive"
    )
    kernel_name: str = Field(..., description="Kaggle kernel name template")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Job creation timestamp",
    )

    @property
    def page_count(self) -> int:
        """Number of pages in this job."""
        start, end = self.page_range
        return end - start + 1


class JobStatus(BaseModel):
    """Canonical job status combining remote and local state.

    This is the Single Source of Truth for job status. Always query remote
    first, then combine with local state.
    """

    model_config = ConfigDict(strict=True)

    manifest: JobManifest = Field(..., description="Job configuration (immutable)")
    remote: RemoteJobState | None = Field(
        None, description="Remote Kaggle state (None if never queried)"
    )
    local: LocalJobState = Field(..., description="Local workflow state")

    @property
    def effective_state(self) -> JobState:
        """Compute effective state from remote + local.

        Remote state takes precedence for failure detection.
        Local state tracks our workflow progress.
        """
        # Remote failure overrides everything
        if self.remote and self.remote.is_failed:
            return JobState.FAILED

        # Remote completion + not downloaded = complete_remote
        if self.remote and self.remote.is_complete and not self.local.downloaded:
            return JobState.COMPLETE_REMOTE

        # Use local state for workflow tracking
        return self.local.state

    @property
    def is_stale(self) -> bool:
        """True if remote state hasn't been queried in >5 minutes."""
        if not self.remote:
            return True
        age = datetime.now(UTC) - self.remote.query_timestamp
        return age.total_seconds() > 300  # 5 minutes

    @property
    def staleness_seconds(self) -> float:
        """Seconds since last remote query."""
        if not self.remote:
            return float("inf")
        return (datetime.now(UTC) - self.remote.query_timestamp).total_seconds()

    def with_remote(self, remote: RemoteJobState) -> Self:
        """Update with fresh remote state."""
        return self.model_copy(update={"remote": remote})

    def with_local(self, local: LocalJobState) -> Self:
        """Update local state."""
        return self.model_copy(update={"local": local})


class BatchManifest(BaseModel):
    """Collection of related jobs (e.g., multi-batch extraction).

    Used for tracking batch operations and merged outputs.
    """

    model_config = ConfigDict(strict=True)

    name: str = Field(..., description="Batch identifier")
    source_pdf: Path = Field(..., description="Original PDF being extracted")
    jobs: list[Path] = Field(
        default_factory=list, description="List of job directory paths"
    )
    merged_output: Path | None = Field(
        None, description="Path to merged markdown if complete"
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Batch creation timestamp",
    )

    def add_job(self, job_dir: Path) -> Self:
        """Add job to batch."""
        return self.model_copy(update={"jobs": self.jobs + [job_dir]})

    def mark_merged(self, output_path: Path) -> Self:
        """Mark batch as merged."""
        return self.model_copy(update={"merged_output": output_path})


class InvalidStateTransition(Exception):
    """Raised when attempting invalid state transition."""

    def __init__(self, from_state: JobState, to_state: JobState, reason: str):
        self.from_state = from_state
        self.to_state = to_state
        self.reason = reason
        super().__init__(
            f"Invalid transition {from_state.value} → {to_state.value}: {reason}"
        )


class StaleStateWarning(Warning):
    """Warning when using stale cached state."""

    def __init__(self, staleness_seconds: float):
        self.staleness_seconds = staleness_seconds
        minutes = staleness_seconds / 60
        super().__init__(
            f"Remote state is {minutes:.1f} minutes old - consider refreshing"
        )
