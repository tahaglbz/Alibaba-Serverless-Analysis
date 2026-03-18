#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import pandas as pd


def _warn(msg: str) -> None:
    print(f"[WARN] {msg}")


def _info(msg: str) -> None:
    print(f"[INFO] {msg}")


def _normalize_col_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(name).strip().lower())


def _find_col(columns: Iterable[str], candidates: Iterable[str]) -> Optional[str]:
    normalized_map = {_normalize_col_name(col): col for col in columns}
    for cand in candidates:
        matched = normalized_map.get(_normalize_col_name(cand))
        if matched is not None:
            return matched
    return None


def _extract_function_set_from_path(path: Path) -> Optional[str]:
    for part in path.parts:
        if re.fullmatch(r"NEW\d+", part):
            return part
    match = re.search(r"NEW\d+", path.name)
    if match:
        return match.group(0)
    return None


def _extract_run_id_from_path(path: Path) -> Optional[int]:
    # For paths like .../NEW10/1/file.xlsx and .../StateMachine.../1/file.xls,
    # the immediate parent folder should be the run id.
    run_part = path.parent.name
    if run_part.isdigit():
        return int(run_part)
    return None


def _read_excel_safe(file_path: Path) -> Optional[pd.DataFrame]:
    try:
        if file_path.suffix.lower() == ".xls":
            return pd.read_excel(file_path, engine="xlrd")
        return pd.read_excel(file_path)
    except FileNotFoundError:
        _warn(f"Missing file: {file_path}")
    except Exception as exc:
        _warn(f"Failed to read {file_path}: {exc}")
    return None


def _build_functions_frame(
    df: pd.DataFrame, file_path: Path, source: str
) -> Optional[pd.DataFrame]:
    required_map: Dict[str, List[str]] = {
        "function_id": ["FunctionName", "function_name", "function"],
        "state": ["FunctionState", "state"],
        "memory_mb": ["MemorySize", "memory_mb", "memory"],
        "cpu_cores": ["CpuSize", "cpu_cores", "cpu"],
        "billed_duration_ms": [
            "BilledDuration",
            "billed_duration_ms",
            "duration",
            "duration_ms",
        ],
        "requested_id": ["RequestedId", "RequestId", "requested_id", "request_id"],
        "timestamp": ["UTCTimeStamp", "UTCTimestamp", "utc_timestamp", "timestamp"],
    }

    col_lookup: Dict[str, str] = {}
    for out_col, candidates in required_map.items():
        found = _find_col(df.columns, candidates)
        if found is None and out_col != "requested_id":
            _warn(f"Skipping {file_path}: missing required column for {out_col}")
            return None
        if found is not None:
            col_lookup[out_col] = found

    out = pd.DataFrame()
    out["function_id"] = df[col_lookup["function_id"]].astype(str)
    out["state"] = df[col_lookup["state"]].astype(str)
    out["memory_mb"] = pd.to_numeric(df[col_lookup["memory_mb"]], errors="coerce")
    out["cpu_cores"] = pd.to_numeric(df[col_lookup["cpu_cores"]], errors="coerce")
    out["billed_duration_ms"] = pd.to_numeric(
        df[col_lookup["billed_duration_ms"]], errors="coerce"
    )
    out["timestamp"] = pd.to_numeric(df[col_lookup["timestamp"]], errors="coerce")

    if "requested_id" in col_lookup:
        out["requested_id"] = df[col_lookup["requested_id"]].astype(str)
    else:
        # Keep row but make dedup impossible for this record.
        out["requested_id"] = pd.NA

    function_set = _extract_function_set_from_path(file_path)
    run_id = _extract_run_id_from_path(file_path)

    if function_set is None:
        _warn(f"Could not infer function_set from path: {file_path}")
        return None
    if run_id is None:
        _warn(f"Could not infer run_id from path: {file_path}")
        return None

    out["function_set"] = function_set
    out["run_id"] = run_id
    out["source"] = source

    # Keep both Success and Fail rows, only drop non-positive/invalid durations.
    out = out[out["billed_duration_ms"].notna() & (out["billed_duration_ms"] > 0)]

    # Type normalization.
    out["memory_mb"] = out["memory_mb"].round().astype("Int64")
    out["billed_duration_ms"] = out["billed_duration_ms"].round().astype("Int64")
    out["timestamp"] = out["timestamp"].round().astype("Int64")
    out["cpu_cores"] = out["cpu_cores"].astype(float)
    out["run_id"] = out["run_id"].astype(int)

    out = out[
        [
            "function_id",
            "memory_mb",
            "cpu_cores",
            "billed_duration_ms",
            "state",
            "timestamp",
            "function_set",
            "run_id",
            "source",
            "requested_id",
        ]
    ]
    return out


