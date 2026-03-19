"""Tests for state machine transitions."""

from __future__ import annotations

import pytest

from pdf_extraction.models import InvalidStateTransition, JobState
from pdf_extraction.state_machine import (
    describe_state,
    get_valid_transitions,
    get_workflow_progress,
    is_terminal_state,
    is_valid_transition,
    transition,
)


class TestValidTransitions:
    """Test valid state transitions."""

    def test_prepared_to_submitted(self):
        """PREPARED → SUBMITTED is valid."""
        assert transition(JobState.PREPARED, JobState.SUBMITTED) == JobState.SUBMITTED

    def test_prepared_to_failed(self):
        """PREPARED → FAILED is valid."""
        assert transition(JobState.PREPARED, JobState.FAILED) == JobState.FAILED

    def test_submitted_to_running(self):
        """SUBMITTED → RUNNING is valid."""
        assert transition(JobState.SUBMITTED, JobState.RUNNING) == JobState.RUNNING

    def test_running_to_complete_remote(self):
        """RUNNING → COMPLETE_REMOTE is valid."""
        assert (
            transition(JobState.RUNNING, JobState.COMPLETE_REMOTE)
            == JobState.COMPLETE_REMOTE
        )

    def test_complete_remote_to_downloaded(self):
        """COMPLETE_REMOTE → DOWNLOADED is valid."""
        assert (
            transition(JobState.COMPLETE_REMOTE, JobState.DOWNLOADED)
            == JobState.DOWNLOADED
        )

    def test_downloaded_to_merged(self):
        """DOWNLOADED → MERGED is valid."""
        assert transition(JobState.DOWNLOADED, JobState.MERGED) == JobState.MERGED


class TestInvalidTransitions:
    """Test invalid state transitions are rejected."""

    def test_prepared_to_downloaded(self):
        """PREPARED → DOWNLOADED is invalid (skips steps)."""
        with pytest.raises(InvalidStateTransition) as exc_info:
            transition(JobState.PREPARED, JobState.DOWNLOADED)
        assert exc_info.value.from_state == JobState.PREPARED
        assert exc_info.value.to_state == JobState.DOWNLOADED

    def test_running_to_merged(self):
        """RUNNING → MERGED is invalid (skips download)."""
        with pytest.raises(InvalidStateTransition):
            transition(JobState.RUNNING, JobState.MERGED)

    def test_merged_to_prepared(self):
        """MERGED → PREPARED is invalid (terminal state)."""
        with pytest.raises(InvalidStateTransition):
            transition(JobState.MERGED, JobState.PREPARED)

    def test_failed_to_anything(self):
        """FAILED → any state is invalid (terminal state)."""
        for state in JobState:
            if state != JobState.FAILED:
                with pytest.raises(InvalidStateTransition):
                    transition(JobState.FAILED, state)


class TestIsvalidTransition:
    """Test is_valid_transition function."""

    def test_valid_transition(self):
        """Valid transition returns True."""
        assert is_valid_transition(JobState.PREPARED, JobState.SUBMITTED)

    def test_invalid_transition(self):
        """Invalid transition returns False."""
        assert not is_valid_transition(JobState.PREPARED, JobState.MERGED)

    def test_terminal_state(self):
        """Terminal state has no valid transitions."""
        assert not is_valid_transition(JobState.MERGED, JobState.DOWNLOADED)
        assert not is_valid_transition(JobState.FAILED, JobState.PREPARED)


class TestGetValidTransitions:
    """Test get_valid_transitions function."""

    def test_prepared_transitions(self):
        """PREPARED can go to SUBMITTED or FAILED."""
        valid = get_valid_transitions(JobState.PREPARED)
        assert JobState.SUBMITTED in valid
        assert JobState.FAILED in valid
        assert JobState.RUNNING not in valid

    def test_merged_transitions(self):
        """MERGED has no valid transitions."""
        valid = get_valid_transitions(JobState.MERGED)
        assert len(valid) == 0

    def test_failed_transitions(self):
        """FAILED has no valid transitions."""
        valid = get_valid_transitions(JobState.FAILED)
        assert len(valid) == 0


class TestIsTerminalState:
    """Test is_terminal_state function."""

    def test_terminal_states(self):
        """MERGED and FAILED are terminal."""
        assert is_terminal_state(JobState.MERGED)
        assert is_terminal_state(JobState.FAILED)

    def test_non_terminal_states(self):
        """Other states are not terminal."""
        assert not is_terminal_state(JobState.PREPARED)
        assert not is_terminal_state(JobState.RUNNING)
        assert not is_terminal_state(JobState.COMPLETE_REMOTE)


class TestDescribeState:
    """Test describe_state function."""

    def test_all_states_described(self):
        """All states have descriptions."""
        for state in JobState:
            description = describe_state(state)
            assert description
            assert len(description) > 0

    def test_specific_descriptions(self):
        """Spot check specific descriptions."""
        assert "ready to submit" in describe_state(JobState.PREPARED).lower()
        assert "completed" in describe_state(JobState.COMPLETE_REMOTE).lower()
        assert "merged" in describe_state(JobState.MERGED).lower()


class TestGetWorkflowProgress:
    """Test get_workflow_progress function."""

    def test_initial_progress(self):
        """PREPARED is step 1 of 6."""
        current, total = get_workflow_progress(JobState.PREPARED)
        assert current == 1
        assert total == 6

    def test_middle_progress(self):
        """COMPLETE_REMOTE is step 4 of 6."""
        current, total = get_workflow_progress(JobState.COMPLETE_REMOTE)
        assert current == 4
        assert total == 6

    def test_complete_progress(self):
        """MERGED is step 6 of 6."""
        current, total = get_workflow_progress(JobState.MERGED)
        assert current == 6
        assert total == 6

    def test_failed_progress(self):
        """FAILED returns 0 progress."""
        current, total = get_workflow_progress(JobState.FAILED)
        assert current == 0
