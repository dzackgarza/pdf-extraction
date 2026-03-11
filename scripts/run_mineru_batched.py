#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
import traceback
from datetime import UTC, datetime
from pathlib import Path

import psutil
from pypdf import PdfReader

DEFAULT_BATCH_SIZE = 1
DEFAULT_HEARTBEAT_SECONDS = 10.0
DEFAULT_INFERENCE_BATCH = 1
DEFAULT_METHOD = "auto"
DEFAULT_MONITOR_INTERVAL_SECONDS = 1.0
DEFAULT_RENDER_THREADS = 1
DEFAULT_TERMINATE_GRACE_SECONDS = 15.0

_JSON_INDENT = 2
_MB = 1024 * 1024
_GB = 1024 * 1024 * 1024


class TerminationRequested(RuntimeError):
    """Raised when the supervisor receives a termination signal."""


class CpuTracker:
    """Tracks per-process CPU usage between snapshots."""

    def __init__(self) -> None:
        self._last_wall_time = time.monotonic()
        self._last_cpu_times: dict[int, float] = {}

    def prime(self, processes: list[psutil.Process]) -> None:
        self._last_wall_time = time.monotonic()
        for proc in processes:
            try:
                cpu_times = proc.cpu_times()
            except psutil.Error:
                continue
            self._last_cpu_times[proc.pid] = cpu_times.user + cpu_times.system

    def cpu_pct(self, proc: psutil.Process, *, now: float) -> float:
        try:
            cpu_times = proc.cpu_times()
        except psutil.Error:
            return 0.0

        current_total = cpu_times.user + cpu_times.system
        previous_total = self._last_cpu_times.get(proc.pid)
        self._last_cpu_times[proc.pid] = current_total
        elapsed = max(now - self._last_wall_time, 1e-6)
        if previous_total is None:
            return 0.0
        return round(max(0.0, (current_total - previous_total) / elapsed * 100), 2)

    def finish_snapshot(self, *, now: float, active_pids: set[int]) -> None:
        self._last_wall_time = now
        self._last_cpu_times = {
            pid: cpu_time
            for pid, cpu_time in self._last_cpu_times.items()
            if pid in active_pids
        }


class ProgressTail:
    """Reads appended MinerU progress events without rescanning the whole log."""

    def __init__(self, path: Path) -> None:
        self._path = path
        self._offset = 0
        self._event_count = 0
        self._last_payload: dict[str, object] | None = None

    def snapshot(self) -> dict[str, object]:
        if not self._path.exists():
            return {
                "path": str(self._path),
                "exists": False,
                "event_count": self._event_count,
                "last_event": None,
                "last_timestamp": None,
            }

        file_size = self._path.stat().st_size
        if file_size < self._offset:
            self._offset = 0

        with self._path.open("r", encoding="utf-8") as handle:
            handle.seek(self._offset)
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                payload = json.loads(line)
                if isinstance(payload, dict):
                    self._last_payload = payload
                    self._event_count += 1
            self._offset = handle.tell()

        return {
            "path": str(self._path),
            "exists": True,
            "event_count": self._event_count,
            "last_event": None if self._last_payload is None else self._last_payload.get("event"),
            "last_timestamp": None if self._last_payload is None else self._last_payload.get("timestamp"),
        }


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "job"


def mb(value: int) -> float:
    return round(value / _MB, 2)


def gb(value: int) -> float:
    return round(value / _GB, 2)


def read_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"expected object in {path}"
    return payload


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=_JSON_INDENT), encoding="utf-8")


def append_json_line(path: Path, payload: dict[str, object]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        json.dump(payload, handle, sort_keys=True)
        handle.write("\n")


def emit_event(events_path: Path, event: str, **fields: object) -> None:
    payload = {"timestamp": utc_now(), "event": event, **fields}
    print(json.dumps(payload, sort_keys=True), flush=True)
    append_json_line(events_path, payload)


def coalesce(value: object, fallback: object) -> object:
    return fallback if value is None else value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Supervise MinerU page batches with resumable manifests and resource logging.",
    )
    parser.add_argument("--resume-job-dir", type=Path, help="Resume an existing job from run-config.json.")
    parser.add_argument("--pdf", type=Path, help="Input PDF path.")
    parser.add_argument("--job-dir", type=Path, help="Output directory for logs, manifests, and batch artifacts.")
    parser.add_argument("--batch-size", type=int, help="Pages per MinerU worker batch.")
    parser.add_argument("--start-page", type=int, help="0-based inclusive start page.")
    parser.add_argument("--end-page", type=int, help="0-based inclusive end page.")
    parser.add_argument(
        "--method",
        choices=["auto", "txt", "ocr"],
        help="MinerU pipeline parse method.",
    )
    parser.add_argument("--lang", help="OCR language hint for MinerU pipeline mode.")
    parser.add_argument("--heartbeat-seconds", type=float, help="Seconds between resource heartbeats.")
    parser.add_argument("--render-threads", type=int, help="Value for MINERU_PDF_RENDER_THREADS.")
    parser.add_argument("--min-inference-batch", type=int, help="Value for MINERU_MIN_BATCH_INFERENCE_SIZE.")
    parser.add_argument("--model-source", help="Value for MINERU_MODEL_SOURCE.")
    parser.add_argument(
        "--monitor-interval-seconds",
        type=float,
        default=DEFAULT_MONITOR_INTERVAL_SECONDS,
        help="Polling interval for worker process monitoring.",
    )
    parser.add_argument(
        "--terminate-grace-seconds",
        type=float,
        default=DEFAULT_TERMINATE_GRACE_SECONDS,
        help="Grace period before escalating a worker termination to SIGKILL.",
    )
    parser.add_argument(
        "--stop-after-batches",
        type=int,
        default=None,
        help="Process at most this many pending batches, then pause cleanly.",
    )
    parser.add_argument(
        "--formula",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Enable formula parsing.",
    )
    parser.add_argument(
        "--table",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Enable table parsing.",
    )
    return parser.parse_args()