def process_function_logs(datasets_dir: Path) -> pd.DataFrame:
    frames: List[pd.DataFrame] = []

    invoke_root = (
        datasets_dir / "aliyunfc_functions_invoke_results_got_by_cloudwatchlog"
    )
    if not invoke_root.exists():
        _warn(f"Missing invoke results directory: {invoke_root}")
    else:
        for set_dir in sorted(p for p in invoke_root.iterdir() if p.is_dir()):
            for run_dir in sorted(p for p in set_dir.iterdir() if p.is_dir()):
                loaded_rows = 0
                for xlsx_file in sorted(run_dir.glob("*.xlsx")):
                    raw = _read_excel_safe(xlsx_file)
                    if raw is None:
                        continue
                    cleaned = _build_functions_frame(
                        raw, xlsx_file, source="invoke_log"
                    )
                    if cleaned is None:
                        continue
                    loaded_rows += len(cleaned)
                    frames.append(cleaned)
                _info(f"Processed {run_dir}: loaded {loaded_rows} rows")

    sm_root = datasets_dir / "aliyunfc_StateMachine_invoke_results"
    if not sm_root.exists():
        _warn(f"Missing state machine directory: {sm_root}")
    else:
        for run_dir in sorted(p for p in sm_root.iterdir() if p.is_dir()):
            loaded_rows = 0
            for xls_file in sorted(run_dir.glob("*.xls")):
                raw = _read_excel_safe(xls_file)
                if raw is None:
                    continue
                cleaned = _build_functions_frame(raw, xls_file, source="statemachine")
                if cleaned is None:
                    continue
                loaded_rows += len(cleaned)
                frames.append(cleaned)
            _info(f"Processed {run_dir}: loaded {loaded_rows} rows")

    if not frames:
        return pd.DataFrame(
            columns=[
                "function_id",
                "memory_mb",
                "cpu_cores",
                "billed_duration_ms",
                "state",
                "timestamp",
                "function_set",
                "run_id",
                "source",
            ]
        )

    combined = pd.concat(frames, ignore_index=True)

    # Remove exact duplicates by request id when available.
    has_request_id = combined["requested_id"].notna() & (combined["requested_id"] != "")
    with_req = combined[has_request_id].drop_duplicates(
        subset=["requested_id"], keep="first"
    )
    without_req = combined[~has_request_id]
    combined = pd.concat([with_req, without_req], ignore_index=True)

    combined = combined.sort_values(
        ["function_id", "timestamp"], kind="stable"
    ).reset_index(drop=True)

    return combined.drop(columns=["requested_id"])


def process_perf_profiles(datasets_dir: Path) -> pd.DataFrame:
    perf_dir = datasets_dir / "aliyunfc_functions_perf_profile_cpu"
    rows: List[Dict[str, object]] = []

    if not perf_dir.exists():
        _warn(f"Missing perf profile directory: {perf_dir}")
        return pd.DataFrame(
            columns=["function_id", "memory_mb", "cpu_cores", "duration_ms"]
        )

    loaded_total = 0
    for json_file in sorted(perf_dir.glob("f*_perf_profile.json")):
        match = re.match(r"(f\d+)_perf_profile\.json$", json_file.name)
        if not match:
            _warn(f"Skipping unexpected perf profile filename: {json_file.name}")
            continue
        function_id = match.group(1)

        try:
            with json_file.open("r", encoding="utf-8") as f:
                payload = json.load(f)
        except FileNotFoundError:
            _warn(f"Missing file: {json_file}")
            continue
        except Exception as exc:
            _warn(f"Failed to parse {json_file}: {exc}")
            continue

        if not isinstance(payload, dict):
            _warn(f"Skipping {json_file}: expected a flat dict")
            continue

        file_rows = 0
        for key, duration in payload.items():
            try:
                memory_str, cpu_str = str(key).split(",", maxsplit=1)
                memory_mb = int(float(memory_str))
                cpu_cores = float(cpu_str)
                duration_ms = int(duration)
            except Exception:
                _warn(f"Skipping malformed entry in {json_file}: {key} -> {duration}")
                continue

            if duration_ms <= 0:
                continue

            rows.append(
                {
                    "function_id": function_id,
                    "memory_mb": memory_mb,
                    "cpu_cores": cpu_cores,
                    "duration_ms": duration_ms,
                }
            )
            file_rows += 1
        loaded_total += file_rows
        _info(
            f"Processed {json_file.parent.name}/{json_file.name}: loaded {file_rows} rows"
        )

    _info(f"Processed {perf_dir}: loaded {loaded_total} rows")

    if not rows:
        return pd.DataFrame(
            columns=["function_id", "memory_mb", "cpu_cores", "duration_ms"]
        )

    return (
        pd.DataFrame(rows)
        .sort_values(["function_id", "memory_mb", "cpu_cores"], kind="stable")
        .reset_index(drop=True)
    )


def print_summary(functions_df: pd.DataFrame, perf_df: pd.DataFrame) -> None:
    total_function_rows = len(functions_df)
    unique_functions = (
        int(functions_df["function_id"].nunique()) if total_function_rows > 0 else 0
    )

    if total_function_rows > 0:
        success_count = int((functions_df["state"] == "Success").sum())
        success_rate = (success_count / total_function_rows) * 100.0
    else:
        success_rate = 0.0

    print("\n=== Preprocess Summary ===")
    print(f"Total rows in functions_combined.csv: {total_function_rows}")
    print(f"Unique function IDs: {unique_functions}")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Total rows in perf_profile_combined.csv: {len(perf_df)}")


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    datasets_dir = repo_root / "data" / "datasets"
    processed_dir = repo_root / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    if importlib.util.find_spec("xlrd") is None:
        _warn(
            "xlrd is not installed. .xls files may fail to load. Install with: pip install xlrd"
        )

    _info(f"Using datasets directory: {datasets_dir}")

    functions_df = process_function_logs(datasets_dir)
    perf_df = process_perf_profiles(datasets_dir)

    functions_out = processed_dir / "functions_combined.csv"
    perf_out = processed_dir / "perf_profile_combined.csv"

    functions_df.to_csv(functions_out, index=False)
    perf_df.to_csv(perf_out, index=False)

    _info(f"Wrote {functions_out}")
    _info(f"Wrote {perf_out}")

    print_summary(functions_df, perf_df)


if __name__ == "__main__":
    main()
