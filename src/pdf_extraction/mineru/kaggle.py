from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter


def split_pdf(pdf_path: Path, batch_size: int, output_dir: Path) -> list[tuple[Path, int, int]]:
    """Split PDF into multiple files of batch_size pages each."""
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    batches = []

    for start_page in range(0, total_pages, batch_size):
        end_page = min(start_page + batch_size, total_pages)
        writer = PdfWriter()
        for i in range(start_page, end_page):
            writer.add_page(reader.pages[i])

        batch_name = f"{pdf_path.stem}_batch_{start_page + 1}-{end_page}.pdf"
        batch_path = output_dir / batch_name
        with batch_path.open("wb") as f:
            writer.write(f)
        
        batches.append((batch_path, start_page + 1, end_page))
    
    return batches


def merge_extractions(batch_data: list[dict], output_md_path: Path):
    """Merge multiple markdown extractions and their assets."""
    final_md_content = []
    assets_dir_name = f"{output_md_path.stem}_assets"
    final_assets_dir = output_md_path.parent / assets_dir_name
    final_assets_dir.mkdir(parents=True, exist_ok=True)

    # Regex to find images like ![](assets/img.png) or ![](images/img.png)
    # MinerU usually uses "images" or "assets"
    img_regex = re.compile(r"!\[(.*?)\]\((assets|images)/(.*?)\)")

    for i, batch in enumerate(batch_data):
        md_path = Path(batch["markdown_path"])
        batch_assets_dir = md_path.parent / "images"
        if not batch_assets_dir.exists():
            batch_assets_dir = md_path.parent / "assets"

        content = md_path.read_text(encoding="utf-8")

        def replace_img(match):
            alt_text = match.group(1)
            # group 2 is assets/images
            orig_img_name = match.group(3)
            new_img_name = f"batch_{i+1}_{orig_img_name}"
            
            src_img = batch_assets_dir / orig_img_name
            if src_img.exists():
                shutil.copy2(src_img, final_assets_dir / new_img_name)
            
            return f"![{alt_text}]({assets_dir_name}/{new_img_name})"

        new_content = img_regex.sub(replace_img, content)
        final_md_content.append(f"<!-- Batch {i+1} (Pages {batch['start_page']}-{batch['end_page']}) -->\n" + new_content)

    output_md_path.write_text("\n\n".join(final_md_content), encoding="utf-8")
    print(f"Merged {len(batch_data)} batches into {output_md_path}")
    print(f"Assets consolidated in {final_assets_dir}")
import requests
from requests import HTTPError

if TYPE_CHECKING:
    from kaggle.api.kaggle_api_extended import KaggleApi
else:
    KaggleApi = Any

DEFAULT_POLL_SECONDS = 30.0
NOTEBOOK_FILENAME = "notebook.ipynb"
REMOTE_WORK_DIR = Path("/kaggle/working")
REMOTE_OUTPUT_DIR = REMOTE_WORK_DIR / "mineru-output"
REMOTE_SUMMARY_PATH = REMOTE_WORK_DIR / "mineru-summary.json"
REMOTE_BUNDLE_PATH = REMOTE_WORK_DIR / "mineru-output.zip"


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def compact_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def slugify(value: str) -> str:
    chars = [ch.lower() if ch.isalnum() else "-" for ch in value]
    slug = "".join(chars).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "pdf"


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"expected object payload in {path}"
    return cast(dict[str, object], payload)


def append_event(events_path: Path, event: str, **fields: object) -> None:
    payload = {"timestamp": utc_timestamp(), "event": event, **fields}
    events_path.parent.mkdir(parents=True, exist_ok=True)
    with events_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True))
        handle.write("\n")