def configure_env(args: argparse.Namespace) -> dict[str, str]:
    env_updates = {
        "MINERU_DEVICE_MODE": "cpu",
        "MINERU_MODEL_SOURCE": args.model_source,
        "MINERU_PDF_RENDER_THREADS": str(args.render_threads),
        "MINERU_MIN_BATCH_INFERENCE_SIZE": str(args.min_inference_batch),
        "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1",
        "PYTHONUNBUFFERED": "1",
        "TOKENIZERS_PARALLELISM": "false",
    }
    for key, value in env_updates.items():
        os.environ[key] = value
    return env_updates


def get_page_count(pdf_path: Path) -> int:
    with pdf_path.open("rb") as handle:
        return len(PdfReader(handle).pages)


def plan_batches(start_page: int, end_page: int, batch_size: int) -> list[tuple[int, int]]:
    batches: list[tuple[int, int]] = []
    page = start_page
    while page <= end_page:
        batch_end = min(page + batch_size - 1, end_page)
        batches.append((page, batch_end))
        page = batch_end + 1
    return batches


def batch_tag(page_start: int, page_end: int) -> str:
    return f"p{page_start:04d}-p{page_end:04d}"


def default_batch_record(batch_index: int, page_start: int, page_end: int) -> dict[str, object]:
    return {
        "batch_index": batch_index,
        "batch_tag": batch_tag(page_start, page_end),
        "page_start": page_start,
        "page_end": page_end,
        "status": "pending",
        "attempts": [],
        "duration_seconds": None,
        "markdown_path": None,
        "markdown_size_bytes": None,
        "peak_rss_mb": 0.0,
        "peak_vms_mb": 0.0,
        "peak_cpu_pct": 0.0,
        "peak_process_count": 0,
        "last_progress_event": None,
        "last_progress_timestamp": None,
    }


def is_complete_batch_record(record: dict[str, object]) -> bool:
    markdown_path = record.get("markdown_path")
    if record.get("status") != "complete" or not isinstance(markdown_path, str):
        return False
    return Path(markdown_path).is_file()


def repair_batch_record(record: dict[str, object]) -> dict[str, object]:
    if record.get("status") == "running":
        record["status"] = "pending"
    if record.get("status") == "complete" and not is_complete_batch_record(record):
        record["status"] = "pending"
        record["markdown_path"] = None
        record["markdown_size_bytes"] = None
    if "attempts" not in record or not isinstance(record["attempts"], list):
        record["attempts"] = []
    return record


def merge_manifest_batches(
    planned_batches: list[tuple[int, int]],
    existing_batches: list[dict[str, object]],
) -> list[dict[str, object]]:
    existing_by_tag = {}
    for record in existing_batches:
        tag = record.get("batch_tag")
        if isinstance(tag, str):
            existing_by_tag[tag] = repair_batch_record(record)

    merged: list[dict[str, object]] = []
    for batch_index, (page_start, page_end) in enumerate(planned_batches, start=1):
        default_record = default_batch_record(batch_index, page_start, page_end)
        current_tag = default_record["batch_tag"]
        assert isinstance(current_tag, str)
        existing = existing_by_tag.get(current_tag)
        if existing is None:
            merged.append(default_record)
            continue

        merged_record = default_record | {
            "status": existing.get("status", "pending"),
            "attempts": existing.get("attempts", []),
            "duration_seconds": existing.get("duration_seconds"),
            "markdown_path": existing.get("markdown_path"),
            "markdown_size_bytes": existing.get("markdown_size_bytes"),
            "peak_rss_mb": existing.get("peak_rss_mb", 0.0),
            "peak_vms_mb": existing.get("peak_vms_mb", 0.0),
            "peak_cpu_pct": existing.get("peak_cpu_pct", 0.0),
            "peak_process_count": existing.get("peak_process_count", 0),
            "last_progress_event": existing.get("last_progress_event"),
            "last_progress_timestamp": existing.get("last_progress_timestamp"),
        }
        merged.append(repair_batch_record(merged_record))
    return merged


