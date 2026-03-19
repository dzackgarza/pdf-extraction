"""Tests for PDF extraction models."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from pydantic import ValidationError

from pdf_extraction.models import (
    JobManifest,
    JobState,
    JobStatus,
    KernelStatus,
    LocalJobState,
    RemoteJobState,
)


class TestJobState:
    """Test JobState enum."""

    def test_all_states_exist(self):
        """Verify all expected states are defined."""
        states = [s.value for s in JobState]
        assert "prepared" in states
        assert "submitted" in states
        assert "running" in states
        assert "complete_remote" in states
        assert "downloaded" in states
        assert "merged" in states
        assert "failed" in states


class TestRemoteJobState:
    """Test RemoteJobState model."""

    def test_create_complete_state(self):
        """Create remote state for completed kernel."""
        remote = RemoteJobState(
            kernel_ref="user/kernel-name",
            status=KernelStatus.COMPLETE,
            started_at=datetime(2026, 3, 19, 10, 0, tzinfo=UTC),
            completed_at=datetime(2026, 3, 19, 12, 0, tzinfo=UTC),
        )
        assert remote.is_complete
        assert not remote.is_failed
        assert not remote.is_running

    def test_create_failed_state(self):
        """Create remote state for failed kernel."""
        remote = RemoteJobState(
            kernel_ref="user/kernel-name",
            status=KernelStatus.ERROR,
            error_message="Out of memory",
        )
        assert remote.is_failed
        assert not remote.is_complete
        assert remote.error_message == "Out of memory"

    def test_create_running_state(self):
        """Create remote state for running kernel."""
        remote = RemoteJobState(
            kernel_ref="user/kernel-name",
            status=KernelStatus.RUNNING,
        )
        assert remote.is_running
        assert not remote.is_complete
        assert not remote.is_failed

    def test_frozen_model(self):
        """Verify remote state is immutable."""
        remote = RemoteJobState(
            kernel_ref="user/kernel-name",
            status=KernelStatus.QUEUED,
        )
        with pytest.raises(ValidationError):
            remote.status = KernelStatus.RUNNING  # type: ignore[misc]


class TestLocalJobState:
    """Test LocalJobState model."""

    def test_create_initial_state(self):
        """Create initial local state."""
        local = LocalJobState(state=JobState.PREPARED)
        assert local.state == JobState.PREPARED
        assert not local.downloaded
        assert not local.merged
        assert local.merge_target is None

    def test_transition_to(self):
        """Test state transition creates new instance."""
        local = LocalJobState(state=JobState.PREPARED)
        new_local = local.transition_to(JobState.SUBMITTED)
        assert new_local.state == JobState.SUBMITTED
        assert local.state == JobState.PREPARED  # Original unchanged
        assert new_local.last_updated > local.last_updated

    def test_mark_downloaded(self):
        """Test marking as downloaded."""
        local = LocalJobState(state=JobState.COMPLETE_REMOTE)
        new_local = local.mark_downloaded()
        assert new_local.downloaded
        assert new_local.state == JobState.COMPLETE_REMOTE  # State unchanged

    def test_mark_merged(self):
        """Test marking as merged."""
        local = LocalJobState(state=JobState.DOWNLOADED)
        target = Path("/output/merged.md")
        new_local = local.mark_merged(target)
        assert new_local.merged
        assert new_local.merge_target == target


class TestJobManifest:
    """Test JobManifest model."""

    def test_create_manifest(self):
        """Create job manifest."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test-job"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test-kernel",
        )
        assert manifest.page_count == 100
        assert manifest.job_dir.is_absolute()
        assert manifest.pdf_path.is_absolute()

    def test_page_count_calculation(self):
        """Test page count is inclusive."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 1),  # Single page
            kernel_name="test",
        )
        assert manifest.page_count == 1


class TestJobStatus:
    """Test JobStatus model combining remote and local state."""

    def test_create_without_remote(self):
        """Create status without remote query."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test",
        )
        local = LocalJobState(state=JobState.PREPARED)
        status = JobStatus(manifest=manifest, remote=None, local=local)
        assert status.remote is None
        assert status.is_stale

    def test_effective_state_remote_failure(self):
        """Remote failure overrides local state."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test",
        )
        local = LocalJobState(state=JobState.RUNNING)
        remote = RemoteJobState(
            kernel_ref="user/test",
            status=KernelStatus.ERROR,
        )
        status = JobStatus(manifest=manifest, remote=remote, local=local)
        assert status.effective_state == JobState.FAILED

    def test_effective_state_complete_not_downloaded(self):
        """Complete remote + not downloaded = complete_remote."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test",
        )
        local = LocalJobState(state=JobState.RUNNING)
        remote = RemoteJobState(
            kernel_ref="user/test",
            status=KernelStatus.COMPLETE,
        )
        status = JobStatus(manifest=manifest, remote=remote, local=local)
        assert status.effective_state == JobState.COMPLETE_REMOTE

    def test_staleness_detection(self):
        """Detect stale remote state."""
        from datetime import timedelta

        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test",
        )
        local = LocalJobState(state=JobState.RUNNING)
        # Create remote state from 10 minutes ago
        old_time = datetime.now(UTC) - timedelta(minutes=10)
        remote = RemoteJobState(
            kernel_ref="user/test",
            status=KernelStatus.RUNNING,
            query_timestamp=old_time,
        )
        status = JobStatus(manifest=manifest, remote=remote, local=local)
        assert status.is_stale
        assert status.staleness_seconds > 300

    def test_with_remote_update(self):
        """Update with fresh remote state creates new instance."""
        manifest = JobManifest(
            job_dir=Path("/jobs/test"),
            pdf_path=Path("/pdfs/test.pdf"),
            page_range=(1, 100),
            kernel_name="test",
        )
        local = LocalJobState(state=JobState.RUNNING)
        old_remote = RemoteJobState(
            kernel_ref="user/test",
            status=KernelStatus.RUNNING,
        )
        status = JobStatus(manifest=manifest, remote=old_remote, local=local)

        # Simulate kernel completion
        new_remote = RemoteJobState(
            kernel_ref="user/test",
            status=KernelStatus.COMPLETE,
        )
        new_status = status.with_remote(new_remote)
        assert new_status.effective_state == JobState.COMPLETE_REMOTE
        assert status.effective_state == JobState.RUNNING  # Original unchanged


class TestStrictValidation:
    """Test Pydantic strict mode catches type errors."""

    def test_reject_wrong_type(self):
        """Strict mode rejects type coercion."""
        with pytest.raises(ValidationError):
            RemoteJobState(
                kernel_ref="user/test",
                status="complete",  # String instead of KernelStatus enum
            )

    def test_reject_extra_fields(self):
        """Strict mode rejects extra fields."""
        with pytest.raises(ValidationError):
            LocalJobState(
                state=JobState.PREPARED,
                extra_field="not allowed",  # type: ignore[call-arg]
            )
