#!/usr/bin/env python3
"""Build, run, and independently verify scalar-symplectic clique searches."""

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

from exact_invariants import verify_clique, verify_coloring
from scalar_symplectic import (
    projective_symplectic_graph,
    quotient_vectors,
    scalar_symplectic_adjacency,
    symplectic_spread,
)


CASE_PATTERN = re.compile(
    r"^case tail=(zero|nonzero) scalar=(square|nonsquare) "
    r"residual_vertices=(\d+) maximum_at_most=(\d+) "
    r"search_nodes=(\d+) cpu_seconds=([0-9.]+)$"
)
RESULT_PATTERN = re.compile(
    r"^result maximum=(\d+) total_search_nodes=(\d+) total_cpu_seconds=([0-9.]+)$"
)


def compile_solver(repository: Path, compiler: str, output: Path) -> str:
    command = [
        compiler,
        "-O3",
        "-std=c11",
        "-Wall",
        "-Wextra",
        "-Werror",
        str(repository / "src" / "c" / "scalar_symplectic_clique.c"),
        "-o",
        str(output),
    ]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    if completed.stderr:
        raise RuntimeError("compiler emitted diagnostics: %s" % completed.stderr)
    version = subprocess.run(
        [compiler, "--version"], check=True, capture_output=True, text=True
    ).stdout.splitlines()[0]
    return version


def parse_solver_output(stdout: str) -> dict:
    lines = stdout.splitlines()
    cases = []
    result = None
    for line in lines:
        match = CASE_PATTERN.match(line)
        if match:
            cases.append(
                {
                    "tail_orbit": match.group(1),
                    "scalar_square_class": match.group(2),
                    "residual_vertex_count": int(match.group(3)),
                    "maximum_at_most": int(match.group(4)),
                    "search_nodes": int(match.group(5)),
                    "cpu_seconds": float(match.group(6)),
                }
            )
            continue
        match = RESULT_PATTERN.match(line)
        if match:
            result = {
                "maximum": int(match.group(1)),
                "total_search_nodes": int(match.group(2)),
                "total_cpu_seconds": float(match.group(3)),
            }
    if len(cases) != 4 or result is None:
        raise ValueError("solver did not emit four cases and one final result")
    if sum(case["search_nodes"] for case in cases) != result["total_search_nodes"]:
        raise ValueError("case and total search-node counts disagree")
    return {"cases": cases, **result}


def verify_spread_certificate(prime: int, rank: int) -> dict:
    vectors = quotient_vectors(prime, rank)
    adjacency_vectors, adjacency = scalar_symplectic_adjacency(prime, rank)
    if vectors != adjacency_vectors:
        raise AssertionError("quotient vector order changed")
    spread = symplectic_spread(prime, rank, vectors)
    if not verify_coloring(adjacency, spread.colors):
        raise AssertionError("spread is not a coloring")
    return {
        "color_count": max(spread.colors) + 1,
        "field_modulus_low_to_high": list(spread.modulus),
        "trace_gram": [list(row) for row in spread.trace_gram],
        "subspace_vertices": [list(space) for space in spread.subspaces],
        "colors": list(spread.colors),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    parser.add_argument("--compiler", default="cc")
    args = parser.parse_args()

    repository = Path(__file__).resolve().parents[2]
    raw = args.config.read_bytes()
    configuration = json.loads(raw)
    records = []
    transcript = []
    source_path = repository / "src" / "c" / "scalar_symplectic_clique.c"
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="erdos117-symplectic-") as temporary:
        executable = Path(temporary) / "scalar_symplectic_clique"
        compiler_version = compile_solver(repository, args.compiler, executable)
        for entry in configuration["groups"]:
            prime = int(entry["prime"])
            rank = int(entry["rank"])
            known_lower = int(entry["known_clique_lower_bound"])
            projective_vectors, projective_adjacency = projective_symplectic_graph(prime, rank)
            clique = tuple(int(vertex) for vertex in entry["clique_projective_vertices"])
            if len(clique) != known_lower or not verify_clique(projective_adjacency, clique):
                raise AssertionError("configured clique witness failed")
            command = [str(executable), str(prime), str(rank), str(known_lower)]
            command_start = time.monotonic()
            completed = subprocess.run(command, capture_output=True, text=True, check=True)
            wall_seconds = time.monotonic() - command_start
            parsed = parse_solver_output(completed.stdout)
            if parsed["maximum"] != known_lower:
                raise AssertionError("C upper certificate and clique witness disagree")
            spread = verify_spread_certificate(prime, rank)
            q = prime ** rank
            if spread["color_count"] != q + 1:
                raise AssertionError("spread has the wrong number of colors")
            record = {
                "status": "[COMPUTED]",
                "prime": prime,
                "rank": rank,
                "projective_vertex_count": len(projective_vectors),
                "compressed_vertex_count": prime ** (2 * rank),
                "group_order": prime ** (2 * rank + 1),
                "center_order": prime,
                "nu": known_lower,
                "a": q + 1,
                "log_a_over_nu": __import__("math").log(q + 1) / known_lower,
                "clique_certificate": {
                    "projective_vertices": list(clique),
                    "vectors": [list(projective_vectors[vertex]) for vertex in clique],
                },
                "clique_upper_certificate": parsed,
                "spread_certificate": spread,
                "wall_seconds": wall_seconds,
            }
            records.append(record)
            transcript.append(completed.stdout.rstrip())
            transcript.append(
                "verified p=%d m=%d: nu=%d a=%d wall_seconds=%.6f"
                % (prime, rank, known_lower, q + 1, wall_seconds)
            )

    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "configuration": str(args.config),
        "configuration_sha256": hashlib.sha256(raw).hexdigest(),
        "solver_source": str(source_path.relative_to(repository)),
        "solver_source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "compiler": compiler_version,
            "external_dependencies": [],
        },
        "elapsed_wall_seconds": time.monotonic() - start,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    transcript.append("wrote %d certified records to %s" % (len(records), args.output))
    text = "\n".join(transcript) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
