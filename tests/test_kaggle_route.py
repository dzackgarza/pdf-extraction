"""Tests of the Kaggle MinerU route: the notebook environment and the poller."""

from __future__ import annotations

import subprocess
import sys
import threading
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace

import pytest

from pdf_extraction.mineru import kaggle

LOREM_PDF = Path(__file__).parent.parent / "fixtures" / "lorem.pdf"


def test_notebook_environment_resolves_on_kaggle_python(tmp_path: Path) -> None:
    """The torch and MinerU requirements resolve for the Kaggle image's Python."""
    requirements = tmp_path / "requirements.in"
    requirements.write_text(
        "\n".join([*kaggle.TORCH_REQUIREMENTS, kaggle.MINERU_REQUIREMENT]) + "\n"
    )
    result = subprocess.run(
        [
            "uv", "pip", "compile", str(requirements),
            "--python-version", kaggle.NOTEBOOK_PYTHON,
            "--python-platform", "x86_64-manylinux_2_28",
            "--extra-index-url", kaggle.TORCH_INDEX_URL,
            "--index-strategy", "unsafe-best-match",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


class FailedKernelApi:
    """Kaggle API boundary for a kernel whose run ended in status error."""

    def __init__(self, log: str) -> None:
        self.log = log

    def kernels_status(self, kernel_ref: str) -> SimpleNamespace:
        return SimpleNamespace(status="KernelWorkerStatus.ERROR", failure_message="")

    def validate_kernel_string(self, kernel_ref: str) -> None:
        assert "/" in kernel_ref

    @contextmanager
    def build_kaggle_client(self):
        response = SimpleNamespace(log=self.log, files=[], next_page_token=None)
        client = SimpleNamespace(list_kernel_session_output=lambda request: response)
        yield SimpleNamespace(kernels=SimpleNamespace(kernels_api_client=client))


def test_poller_reports_failed_kernel_with_log_tail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A kernel in status error ends the run with the kernel's log tail."""
    monkeypatch.setattr(
        sys, "argv", ["pdf-mineru", "--pdf", str(LOREM_PDF), "--job-dir", str(tmp_path)]
    )
    args = kaggle.parse_args()
    args.device = "cuda"
    manifest = kaggle.prepare_job("someone", args)
    log_tail = "subprocess.CalledProcessError: Command '['pip', 'install', 'torch==2.2.0']' returned non-zero exit status 1."
    api = FailedKernelApi(log=f"setup line\n{log_tail}\n")

    outcome: list[BaseException] = []

    def run() -> None:
        try:
            kaggle.monitor_remote_jobs(api, [manifest], 0.01, None)
            kaggle.finalize_remote_job(api, manifest, args)
        except BaseException as exc:  # the outcome under test
            outcome.append(exc)

    worker = threading.Thread(target=run, daemon=True)
    worker.start()
    worker.join(timeout=10)

    assert not worker.is_alive(), "poller kept waiting on a kernel in status error"
    assert outcome, "a failed kernel finished without an error"
    assert log_tail in str(outcome[0])