def validate_config(args: argparse.Namespace, page_count: int, end_page: int) -> None:
    if not args.pdf.is_file():
        raise SystemExit(f"input pdf does not exist: {args.pdf}")
    if args.batch_size <= 0:
        raise SystemExit("--batch-size must be positive")
    if args.start_page < 0:
        raise SystemExit("--start-page must be >= 0")
    if args.start_page > end_page:
        raise SystemExit("--start-page is past the last page of the pdf")
    if args.end_page is not None and args.end_page < args.start_page:
        raise SystemExit("--end-page must be >= --start-page")
    if args.heartbeat_seconds <= 0:
        raise SystemExit("--heartbeat-seconds must be positive")
    if args.render_threads <= 0:
        raise SystemExit("--render-threads must be positive")
    if args.min_inference_batch <= 0:
        raise SystemExit("--min-inference-batch must be positive")
    if args.monitor_interval_seconds <= 0:
        raise SystemExit("--monitor-interval-seconds must be positive")
    if args.terminate_grace_seconds <= 0:
        raise SystemExit("--terminate-grace-seconds must be positive")
    if page_count == 0:
        raise RuntimeError(f"pdf has no pages: {args.pdf}")


def resolve_args(args: argparse.Namespace) -> argparse.Namespace:
    config: dict[str, object] | None = None
    if args.resume_job_dir is not None:
        args.job_dir = args.resume_job_dir.expanduser().resolve()
        config_path = args.job_dir / "run-config.json"
        if not config_path.is_file():
            raise SystemExit(f"resume job is missing run-config.json: {config_path}")
        config = read_json(config_path)

    if args.job_dir is None:
        raise SystemExit("--job-dir is required unless --resume-job-dir is used")
    if args.pdf is None and config is None:
        raise SystemExit("--pdf is required unless --resume-job-dir is used")

    pdf_value = args.pdf
    if pdf_value is None:
        assert config is not None
        pdf_value = Path(str(config["pdf"]))
    args.pdf = pdf_value.expanduser().resolve()
    args.job_dir = args.job_dir.expanduser().resolve()
    args.batch_size = int(coalesce(args.batch_size, None if config is None else config.get("batch_size")) or DEFAULT_BATCH_SIZE)
    args.start_page = int(coalesce(args.start_page, None if config is None else config.get("selected_start_page")) or 0)
    if args.end_page is None and config is not None:
        config_end_page = config.get("selected_end_page")
        args.end_page = None if config_end_page is None else int(config_end_page)
    args.method = str(coalesce(args.method, None if config is None else config.get("method")) or DEFAULT_METHOD)
    args.lang = str(coalesce(args.lang, None if config is None else config.get("lang")) or "en")
    args.heartbeat_seconds = float(
        coalesce(args.heartbeat_seconds, None if config is None else config.get("heartbeat_seconds"))
        or DEFAULT_HEARTBEAT_SECONDS
    )
    args.render_threads = int(
        coalesce(args.render_threads, None if config is None else config.get("render_threads")) or DEFAULT_RENDER_THREADS
    )
    args.min_inference_batch = int(
        coalesce(args.min_inference_batch, None if config is None else config.get("min_inference_batch"))
        or DEFAULT_INFERENCE_BATCH
    )
    args.model_source = str(
        coalesce(args.model_source, None if config is None else config.get("model_source"))
        or os.environ.get("MINERU_MODEL_SOURCE", "huggingface")
    )
    if args.formula is None:
        args.formula = True if config is None else bool(config.get("formula", True))
    if args.table is None:
        args.table = True if config is None else bool(config.get("table", True))

    args.job_dir.mkdir(parents=True, exist_ok=True)
    page_count = get_page_count(args.pdf)
    end_page = page_count - 1 if args.end_page is None else min(args.end_page, page_count - 1)
    validate_config(args, page_count, end_page)
    args.end_page = end_page
    return args


def config_payload(args: argparse.Namespace, page_count: int) -> dict[str, object]:
    return {
        "pdf": str(args.pdf),
        "job_dir": str(args.job_dir),
        "page_count": page_count,
        "selected_start_page": args.start_page,
        "selected_end_page": args.end_page,
        "batch_size": args.batch_size,
        "method": args.method,
        "lang": args.lang,
        "formula": args.formula,
        "table": args.table,
        "heartbeat_seconds": args.heartbeat_seconds,
        "render_threads": args.render_threads,
        "min_inference_batch": args.min_inference_batch,
        "model_source": args.model_source,
        "monitor_interval_seconds": args.monitor_interval_seconds,
        "terminate_grace_seconds": args.terminate_grace_seconds,
    }