def record_extraction_history(pdf_path: Path, page_count: int, elapsed_seconds: float, status: str, failure_reason: str | None = None) -> None:
    history_file = Path("EXTRACTIONS.md")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    file_name = pdf_path.name
    minutes = int(elapsed_seconds // 60)
    seconds = int(elapsed_seconds % 60)
    time_str = f"{minutes:02d}m {seconds:02d}s"
    
    display_status = status.upper()
    if failure_reason:
        display_status += f" ({failure_reason})"

    header = "| Timestamp | File Name | Pages | Time | Status |\n| :--- | :--- | :--- | :--- | :--- |\n"
    new_entry = f"| {timestamp} | {file_name} | {page_count} | {time_str} | {display_status} |\n"

    if not history_file.exists():
        history_file.write_text(header + new_entry, encoding="utf-8")
    else:
        with history_file.open("a", encoding="utf-8") as f:
            f.write(new_entry)


def get_page_count(pdf_path: Path) -> int:
    with pdf_path.open("rb") as handle:
        return len(PdfReader(handle).pages)


def build_remote_slug(pdf_stem: str, role: str, stamp: str, batch_num: int | None = None, max_length: int = 50) -> str:
    if batch_num is not None:
        suffix = f"mineru-{role}-{batch_num}-{stamp}"
    else:
        suffix = f"mineru-{role}-{stamp}"
    
    room = max_length - len(suffix) - 1
    assert room >= 3, f"max_length {max_length} is too small for suffix {suffix}"
    trimmed = slugify(pdf_stem)[:room].strip("-") or "pdf"
    slug = f"{trimmed}-{suffix}"
    assert 6 <= len(slug) <= max_length, f"invalid remote slug {slug!r}"
    return slug


def build_title(slug: str, max_length: int = 50) -> str:
    return slug.replace("-", " ")[:max_length]


def build_output_file_pattern() -> str:
    names = (REMOTE_SUMMARY_PATH.name, REMOTE_BUNDLE_PATH.name)
    joined = "|".join(re.escape(name) for name in names)
    return rf"^(?:{joined})$"


def download_kernel_outputs(
    api: KaggleApi,
    kernel_ref: str,
    downloads_dir: Path,
    file_pattern: str,
) -> tuple[list[str], str | None]:
    from kagglesdk.kernels.types.kernels_api_service import ApiListKernelSessionOutputRequest

    compiled_pattern = re.compile(file_pattern)
    api.validate_kernel_string(kernel_ref)
    owner_slug, kernel_slug = kernel_ref.split("/", 1)
    downloads_dir.mkdir(parents=True, exist_ok=True)

    downloaded_files: list[str] = []
    next_page_token: str | None = None
    wrote_log = False
    with api.build_kaggle_client() as kaggle:
        while True:
            request = ApiListKernelSessionOutputRequest()
            request.user_name = owner_slug
            request.kernel_slug = kernel_slug
            request.page_size = 100
            request.page_token = next_page_token
            response = kaggle.kernels.kernels_api_client.list_kernel_session_output(request)
            if response.log and not wrote_log:
                log_path = downloads_dir / f"{kernel_slug}.log"
                log_path.write_text(response.log, encoding="utf-8")
                downloaded_files.append(str(log_path))
                wrote_log = True
            for item in response.files:
                file_name = item.file_name
                if file_name is None or not compiled_pattern.search(file_name):
                    continue
                output_path = downloads_dir / file_name
                output_path.parent.mkdir(parents=True, exist_ok=True)
                response_stream = requests.get(item.url, stream=True, timeout=300)
                response_stream.raise_for_status()
                output_path.write_bytes(response_stream.content)
                downloaded_files.append(str(output_path))
            next_page_token = response.next_page_token
            if not next_page_token:
                break
    return downloaded_files, next_page_token


def resolve_kernel_ref(owner: str, requested_ref: str, kernel_url: str | None) -> str:
    if not kernel_url:
        return requested_ref
    marker = "/code/"
    if marker not in kernel_url:
        return requested_ref
    suffix = kernel_url.split(marker, 1)[1].strip("/")
    parts = suffix.split("/", 1)
    if len(parts) != 2:
        return requested_ref
    url_owner, url_slug = parts
    if url_owner != owner or not url_slug:
        return requested_ref
    return f"{url_owner}/{url_slug}"


def notebook_cell(source: str) -> dict[str, object]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source,
    }


