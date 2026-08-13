#!/usr/bin/env python3
"""Build, run, and independently verify the C2^5 h(6) obstruction."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

from h6_c2_5 import independent_certificate


ENUMERATION_PATTERN = re.compile(
    r"^enumeration pencils=(\d+) common_radical_zero=(\d+)$"
)
PROFILES_PATTERN = re.compile(r"^profiles rank_244=(\d+) rank_444=(\d+)$")
SEARCH_PATTERN = re.compile(
    r"^search target=(\d+) witnesses=(\d+) total_nodes=(\d+) "
    r"maximum_nodes=(\d+) hardest=(\d+),(\d+) digest=([0-9a-f]+) "
    r"cpu_seconds=([0-9.]+)$"
)
REPRESENTATIVE_PATTERN = re.compile(
    r"^representative profile=(244|444) a=(\d+) b=(\d+) clique=([0-9,]+)$"
)


def parse_c_output(stdout: str) -> dict:
    result = {"representatives": []}
    for line in stdout.splitlines():
        match = ENUMERATION_PATTERN.match(line)
        if match:
            result["pencil_count"] = int(match.group(1))
            result["common_radical_zero_pencil_count"] = int(match.group(2))
            continue
        match = PROFILES_PATTERN.match(line)
        if match:
            result["rank_profile_counts"] = {
                "244": int(match.group(1)),
                "444": int(match.group(2)),
            }
            continue
        match = SEARCH_PATTERN.match(line)
        if match:
            result["search"] = {
                "target_clique_size": int(match.group(1)),
                "witness_count": int(match.group(2)),
                "total_search_nodes": int(match.group(3)),
                "maximum_search_nodes": int(match.group(4)),
                "hardest_pencil": [int(match.group(5)), int(match.group(6))],
                "witness_digest_fnv1a64": match.group(7),
                "cpu_seconds": float(match.group(8)),
            }
            continue
        match = REPRESENTATIVE_PATTERN.match(line)
        if match:
            result["representatives"].append(
                {
                    "rank_profile": match.group(1),
                    "pencil": [int(match.group(2)), int(match.group(3))],
                    "clique_vectors": [int(value) for value in match.group(4).split(",")],
                }
            )
    required = {
        "pencil_count",
        "common_radical_zero_pencil_count",
        "rank_profile_counts",
        "search",
        "representatives",
    }
    if set(result) != required or len(result["representatives"]) != 2:
        raise ValueError("incomplete C solver output")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    parser.add_argument("--compiler", default="cc")
    args = parser.parse_args()

    repository = Path(__file__).resolve().parents[2]
    config_raw = args.config.read_bytes()
    config = json.loads(config_raw)
    source = repository / config["c_source"]
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="erdos117-h6-c2-5-") as temporary:
        executable = Path(temporary) / "h6_c2_5_pencils"
        compile_command = [
            args.compiler,
            "-O3",
            "-std=c11",
            "-Wall",
            "-Wextra",
            "-Werror",
            str(source),
            "-o",
            str(executable),
        ]
        subprocess.run(compile_command, check=True, capture_output=True, text=True)
        compiler_version = subprocess.run(
            [args.compiler, "--version"], check=True, capture_output=True, text=True
        ).stdout.splitlines()[0]
        completed = subprocess.run(
            [str(executable)], check=True, capture_output=True, text=True
        )
    c_certificate = parse_c_output(completed.stdout)
    independent = independent_certificate()

    expected = config["expected"]
    if c_certificate["pencil_count"] != expected["pencil_count"]:
        raise AssertionError("C pencil count differs from configuration")
    if c_certificate["common_radical_zero_pencil_count"] != expected[
        "common_radical_zero_pencil_count"
    ]:
        raise AssertionError("C radical-zero count differs from configuration")
    if c_certificate["rank_profile_counts"] != expected["rank_profile_counts"]:
        raise AssertionError("C rank-profile counts differ from configuration")
    if c_certificate["search"]["target_clique_size"] != expected["target_clique_size"]:
        raise AssertionError("C target differs from configuration")
    if c_certificate["search"]["witness_count"] != independent[
        "common_radical_zero_pencil_count"
    ]:
        raise AssertionError("C did not find one witness for every pencil")
    if c_certificate["pencil_count"] != independent["pencil_count"]:
        raise AssertionError("C and Python pencil counts disagree")
    if c_certificate["common_radical_zero_pencil_count"] != independent[
        "common_radical_zero_pencil_count"
    ]:
        raise AssertionError("C and Python radical-zero counts disagree")
    python_profiles = {
        "".join(map(str, record["rank_profile"])): record["pencil_count"]
        for record in independent["pencil_orbits"]
    }
    if c_certificate["rank_profile_counts"] != python_profiles:
        raise AssertionError("C and Python rank-profile counts disagree")

    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "configuration": str(args.config),
        "configuration_sha256": hashlib.sha256(config_raw).hexdigest(),
        "solver_source": config["c_source"],
        "solver_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "compiler": compiler_version,
            "external_dependencies": [],
        },
        "elapsed_wall_seconds": time.monotonic() - started,
        "c_exhaustive_certificate": c_certificate,
        "independent_python_certificate": independent,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    transcript = completed.stdout.rstrip() + "\n"
    transcript += (
        "independent_python pencils=%d radical_zero=%d pencil_orbits=%s "
        "rank_two_subspaces=%d rank_two_radical_zero=%d elapsed_wall_seconds=%.6f\n"
        % (
            independent["pencil_count"],
            independent["common_radical_zero_pencil_count"],
            [(record["rank_profile"], record["pencil_count"], record["omega"])
             for record in independent["pencil_orbits"]],
            independent["rank_two_subspace_count"],
            independent["rank_two_radical_zero_orbit"]["subspace_count"],
            output["elapsed_wall_seconds"],
        )
    )
    transcript += "wrote certificate to %s\n" % args.output
    print(transcript, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(transcript, encoding="utf-8")


if __name__ == "__main__":
    main()