def combined_markdown_path(job_dir: Path, pdf_path: Path) -> Path:
    return job_dir / "combined" / f"{slugify(pdf_path.stem)}.md"


def load_or_init_manifest(
    *,
    args: argparse.Namespace,
    manifest_path: Path,
    page_count: int,
    planned_batches: list[tuple[int, int]],
) -> dict[str, object]:
    combined_path = combined_markdown_path(args.job_dir, args.pdf)
    if manifest_path.is_file():
        manifest = read_json(manifest_path)
        existing_pdf = manifest.get("pdf")
        if existing_pdf is not None and str(existing_pdf) != str(args.pdf):
            raise RuntimeError(f"job dir points at a different pdf: {existing_pdf}")
        existing_batches = manifest.get("batches", [])
        assert isinstance(existing_batches, list), "manifest batches must be a list"
        batches = merge_manifest_batches(planned_batches, existing_batches)
    else:
        batches = [default_batch_record(index, start, end) for index, (start, end) in enumerate(planned_batches, start=1)]
        manifest = {}

    merged_manifest = {
        "version": 2,
        "status": manifest.get("status", "pending"),
        "pdf": str(args.pdf),
        "job_dir": str(args.job_dir),
        "combined_markdown": str(combined_path),
        "page_count": page_count,
        "selected_start_page": args.start_page,
        "selected_end_page": args.end_page,
        "batch_size": args.batch_size,
        "method": args.method,
        "lang": args.lang,
        "formula": args.formula,
        "table": args.table,
        "heartbeat_seconds": args.heartbeat_seconds,
        "render_threads": args.render_threads,
        "min_inference_batch": args.min_inference_batch,
        "model_source": args.model_source,
        "batches": batches,
    }
    refresh_manifest_summary(merged_manifest)
    return merged_manifest


def refresh_manifest_summary(manifest: dict[str, object]) -> None:
    batches = manifest.get("batches", [])
    assert isinstance(batches, list)
    completed = sum(1 for record in batches if isinstance(record, dict) and is_complete_batch_record(record))
    manifest["completed_batches"] = completed
    manifest["batch_count"] = len(batches)
    manifest["pending_batches"] = len(batches) - completed
    manifest["peak_rss_mb"] = max(
        (
            float(record.get("peak_rss_mb", 0.0))
            for record in batches
            if isinstance(record, dict)
        ),
        default=0.0,
    )


def rebuild_combined_markdown(manifest: dict[str, object]) -> None:
    batches = manifest.get("batches", [])
    assert isinstance(batches, list)
    combined_path = Path(str(manifest["combined_markdown"]))
    combined_path.parent.mkdir(parents=True, exist_ok=True)
    parts: list[str] = []
    for record in batches:
        assert isinstance(record, dict)
        if not is_complete_batch_record(record):
            continue
        page_start = int(record["page_start"])
        page_end = int(record["page_end"])
        markdown_path = Path(str(record["markdown_path"]))
        markdown = markdown_path.read_text(encoding="utf-8").rstrip()
        parts.append(f"<!-- pages {page_start + 1}-{page_end + 1} -->\n\n{markdown}")
    combined_path.write_text("\n\n".join(parts) + ("\n" if parts else ""), encoding="utf-8")


def write_status(path: Path, payload: dict[str, object]) -> None:
    write_json(path, payload)


def get_processes(root_pid: int) -> list[psutil.Process]:
    try:
        root = psutil.Process(root_pid)
        return [root, *root.children(recursive=True)]
    except psutil.Error:
        return []


def prime_cpu_percent(root_pid: int, cpu_tracker: CpuTracker) -> None:
    processes = get_processes(root_pid)
    psutil.cpu_percent(None)
    cpu_tracker.prime(processes)


def collect_process_snapshot(root_pid: int, cpu_tracker: CpuTracker) -> dict[str, object]:
    system_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    system_cpu_pct = psutil.cpu_percent(None)
    now = time.monotonic()
    processes = get_processes(root_pid)

    total_rss = 0
    total_vms = 0
    total_cpu = 0.0
    top_processes: list[dict[str, object]] = []

    for proc in processes:
        try:
            memory_info = proc.memory_info()
            total_rss += memory_info.rss
            total_vms += memory_info.vms
            cpu_pct = cpu_tracker.cpu_pct(proc, now=now)
            total_cpu += cpu_pct
            top_processes.append(
                {
                    "pid": proc.pid,
                    "ppid": proc.ppid(),
                    "name": proc.name(),
                    "status": proc.status(),
                    "cpu_pct": round(cpu_pct, 2),
                    "rss_mb": mb(memory_info.rss),
                    "vms_mb": mb(memory_info.vms),
                    "cmd": " ".join(proc.cmdline()[:6]),
                }
            )
        except psutil.Error:
            continue

    top_processes.sort(key=lambda item: float(item["rss_mb"]), reverse=True)
    cpu_tracker.finish_snapshot(now=now, active_pids={int(item["pid"]) for item in top_processes})
    snapshot: dict[str, object] = {
        "process_count": len(top_processes),
        "rss_mb": mb(total_rss),
        "vms_mb": mb(total_vms),
        "cpu_pct": round(total_cpu, 2),
        "system_cpu_pct": round(system_cpu_pct, 2),
        "system_memory_pct": round(system_memory.percent, 2),
        "system_available_gb": gb(system_memory.available),
        "system_used_gb": gb(system_memory.used),
        "swap_used_gb": gb(swap_memory.used),
        "swap_pct": round(swap_memory.percent, 2),
        "top_processes": top_processes[:5],
    }
    if hasattr(os, "getloadavg"):
        load1, load5, load15 = os.getloadavg()
        snapshot["load_avg"] = [round(load1, 2), round(load5, 2), round(load15, 2)]
    return snapshot


