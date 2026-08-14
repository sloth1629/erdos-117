#!/usr/bin/env python3
"""Verify the exact order-16, clique-five local dichotomy used at cutoff nine."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
H5_JSON = REPOSITORY / "experiments" / "logs" / "h5_exterior.json"
H5_TSV = REPOSITORY / "experiments" / "logs" / "h5_exterior.tsv"
DEFAULT_OUTPUT = (
    REPOSITORY / "experiments" / "logs" / "h9_h5_local_dichotomy.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data_rows(path: Path) -> list[dict[str, str]]:
    lines = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    return list(csv.DictReader(lines, delimiter="\t"))


def parse_adjacency(raw: str, order: int) -> tuple[int, ...]:
    rows = raw.split(";")
    if len(rows) != order:
        raise AssertionError(f"expected {order} adjacency rows, found {len(rows)}")
    adjacency = tuple(
        sum(1 << (int(value) - 1) for value in row.split(",") if value)
        for row in rows
    )
    allowed = (1 << order) - 1
    for vertex, neighbors in enumerate(adjacency):
        if neighbors & ~allowed or neighbors & (1 << vertex):
            raise AssertionError("invalid noncommuting adjacency row")
        for target in range(order):
            if bool(neighbors & (1 << target)) != bool(
                adjacency[target] & (1 << vertex)
            ):
                raise AssertionError("asymmetric noncommuting adjacency")
    return adjacency


def degree_profile(adjacency: tuple[int, ...]) -> dict[int, int]:
    return dict(sorted(Counter(bin(mask).count("1") for mask in adjacency).items()))


def assert_five_spread_complement(adjacency: tuple[int, ...]) -> None:
    """Check that the 15 nonzero vertices split into five commuting triples."""

    radical = [vertex for vertex, neighbors in enumerate(adjacency) if not neighbors]
    if len(radical) != 1:
        raise AssertionError("determinant row does not have exact radical")
    identity = radical[0]
    remaining = set(range(16))
    remaining.remove(identity)
    components: list[set[int]] = []
    while remaining:
        start = min(remaining)
        component = {
            vertex
            for vertex in remaining
            if vertex == start or not (adjacency[start] & (1 << vertex))
        }
        if len(component) != 3:
            raise AssertionError("commuting complement component is not a triple")
        for left in component:
            for right in component:
                if left != right and adjacency[left] & (1 << right):
                    raise AssertionError("commuting complement triple has an edge")
        components.append(component)
        remaining -= component
    if len(components) != 5:
        raise AssertionError("determinant row does not yield a five-spread")


def build_certificate() -> dict[str, object]:
    canonical = json.loads(H5_JSON.read_text(encoding="utf-8"))
    tsv_by_key: dict[tuple[int, int, int], dict[str, str]] = {}
    for row in data_rows(H5_TSV):
        key = (
            int(row["q_order"]),
            int(row["q_id"]),
            int(row["kernel_serial"]),
        )
        if key in tsv_by_key:
            raise AssertionError(f"duplicate TSV key {key}")
        tsv_by_key[key] = row

    target = [
        record
        for record in canonical["records"]
        if record["q_order"] == 16 and record["nu"] == 5
    ]
    if len(target) != 225:
        raise AssertionError(f"expected 225 target rows, found {len(target)}")

    exact: list[tuple[dict[str, object], tuple[int, ...]]] = []
    for record in target:
        key = (record["q_order"], record["q_id"], record["kernel_serial"])
        if key not in tsv_by_key:
            raise AssertionError(f"missing TSV key {key}")
        row = tsv_by_key[key]
        for field in (
            "q_order",
            "q_id",
            "cover_order",
            "exterior_order",
            "kernel_order",
            "kernel_index",
        ):
            if int(row[field]) != int(record[field]):
                raise AssertionError(f"JSON/TSV mismatch for {key}: {field}")
        if row["structure"] != record["structure"]:
            raise AssertionError(f"JSON/TSV structure mismatch for {key}")
        adjacency = parse_adjacency(row["adjacency"], 16)
        if sum(not neighbors for neighbors in adjacency) == 1:
            exact.append((record, adjacency))

    if len(exact) != 84:
        raise AssertionError(f"expected 84 exact-center rows, found {len(exact)}")

    type_counts: Counter[str] = Counter()
    for record, adjacency in exact:
        if (
            record["q_id"] != 14
            or record["structure"] != "C2 x C2 x C2 x C2"
        ):
            raise AssertionError("exact-center quotient is not C2^4")
        profile = degree_profile(adjacency)
        if record["kernel_index"] == 2 and profile == {0: 1, 8: 15}:
            type_counts["scalar"] += 1
        elif record["kernel_index"] == 4 and profile == {0: 1, 12: 15}:
            assert_five_spread_complement(adjacency)
            type_counts["determinant"] += 1
        else:
            raise AssertionError(
                "exact-center row lies outside the scalar/determinant dichotomy: "
                f"kernel index {record['kernel_index']}, profile {profile}"
            )

    if type_counts != {"scalar": 28, "determinant": 56}:
        raise AssertionError(f"wrong dichotomy counts: {dict(type_counts)}")

    return {
        "status": "[COMPUTED]",
        "claim": (
            "Every exact-center q_order=16, nu=5 exterior row is C2^4 "
            "and is scalar or determinant/spread."
        ),
        "sources": {
            "json": {
                "path": str(H5_JSON.relative_to(REPOSITORY)),
                "sha256": sha256(H5_JSON),
            },
            "tsv": {
                "path": str(H5_TSV.relative_to(REPOSITORY)),
                "sha256": sha256(H5_TSV),
            },
        },
        "target_record_count": len(target),
        "exact_center_record_count": len(exact),
        "exact_quotient": {
            "q_id": 14,
            "structure": "C2 x C2 x C2 x C2",
            "order": 16,
        },
        "types": [
            {
                "name": "scalar",
                "count": type_counts["scalar"],
                "commutator_image_order": 2,
                "degree_profile": {"0": 1, "8": 15},
            },
            {
                "name": "determinant",
                "count": type_counts["determinant"],
                "commutator_image_order": 4,
                "degree_profile": {"0": 1, "12": 15},
                "commuting_nonzero_partition": "five triples",
            },
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "target=225 exact_center=84 scalar=28 determinant=56 "
        f"output={args.output}"
    )


if __name__ == "__main__":
    main()
