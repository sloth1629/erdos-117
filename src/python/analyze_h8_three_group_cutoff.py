#!/usr/bin/env python3
"""Verify the bounded cutoff-eight inventory of finite 3-groups."""

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
EXPECTED_TOTALS = {3: 1, 9: 2, 27: 5, 81: 15, 243: 67, 729: 504}
EXPECTED_ELIGIBLE = {3: 1, 9: 2, 27: 5, 81: 11, 243: 24, 729: 49}
EXPECTED_DISTRIBUTIONS = {
    3: {(1, 1): 1},
    9: {(1, 1): 2},
    27: {(1, 1): 3, (4, 4): 2},
    81: {(1, 1): 5, (4, 4): 6},
    243: {(1, 1): 7, (4, 4): 15, (7, 10): 2},
    729: {(1, 1): 11, (4, 4): 31, (7, 10): 7},
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


def greedy_target_clique(adjacency: Sequence[int], target: int) -> Tuple[int, ...]:
    """Return a checked deterministic target clique, or the empty tuple."""

    starts = sorted(
        range(len(adjacency)),
        key=lambda vertex: (-bin(adjacency[vertex]).count("1"), vertex),
    )
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            vertex = max(
                bits(candidates),
                key=lambda item: (
                    bin(candidates & adjacency[item]).count("1"), -item
                ),
            )
            clique.append(vertex)
            candidates &= adjacency[vertex]
        if len(clique) == target:
            result = tuple(clique)
            if not verify_clique(adjacency, result):
                raise AssertionError("greedy target clique failed verification")
            return result
    return ()


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


def graph_centralizer_indices(adjacency: Sequence[int]) -> Tuple[int, ...]:
    count = len(adjacency)
    values = []
    for neighbors in adjacency:
        centralizer_cosets = count - bin(neighbors).count("1")
        if count % centralizer_cosets:
            raise AssertionError("nonintegral graph-derived centralizer index")
        values.append(count // centralizer_cosets)
    return tuple(values)


def row_common(row: Dict[str, str]) -> Tuple[int, int, int, Tuple[int, ...]]:
    group_order = int(row["group_order"])
    center_order = int(row["center_order"])
    coset_count = int(row["coset_count"])
    if center_order * coset_count != group_order:
        raise AssertionError("center order and center index are inconsistent")
    relative_orders = tuple(int(value) for value in row["pc_relative_orders"].split(","))
    product = 1
    for value in relative_orders:
        product *= value
    if product != group_order:
        raise AssertionError("pc relative orders do not multiply to group order")
    return group_order, center_order, coset_count, relative_orders


def pc_exclusion_record(row: Dict[str, str]) -> Dict[str, object]:
    group_order, center_order, coset_count, relative_orders = row_common(row)
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
    if any(
        row[field]
        for field in ("structure", "is_ac", "centralizer_indices", "adjacency_masks")
    ):
        raise AssertionError("pc-excluded row stores candidate-only fields")
    return {
        "small_group": [group_order, int(row["group_id"])],
        "exclusion_kind": "saved_pc_nine_clique",
        "center_order": center_order,
        "central_coset_graph_order": coset_count,
        "pc_relative_orders": list(relative_orders),
        "nine_clique_vertices": list(vertices),
        "nine_clique_exponents": [list(vector) for vector in witnesses],
        "pair_product_inequality_count": 36,
    }


def analyze_adjacency_row(
    row: Dict[str, str],
) -> Tuple[Optional[Dict[str, object]], Optional[Dict[str, object]]]:
    group_order, center_order, coset_count, _ = row_common(row)
    if any(
        row[field]
        for field in (
            "witness_vertices", "witness_exponents",
            "witness_forward_products", "witness_reverse_products",
        )
    ):
        raise AssertionError("adjacency row unexpectedly stores pc witness fields")
    adjacency = parse_adjacency(row["adjacency_masks"], coset_count)
    computed_ac = is_ac_graph(adjacency)
    if row["is_ac"] not in ("true", "false"):
        raise AssertionError("invalid GAP AC flag")
    if computed_ac != (row["is_ac"] == "true"):
        raise AssertionError("GAP and Python AC tests disagree")
    computed_indices = graph_centralizer_indices(adjacency)
    saved_indices = tuple(int(value) for value in row["centralizer_indices"].split(","))
    if saved_indices != computed_indices:
        raise AssertionError("GAP and Python centralizer indices disagree")

    nine_clique = greedy_target_clique(adjacency, 9)
    if nine_clique:
        return None, {
            "small_group": [group_order, int(row["group_id"])],
            "exclusion_kind": "saved_adjacency_nine_clique",
            "structure": row["structure"],
            "center_order": center_order,
            "central_coset_graph_order": coset_count,
            "is_ac_group": computed_ac,
            "nine_clique_vertices": list(nine_clique),
        }

    representatives, reduced, classes = compress_independent_twins(adjacency)
    clique = maximum_clique(reduced)
    if clique.size > 8:
        lifted = tuple(representatives[vertex] for vertex in clique.vertices[:9])
        if not verify_clique(adjacency, lifted):
            raise AssertionError("lifted exact nine-clique failed")
        return None, {
            "small_group": [group_order, int(row["group_id"])],
            "exclusion_kind": "exact_adjacency_nine_clique",
            "structure": row["structure"],
            "center_order": center_order,
            "central_coset_graph_order": coset_count,
            "is_ac_group": computed_ac,
            "nine_clique_vertices": list(lifted),
        }
    coloring = exact_chromatic_number(reduced, clique.size)
    lifted_clique = tuple(representatives[vertex] for vertex in clique.vertices)
    lifted_coloring = tuple(coloring.colors[vertex_class] for vertex_class in classes)
    if not verify_clique(adjacency, lifted_clique):
        raise AssertionError("lifted exact clique failed")
    if not verify_coloring(adjacency, lifted_coloring):
        raise AssertionError("lifted exact coloring failed")
    cover_indices = tuple(sorted(computed_indices[vertex] for vertex in lifted_clique))
    record = {
        "small_group": [group_order, int(row["group_id"])],
        "structure": row["structure"],
        "center_order": center_order,
        "central_coset_graph_order": coset_count,
        "twin_quotient_order": len(reduced),
        "twin_representatives": list(representatives),
        "is_ac_group": computed_ac,
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
        "centralizer_indices": list(computed_indices),
        "centralizer_cover_indices": list(cover_indices),
        "centralizer_cover_maximal_member_count": sum(
            value == 3 for value in cover_indices
        ),
    }
    return record, None


def exact_certificate(input_path: Path) -> Dict[str, object]:
    metadata, rows = read_export(input_path)
    if metadata.get("ORDERS") != "3,9,27,81,243,729":
        raise AssertionError("wrong bounded order list")
    if metadata.get("EXPECTED_TOTALS") != "1,2,5,15,67,504":
        raise AssertionError("wrong expected SmallGroups totals")
    if metadata.get("TOTAL_GROUPS") != "594":
        raise AssertionError("wrong total SmallGroups count")
    if (
        metadata.get("NEXT_ORDER") != "2187"
        or metadata.get("NEXT_ORDER_TOTAL") != "9310"
        or metadata.get("NEXT_ORDER_SCANNED") != "false"
    ):
        raise AssertionError("wrong unscanned next-order metadata")
    if metadata.get("CLIQUE_CUTOFF") != "8" or metadata.get("TARGET_CLIQUE") != "9":
        raise AssertionError("wrong clique cutoff metadata")
    if metadata.get("SCOPE") != (
        "finite_SmallGroups_orders_3_through_729_only_order_2187_not_scanned"
    ):
        raise AssertionError("wrong three-group scope")

    keys = [(int(row["group_order"]), int(row["group_id"])) for row in rows]
    expected_keys = [
        (order, identifier)
        for order, total in EXPECTED_TOTALS.items()
        for identifier in range(1, total + 1)
    ]
    if keys != expected_keys or len(set(keys)) != len(keys):
        raise AssertionError("SmallGroup rows are missing, duplicated, or out of order")

    eligible: List[Dict[str, object]] = []
    excluded: List[Dict[str, object]] = []
    raw_status = Counter()
    for row in rows:
        status = row["status"]
        raw_status[status] += 1
        if status == "clique_ge_9":
            excluded.append(pc_exclusion_record(row))
        elif status == "candidate":
            accepted, rejected = analyze_adjacency_row(row)
            if accepted is not None:
                eligible.append(accepted)
            if rejected is not None:
                excluded.append(rejected)
        else:
            raise AssertionError("unknown GAP row status")

    by_order: List[Dict[str, object]] = []
    for order, total in EXPECTED_TOTALS.items():
        selected = [record for record in eligible if record["small_group"][0] == order]
        rejected = [record for record in excluded if record["small_group"][0] == order]
        distribution = Counter((record["nu"], record["a"]) for record in selected)
        if len(selected) != EXPECTED_ELIGIBLE[order]:
            raise AssertionError("unexpected cutoff-eight survivor count")
        if dict(distribution) != EXPECTED_DISTRIBUTIONS[order]:
            raise AssertionError("unexpected exact survivor distribution")
        if len(selected) + len(rejected) != total:
            raise AssertionError("per-order partition is incomplete")
        by_order.append({
            "order": order,
            "total_smallgroups": total,
            "eligible_count": len(selected),
            "excluded_by_nine_clique_count": len(rejected),
            "nu_a_distribution": [
                {"nu": pair[0], "a": pair[1], "count": count}
                for pair, count in sorted(distribution.items())
            ],
        })

    signature_by_nu = {
        nu: sorted({tuple(record["centralizer_cover_indices"]) for record in eligible if record["nu"] == nu})
        for nu in (1, 4, 7)
    }
    expected_signatures = {1: [(1,)], 4: [(3, 3, 3, 3)], 7: [(3,) * 7]}
    if signature_by_nu != expected_signatures:
        raise AssertionError("unexpected maximal-centralizer cover signature")
    non_ac = [record for record in eligible if not record["is_ac_group"]]
    if len(non_ac) != 9 or any((record["nu"], record["a"]) != (7, 10) for record in non_ac):
        raise AssertionError("unexpected non-AC survivor census")
    if any(record["nu"] not in (1, 4, 7) for record in eligible):
        raise AssertionError("unexpected eligible clique number")
    if any(record["a"] > 10 for record in eligible):
        raise AssertionError("unexpected eligible cover number above ten")
    if len(eligible) != 92 or len(excluded) != 502:
        raise AssertionError("unexpected total cutoff partition")

    return {
        "scope": "all finite SmallGroups of orders 3, 9, 27, 81, 243, and 729 only",
        "unscanned_next_order": 2187,
        "unscanned_next_order_smallgroups_count": 9310,
        "gap_metadata": metadata,
        "total_smallgroups": len(rows),
        "gap_pc_nine_clique_count": raw_status["clique_ge_9"],
        "gap_adjacency_candidate_count": raw_status["candidate"],
        "eligible_count": len(eligible),
        "excluded_by_nine_clique_count": len(excluded),
        "nu_eight_count": sum(record["nu"] == 8 for record in eligible),
        "maximum_a_among_eligible": max(record["a"] for record in eligible),
        "eligible_ac_count": len(eligible) - len(non_ac),
        "eligible_non_ac_count": len(non_ac),
        "eligible_a_greater_nu_count": sum(
            record["a"] > record["nu"] for record in eligible
        ),
        "all_eligible_maximum_clique_centralizers_are_maximal_except_abelian": all(
            record["nu"] == 1
            or record["centralizer_cover_maximal_member_count"] == record["nu"]
            for record in eligible
        ),
        "centralizer_cover_signatures_by_nu": {
            str(nu): [list(signature) for signature in signatures]
            for nu, signatures in signature_by_nu.items()
        },
        "by_order": by_order,
        "eligible_records": eligible,
        "excluded_records": excluded,
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
            raise AssertionError("three-group artifact hash mismatch: " + field)
    for dependency in document["dependencies"]:
        path = resolve_record_path(dependency, root)
        if sha256(path) != dependency["sha256"]:
            raise AssertionError("three-group dependency hash mismatch")
    input_path = Path(document["input"])
    if not input_path.is_absolute():
        input_path = root / input_path
    if document["certificate"] != exact_certificate(input_path):
        raise AssertionError("saved three-group certificate changed")


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
    dependencies = [root / "src/python/exact_invariants.py"]
    certificate = exact_certificate(args.input)
    document = {
        "schema_version": 1,
        "status": "[COMPUTED] finite SmallGroups of orders 3 through 729 only; no all-finite-3-group theorem; order 2187 not scanned",
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
        "nu8_count=%d maximum_eligible_a=%d non_ac_eligible=%d"
        % (
            certificate["nu_eight_count"],
            certificate["maximum_a_among_eligible"],
            certificate["eligible_non_ac_count"],
        ),
        "next_order=2187 smallgroups=9310 scanned=false",
        "wrote %s" % args.output,
    ])
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