def batch_paths(job_dir: Path, batch_tag_value: str, attempt_number: int) -> dict[str, Path]:
    attempt_dir = job_dir / "batches" / batch_tag_value / f"attempt-{attempt_number:03d}"
    output_dir = attempt_dir / "output"
    return {
        "attempt_dir": attempt_dir,
        "output_dir": output_dir,
        "progress_log_path": attempt_dir / "progress.jsonl",
        "worker_log_path": attempt_dir / "worker.log",
    }


def exit_signal_name(returncode: int | None) -> str | None:
    if returncode is None or returncode >= 0:
        return None
    try:
        return signal.Signals(-returncode).name
    except ValueError:
        return f"SIG{-returncode}"


def terminate_process_tree(process: subprocess.Popen[str], grace_seconds: float) -> None:
    processes = []
    try:
        root = psutil.Process(process.pid)
        processes = [*root.children(recursive=True), root]
    except psutil.Error:
        processes = []

    for proc in processes:
        try:
            proc.terminate()
        except psutil.Error:
            continue

    _, alive = psutil.wait_procs(processes, timeout=grace_seconds)
    for proc in alive:
        try:
            proc.kill()
        except psutil.Error:
            continue

    try:
        process.wait(timeout=max(1.0, grace_seconds))
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=1.0)


def find_batch_markdown(output_dir: Path, batch_name: str) -> Path:
    matches = sorted(output_dir.rglob(f"{batch_name}.md"))
    if len(matches) != 1:
        raise RuntimeError(f"expected exactly one markdown output for {batch_name}, found {len(matches)}")
    return matches[0]


def install_signal_handlers(
    events_path: Path,
    signal_state: dict[str, object],
) -> None:
    def handle_signal(signum: int, _frame: object) -> None:
        signal_name = signal.Signals(signum).name
        signal_state["requested"] = True
        signal_state["signal"] = signal_name
        emit_event(events_path, "signal", signal=signal_name)

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)


def monitor_worker(
    *,
    args: argparse.Namespace,
    events_path: Path,
    status_path: Path,
    signal_state: dict[str, object],
    manifest: dict[str, object],
    batch_record: dict[str, object],
    process: subprocess.Popen[str],
    progress_log_path: Path,
) -> dict[str, object]:
    cpu_tracker = CpuTracker()
    prime_cpu_percent(process.pid, cpu_tracker)
    progress_tail = ProgressTail(progress_log_path)
    next_heartbeat = time.monotonic() + args.heartbeat_seconds
    peak_rss_mb = 0.0
    peak_vms_mb = 0.0
    peak_cpu_pct = 0.0
    peak_process_count = 0
    stop_requested = False
    attempt_started_at = utc_now()
    started_monotonic = time.monotonic()

    while True:
        snapshot = collect_process_snapshot(process.pid, cpu_tracker)
        progress_state = progress_tail.snapshot()
        peak_rss_mb = max(peak_rss_mb, float(snapshot["rss_mb"]))
        peak_vms_mb = max(peak_vms_mb, float(snapshot["vms_mb"]))
        peak_cpu_pct = max(peak_cpu_pct, float(snapshot["cpu_pct"]))
        peak_process_count = max(peak_process_count, int(snapshot["process_count"]))

        status_payload = {
            "timestamp": utc_now(),
            "phase": "running_batch",
            "job_dir": str(manifest["job_dir"]),
            "pdf": str(manifest["pdf"]),
            "completed_batches": manifest["completed_batches"],
            "batch_count": manifest["batch_count"],
            "pending_batches": manifest["pending_batches"],
            "current_batch": {
                "batch_index": batch_record["batch_index"],
                "batch_tag": batch_record["batch_tag"],
                "page_start": batch_record["page_start"],
                "page_end": batch_record["page_end"],
            },
            "progress": progress_state,
            "resources": snapshot,
            "peak_rss_mb": peak_rss_mb,
        }

        now = time.monotonic()
        if now >= next_heartbeat:
            emit_event(
                events_path,
                "heartbeat",
                batch_index=batch_record["batch_index"],
                batch_tag=batch_record["batch_tag"],
                page_start=batch_record["page_start"],
                page_end=batch_record["page_end"],
                progress=progress_state,
                resources=snapshot,
            )
            write_status(status_path, status_payload)
            next_heartbeat = now + args.heartbeat_seconds

        if bool(signal_state.get("requested")) and process.poll() is None:
            stop_requested = True
            emit_event(
                events_path,
                "batch_stop_requested",
                batch_index=batch_record["batch_index"],
                batch_tag=batch_record["batch_tag"],
                signal=signal_state.get("signal"),
                progress=progress_state,
            )
            terminate_process_tree(process, args.terminate_grace_seconds)

        returncode = process.poll()
        if returncode is not None:
            final_progress = progress_tail.snapshot()
            write_status(status_path, status_payload | {"phase": "batch_exited", "progress": final_progress})
            return {
                "started_at": attempt_started_at,
                "finished_at": utc_now(),
                "duration_seconds": round(time.monotonic() - started_monotonic, 2),
                "returncode": returncode,
                "exit_signal": exit_signal_name(returncode),
                "stop_requested": stop_requested,
                "peak_rss_mb": round(peak_rss_mb, 2),
                "peak_vms_mb": round(peak_vms_mb, 2),
                "peak_cpu_pct": round(peak_cpu_pct, 2),
                "peak_process_count": peak_process_count,
                "progress_event_count": final_progress["event_count"],
                "last_progress_event": final_progress["last_event"],
                "last_progress_timestamp": final_progress["last_timestamp"],
            }

        time.sleep(args.monitor_interval_seconds)


