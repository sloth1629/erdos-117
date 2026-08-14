#!/usr/bin/env python3
"""Verify the complete cutoff-eight scan for SmallGroup(108,41)."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from analyze_h7_exterior_batch import (
    parse_adjacency,
    parse_export,
    parse_vertices,
)
from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)
from h8_order64_dual import (
    adjacency_sha256_payload,
    compress_independent_twins,
    lift_clique,
    lift_coloring,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display_path(path: Path, root: Path) -> str:
    value = path if path.is_absolute() else root / path
    value = value.resolve()
    try:
        return str(value.relative_to(root.resolve()))
    except ValueError:
        return str(value)


def exact_certificate(input_path: Path, inventory_path: Path) -> dict[str, object]:
    metadata, rows = parse_export(input_path)
    if metadata != {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "Q_ORDER": "108",
        "Q_ID": "41",
        "CLIQUE_CUTOFF": "8",
        "TARGET_CLIQUE": "9",
        "SCOPE": "single_post81_literature_candidate_only",
    }:
        raise AssertionError("unexpected SG108 raw-scan metadata")
    if len(rows) != 84:
        raise AssertionError("SG108 normal-kernel serial range is incomplete")

    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    inventory_records = [
        record
        for record in inventory["certificate"]["records"]
        if record["small_group"] == [108, 41]
    ]
    if len(inventory_records) != 1:
        raise AssertionError("SG108 feasibility inventory record is missing")
    inventory_record = inventory_records[0]
    if (
        inventory_record["abstract_q_omega"],
        inventory_record["exterior_order"],
        inventory_record["all_exterior_subgroup_count"],
        inventory_record["normal_kernel_count"],
        inventory_record["selected_cover_center_image_size"],
    ) != (5, 216, 168, 84, 1):
        raise AssertionError("SG108 feasibility binding changed")

    statuses = Counter()
    exact_omega = Counter()
    serials = set()
    faithful_graphs = set()
    records = []
    candidate_records = []
    invariant = None
    for row_number, row in enumerate(rows, 1):
        current_invariant = (
            int(row["q_order"]), int(row["q_id"]), row["structure"],
            int(row["cover_order"]), int(row["cover_kernel_order"]),
            row["cover_kernel_central"], row["cover_kernel_in_derived"],
            int(row["exterior_order"]), int(row["all_exterior_subgroups"]),
            int(row["normal_kernel_count"]),
        )
        if invariant is None:
            invariant = current_invariant
        elif current_invariant != invariant:
            raise AssertionError("inconsistent SG108 per-kernel invariants")
        if current_invariant[:2] != (108, 41) or current_invariant[3:] != (
            5832, 54, "true", "true", 216, 168, 84
        ):
            raise AssertionError("wrong SG108 cover or exterior data")
        serial = int(row["kernel_serial"])
        if not 1 <= serial <= 84 or serial in serials:
            raise AssertionError("invalid SG108 kernel serial")
        serials.add(serial)
        kernel_order = int(row["kernel_order"])
        kernel_index = int(row["kernel_index"])
        if kernel_order * kernel_index != 216:
            raise AssertionError("SG108 kernel order/index mismatch")
        adjacency = parse_adjacency(row["adjacency"], 108)
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        if int(row["radical_count"]) != len(radical):
            raise AssertionError("SG108 radical count mismatch")
        saved_witness = parse_vertices(row["witness"])
        status = row["status"]
        statuses[status] += 1
        record: dict[str, object] = {
            "row_number": row_number,
            "kernel_serial": serial,
            "kernel_order": kernel_order,
            "kernel_index": kernel_index,
            "adjacency_sha256": hashlib.sha256(
                adjacency_sha256_payload(adjacency)
            ).hexdigest(),
            "status": status,
        }
        if status == "nonfaithful_radical":
            if len(radical) <= 1 or saved_witness != radical:
                raise AssertionError("invalid SG108 nonfaithful radical witness")
            record["radical"] = list(radical)
        else:
            if radical != (0,):
                raise AssertionError("SG108 purported faithful graph is nonfaithful")
            faithful_graphs.add(adjacency)
            representatives, reduced, classes = compress_independent_twins(adjacency)
            clique = maximum_clique(reduced)
            lifted_clique = lift_clique(representatives, clique.vertices)
            if not verify_clique(adjacency, lifted_clique):
                raise AssertionError("invalid SG108 exact clique")
            exact_omega[clique.size] += 1
            record.update({
                "omega": clique.size,
                "clique": list(lifted_clique),
                "twin_quotient_order": len(reduced),
                "clique_search_nodes": clique.search_nodes,
            })
            if status == "clique_ge_9":
                if len(saved_witness) != 9 or not verify_clique(
                    adjacency, saved_witness
                ):
                    raise AssertionError("invalid SG108 saved nine-clique")
                if clique.size < 9:
                    raise AssertionError("SG108 nine-clique status exceeds exact omega")
                record["saved_nine_clique"] = list(saved_witness)
            elif status == "candidate":
                if saved_witness or clique.size > 8:
                    raise AssertionError("SG108 candidate cutoff classification failed")
                coloring = exact_chromatic_number(reduced, clique.size)
                lifted_coloring = lift_coloring(classes, coloring.colors)
                if not verify_coloring(adjacency, lifted_coloring):
                    raise AssertionError("invalid SG108 exact candidate coloring")
                candidate = {
                    "kernel_serial": serial,
                    "omega": clique.size,
                    "chi": coloring.size,
                    "clique": list(lifted_clique),
                    "coloring": list(lifted_coloring),
                    "coloring_search_nodes_by_k": [
                        list(item) for item in coloring.search_nodes_by_k
                    ],
                }
                candidate_records.append(candidate)
                record.update(candidate)
            else:
                raise AssertionError("unknown SG108 row status")
        records.append(record)

    if serials != set(range(1, 85)):
        raise AssertionError("SG108 kernel serial coverage is incomplete")
    expected_statuses = {"clique_ge_9": 46, "nonfaithful_radical": 38}
    expected_omega = {20: 9, 28: 9, 32: 12, 37: 1, 39: 1, 40: 13, 48: 1}
    if dict(sorted(statuses.items())) != expected_statuses:
        raise AssertionError("unexpected SG108 cutoff-eight status census")
    if dict(sorted(exact_omega.items())) != expected_omega:
        raise AssertionError("unexpected SG108 faithful exact-omega census")
    if len(faithful_graphs) != 46 or candidate_records:
        raise AssertionError("unexpected SG108 faithful candidate census")
    return {
        "metadata": metadata,
        "small_group": [108, 41],
        "structure": invariant[2],
        "cover_order": 5832,
        "cover_kernel_order": 54,
        "exterior_order": 216,
        "all_exterior_subgroup_count": 168,
        "normal_kernel_count": 84,
        "status_distribution": expected_statuses,
        "faithful_kernel_count": 46,
        "distinct_faithful_adjacency_count": len(faithful_graphs),
        "minimum_faithful_omega": min(exact_omega),
        "exact_omega_distribution_faithful": [
            {"omega": omega, "count": count}
            for omega, count in sorted(exact_omega.items())
        ],
        "candidate_count": len(candidate_records),
        "candidate_records": candidate_records,
        "records": records,
        "inventory_binding": {
            "path": str(inventory_path),
            "sha256": sha256(inventory_path),
            "abstract_q_omega": inventory_record["abstract_q_omega"],
        },
        "conclusion": (
            "All 84 normal exterior kernels are covered. Thirty-eight have a "
            "saved nonidentity radical. The other 46 are faithful, distinct "
            "graphs with exact clique number at least 20. Therefore "
            "SmallGroup(108,41) contributes no central extension graph at "
            "clique cutoff eight."
        ),
    }


def verify_saved_document(document_path: Path, root: Path | None = None) -> None:
    root = root or Path.cwd()
    document = json.loads(document_path.read_text(encoding="utf-8"))
    resolved = {}
    for field in ("input", "gap_script", "gap_stdout", "inventory", "producer"):
        path = Path(document[field])
        if not path.is_absolute():
            path = root / path
        if sha256(path) != document[field + "_sha256"]:
            raise AssertionError("SG108 saved artifact hash mismatch: " + field)
        resolved[field] = path
    rebuilt = exact_certificate(resolved["input"], resolved["inventory"])
    # Normalize the path label, which is repository-relative in the saved run.
    rebuilt["inventory_binding"]["path"] = document["certificate"][
        "inventory_binding"
    ]["path"]
    if rebuilt != document["certificate"]:
        raise AssertionError("saved SG108 cutoff-eight certificate changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    root = Path.cwd()
    certificate = exact_certificate(args.input, args.inventory)
    certificate["inventory_binding"]["path"] = display_path(args.inventory, root)
    producer = Path(__file__)
    document = {
        "schema_version": 1,
        "status": "[COMPUTED] complete SG(108,41) cutoff-eight normal-kernel scan; no global h(8) claim",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input": display_path(args.input, root),
        "input_sha256": sha256(args.input),
        "gap_script": display_path(args.gap_script, root),
        "gap_script_sha256": sha256(args.gap_script),
        "gap_stdout": display_path(args.gap_stdout, root),
        "gap_stdout_sha256": sha256(args.gap_stdout),
        "inventory": display_path(args.inventory, root),
        "inventory_sha256": sha256(args.inventory),
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
    lines = [
        document["status"],
        "normal_kernels=84 statuses=%r faithful_unique=46 minimum_faithful_omega=20"
        % sorted(certificate["status_distribution"].items()),
        "candidate_count=0",
        "wrote %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