def build_notebook(pdf_name: str, args: argparse.Namespace) -> dict[str, object]:
    formula_value = "true" if args.formula else "false"
    table_value = "true" if args.table else "false"
    virtual_vram_size = "" if args.virtual_vram_size is None else str(args.virtual_vram_size)
    install_source = "\n".join(
        [
            "import os",
            "from pathlib import Path",
            "import shutil",
            "import subprocess",
            "import sys",
            "",
            "os.environ['MPLBACKEND'] = 'Agg'",
            "subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'mineru[pipeline]'], check=True)",
            f"WORK_DIR = Path('{REMOTE_WORK_DIR.as_posix()}')",
            f"OUTPUT_DIR = Path('{REMOTE_OUTPUT_DIR.as_posix()}')",
            f"SUMMARY_PATH = Path('{REMOTE_SUMMARY_PATH.as_posix()}')",
            f"BUNDLE_PATH = Path('{REMOTE_BUNDLE_PATH.as_posix()}')",
            "if OUTPUT_DIR.exists():",
            "    shutil.rmtree(OUTPUT_DIR)",
            "if SUMMARY_PATH.exists():",
            "    SUMMARY_PATH.unlink()",
            "if BUNDLE_PATH.exists():",
            "    BUNDLE_PATH.unlink()",
            "OUTPUT_DIR.mkdir(parents=True, exist_ok=True)",
            "print('mineru install complete', flush=True)",
        ]
    )
    healthcheck_source = "\n".join(
        [
            "import importlib.metadata",
            "import os",
            "import shutil",
            "import subprocess",
            "import sys",
            "",
            "print('python', sys.version, flush=True)",
            "print('mineru version', importlib.metadata.version('mineru'), flush=True)",
            "print('mineru cli', shutil.which('mineru'), flush=True)",
            "nvidia_smi = shutil.which('nvidia-smi')",
            "if nvidia_smi:",
            "    gpu_result = subprocess.run([nvidia_smi, '-L'], check=False, capture_output=True, text=True)",
            "    print('nvidia-smi -L', gpu_result.stdout.strip() or gpu_result.stderr.strip() or '<no output>', flush=True)",
            "else:",
            "    print('nvidia-smi -L unavailable', flush=True)",
            "try:",
            "    import torch",
            "except Exception as exc:",
            "    print('torch import failed', repr(exc), flush=True)",
            "else:",
            "    print('torch.cuda.is_available', torch.cuda.is_available(), flush=True)",
            "    print('torch.cuda.device_count', torch.cuda.device_count(), flush=True)",
            "    if torch.cuda.is_available() and torch.cuda.device_count() > 0:",
            "        print('torch.cuda.device_name', torch.cuda.get_device_name(0), flush=True)",
            "print('CUDA_VISIBLE_DEVICES', os.environ.get('CUDA_VISIBLE_DEVICES'), flush=True)",
            "print('MINERU_VIRTUAL_VRAM_SIZE', os.environ.get('MINERU_VIRTUAL_VRAM_SIZE'), flush=True)",
        ]
    )
    run_mineru_source = "\n".join(
        [
            "import json",
            "from pathlib import Path",
            "import os",
            "import shutil",
            "import subprocess",
            "",
            "def collect_relative_files(root: Path) -> list[str]:",
            "    if not root.exists():",
            "        return []",
            "    return sorted(",
            "        str(path.relative_to(root))",
            "        for path in root.rglob('*')",
            "        if path.is_file()",
            "    )",
            "",
            "def find_markdown_path(output_dir: Path, pdf_stem: str) -> Path | None:",
            "    candidates = sorted(path for path in output_dir.rglob('*.md') if path.is_file())",
            "    exact = [path for path in candidates if path.stem == pdf_stem]",
            "    if exact:",
            "        return exact[0]",
            "    if candidates:",
            "        return candidates[0]",
            "    return None",
            "",
            f"matches = sorted(Path('/kaggle/input').glob('**/{pdf_name}'))",
            f"assert matches, 'could not locate {pdf_name} under /kaggle/input'",
            "input_pdf = matches[0]",
            "command = [",
            "    'mineru',",
            "    '-p', str(input_pdf),",
            f"    '-o', '{REMOTE_OUTPUT_DIR.as_posix()}',",
            f"    '-b', '{args.backend}',",
            f"    '-m', '{args.method}',",
            f"    '-l', '{args.lang}',",
            f"    '-d', '{args.device}',",
            "    '--source',",
            f"    '{args.model_source}',",
            "    '-f',",
            f"    '{formula_value}',",
            "    '-t',",
            f"    '{table_value}',",
            "]",
            "env = os.environ.copy()",
            "env['MINERU_MODEL_SOURCE'] = "
            f"'{args.model_source}'",
            "env['MPLBACKEND'] = 'Agg'",
            f"if '{virtual_vram_size}':",
            f"    env['MINERU_VIRTUAL_VRAM_SIZE'] = '{virtual_vram_size}'",
            "print('effective MINERU_VIRTUAL_VRAM_SIZE', env.get('MINERU_VIRTUAL_VRAM_SIZE'), flush=True)",
            "print(json.dumps({'event': 'mineru_start', 'pdf': str(input_pdf), 'command': command}, sort_keys=True), flush=True)",
            "result = subprocess.run(command, check=False, env=env)",
            "output_files = collect_relative_files(OUTPUT_DIR)",
            "working_files = collect_relative_files(WORK_DIR)",
            "markdown_path = find_markdown_path(OUTPUT_DIR, input_pdf.stem) if result.returncode == 0 else None",
            "complete = result.returncode == 0 and bool(output_files)",
            "failure = None",
            "if result.returncode != 0:",
            "    failure = f'MinerU exited with code {result.returncode}.'",
            "elif not output_files:",
            "    failure = 'MinerU exited successfully but produced no output files.'",
            "summary = {",
            "    'pdf': str(input_pdf),",
            "    'output_dir': str(OUTPUT_DIR),",
            "    'summary_path': str(SUMMARY_PATH),",
            "    'bundle_path': str(BUNDLE_PATH),",
            "    'command': command,",
            "    'returncode': result.returncode,",
            "    'complete': complete,",
            "    'failure': failure,",
            "    'output_files': output_files,",
            "    'working_files': working_files,",
            "    'output_dir_exists': OUTPUT_DIR.exists(),",
            "    'markdown_relpath': None if markdown_path is None else str(markdown_path.relative_to(OUTPUT_DIR)),",
            "}",
            "if complete:",
            "    archive_base = BUNDLE_PATH.with_suffix('')",
            "    created_bundle = shutil.make_archive(str(archive_base), 'zip', root_dir=OUTPUT_DIR)",
            "    summary['bundle_path'] = created_bundle",
            "    summary['bundle_size_bytes'] = Path(created_bundle).stat().st_size",
            "SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding='utf-8')",
            "print(json.dumps({'event': 'mineru_complete', **summary}, sort_keys=True), flush=True)",
        ]
    )
    return {
        "cells": [
            notebook_cell(install_source),
            notebook_cell(healthcheck_source),
            notebook_cell(run_mineru_source),
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.12",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package and run a one-off MinerU extraction job on Kaggle.",
    )
    parser.add_argument("--pdf", type=Path, required=True, help="Input PDF path.")
    parser.add_argument("--job-dir", type=Path, help="Output directory for local job artifacts.")
    parser.add_argument("--owner", help="Kaggle owner slug. Required when auth does not expose a username.")
    parser.add_argument(
        "--method",
        choices=["auto", "txt", "ocr"],
        default="auto",
        help="MinerU pipeline parse method.",
    )
    parser.add_argument("--lang", default="en", help="OCR language hint for MinerU pipeline mode.")
    parser.add_argument("--backend", default="pipeline", help="MinerU backend to use in Kaggle.")
    parser.add_argument(
        "--device",
        help="MinerU device selector for the Kaggle notebook. Defaults to cuda when GPU is enabled, else cpu.",
    )
    parser.add_argument("--model-source", default="huggingface", help="MinerU model source.")
    parser.add_argument(
        "--virtual-vram-size",
        type=int,
        help="Optional MINERU_VIRTUAL_VRAM_SIZE value for Kaggle notebook runs.",
    )
    parser.add_argument("--poll-seconds", type=float, default=DEFAULT_POLL_SECONDS, help="Polling interval for Kaggle status checks.")
    parser.add_argument("--timeout-seconds", type=int, help="Optional Kaggle run timeout and local poll ceiling.")
    parser.add_argument(
        "--formula",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable formula parsing.",
    )
    parser.add_argument(
        "--table",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Enable table parsing.",
    )
    parser.add_argument(
        "--enable-gpu",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Request a GPU-backed Kaggle notebook.",
    )
    parser.add_argument(
        "--accelerator",
        help="Optional Kaggle accelerator name passed to kernels_push. Defaults to P100 when GPU is enabled.",
    )
    parser.add_argument(
        "--cleanup-remote",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Delete the remote Kaggle kernel and input dataset after a successful download.",
    )
    parser.add_argument(
        "--save-artifacts",
        action="store_true",
        help="Keep local job artifacts after completion. If False, deletes the local job directory after extraction.",
    )
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="Prepare the local Kaggle dataset/kernel bundle but do not call the Kaggle API.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=200,
        help="Maximum number of pages per Kaggle job batch.",
    )
    parser.add_argument(
        "--max-parallel",
        type=int,
        default=2,
        help="Maximum number of parallel Kaggle GPU sessions.",
    )
    return parser.parse_args()


