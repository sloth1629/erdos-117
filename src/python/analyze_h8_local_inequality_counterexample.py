#!/usr/bin/env python3
"""Certify a counterexample to a proposed centralizer-index inequality."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from exact_invariants import analyze_group, verify_clique, verify_coloring
from finite_groups import FiniteGroup


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display_path(path: Path, root: Path) -> str:
    value = path if path.is_absolute() else root / path
    value = value.resolve()
    try:
        return str(value.relative_to(root.resolve()))
    except ValueError:
        return str(value)


def read_export(path: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    metadata: Dict[str, str] = {}
    data_lines: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            data_lines.append(line)
    rows = list(csv.DictReader(data_lines, delimiter="\t"))
    if len(rows) != 1:
        raise AssertionError("expected exactly one exported group")
    return metadata, rows[0]


def parse_group(row: Dict[str, str]) -> FiniteGroup:
    order = int(row["element_count"])
    table = tuple(
        tuple(int(value) - 1 for value in raw_row.split(","))
        for raw_row in row["multiplication_table"].split(";")
    )
    if len(table) != order or any(len(table_row) != order for table_row in table):
        raise AssertionError("wrong multiplication-table dimensions")
    group = FiniteGroup(
        "SmallGroup(48,15)",
        tuple("g%d" % (index + 1) for index in range(order)),
        table,
    )
    group.validate()
    return group


def element_order(group: FiniteGroup, element: int) -> int:
    value = group.identity
    for exponent in range(1, group.order + 1):
        value = group.multiply(value, element)
        if value == group.identity:
            return exponent
    raise AssertionError("element order did not divide the group order")


def induced_subgroup(group: FiniteGroup, elements: Sequence[int]) -> FiniteGroup:
    ordered = tuple(sorted(elements))
    if not group.is_subgroup(ordered):
        raise AssertionError("centralizer positions do not form a subgroup")
    local = {element: index for index, element in enumerate(ordered)}
    table = tuple(
        tuple(local[group.multiply(left, right)] for right in ordered)
        for left in ordered
    )
    subgroup = FiniteGroup(
        "C_G(g2)",
        tuple(group.elements[element] for element in ordered),
        table,
    )
    subgroup.validate()
    return subgroup


def compact_analysis(group: FiniteGroup) -> Dict[str, object]:
    record = analyze_group(group, independent_cover=False)
    # The complete multiplication table remains in the checksummed GAP TSV.
    del record["multiplication_table"]
    clique = record["clique_certificate"]["coset_vertices"]
    adjacency = tuple(
        sum(1 << neighbor for neighbor in row)
        for row in record["compressed_adjacency"]
    )
    colors = record["coloring_certificate"]["colors_by_coset"]
    if not verify_clique(adjacency, clique):
        raise AssertionError("saved clique failed independent verification")
    if not verify_coloring(adjacency, colors):
        raise AssertionError("saved coloring failed independent verification")
    return record


def exact_certificate(input_path: Path) -> Dict[str, object]:
    metadata, row = read_export(input_path)
    if metadata.get("SCOPE") != "single_group_counterexample_only":
        raise AssertionError("wrong export scope")
    if metadata.get("MINIMALITY_CLAIM") != "false":
        raise AssertionError("the export unexpectedly claims minimality")
    if [int(row["small_group_order"]), int(row["small_group_id"])] != [48, 15]:
        raise AssertionError("wrong SmallGroup identifier")

    group = parse_group(row)
    if group.order != 48:
        raise AssertionError("wrong group order")
    target = int(row["target_serial"]) - 1
    if target != 1 or element_order(group, target) != int(row["target_order"]):
        raise AssertionError("target element mismatch")
    if element_order(group, target) != 2:
        raise AssertionError("target element does not have order two")

    centralizer = tuple(
        element for element in range(group.order) if group.commute(target, element)
    )
    exported_centralizer = tuple(
        sorted(int(value) - 1 for value in row["centralizer_positions"].split(","))
    )
    if centralizer != exported_centralizer:
        raise AssertionError("GAP and Python centralizers disagree")
    if len(centralizer) != int(row["centralizer_order"]):
        raise AssertionError("centralizer order mismatch")
    if group.order // len(centralizer) != int(row["centralizer_index"]):
        raise AssertionError("centralizer index mismatch")
    if row["centralizer_abelian"] != "true" or not group.is_abelian_subset(centralizer):
        raise AssertionError("centralizer is not abelian")

    centralizer_group = induced_subgroup(group, centralizer)
    group_record = compact_analysis(group)
    centralizer_record = compact_analysis(centralizer_group)
    if (group_record["nu"], group_record["a"]) != (12, 12):
        raise AssertionError("unexpected exact invariants for SmallGroup(48,15)")
    if (centralizer_record["nu"], centralizer_record["a"]) != (1, 1):
        raise AssertionError("unexpected exact invariants for the centralizer")

    left_side = group.order // len(centralizer)
    right_side = int(group_record["nu"]) - int(centralizer_record["nu"])
    if not left_side > right_side:
        raise AssertionError("the proposed inequality was not contradicted")
    return {
        "scope": "single SmallGroup(48,15) counterexample; no minimality claim",
        "gap_metadata": metadata,
        "small_group": [48, 15],
        "structure_description": row["structure_description"],
        "target": {
            "as_list_serial": target + 1,
            "gap_string": row["target_gap_string"],
            "order": element_order(group, target),
        },
        "centralizer": {
            "positions_zero_based": list(centralizer),
            "order": len(centralizer),
            "index": left_side,
            "abelian": True,
            "exact_graph_record": centralizer_record,
        },
        "group_exact_graph_record": group_record,
        "disproved_inequality": {
            "formula": "[G:C_G(x)] <= nu(G) - nu(C_G(x))",
            "left_side": left_side,
            "right_side": right_side,
            "nu_group": group_record["nu"],
            "nu_centralizer": centralizer_record["nu"],
            "strict_failure": True,
        },
    }


def verify_saved_document(document_path: Path, root: Optional[Path] = None) -> None:
    root = root or Path.cwd()
    document = json.loads(document_path.read_text(encoding="utf-8"))
    resolved: Dict[str, Path] = {}
    for field in ("input", "gap_script", "gap_stdout", "producer"):
        path = Path(document[field])
        if not path.is_absolute():
            path = root / path
        if sha256(path) != document[field + "_sha256"]:
            raise AssertionError("local-inequality artifact hash mismatch: " + field)
        resolved[field] = path
    if document["certificate"] != exact_certificate(resolved["input"]):
        raise AssertionError("saved local-inequality certificate changed")


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
    certificate = exact_certificate(args.input)
    document = {
        "schema_version": 1,
        "status": "[DISPROVED] [G:C_G(x)] <= nu(G)-nu(C_G(x))",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": display_path(args.input, root),
        "input_sha256": sha256(args.input),
        "gap_script": display_path(args.gap_script, root),
        "gap_script_sha256": sha256(args.gap_script),
        "gap_stdout": display_path(args.gap_stdout, root),
        "gap_stdout_sha256": sha256(args.gap_stdout),
        "producer": display_path(producer, root),
        "producer_sha256": sha256(producer),
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
    result = certificate["disproved_inequality"]
    text = (
        document["status"] + "\n"
        + "SmallGroup(48,15) target_serial=2 nu_G=12 nu_C=1 "
        + "centralizer_index=12 left=12 right=11\n"
        + "wrote %s\n" % args.output
    )
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