def run_batch_attempt(
    *,
    args: argparse.Namespace,
    manifest: dict[str, object],
    batch_record: dict[str, object],
    events_path: Path,
    status_path: Path,
    signal_state: dict[str, object],
    env_updates: dict[str, str],
) -> tuple[dict[str, object], Path | None]:
    attempts = batch_record.get("attempts", [])
    assert isinstance(attempts, list)
    attempt_number = len(attempts) + 1
    current_batch_tag = str(batch_record["batch_tag"])
    current_batch_name = f"{slugify(Path(str(manifest['pdf'])).stem)}_{current_batch_tag}"
    paths = batch_paths(args.job_dir, current_batch_tag, attempt_number)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    paths["output_dir"].mkdir(parents=True, exist_ok=True)

    worker_script = Path(__file__).with_name("run_mineru_batch_worker.py")
    command = [
        sys.executable,
        str(worker_script),
        "--pdf",
        str(args.pdf),
        "--output-dir",
        str(paths["output_dir"]),
        "--batch-name",
        current_batch_name,
        "--page-start",
        str(batch_record["page_start"]),
        "--page-end",
        str(batch_record["page_end"]),
        "--method",
        args.method,
        "--lang",
        args.lang,
        "--progress-log",
        str(paths["progress_log_path"]),
        "--progress-heartbeat-seconds",
        str(args.heartbeat_seconds),
    ]
    command.append("--formula" if args.formula else "--no-formula")
    command.append("--table" if args.table else "--no-table")

    emit_event(
        events_path,
        "batch_start",
        batch_index=batch_record["batch_index"],
        batch_count=manifest["batch_count"],
        batch_tag=current_batch_tag,
        page_start=batch_record["page_start"],
        page_end=batch_record["page_end"],
        attempt_number=attempt_number,
        worker_log_path=str(paths["worker_log_path"]),
        progress_log_path=str(paths["progress_log_path"]),
        output_dir=str(paths["output_dir"]),
        command=command,
    )

    child_env = os.environ.copy()
    child_env.update(env_updates)
    with paths["worker_log_path"].open("a", encoding="utf-8") as worker_log:
        process = subprocess.Popen(
            command,
            stdout=worker_log,
            stderr=subprocess.STDOUT,
            text=True,
            env=child_env,
        )
        monitor_summary = monitor_worker(
            args=args,
            events_path=events_path,
            status_path=status_path,
            signal_state=signal_state,
            manifest=manifest,
            batch_record=batch_record,
            process=process,
            progress_log_path=paths["progress_log_path"],
        )

    attempt_record = {
        "attempt_number": attempt_number,
        "started_at": monitor_summary["started_at"],
        "finished_at": monitor_summary["finished_at"],
        "duration_seconds": monitor_summary["duration_seconds"],
        "returncode": monitor_summary["returncode"],
        "exit_signal": monitor_summary["exit_signal"],
        "stop_requested": monitor_summary["stop_requested"],
        "peak_rss_mb": monitor_summary["peak_rss_mb"],
        "peak_vms_mb": monitor_summary["peak_vms_mb"],
        "peak_cpu_pct": monitor_summary["peak_cpu_pct"],
        "peak_process_count": monitor_summary["peak_process_count"],
        "progress_event_count": monitor_summary["progress_event_count"],
        "last_progress_event": monitor_summary["last_progress_event"],
        "last_progress_timestamp": monitor_summary["last_progress_timestamp"],
        "worker_log_path": str(paths["worker_log_path"]),
        "progress_log_path": str(paths["progress_log_path"]),
        "output_dir": str(paths["output_dir"]),
    }

    if int(monitor_summary["returncode"]) == 0:
        markdown_path = find_batch_markdown(paths["output_dir"], current_batch_name)
        attempt_record["status"] = "complete"
        attempt_record["markdown_path"] = str(markdown_path)
        attempt_record["markdown_size_bytes"] = markdown_path.stat().st_size
        return attempt_record, markdown_path

    attempt_record["status"] = "failed"
    if monitor_summary["stop_requested"] or monitor_summary["exit_signal"] is not None:
        attempt_record["status"] = "terminated"
    attempt_record["markdown_path"] = None
    attempt_record["markdown_size_bytes"] = None
    return attempt_record, None