def manifest_path(manifest: dict[str, object]) -> Path:
    return Path(cast(str, manifest["job_dir"])) / "manifest.json"


def status_path(manifest: dict[str, object]) -> Path:
    return Path(cast(str, manifest["job_dir"])) / "status.json"


def events_path(manifest: dict[str, object]) -> Path:
    return Path(cast(str, manifest["job_dir"])) / "events.jsonl"


def persist_state(manifest: dict[str, object], phase: str, failure: str | None = None) -> None:
    manifest["phase"] = phase
    if failure is None:
        manifest.pop("failure", None)
    else:
        manifest["failure"] = failure
    write_json(manifest_path(manifest), manifest)
    status_payload = {
        "phase": phase,
        "job_dir": manifest["job_dir"],
        "pdf": manifest["pdf"],
        "page_count": manifest["page_count"],
        "dataset_ref": manifest["dataset_ref"],
        "dataset_status": manifest["dataset_status"],
        "kernel_ref": manifest["kernel_ref"],
        "kernel_status": manifest["kernel_status"],
        "downloads_dir": manifest["downloads_dir"],
        "downloaded_files": manifest["downloaded_files"],
        "markdown_path": manifest["markdown_path"],
        "failure": manifest.get("failure"),
    }
    write_json(status_path(manifest), status_payload)


def resolve_owner(args_owner: str | None, api: KaggleApi | None, prepare_only: bool) -> str:
    if args_owner:
        return args_owner
    if prepare_only:
        raise SystemExit("--owner is required with --prepare-only when Kaggle auth is not consulted")
    assert api is not None, "authenticated api is required to resolve owner"
    username = api.get_config_value(api.CONFIG_NAME_USER)
    if username:
        return username
    raise SystemExit("could not resolve the Kaggle username from auth; pass --owner explicitly")


