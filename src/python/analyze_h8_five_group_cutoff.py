#!/usr/bin/env python3
"""Verify the bounded cutoff-eight inventory of finite 5-groups."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)


Adjacency = Tuple[int, ...]
EXPECTED_TOTALS = {125: 5, 625: 15, 3125: 77, 15625: 684}
EXPECTED_CANDIDATES = {125: 5, 625: 11, 3125: 22, 15625: 42}
EXPECTED_DISTRIBUTIONS = {
    125: {(1, 1): 3, (6, 6): 2},
    625: {(1, 1): 5, (6, 6): 6},
    3125: {(1, 1): 7, (6, 6): 15},
    15625: {(1, 1): 11, (6, 6): 31},
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display_path(path: Path, root: Path) -> str:
    value = path if path.is_absolute() else root / path
    value = value.resolve()
    try:
        return str(value.relative_to(root.resolve()))
    except ValueError:
        return str(value)


def read_export(path: Path) -> Tuple[Dict[str, str], List[Dict[str, str]]]:
    metadata: Dict[str, str] = {}
    data_lines: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            data_lines.append(line)
    return metadata, list(csv.DictReader(data_lines, delimiter="\t"))


def bits(mask: int) -> Iterable[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def parse_adjacency(raw: str, order: int) -> Adjacency:
    values = tuple(int(value) for value in raw.split(","))
    if len(values) != order:
        raise AssertionError("wrong adjacency-mask count")
    allowed = (1 << order) - 1
    for source, mask in enumerate(values):
        if mask < 0 or mask & ~allowed or mask & (1 << source):
            raise AssertionError("invalid simple-graph adjacency")
        for target in bits(mask):
            if not values[target] & (1 << source):
                raise AssertionError("asymmetric adjacency")
    return values


def parse_vector(raw: str, relative_orders: Sequence[int]) -> Tuple[int, ...]:
    vector = tuple(int(value) for value in raw.split(","))
    if len(vector) != len(relative_orders):
        raise AssertionError("wrong pc exponent-vector dimension")
    if any(not 0 <= value < bound for value, bound in zip(vector, relative_orders)):
        raise AssertionError("pc exponent is out of range")
    return vector


def parse_vectors(
    raw: str, count: int, relative_orders: Sequence[int],
) -> Tuple[Tuple[int, ...], ...]:
    vectors = tuple(parse_vector(value, relative_orders) for value in raw.split(";"))
    if len(vectors) != count:
        raise AssertionError("wrong saved-vector count")
    return vectors


def compress_independent_twins(
    adjacency: Sequence[int],
) -> Tuple[Tuple[int, ...], Adjacency, Tuple[int, ...]]:
    mask_to_class: Dict[int, int] = {}
    representatives: List[int] = []
    classes: List[int] = []
    for vertex, mask in enumerate(adjacency):
        if mask not in mask_to_class:
            mask_to_class[mask] = len(representatives)
            representatives.append(vertex)
        classes.append(mask_to_class[mask])
    for left in range(len(adjacency)):
        for right in range(left + 1, len(adjacency)):
            if classes[left] == classes[right] and adjacency[left] & (1 << right):
                raise AssertionError("equal-neighborhood class is not independent")
    reduced = tuple(
        sum(
            1 << target_class
            for target_class, target in enumerate(representatives)
            if adjacency[source] & (1 << target)
        )
        for source in representatives
    )
    return tuple(representatives), reduced, tuple(classes)


def is_ac_graph(adjacency: Sequence[int]) -> bool:
    all_vertices = (1 << len(adjacency)) - 1
    for vertex, neighbors in enumerate(adjacency):
        if not neighbors:
            continue
        centralizer = all_vertices & ~neighbors
        for member in bits(centralizer):
            if adjacency[member] & centralizer:
                return False
    return True


def candidate_record(row: Dict[str, str]) -> Dict[str, object]:
    group_order = int(row["group_order"])
    center_order = int(row["center_order"])
    coset_count = int(row["coset_count"])
    if center_order * coset_count != group_order:
        raise AssertionError("center order and coset count do not multiply correctly")
    relative_orders = tuple(int(value) for value in row["pc_relative_orders"].split(","))
    product = 1
    for value in relative_orders:
        product *= value
    if product != group_order:
        raise AssertionError("candidate pc relative orders are inconsistent")
    adjacency = parse_adjacency(row["adjacency_masks"], coset_count)
    representatives, reduced, classes = compress_independent_twins(adjacency)
    clique = maximum_clique(reduced)
    coloring = exact_chromatic_number(reduced, clique.size)
    lifted_clique = tuple(representatives[vertex] for vertex in clique.vertices)
    lifted_coloring = tuple(coloring.colors[vertex_class] for vertex_class in classes)
    if not verify_clique(adjacency, lifted_clique):
        raise AssertionError("lifted clique failed")
    if not verify_coloring(adjacency, lifted_coloring):
        raise AssertionError("lifted coloring failed")
    if clique.size > 8:
        raise AssertionError("candidate graph crosses cutoff eight")
    return {
        "small_group": [group_order, int(row["group_id"])],
        "structure": row["structure"],
        "center_order": center_order,
        "central_coset_graph_order": coset_count,
        "twin_quotient_order": len(reduced),
        "twin_representatives": list(representatives),
        "is_ac_group": is_ac_graph(adjacency),
        "nu": clique.size,
        "a": coloring.size,
        "clique": list(lifted_clique),
        "coloring": list(lifted_coloring),
        "commuting_color_classes": [
            [
                vertex
                for vertex, assigned in enumerate(lifted_coloring)
                if assigned == color
            ]
            for color in range(coloring.size)
        ],
        "clique_search_nodes": clique.search_nodes,
        "coloring_search_nodes_by_k": [
            list(item) for item in coloring.search_nodes_by_k
        ],
    }


def exclusion_record(row: Dict[str, str]) -> Dict[str, object]:
    group_order = int(row["group_order"])
    center_order = int(row["center_order"])
    coset_count = int(row["coset_count"])
    if center_order * coset_count != group_order:
        raise AssertionError("excluded row has inconsistent center index")
    relative_orders = tuple(int(value) for value in row["pc_relative_orders"].split(","))
    product = 1
    for value in relative_orders:
        product *= value
    if product != group_order:
        raise AssertionError("pc relative orders do not multiply to the group order")
    vertices = tuple(int(value) - 1 for value in row["witness_vertices"].split(","))
    if len(vertices) != 9 or len(set(vertices)) != 9:
        raise AssertionError("wrong nine-clique vertex list")
    if any(not 0 <= vertex < coset_count for vertex in vertices):
        raise AssertionError("nine-clique vertex is out of range")
    witnesses = parse_vectors(row["witness_exponents"], 9, relative_orders)
    if len(set(witnesses)) != 9:
        raise AssertionError("nine-clique pc elements are not distinct")
    forward = parse_vectors(row["witness_forward_products"], 36, relative_orders)
    reverse = parse_vectors(row["witness_reverse_products"], 36, relative_orders)
    if any(left == right for left, right in zip(forward, reverse)):
        raise AssertionError("saved nine-clique contains a commuting pair")
    return {
        "small_group": [group_order, int(row["group_id"])],
        "center_order": center_order,
        "central_coset_graph_order": coset_count,
        "pc_relative_orders": list(relative_orders),
        "nine_clique_vertices": list(vertices),
        "nine_clique_exponents": [list(vector) for vector in witnesses],
        "pair_product_inequality_count": 36,
    }


def exact_certificate(input_path: Path) -> Dict[str, object]:
    metadata, rows = read_export(input_path)
    if metadata.get("ORDERS") != "125,625,3125,15625":
        raise AssertionError("wrong bounded order list")
    if metadata.get("EXPECTED_TOTALS") != "5,15,77,684":
        raise AssertionError("wrong expected SmallGroups totals")
    if metadata.get("CLIQUE_CUTOFF") != "8" or metadata.get("TARGET_CLIQUE") != "9":
        raise AssertionError("wrong clique cutoff metadata")
    if metadata.get("SCOPE") != "finite_SmallGroups_orders_5^3_through_5^6_only":
        raise AssertionError("wrong five-group scope")

    keys = [(int(row["group_order"]), int(row["group_id"])) for row in rows]
    expected_keys = [
        (order, identifier)
        for order, total in EXPECTED_TOTALS.items()
        for identifier in range(1, total + 1)
    ]
    if keys != expected_keys or len(set(keys)) != len(keys):
        raise AssertionError("SmallGroup rows are missing, duplicated, or out of order")

    candidates: List[Dict[str, object]] = []
    exclusions: List[Dict[str, object]] = []
    for row in rows:
        status = row["status"]
        if status == "candidate":
            if any(
                row[field]
                for field in (
                    "witness_vertices", "witness_exponents",
                    "witness_forward_products", "witness_reverse_products",
                )
            ):
                raise AssertionError("candidate row unexpectedly stores a boundary witness")
            candidates.append(candidate_record(row))
        elif status == "clique_ge_9":
            if row["structure"] or row["adjacency_masks"]:
                raise AssertionError("excluded row stores unexpected candidate fields")
            exclusions.append(exclusion_record(row))
        else:
            raise AssertionError("unknown row status")

    by_order: List[Dict[str, object]] = []
    for order, total in EXPECTED_TOTALS.items():
        selected = [record for record in candidates if record["small_group"][0] == order]
        excluded = [record for record in exclusions if record["small_group"][0] == order]
        distribution = Counter((record["nu"], record["a"]) for record in selected)
        if len(selected) != EXPECTED_CANDIDATES[order]:
            raise AssertionError("unexpected cutoff-eight survivor count")
        if dict(distribution) != EXPECTED_DISTRIBUTIONS[order]:
            raise AssertionError("unexpected exact survivor distribution")
        if len(selected) + len(excluded) != total:
            raise AssertionError("per-order partition is incomplete")
        by_order.append({
            "order": order,
            "total_smallgroups": total,
            "eligible_count": len(selected),
            "excluded_by_nine_clique_count": len(excluded),
            "nu_a_distribution": [
                {"nu": pair[0], "a": pair[1], "count": count}
                for pair, count in sorted(distribution.items())
            ],
        })

    if any(not record["is_ac_group"] for record in candidates):
        raise AssertionError("a cutoff-eight survivor is not an AC-group")
    if any(record["a"] != record["nu"] for record in candidates):
        raise AssertionError("a cutoff-eight survivor has a different cover number")
    abelian = [record for record in candidates if record["nu"] == 1]
    nonabelian = [record for record in candidates if record["nu"] > 1]
    if len(abelian) != 26 or len(nonabelian) != 54:
        raise AssertionError("unexpected abelian/nonabelian eligible partition")
    if any(record["central_coset_graph_order"] != 1 for record in abelian):
        raise AssertionError("an eligible abelian graph has more than one central coset")
    if any(
        record["central_coset_graph_order"] != 25
        or record["twin_quotient_order"] != 7
        for record in nonabelian
    ):
        raise AssertionError("unexpected eligible nonabelian graph shape")
    return {
        "scope": "finite SmallGroups of orders 5^3, 5^4, 5^5, and 5^6 only",
        "gap_metadata": metadata,
        "total_smallgroups": len(rows),
        "eligible_count": len(candidates),
        "excluded_by_nine_clique_count": len(exclusions),
        "nu_eight_count": sum(record["nu"] == 8 for record in candidates),
        "maximum_a_among_eligible": max(record["a"] for record in candidates),
        "eligible_abelian_count": len(abelian),
        "eligible_nonabelian_count": len(nonabelian),
        "all_eligible_are_ac": True,
        "all_eligible_have_a_equal_nu": True,
        "all_eligible_nonabelian_have_center_index_25": True,
        "all_eligible_nonabelian_have_twin_quotient_order_7": True,
        "by_order": by_order,
        "eligible_records": candidates,
        "excluded_records": exclusions,
    }


def resolve_record_path(record: Dict[str, str], root: Path) -> Path:
    path = Path(record["path"])
    return path if path.is_absolute() else root / path


def verify_saved_document(document_path: Path, root: Optional[Path] = None) -> None:
    root = root or Path.cwd()
    document = json.loads(document_path.read_text(encoding="utf-8"))
    for field in ("input", "gap_script", "gap_stdout", "producer"):
        path = Path(document[field])
        if not path.is_absolute():
            path = root / path
        if sha256(path) != document[field + "_sha256"]:
            raise AssertionError("five-group artifact hash mismatch: " + field)
    for dependency in document["dependencies"]:
        path = resolve_record_path(dependency, root)
        if sha256(path) != dependency["sha256"]:
            raise AssertionError("five-group dependency hash mismatch")
    input_path = Path(document["input"])
    if not input_path.is_absolute():
        input_path = root / input_path
    if document["certificate"] != exact_certificate(input_path):
        raise AssertionError("saved five-group certificate changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    root = Path.cwd()
    producer = Path(__file__)
    dependencies = [
        root / "src/python/exact_invariants.py",
        root / "src/python/finite_groups.py",
    ]
    certificate = exact_certificate(args.input)
    document = {
        "schema_version": 1,
        "status": "[COMPUTED] finite SmallGroups of orders 5^3 through 5^6 only; no classification beyond scanned orders",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": display_path(args.input, root),
        "input_sha256": sha256(args.input),
        "gap_script": display_path(args.gap_script, root),
        "gap_script_sha256": sha256(args.gap_script),
        "gap_stdout": display_path(args.gap_stdout, root),
        "gap_stdout_sha256": sha256(args.gap_stdout),
        "producer": display_path(producer, root),
        "producer_sha256": sha256(producer),
        "dependencies": [
            {"path": display_path(path, root), "sha256": sha256(path)}
            for path in dependencies
        ],
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "certificate": certificate,
    }
    args.output.write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [document["status"]]
    for record in certificate["by_order"]:
        lines.append(
            "order=%d total=%d eligible=%d excluded_by_K9=%d distribution=%r"
            % (
                record["order"], record["total_smallgroups"],
                record["eligible_count"], record["excluded_by_nine_clique_count"],
                [
                    (item["nu"], item["a"], item["count"])
                    for item in record["nu_a_distribution"]
                ],
            )
        )
    lines.extend([
        "nu8_count=%d maximum_eligible_a=%d all_eligible_ac=%s"
        % (
            certificate["nu_eight_count"],
            certificate["maximum_a_among_eligible"],
            certificate["all_eligible_are_ac"],
        ),
        "wrote %s" % args.output,
    ])
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