def update_batch_record(
    batch_record: dict[str, object],
    attempt_record: dict[str, object],
    markdown_path: Path | None,
) -> None:
    attempts = batch_record.get("attempts", [])
    assert isinstance(attempts, list)
    attempts.append(attempt_record)
    batch_record["attempts"] = attempts
    batch_record["status"] = attempt_record["status"]
    batch_record["duration_seconds"] = attempt_record["duration_seconds"]
    batch_record["peak_rss_mb"] = attempt_record["peak_rss_mb"]
    batch_record["peak_vms_mb"] = attempt_record["peak_vms_mb"]
    batch_record["peak_cpu_pct"] = attempt_record["peak_cpu_pct"]
    batch_record["peak_process_count"] = attempt_record["peak_process_count"]
    batch_record["last_progress_event"] = attempt_record["last_progress_event"]
    batch_record["last_progress_timestamp"] = attempt_record["last_progress_timestamp"]
    if markdown_path is None:
        batch_record["markdown_path"] = None
        batch_record["markdown_size_bytes"] = None
        return
    batch_record["status"] = "complete"
    batch_record["markdown_path"] = str(markdown_path)
    batch_record["markdown_size_bytes"] = markdown_path.stat().st_size


def pause_requested(args: argparse.Namespace, processed_this_run: int) -> bool:
    if args.stop_after_batches is None:
        return False
    return processed_this_run >= args.stop_after_batches


