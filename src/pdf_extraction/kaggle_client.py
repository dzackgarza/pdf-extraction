"""Kaggle API client for remote job state queries.

Provides typed interface to Kaggle API with proper error handling and rate limiting.
"""

from __future__ import annotations

import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .models import KernelStatus, RemoteJobState


class KaggleAPIError(Exception):
    """Base exception for Kaggle API errors."""

    def __init__(self, message: str, command: list[str] | None = None):
        self.message = message
        self.command = command
        super().__init__(message)


class KernelNotFoundError(KaggleAPIError):
    """Raised when kernel doesn't exist."""

    pass


class RateLimitExceeded(KaggleAPIError):
    """Raised when Kaggle API rate limit is hit."""

    pass


class KaggleClient:
    """Kaggle API client using official kaggle CLI.

    Wraps `kaggle kernels` commands with typed responses and error handling.
    """

    def __init__(self, timeout: int = 120):
        """Initialize Kaggle client.

        Args:
            timeout: Command timeout in seconds
        """
        self.timeout = timeout

    def _run_command(self, args: list[str]) -> str:
        """Run kaggle CLI command and return stdout.

        Args:
            args: Command arguments (without 'kaggle' prefix)

        Returns:
            Command stdout as string

        Raises:
            KernelNotFoundError: If kernel doesn't exist
            RateLimitExceeded: If rate limited
            KaggleAPIError: For other API errors
        """
        cmd = ["kaggle"] + args
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            raise KaggleAPIError(
                f"Command timed out after {self.timeout}s", command=cmd
            )

        if result.returncode != 0:
            error_msg = result.stderr.strip()
            if "404" in error_msg or "not found" in error_msg.lower():
                raise KernelNotFoundError(
                    f"Kernel not found: {' '.join(args)}", command=cmd
                )
            if "429" in error_msg or "rate limit" in error_msg.lower():
                raise RateLimitExceeded(
                    f"Rate limit exceeded: {' '.join(args)}", command=cmd
                )
            raise KaggleAPIError(f"Kaggle API error: {error_msg}", command=cmd)

        return result.stdout

    def get_kernel_status(self, kernel_ref: str) -> RemoteJobState:
        """Query kernel status from Kaggle API.

        Args:
            kernel_ref: Kernel reference in format 'user/kernel-slug'

        Returns:
            RemoteJobState with current kernel status

        Raises:
            KernelNotFoundError: If kernel doesn't exist
            KaggleAPIError: For other API errors
        """
        # Get kernel metadata using kaggle kernels status
        output = self._run_command(["kernels", "status", kernel_ref])

        # Parse the output - it's in format "status: complete" or similar
        status_line = output.strip()
        status_text = (
            status_line.split(":", 1)[1].strip() if ":" in status_line else status_line
        )

        # Map Kaggle status to our KernelStatus enum
        status_map = {
            "queued": KernelStatus.QUEUED,
            "running": KernelStatus.RUNNING,
            "complete": KernelStatus.COMPLETE,
            "error": KernelStatus.ERROR,
            "cancelled": KernelStatus.CANCELLED,
        }

        # Handle case-insensitive matching
        status_lower = status_text.lower()
        kernel_status = KernelStatus.QUEUED  # default
        for key, value in status_map.items():
            if key in status_lower:
                kernel_status = value
                break

        return RemoteJobState(
            kernel_ref=kernel_ref,
            status=kernel_status,
            query_timestamp=datetime.now(UTC),
        )

    def download_output(self, kernel_ref: str, dest: Path) -> list[Path]:
        """Download kernel output files.

        Args:
            kernel_ref: Kernel reference in format 'user/kernel-slug'
            dest: Destination directory

        Returns:
            List of downloaded file paths

        Raises:
            KernelNotFoundError: If kernel doesn't exist
            KaggleAPIError: For other API errors
        """
        dest.mkdir(parents=True, exist_ok=True)

        # Use kaggle kernels output command
        self._run_command(["kernels", "output", kernel_ref, "-p", str(dest)])

        # List downloaded files
        files = []
        for item in dest.rglob("*"):
            if item.is_file():
                files.append(item)

        return files

    def list_files(self, kernel_ref: str) -> list[dict[str, Any]]:
        """List kernel output files without downloading.

        Args:
            kernel_ref: Kernel reference in format 'user/kernel-slug'

        Returns:
            List of file metadata dicts

        Raises:
            KernelNotFoundError: If kernel doesn't exist
            KaggleAPIError: For other API errors
        """
        output = self._run_command(["kernels", "output", kernel_ref, "-l"])

        files = []
        for line in output.strip().split("\n")[1:]:  # Skip header
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 4:
                files.append(
                    {
                        "name": parts[-1],
                        "size": parts[0],
                        "date": " ".join(parts[1:3]),
                    }
                )

        return files