def prepare_job(owner: str, args: argparse.Namespace, batch_num: int | None = None) -> dict[str, object]:
    stamp = compact_timestamp()
    pdf_slug = slugify(args.pdf.stem)
    job_stamp = utc_timestamp()
    
    dir_name = f"{pdf_slug}-kaggle-{job_stamp}"
    if batch_num is not None:
        dir_name = f"{pdf_slug}-batch-{batch_num}-kaggle-{job_stamp}"
        
    job_dir = args.job_dir or Path("outputs/kaggle-jobs") / dir_name
    job_dir = job_dir.expanduser().resolve()
    input_dataset_dir = job_dir / "input-dataset"
    kernel_dir = job_dir / "kernel"
    downloads_dir = job_dir / "downloads"
    extracted_dir = job_dir / "extracted"
    input_dataset_dir.mkdir(parents=True, exist_ok=True)
    kernel_dir.mkdir(parents=True, exist_ok=True)
    downloads_dir.mkdir(parents=True, exist_ok=True)
    extracted_dir.mkdir(parents=True, exist_ok=True)

    dataset_slug = build_remote_slug(args.pdf.stem, "input", stamp, batch_num=batch_num)
    kernel_slug = build_remote_slug(args.pdf.stem, "job", stamp, batch_num=batch_num)
    dataset_ref = f"{owner}/{dataset_slug}"
    kernel_ref = f"{owner}/{kernel_slug}"

    copied_pdf = input_dataset_dir / args.pdf.name
    shutil.copy2(args.pdf, copied_pdf)
    dataset_metadata = {
        "title": build_title(dataset_slug),
        "id": dataset_ref,
        "licenses": [{"name": "other"}],
        "description": f"Private one-off MinerU input for {args.pdf.name}",
        "resources": [{"path": copied_pdf.name, "description": "Input PDF for MinerU extraction"}],
    }
    write_json(input_dataset_dir / "dataset-metadata.json", dataset_metadata)

    notebook_payload = build_notebook(copied_pdf.name, args)
    write_json(kernel_dir / NOTEBOOK_FILENAME, notebook_payload)
    kernel_metadata = {
        "id": kernel_ref,
        "title": build_title(kernel_slug),
        "code_file": NOTEBOOK_FILENAME,
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": args.enable_gpu,
        "enable_internet": True,
        "dataset_sources": [dataset_ref],
        "competition_sources": [],
        "kernel_sources": [],
        "model_sources": [],
    }
    write_json(kernel_dir / "kernel-metadata.json", kernel_metadata)

    manifest: dict[str, object] = {
        "phase": "prepared",
        "pdf": str(args.pdf),
        "page_count": get_page_count(args.pdf),
        "job_dir": str(job_dir),
        "input_dataset_dir": str(input_dataset_dir),
        "kernel_dir": str(kernel_dir),
        "downloads_dir": str(downloads_dir),
        "extracted_dir": str(extracted_dir),
        "dataset_ref": dataset_ref,
        "dataset_status": "prepared",
        "kernel_ref": kernel_ref,
        "kernel_status": "prepared",
        "kernel_url": None,
        "downloaded_files": [],
        "summary_path": None,
        "bundle_path": None,
        "markdown_path": None,
        "prepare_only": args.prepare_only,
    }
    persist_state(manifest, "prepared")
    append_event(
        events_path(manifest),
        "prepared",
        dataset_ref=dataset_ref,
        kernel_ref=kernel_ref,
        input_pdf=str(args.pdf),
        copied_pdf=str(copied_pdf),
    )
    return manifest


def authenticate_kaggle() -> KaggleApi:
    from kaggle.api.kaggle_api_extended import KaggleApi as RuntimeKaggleApi

    oauth_enabled = os.environ.get("KAGGLE_ENABLE_OAUTH", "").lower() in {"1", "true", "yes"}
    username = os.environ.get("KAGGLE_USERNAME")
    key = os.environ.get("KAGGLE_KEY") or os.environ.get("KAGGLE_API_KEY")
    original_key = os.environ.get("KAGGLE_KEY")
    original_token = os.environ.get("KAGGLE_API_TOKEN")
    if username and key:
        os.environ["KAGGLE_KEY"] = key
        os.environ.pop("KAGGLE_API_TOKEN", None)
    api = RuntimeKaggleApi(enable_oauth=oauth_enabled)
    try:
        api.authenticate()
    except Exception as exc:  # pragma: no cover - boundary with local auth config
        raise SystemExit(f"Kaggle auth failed: {exc}") from exc
    finally:
        if username and key:
            if original_token is None:
                os.environ.pop("KAGGLE_API_TOKEN", None)
            else:
                os.environ["KAGGLE_API_TOKEN"] = original_token
            if original_key is None:
                os.environ.pop("KAGGLE_KEY", None)
            else:
                os.environ["KAGGLE_KEY"] = original_key
    return api


def wait_for_dataset_ready(
    api: KaggleApi,
    dataset_ref: str,
    manifest: dict[str, object],
    poll_seconds: float,
    timeout_seconds: int | None,
) -> None:
    started = time.monotonic()
    last_status: str | None = None
    while True:
        try:
            status = api.dataset_status(dataset_ref)
        except HTTPError as exc:
            response = exc.response
            body = "" if response is None else response.text
            if response is not None and response.status_code == 403 and "datasets.get" in body:
                persist_state(manifest, "waiting_for_dataset")
                append_event(
                    events_path(manifest),
                    "dataset_status_pending",
                    dataset_ref=dataset_ref,
                    http_status=response.status_code,
                    error_body=body,
                )
                if timeout_seconds is not None and time.monotonic() - started > timeout_seconds:
                    raise SystemExit(f"timed out waiting for dataset {dataset_ref} to become readable") from exc
                time.sleep(poll_seconds)
                continue
            raise
        manifest["dataset_status"] = status
        persist_state(manifest, "waiting_for_dataset")
        if status != last_status:
            append_event(events_path(manifest), "dataset_status", dataset_ref=dataset_ref, dataset_status=status)
            last_status = status
        if status == "ready":
            return
        if status in {"error", "failed"}:
            raise SystemExit(f"dataset {dataset_ref} entered terminal status {status}")
        if timeout_seconds is not None and time.monotonic() - started > timeout_seconds:
            raise SystemExit(f"timed out waiting for dataset {dataset_ref} to become ready")
        time.sleep(poll_seconds)


