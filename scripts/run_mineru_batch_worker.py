#!/usr/bin/env python3
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from mineru.cli.common import do_parse
from pypdf import PdfReader, PdfWriter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a single MinerU batch over a sliced PDF page window.",
    )
    parser.add_argument("--pdf", type=Path, required=True, help="Input PDF path.")
    parser.add_argument("--output-dir", type=Path, required=True, help="MinerU output directory for this batch.")
    parser.add_argument("--batch-name", required=True, help="Logical output name for the batch.")
    parser.add_argument("--page-start", type=int, required=True, help="0-based inclusive start page.")
    parser.add_argument("--page-end", type=int, required=True, help="0-based inclusive end page.")
    parser.add_argument(
        "--method",
        choices=["auto", "txt", "ocr"],
        default="auto",
        help="MinerU pipeline parse method.",
    )
    parser.add_argument("--lang", default="en", help="OCR language hint for MinerU pipeline mode.")
    parser.add_argument("--progress-log", type=Path, required=True, help="Path for MinerU progress JSONL.")
    parser.add_argument(
        "--progress-heartbeat-seconds",
        type=float,
        default=10.0,
        help="Seconds between MinerU-internal progress heartbeats.",
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


def slice_pdf_bytes(pdf_path: Path, page_start: int, page_end: int) -> bytes:
    writer = PdfWriter()
    with pdf_path.open("rb") as handle:
        reader = PdfReader(handle)
        page_count = len(reader.pages)
        if page_start < 0 or page_end < page_start or page_end >= page_count:
            raise SystemExit(
                f"invalid page window {page_start}-{page_end} for pdf with {page_count} pages: {pdf_path}"
            )
        for page_number in range(page_start, page_end + 1):
            writer.add_page(reader.pages[page_number])
        buffer = io.BytesIO()
        writer.write(buffer)
    return buffer.getvalue()


def main() -> int:
    args = parse_args()
    args.pdf = args.pdf.expanduser().resolve()
    args.output_dir = args.output_dir.expanduser().resolve()
    args.progress_log = args.progress_log.expanduser().resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.progress_log.parent.mkdir(parents=True, exist_ok=True)

    pdf_bytes = slice_pdf_bytes(args.pdf, args.page_start, args.page_end)
    metadata = {
        "event": "worker_start",
        "pdf": str(args.pdf),
        "output_dir": str(args.output_dir),
        "batch_name": args.batch_name,
        "page_start": args.page_start,
        "page_end": args.page_end,
        "page_count": args.page_end - args.page_start + 1,
        "slice_size_bytes": len(pdf_bytes),
    }
    print(json.dumps(metadata, sort_keys=True), flush=True)

    do_parse(
        output_dir=str(args.output_dir),
        pdf_file_names=[args.batch_name],
        pdf_bytes_list=[pdf_bytes],
        p_lang_list=[args.lang],
        backend="pipeline",
        parse_method=args.method,
        formula_enable=args.formula,
        table_enable=args.table,
        f_draw_layout_bbox=False,
        f_draw_span_bbox=False,
        f_dump_md=True,
        f_dump_middle_json=False,
        f_dump_model_output=False,
        f_dump_orig_pdf=False,
        f_dump_content_list=False,
        f_make_md_mode="mm_markdown",
        start_page_id=0,
        end_page_id=args.page_end - args.page_start,
        progress_log_path=str(args.progress_log),
        progress_heartbeat_seconds=args.progress_heartbeat_seconds,
        progress_include_resources=True,
    )
    print(
        json.dumps(
            {
                "event": "worker_complete",
                "batch_name": args.batch_name,
                "output_dir": str(args.output_dir),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
