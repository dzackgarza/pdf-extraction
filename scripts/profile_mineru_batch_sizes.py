#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

DEFAULT_BATCH_SIZES = "1,2,4,6,8"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run MinerU batch-size probes and summarize observed peak RSS.",
    )
    parser.add_argument("--pdf", type=Path, required=True, help="Input PDF path.")
    parser.add_argument("--experiment-dir", type=Path, required=True, help="Directory for experiment outputs.")
    parser.add_argument(
        "--batch-sizes",
        default=DEFAULT_BATCH_SIZES,
        help="Comma-separated batch sizes to test in ascending order.",
    )
    parser.add_argument("--start-page", type=int, default=0, help="0-based inclusive starting page for experiments.")
    parser.add_argument(
        "--method",
        choices=["auto", "txt", "ocr"],
        default="auto",
        help="MinerU pipeline parse method.",
    )
    parser.add_argument("--lang", default="en", help="OCR language hint for MinerU pipeline mode.")
    parser.add_argument("--heartbeat-seconds", type=float, default=5.0, help="Supervisor heartbeat interval.")
    parser.add_argument("--render-threads", type=int, default=1, help="Value for MINERU_PDF_RENDER_THREADS.")
    parser.add_argument(
        "--min-inference-batch",
        type=int,
        default=1,
        help="Value for MINERU_MIN_BATCH_INFERENCE_SIZE.",
    )
    parser.add_argument("--model-source", default="huggingface", help="Value for MINERU_MODEL_SOURCE.")
    parser.add_argument(
        "--stop-on-failure",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Stop after the first batch size that fails.",
    )
    parser.add_argument(
        "--formula",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable formula parsing.",
    )
    parser.add_argument(
        "--table",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable table parsing.",
    )
    return parser.parse_args()


def read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"expected object in {path}"
    return payload


def parse_batch_sizes(raw_value: str) -> list[int]:
    values = []
    for token in raw_value.split(","):
        token = token.strip()
        if not token:
            continue
        values.append(int(token))
    if not values:
        raise SystemExit("--batch-sizes must include at least one positive integer")
    if any(value <= 0 for value in values):
        raise SystemExit("--batch-sizes must contain positive integers")
    return values


def get_page_count(pdf_path: Path) -> int:
    with pdf_path.open("rb") as handle:
        return len(PdfReader(handle).pages)


def markdown_summary_path(experiment_dir: Path) -> Path:
    return experiment_dir / "summary.md"


def json_summary_path(experiment_dir: Path) -> Path:
    return experiment_dir / "summary.json"


def largest_completed_batch_size(rows: list[dict[str, object]]) -> int | None:
    completed_sizes = [
        int(row["batch_size"])
        for row in rows
        if row.get("status") == "complete"
    ]
    return max(completed_sizes, default=None)


def append_summary_markdown(summary_path: Path, rows: list[dict[str, object]], largest_completed: int | None) -> None:
    lines = [
        "| batch_size | page_window | status | peak_rss_mb | duration_seconds | exit_code | batch_dir |",
        "| --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            "| {batch_size} | {page_window} | {status} | {peak_rss_mb} | {duration_seconds} | {exit_code} | {batch_dir} |".format(
                batch_size=row["batch_size"],
                page_window=row["page_window"],
                status=row["status"],
                peak_rss_mb=row["peak_rss_mb"],
                duration_seconds=row["duration_seconds"],
                exit_code=row["exit_code"],
                batch_dir=row["job_dir"],
            )
        )
    lines.append("")
    lines.append(f"Largest completed batch size observed: {largest_completed}")
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    args.pdf = args.pdf.expanduser().resolve()
    args.experiment_dir = args.experiment_dir.expanduser().resolve()
    args.experiment_dir.mkdir(parents=True, exist_ok=True)
    if not args.pdf.is_file():
        raise SystemExit(f"input pdf does not exist: {args.pdf}")

    page_count = get_page_count(args.pdf)
    if args.start_page < 0 or args.start_page >= page_count:
        raise SystemExit(f"--start-page must be in [0, {page_count - 1}]")

    batch_sizes = parse_batch_sizes(args.batch_sizes)
    runner_script = Path(__file__).with_name("run_mineru_batched.py")
    rows: list[dict[str, object]] = []

    for batch_size in batch_sizes:
        job_dir = args.experiment_dir / f"batch-size-{batch_size:03d}"
        end_page = min(args.start_page + batch_size - 1, page_count - 1)
        command = [
            sys.executable,
            str(runner_script),
            "--pdf",
            str(args.pdf),
            "--job-dir",
            str(job_dir),
            "--batch-size",
            str(batch_size),
            "--start-page",
            str(args.start_page),
            "--end-page",
            str(end_page),
            "--method",
            args.method,
            "--lang",
            args.lang,
            "--heartbeat-seconds",
            str(args.heartbeat_seconds),
            "--render-threads",
            str(args.render_threads),
            "--min-inference-batch",
            str(args.min_inference_batch),
            "--model-source",
            args.model_source,
        ]
        command.append("--formula" if args.formula else "--no-formula")
        command.append("--table" if args.table else "--no-table")

        print(json.dumps({"event": "experiment_start", "batch_size": batch_size, "command": command}, sort_keys=True), flush=True)
        result = subprocess.run(command, check=False)

        manifest_path = job_dir / "manifest.json"
        if not manifest_path.is_file():
            row = {
                "batch_size": batch_size,
                "page_window": f"{args.start_page + 1}-{end_page + 1}",
                "status": "manifest_missing",
                "peak_rss_mb": None,
                "duration_seconds": None,
                "exit_code": result.returncode,
                "job_dir": str(job_dir),
            }
        else:
            manifest = read_json(manifest_path)
            batches = manifest.get("batches", [])
            assert isinstance(batches, list), "manifest batches must be a list"
            assert len(batches) == 1, f"expected a single batch in {manifest_path}"
            batch_record = batches[0]
            assert isinstance(batch_record, dict), "batch record must be an object"
            row = {
                "batch_size": batch_size,
                "page_window": f"{int(batch_record['page_start']) + 1}-{int(batch_record['page_end']) + 1}",
                "status": batch_record.get("status"),
                "peak_rss_mb": batch_record.get("peak_rss_mb"),
                "duration_seconds": batch_record.get("duration_seconds"),
                "exit_code": result.returncode,
                "job_dir": str(job_dir),
            }

        rows.append(row)
        largest_completed = largest_completed_batch_size(rows)
        payload = {
            "pdf": str(args.pdf),
            "start_page": args.start_page,
            "largest_completed_batch_size": largest_completed,
            "rows": rows,
        }
        json_summary_path(args.experiment_dir).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        append_summary_markdown(markdown_summary_path(args.experiment_dir), rows, largest_completed)
        print(json.dumps({"event": "experiment_complete", **row}, sort_keys=True), flush=True)

        failed = result.returncode != 0
        if args.stop_on_failure and failed:
            break

    return 0


if __name__ == "__main__":
    sys.exit(main())