def wait_for_kernel_complete(
    api: KaggleApi,
    kernel_ref: str,
    manifest: dict[str, object],
    poll_seconds: float,
    timeout_seconds: int | None,
) -> tuple[str, str | None]:
    started = time.monotonic()
    last_status: str | None = None
    while True:
        response = api.kernels_status(kernel_ref)
        payload = response.to_dict() if hasattr(response, "to_dict") else {}
        status = str(payload.get("status") or response.status).lower()
        failure_message = getattr(response, "failure_message", None)
        manifest["kernel_status"] = status
        persist_state(manifest, "running")
        if status != last_status:
            append_event(
                events_path(manifest),
                "kernel_status",
                kernel_ref=kernel_ref,
                kernel_status=status,
                failure_message=failure_message,
            )
            last_status = status
        if status in {"complete", "error"}:
            return status, failure_message
        if timeout_seconds is not None and time.monotonic() - started > timeout_seconds:
            raise SystemExit(f"timed out waiting for kernel {kernel_ref} to complete")
        time.sleep(poll_seconds)


def extract_bundle(bundle_path: Path, target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    with ZipFile(bundle_path) as archive:
        archive.extractall(target_dir)


def delete_remote_resources(api: KaggleApi, dataset_ref: str, kernel_ref: str) -> dict[str, object]:
    cleanup: dict[str, object] = {
        "attempted": True,
        "kernel_ref": kernel_ref,
        "dataset_ref": dataset_ref,
        "kernel_deleted": False,
        "dataset_deleted": False,
        "errors": [],
    }
    try:
        api.kernels_delete(kernel_ref, no_confirm=True)
        cleanup["kernel_deleted"] = True
    except Exception as exc:
        cast(list[str], cleanup["errors"]).append(f"kernel delete failed: {exc}")

    owner_slug, dataset_slug = dataset_ref.split("/", 1)
    try:
        api.dataset_delete(owner_slug, dataset_slug, no_confirm=True)
        cleanup["dataset_deleted"] = True
    except Exception as exc:
        cast(list[str], cleanup["errors"]).append(f"dataset delete failed: {exc}")

    return cleanup


def submit_remote_job(api: KaggleApi, manifest: dict[str, object], args: argparse.Namespace) -> None:
    dataset_ref = cast(str, manifest["dataset_ref"])
    kernel_ref = cast(str, manifest["kernel_ref"])
    owner = dataset_ref.split("/", 1)[0]
    input_dataset_dir = cast(str, manifest["input_dataset_dir"])
    kernel_dir = cast(str, manifest["kernel_dir"])

    persist_state(manifest, "creating_dataset")
    append_event(events_path(manifest), "creating_dataset", dataset_ref=dataset_ref, input_dataset_dir=input_dataset_dir)
    dataset_result = api.dataset_create_new(
        folder=input_dataset_dir,
        public=False,
        quiet=False,
        convert_to_csv=False,
        dir_mode="skip",
    )
    dataset_status = getattr(dataset_result, "status", None)
    dataset_error = getattr(dataset_result, "error", None)
    manifest["dataset_url"] = getattr(dataset_result, "url", None)
    append_event(
        events_path(manifest),
        "dataset_submitted",
        dataset_ref=dataset_ref,
        dataset_status=dataset_status,
        dataset_url=getattr(dataset_result, "url", None),
        dataset_error=dataset_error,
    )
    if isinstance(dataset_error, str) and dataset_error:
        raise SystemExit(f"dataset create failed: {dataset_error}")
    if str(dataset_status).lower() == "error":
        raise SystemExit(f"dataset create failed with status {dataset_status}")
    
    wait_for_dataset_ready(api, dataset_ref, manifest, args.poll_seconds, args.timeout_seconds)

    persist_state(manifest, "pushing_kernel")
    append_event(events_path(manifest), "pushing_kernel", kernel_ref=kernel_ref, kernel_dir=kernel_dir)
    kernel_result = api.kernels_push(
        folder=kernel_dir,
        timeout=None if args.timeout_seconds is None else str(args.timeout_seconds),
        acc=args.accelerator,
    )
    kernel_url = getattr(kernel_result, "url", None)
    kernel_error = getattr(kernel_result, "error", None)
    kernel_ref = resolve_kernel_ref(owner, kernel_ref, kernel_url)
    manifest["kernel_ref"] = kernel_ref
    manifest["kernel_url"] = kernel_url
    append_event(
        events_path(manifest),
        "kernel_submitted",
        kernel_ref=kernel_ref,
        kernel_url=kernel_url,
        kernel_version=getattr(kernel_result, "versionNumber", None),
        kernel_error=kernel_error,
    )
    if isinstance(kernel_error, str) and kernel_error:
        raise SystemExit(f"kernel push failed: {kernel_error}")


def monitor_remote_jobs(
    api: KaggleApi, 
    manifests: list[dict[str, object]], 
    poll_seconds: float, 
    timeout_seconds: int | None
) -> None:
    """Monitor multiple kernels in parallel until all are terminal."""
    started = time.monotonic()
    last_statuses: dict[str, str] = {}
    
    while True:
        all_done = True
        for manifest in manifests:
            kernel_ref = cast(str, manifest["kernel_ref"])
            # Skip if already terminal
            current_phase = cast(str, manifest.get("phase", ""))
            if current_phase in {"complete", "failed", "error"}:
                continue
            
            all_done = False
            response = api.kernels_status(kernel_ref)
            payload = response.to_dict() if hasattr(response, "to_dict") else {}
            status = str(payload.get("status") or response.status).lower()
            failure_message = getattr(response, "failure_message", None)
            
            manifest["kernel_status"] = status
            manifest["terminal_status"] = status if status in {"complete", "error"} else None
            manifest["kernel_failure_message"] = failure_message
            
            persist_state(manifest, "running")
            
            if status != last_statuses.get(kernel_ref):
                append_event(
                    events_path(manifest),
                    "kernel_status",
                    kernel_ref=kernel_ref,
                    kernel_status=status,
                    failure_message=failure_message,
                )
                last_statuses[kernel_ref] = status
                print(f"  [{kernel_ref}] status: {status}", flush=True)
        
        if all_done:
            break
            
        if timeout_seconds is not None and time.monotonic() - started > timeout_seconds:
            raise SystemExit("timed out waiting for one or more kernels to complete")
            
        time.sleep(poll_seconds)


def finalize_remote_job(api: KaggleApi, manifest: dict[str, object], args: argparse.Namespace) -> None:
    kernel_ref = cast(str, manifest["kernel_ref"])
    dataset_ref = cast(str, manifest["dataset_ref"])
    downloads_dir = Path(cast(str, manifest["downloads_dir"]))
    extracted_dir = Path(cast(str, manifest["extracted_dir"]))
    terminal_kernel_status = cast(str, manifest.get("terminal_status", "unknown"))
    kernel_failure_message = cast(str | None, manifest.get("kernel_failure_message"))

    persist_state(manifest, "downloading_output")
    output_file_pattern = build_output_file_pattern()
    append_event(
        events_path(manifest),
        "downloading_output",
        kernel_ref=kernel_ref,
        downloads_dir=str(downloads_dir),
        file_pattern=output_file_pattern,
    )
    downloaded_files, next_page_token = download_kernel_outputs(api, kernel_ref, downloads_dir, output_file_pattern)
    manifest["downloaded_files"] = downloaded_files
    append_event(
        events_path(manifest),
        "output_downloaded",
        kernel_ref=kernel_ref,
        downloaded_files=downloaded_files,
        next_page_token=next_page_token,
    )

    summary_path = downloads_dir / REMOTE_SUMMARY_PATH.name
    bundle_path = downloads_dir / REMOTE_BUNDLE_PATH.name
    
    if not summary_path.is_file():
        if terminal_kernel_status == "error":
            raise RuntimeError(f"kernel {kernel_ref} failed: {kernel_failure_message or 'unknown error'}")
        raise RuntimeError(f"expected worker summary was not downloaded: {summary_path}")
    
    run_summary = read_json(summary_path)
    manifest["summary_path"] = str(summary_path)
    manifest["run_summary"] = run_summary
    
    if run_summary.get("complete") is not True:
        failure_message = run_summary.get("failure")
        return_code = run_summary.get("returncode")
        raise RuntimeError(
            f"notebook did not produce extraction output: {failure_message or f'returncode={return_code}'}"
        )
    
    if not bundle_path.is_file():
        raise RuntimeError(f"expected notebook bundle was not downloaded: {bundle_path}")
    
    manifest["bundle_path"] = str(bundle_path)
    extract_bundle(bundle_path, extracted_dir)
    
    markdown_relpath = run_summary.get("markdown_relpath")
    if isinstance(markdown_relpath, str) and markdown_relpath:
        markdown_path = extracted_dir / markdown_relpath
        if markdown_path.is_file():
            manifest["markdown_path"] = str(markdown_path)

    if args.cleanup_remote:
        persist_state(manifest, "cleaning_remote")
        cleanup_result = delete_remote_resources(api, dataset_ref, kernel_ref)
        manifest["remote_cleanup"] = cleanup_result
        append_event(events_path(manifest), "remote_cleanup", **cleanup_result)

    persist_state(manifest, "complete")
    append_event(
        events_path(manifest),
        "complete",
        kernel_ref=kernel_ref,
        summary_path=str(summary_path),
        bundle_path=str(bundle_path),
        markdown_path=manifest["markdown_path"],
    )


def main() -> int:
    start_time = time.monotonic()
    args = parse_args()
    args.pdf = args.pdf.expanduser().resolve()
    if args.device is None:
        args.device = "cuda" if args.enable_gpu else "cpu"
    if args.accelerator is None and args.enable_gpu:
        args.accelerator = "P100"
    if not args.pdf.is_file():
        raise SystemExit(f"input pdf does not exist: {args.pdf}")

    page_count = get_page_count(args.pdf)
    api = None if args.prepare_only else authenticate_kaggle()
    owner = resolve_owner(args.owner, api, args.prepare_only)

    if page_count <= args.batch_size:
        # Single-job logic
        manifest = prepare_job(owner, args)
        if args.prepare_only:
            print(f"job_dir={manifest['job_dir']}")
            print(f"dataset_ref={manifest['dataset_ref']}")
            print(f"kernel_ref={manifest['kernel_ref']}")
            return 0

        assert api is not None, "authenticated api is required for remote jobs"
        try:
            submit_remote_job(api, manifest, args)
            monitor_remote_jobs(api, [manifest], args.poll_seconds, args.timeout_seconds)
            finalize_remote_job(api, manifest, args)
        except (SystemExit, Exception) as exc:
            failure = str(exc)
            persist_state(manifest, "failed", failure)
            append_event(events_path(manifest), "failed", error=failure)
            
            elapsed_seconds = time.monotonic() - start_time
            record_extraction_history(args.pdf, page_count, elapsed_seconds, "failed", failure)
            raise

        markdown_path_str = manifest.get("markdown_path")
        if markdown_path_str:
            markdown_path = Path(markdown_path_str)
            if markdown_path.is_file():
                destination = args.pdf.with_suffix(".md")
                print(f"Moving markdown to {destination}", flush=True)
                shutil.move(markdown_path, destination)
                manifest["markdown_path"] = str(destination)
                persist_state(manifest, "complete")

        elapsed_seconds = time.monotonic() - start_time
        if manifest.get("phase") == "complete":
            record_extraction_history(args.pdf, page_count, elapsed_seconds, "complete")

        if not args.save_artifacts:
            job_dir = Path(cast(str, manifest["job_dir"]))
            if job_dir.is_dir():
                print(f"Cleaning up local job directory: {job_dir}", flush=True)
                shutil.rmtree(job_dir)

        print(f"job_dir={manifest['job_dir']}")
        if "downloads_dir" in manifest:
            print(f"downloads_dir={manifest['downloads_dir']}")
        print(f"markdown_path={manifest['markdown_path']}")
        return 0

    else:
        # Parallel Batching logic with queueing
        print(f"PDF has {page_count} pages, which exceeds batch size {args.batch_size}. Parallel batching (limit: {args.max_parallel})...")
        temp_batch_dir = Path("outputs/tmp-batches") / f"{args.pdf.stem}-{compact_timestamp()}"
        temp_batch_dir.mkdir(parents=True, exist_ok=True)
        
        batches = split_pdf(args.pdf, args.batch_size, temp_batch_dir)
        
        pending_manifests = []
        active_manifests = []
        batch_results = []
        failures = []
        
        try:
            # 1. Prepare all manifests
            for i, (batch_pdf, start_pg, end_page) in enumerate(batches):
                batch_args = argparse.Namespace(**vars(args))
                batch_args.pdf = batch_pdf
                batch_args.job_dir = None
                
                manifest = prepare_job(owner, batch_args, batch_num=i+1)
                manifest["start_page"] = start_pg
                manifest["end_page"] = end_page
                manifest["batch_num"] = i + 1
                pending_manifests.append(manifest)

            if args.prepare_only:
                for m in pending_manifests:
                    print(f"Prepared batch {m['batch_num']}: job_dir={m['job_dir']}")
                return 0

            # 2. Orchestration Loop
            print(f"\nProcessing {len(pending_manifests)} batches...")
            while pending_manifests or active_manifests:
                # Fill active queue
                while pending_manifests and len(active_manifests) < args.max_parallel:
                    m = pending_manifests.pop(0)
                    print(f"\nSubmitting Batch {m['batch_num']}/{len(batches)} (Pages {m['start_page']}-{m['end_page']})...")
                    submit_remote_job(api, m, args)
                    active_manifests.append(m)

                # Poll active jobs
                monitor_remote_jobs(api, active_manifests, args.poll_seconds, args.timeout_seconds)

                # Finalize finished jobs
                still_active = []
                for m in active_manifests:
                    if m.get("terminal_status") in {"complete", "error"}:
                        print(f"  Finalizing Batch {m['batch_num']}...")
                        try:
                            finalize_remote_job(api, m, args)
                            batch_results.append({
                                "markdown_path": m["markdown_path"],
                                "start_page": m["start_page"],
                                "end_page": m["end_page"]
                            })
                        except Exception as exc:
                            failures.append(f"Batch {m['batch_num']} (Pages {m['start_page']}-{m['end_page']}) failed: {exc}")
                    else:
                        still_active.append(m)
                active_manifests = still_active

                if not active_manifests and pending_manifests:
                    # This shouldn't happen with monitor_remote_jobs but for safety
                    time.sleep(args.poll_seconds)

            if failures:
                raise RuntimeError("One or more batches failed:\n" + "\n".join(failures))

            # 3. Merge results
            # Sort batch results by start_page to ensure correct order
            batch_results.sort(key=lambda x: x["start_page"])
            
            final_md_path = args.pdf.with_suffix(".md")
            merge_extractions(batch_results, final_md_path)
            
            elapsed_seconds = time.monotonic() - start_time
            record_extraction_history(args.pdf, page_count, elapsed_seconds, "complete (parallel queued)")
            
            if not args.save_artifacts:
                print(f"Cleaning up temporary batch files: {temp_batch_dir}")
                shutil.rmtree(temp_batch_dir)
                # Manifest job_dirs are already cleaned up by finalize_remote_job if save_artifacts is False
            
            print(f"\nSuccessfully processed {page_count} pages in {len(batches)} batches.")
            print(f"Final output: {final_md_path}")

        except (Exception, BaseException) as exc:
            failure = str(exc)
            elapsed_seconds = time.monotonic() - start_time
            record_extraction_history(args.pdf, page_count, elapsed_seconds, "failed (parallel queued)", failure)
            print(f"Parallel batching failed: {failure}")
            raise
        
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
