from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path

from mistralai.client import Mistral

DEFAULT_MODEL = "mistral-ocr-latest"


def parse_pages(raw: str | None) -> list[int] | None:
    if raw is None or not raw.strip():
        return None
    pages: set[int] = set()
    for chunk in raw.split(","):
        part = chunk.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            if end < start:
                raise ValueError(f"invalid page range {part!r}")
            pages.update(range(start, end + 1))
            continue
        pages.add(int(part))
    return sorted(pages)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Mistral OCR on a local PDF and persist the response.")
    parser.add_argument("--pdf", type=Path, required=True, help="Input PDF path.")
    parser.add_argument("--output-dir", type=Path, help="Directory for OCR artifacts. Defaults to outputs/mistral/<pdf-stem>.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Mistral OCR model.")
    parser.add_argument(
        "--pages",
        help="Optional zero-based page selection, e.g. '0,5-7'.",
    )
    parser.add_argument(
        "--table-format",
        choices=["markdown", "html"],
        help="Optional table extraction format.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file():
        raise SystemExit(f"input pdf does not exist: {pdf_path}")

    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise SystemExit("MISTRAL_API_KEY is not set")

    output_dir = args.output_dir.expanduser().resolve() if args.output_dir else Path("outputs/mistral") / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    encoded_pdf = base64.b64encode(pdf_path.read_bytes()).decode("ascii")
    document = {
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{encoded_pdf}",
    }

    request: dict[str, object] = {
        "model": args.model,
        "document": document,
    }
    pages = parse_pages(args.pages)
    if pages is not None:
        request["pages"] = pages
    if args.table_format:
        request["table_format"] = args.table_format

    client = Mistral(api_key=api_key)
    response = client.ocr.process(**request)
    payload = response.model_dump(mode="json") if hasattr(response, "model_dump") else json.loads(json.dumps(response, default=str))

    json_path = output_dir / "ocr-response.json"
    markdown_path = output_dir / "ocr.md"
    joined_markdown = "\n\n".join(page["markdown"] for page in payload.get("pages", []))

    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    markdown_path.write_text(joined_markdown, encoding="utf-8")

    print(f"json_path={json_path}")
    print(f"markdown_path={markdown_path}")
    print(f"page_count={len(payload.get('pages', []))}")
    return 0


if False:
    raise SystemExit(main())