def run_batches(args: argparse.Namespace) -> int:
    events_path = args.job_dir / "events.jsonl"
    manifest_path = args.job_dir / "manifest.json"
    status_path = args.job_dir / "status.json"
    config_path = args.job_dir / "run-config.json"
    signal_state: dict[str, object] = {"requested": False, "signal": None}
    install_signal_handlers(events_path, signal_state)

    page_count = get_page_count(args.pdf)
    planned_batches = plan_batches(args.start_page, args.end_page, args.batch_size)
    env_updates = configure_env(args)
    write_json(config_path, config_payload(args, page_count))
    manifest = load_or_init_manifest(
        args=args,
        manifest_path=manifest_path,
        page_count=page_count,
        planned_batches=planned_batches,
    )
    rebuild_combined_markdown(manifest)
    refresh_manifest_summary(manifest)
    manifest["status"] = "running"
    write_json(manifest_path, manifest)

    emit_event(
        events_path,
        "job_start",
        pdf=str(args.pdf),
        job_dir=str(args.job_dir),
        page_count=page_count,
        selected_start_page=args.start_page,
        selected_end_page=args.end_page,
        batch_count=manifest["batch_count"],
        completed_batches=manifest["completed_batches"],
        batch_size=args.batch_size,
        method=args.method,
        lang=args.lang,
        env=env_updates,
    )
    write_status(
        status_path,
        {
            "timestamp": utc_now(),
            "phase": "starting",
            "job_dir": str(args.job_dir),
            "pdf": str(args.pdf),
            "completed_batches": manifest["completed_batches"],
            "batch_count": manifest["batch_count"],
            "pending_batches": manifest["pending_batches"],
            "current_batch": None,
        },
    )

    batches = manifest["batches"]
    assert isinstance(batches, list)
    already_complete = sum(1 for record in batches if isinstance(record, dict) and is_complete_batch_record(record))
    if already_complete:
        emit_event(
            events_path,
            "job_resume",
            completed_batches=already_complete,
            pending_batches=manifest["pending_batches"],
            combined_markdown=str(manifest["combined_markdown"]),
        )

    processed_this_run = 0
    for record in batches:
        assert isinstance(record, dict)
        if is_complete_batch_record(record):
            continue
        if bool(signal_state.get("requested")):
            raise TerminationRequested(str(signal_state.get("signal")))
        if pause_requested(args, processed_this_run):
            manifest["status"] = "paused"
            refresh_manifest_summary(manifest)
            write_json(manifest_path, manifest)
            emit_event(
                events_path,
                "job_paused",
                completed_batches=manifest["completed_batches"],
                pending_batches=manifest["pending_batches"],
                combined_markdown=str(manifest["combined_markdown"]),
            )
            write_status(
                status_path,
                {
                    "timestamp": utc_now(),
                    "phase": "paused",
                    "job_dir": str(args.job_dir),
                    "pdf": str(args.pdf),
                    "completed_batches": manifest["completed_batches"],
                    "batch_count": manifest["batch_count"],
                    "pending_batches": manifest["pending_batches"],
                    "current_batch": None,
                },
            )
            return 0

        attempt_record, markdown_path = run_batch_attempt(
            args=args,
            manifest=manifest,
            batch_record=record,
            events_path=events_path,
            status_path=status_path,
            signal_state=signal_state,
            env_updates=env_updates,
        )
        update_batch_record(record, attempt_record, markdown_path)
        refresh_manifest_summary(manifest)
        rebuild_combined_markdown(manifest)
        write_json(manifest_path, manifest)
        processed_this_run += 1

        if is_complete_batch_record(record):
            emit_event(
                events_path,
                "batch_complete",
                batch_index=record["batch_index"],
                batch_tag=record["batch_tag"],
                page_start=record["page_start"],
                page_end=record["page_end"],
                duration_seconds=record["duration_seconds"],
                peak_rss_mb=record["peak_rss_mb"],
                peak_vms_mb=record["peak_vms_mb"],
                peak_cpu_pct=record["peak_cpu_pct"],
                progress_event_count=attempt_record["progress_event_count"],
                markdown_path=record["markdown_path"],
                combined_markdown=str(manifest["combined_markdown"]),
            )
            continue

        manifest["status"] = "failed"
        write_json(manifest_path, manifest)
        emit_event(
            events_path,
            "batch_failed",
            batch_index=record["batch_index"],
            batch_tag=record["batch_tag"],
            page_start=record["page_start"],
            page_end=record["page_end"],
            status=record["status"],
            peak_rss_mb=record["peak_rss_mb"],
            returncode=attempt_record["returncode"],
            exit_signal=attempt_record["exit_signal"],
            worker_log_path=attempt_record["worker_log_path"],
            progress_log_path=attempt_record["progress_log_path"],
        )
        write_status(
            status_path,
            {
                "timestamp": utc_now(),
                "phase": "failed",
                "job_dir": str(args.job_dir),
                "pdf": str(args.pdf),
                "completed_batches": manifest["completed_batches"],
                "batch_count": manifest["batch_count"],
                "pending_batches": manifest["pending_batches"],
                "current_batch": {
                    "batch_index": record["batch_index"],
                    "batch_tag": record["batch_tag"],
                    "page_start": record["page_start"],
                    "page_end": record["page_end"],
                },
                "failure": {
                    "status": record["status"],
                    "returncode": attempt_record["returncode"],
                    "exit_signal": attempt_record["exit_signal"],
                    "worker_log_path": attempt_record["worker_log_path"],
                    "progress_log_path": attempt_record["progress_log_path"],
                },
            },
        )
        return 1

    refresh_manifest_summary(manifest)
    manifest["status"] = "complete"
    write_json(manifest_path, manifest)
    emit_event(
        events_path,
        "job_complete",
        completed_batches=manifest["completed_batches"],
        pending_batches=manifest["pending_batches"],
        combined_markdown=str(manifest["combined_markdown"]),
        combined_markdown_size_bytes=Path(str(manifest["combined_markdown"])).stat().st_size,
        peak_rss_mb=manifest["peak_rss_mb"],
    )
    write_status(
        status_path,
        {
            "timestamp": utc_now(),
            "phase": "complete",
            "job_dir": str(args.job_dir),
            "pdf": str(args.pdf),
            "completed_batches": manifest["completed_batches"],
            "batch_count": manifest["batch_count"],
            "pending_batches": manifest["pending_batches"],
            "current_batch": None,
            "combined_markdown": str(manifest["combined_markdown"]),
            "peak_rss_mb": manifest["peak_rss_mb"],
        },
    )
    return 0


def main() -> int:
    args = resolve_args(parse_args())
    try:
        return run_batches(args)
    except TerminationRequested as exc:
        events_path = args.job_dir / "events.jsonl"
        emit_event(
            events_path,
            "job_terminated",
            error_type=type(exc).__name__,
            message=str(exc),
            traceback=traceback.format_exc(),
        )
        return 143
    except Exception as exc:  # noqa: BLE001
        events_path = args.job_dir / "events.jsonl"
        emit_event(
            events_path,
            "job_failed",
            error_type=type(exc).__name__,
            message=str(exc),
            traceback=traceback.format_exc(),
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
