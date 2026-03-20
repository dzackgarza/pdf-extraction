"""CLI integration tests for PDF extraction commands.

Tests CLI commands using fixture PDFs. These are integration tests
that verify the full workflow end-to-end.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"
LOREM_PDF = FIXTURES_DIR / "lorem.pdf"
MULTI_PAGE_PDF = FIXTURES_DIR / "multi-page.pdf"
MATH_TEST_PDF = FIXTURES_DIR / "math-test.pdf"


class TestCliStatus:
    """Test pdf-status CLI command."""

    def test_status_help(self):
        """Verify status command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-status", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Query and display job status" in result.stdout

    def test_status_missing_job_dir(self, tmp_path):
        """Verify status fails gracefully for missing job directory."""
        job_dir = tmp_path / "nonexistent-job"
        result = subprocess.run(
            ["uv", "run", "pdf-status", str(job_dir)],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode != 0
        assert "Manifest not found" in result.stderr or "Error" in result.stderr


class TestCliSubmit:
    """Test pdf-submit CLI command."""

    def test_submit_help(self):
        """Verify submit command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-submit", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Submit prepared job to Kaggle" in result.stdout

    def test_submit_missing_manifest(self, tmp_path):
        """Verify submit fails gracefully for job without manifest."""
        job_dir = tmp_path / "test-job"
        job_dir.mkdir()
        result = subprocess.run(
            ["uv", "run", "pdf-submit", str(job_dir)],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode != 0
        assert "Manifest not found" in result.stderr or "Error" in result.stderr


class TestCliDownload:
    """Test pdf-download CLI command."""

    def test_download_help(self):
        """Verify download command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-download", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Download completed kernel output" in result.stdout


class TestCliRefresh:
    """Test pdf-refresh CLI command."""

    def test_refresh_help(self):
        """Verify refresh command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-refresh", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Refresh local job state" in result.stdout


class TestCliMerge:
    """Test pdf-merge CLI command."""

    def test_merge_help(self):
        """Verify merge command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-merge", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Merge multiple batch outputs" in result.stdout

    def test_merge_requires_multiple_jobs(self, tmp_path):
        """Verify merge requires at least 2 job directories."""
        job_dir = tmp_path / "test-job"
        job_dir.mkdir()
        result = subprocess.run(
            ["uv", "run", "pdf-merge", "merge", str(job_dir)],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode != 0
        assert "at least 2" in result.stderr.lower() or "Error" in result.stderr


class TestCliPoll:
    """Test pdf-poll CLI command."""

    def test_poll_help(self):
        """Verify poll command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-poll", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Monitor long-running Kaggle" in result.stdout


class TestCliBatch:
    """Test pdf-batch CLI command."""

    def test_batch_help(self):
        """Verify batch command shows help."""
        result = subprocess.run(
            ["uv", "run", "pdf-batch", "--help"],
            capture_output=True,
            text=True,
            cwd=FIXTURES_DIR.parent,
        )
        assert result.returncode == 0
        assert "Batch operations" in result.stdout


class TestFixturePdfs:
    """Test that fixture PDFs are valid and accessible."""

    def test_lorem_pdf_exists(self):
        """Verify lorem.pdf fixture exists."""
        assert LOREM_PDF.exists(), f"Fixture not found: {LOREM_PDF}"

    def test_lorem_pdf_is_valid(self):
        """Verify lorem.pdf is a valid PDF."""
        import subprocess

        result = subprocess.run(
            ["pdfinfo", str(LOREM_PDF)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "PDF" in result.stdout

    def test_multi_page_pdf_exists(self):
        """Verify multi-page.pdf fixture exists."""
        assert MULTI_PAGE_PDF.exists(), f"Fixture not found: {MULTI_PAGE_PDF}"

    def test_multi_page_pdf_has_multiple_pages(self):
        """Verify multi-page.pdf has 5 pages."""
        import subprocess

        result = subprocess.run(
            ["pdfinfo", str(MULTI_PAGE_PDF)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Pages:           5" in result.stdout

    def test_math_test_pdf_exists(self):
        """Verify math-test.pdf fixture exists."""
        assert MATH_TEST_PDF.exists(), f"Fixture not found: {MATH_TEST_PDF}"

    def test_math_test_pdf_is_valid(self):
        """Verify math-test.pdf is a valid PDF."""
        import subprocess

        result = subprocess.run(
            ["pdfinfo", str(MATH_TEST_PDF)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "PDF" in result.stdout
