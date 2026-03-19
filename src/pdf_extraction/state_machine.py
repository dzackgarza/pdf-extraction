"""State machine for PDF extraction job workflow.

Defines valid state transitions and provides validation for workflow operations.
All state changes must go through this module.
"""

from __future__ import annotations

from .models import InvalidStateTransition, JobState

# Valid state transitions: from_state -> set of allowed to_states
VALID_TRANSITIONS: dict[JobState, set[JobState]] = {
    JobState.PREPARED: {JobState.SUBMITTED, JobState.FAILED},
    JobState.SUBMITTED: {JobState.RUNNING, JobState.FAILED},
    JobState.RUNNING: {JobState.COMPLETE_REMOTE, JobState.FAILED},
    JobState.COMPLETE_REMOTE: {JobState.DOWNLOADED, JobState.FAILED},
    JobState.DOWNLOADED: {JobState.MERGED, JobState.FAILED},
    JobState.MERGED: set(),  # Terminal state
    JobState.FAILED: set(),  # Terminal state
}


def get_valid_transitions(state: JobState) -> set[JobState]:
    """Return set of valid next states for given state.

    Args:
        state: Current job state

    Returns:
        Set of states that can be transitioned to
    """
    return VALID_TRANSITIONS.get(state, set())


def is_valid_transition(from_state: JobState, to_state: JobState) -> bool:
    """Check if transition is valid.

    Args:
        from_state: Current state
        to_state: Target state

    Returns:
        True if transition is allowed
    """
    return to_state in get_valid_transitions(from_state)


def transition(from_state: JobState, to_state: JobState) -> JobState:
    """Validate and perform state transition.

    Args:
        from_state: Current state
        to_state: Target state

    Returns:
        The new state (same as to_state if valid)

    Raises:
        InvalidStateTransition: If transition is not allowed
    """
    if not is_valid_transition(from_state, to_state):
        valid = get_valid_transitions(from_state)
        valid_str = (
            ", ".join(s.value for s in valid) if valid else "none (terminal state)"
        )
        raise InvalidStateTransition(
            from_state,
            to_state,
            f"Valid transitions from {from_state.value}: {valid_str}",
        )
    return to_state


def describe_state(state: JobState) -> str:
    """Return human-readable description of state.

    Args:
        state: Job state to describe

    Returns:
        Description string
    """
    descriptions = {
        JobState.PREPARED: "Job configured, ready to submit",
        JobState.SUBMITTED: "Kernel submitted to Kaggle, awaiting execution",
        JobState.RUNNING: "Kernel executing on Kaggle",
        JobState.COMPLETE_REMOTE: "Kernel completed, output ready to download",
        JobState.DOWNLOADED: "Output downloaded locally, ready to merge",
        JobState.MERGED: "Job merged into final output",
        JobState.FAILED: "Job failed",
    }
    return descriptions.get(state, f"Unknown state: {state}")


def is_terminal_state(state: JobState) -> bool:
    """Check if state is terminal (no further transitions).

    Args:
        state: Job state to check

    Returns:
        True if state is terminal
    """
    return len(get_valid_transitions(state)) == 0


def get_workflow_progress(state: JobState) -> tuple[int, int]:
    """Return workflow progress as (current_step, total_steps).

    Args:
        state: Current job state

    Returns:
        Tuple of (current_step, total_steps) for progress tracking
    """
    workflow_order = [
        JobState.PREPARED,
        JobState.SUBMITTED,
        JobState.RUNNING,
        JobState.COMPLETE_REMOTE,
        JobState.DOWNLOADED,
        JobState.MERGED,
    ]

    try:
        current_idx = workflow_order.index(state)
        return current_idx + 1, len(workflow_order)
    except ValueError:
        # FAILED state or unknown
        return 0, len(workflow_order)
