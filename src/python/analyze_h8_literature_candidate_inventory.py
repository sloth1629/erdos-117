#!/usr/bin/env python3
"""Verify the feasibility-only inventory for three post-81 h(8) candidates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

from exact_invariants import maximum_clique, verify_clique
from h8_order64_dual import (
    adjacency_sha256_payload,
    compress_independent_twins,
    lift_clique,
)


EXPECTED = {
    (96, 227): {
        "label": "diagonal_C2_4_semidirect_S3",
        "derived": 48,
        "multiplier": (2, 2, 2),
        "exterior": 384,
        "all_subgroups": 777,
        "normal_kernels": 24,
        "selected_cover_center_image_size": 1,
        "abstract_q_omega": 29,
        "feasibility": "direct_small",
    },
    (108, 41): {
        "label": "C3_2_times_A4",
        "derived": 4,
        "multiplier": (2, 3, 3, 3),
        "exterior": 216,
        "all_subgroups": 168,
        "normal_kernels": 84,
        "selected_cover_center_image_size": 1,
        "abstract_q_omega": 5,
        "feasibility": "direct_small",
    },
    (144, 196): {
        "label": "C2_3_times_generalized_dihedral_C3_2",
        "derived": 9,
        "multiplier": (2, 2, 2, 2, 2, 2, 3),
        "exterior": 1728,
        "all_subgroups": 53675,
        "normal_kernels": 19775,
        "selected_cover_center_image_size": 1,
        "abstract_q_omega": 10,
        "feasibility": "direct_batched",
    },
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


def parse_tsv(path: Path):
    metadata = {}
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            lines.append(line)
    return metadata, list(csv.DictReader(lines, delimiter="\t"))


def exact_certificate(input_path: Path) -> dict[str, object]:
    metadata, rows = parse_tsv(input_path)
    if metadata != {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "SCOPE": "literature_candidates_beyond_order_81_only",
        "CUTOFF8_GRAPH_SCAN_PERFORMED": "false",
        "NAMED_CONSTRUCTIONS_VERIFIED": "true",
    }:
        raise AssertionError("unexpected post-81 feasibility metadata")
    if len(rows) != 3:
        raise AssertionError("post-81 feasibility inventory must have three rows")
    records = []
    for row in rows:
        key = (int(row["q_order"]), int(row["q_id"]))
        if key not in EXPECTED:
            raise AssertionError("unexpected post-81 candidate identity")
        expected = EXPECTED[key]
        adjacency = tuple(
            int(value) for value in row["q_noncommuting_adjacency"].split(",")
        )
        if len(adjacency) != key[0]:
            raise AssertionError("abstract quotient adjacency has wrong order")
        representatives, reduced, _ = compress_independent_twins(adjacency)
        clique = maximum_clique(reduced)
        lifted_clique = lift_clique(representatives, clique.vertices)
        if clique.size != expected["abstract_q_omega"] or not verify_clique(
            adjacency, lifted_clique
        ):
            raise AssertionError("abstract quotient exact clique number changed")
        multiplier = tuple(
            int(value) for value in row["multiplier_invariants"].split(",")
            if value
        )
        multiplier_order = int(row["multiplier_order"])
        derived_order = int(row["q_derived_order"])
        exterior_identity = int(row["exterior_order_identity"])
        exterior_constructed = int(row["exterior_order_constructed"])
        cover_order = int(row["cover_order"])
        cover_kernel_order = int(row["cover_kernel_order"])
        all_subgroups = int(row["all_exterior_subgroup_count"])
        normal_kernels = int(row["normal_kernel_count"])
        if row["label"] != expected["label"]:
            raise AssertionError("candidate label does not identify the intended group")
        if derived_order != expected["derived"] or multiplier != expected["multiplier"]:
            raise AssertionError("candidate multiplier or derived order changed")
        if multiplier_order != __import__("math").prod(multiplier):
            raise AssertionError("multiplier invariant-factor product is wrong")
        if exterior_identity != multiplier_order * derived_order:
            raise AssertionError("exterior-square order identity failed")
        if exterior_identity != expected["exterior"] or exterior_constructed != exterior_identity:
            raise AssertionError("constructed exterior-square order changed")
        if cover_kernel_order != multiplier_order or cover_order != key[0] * multiplier_order:
            raise AssertionError("Schur-cover order data disagree")
        if row["cover_kernel_central"] != "true" or row["cover_kernel_in_derived"] != "true":
            raise AssertionError("chosen Schur cover is not certified stem")
        center_image_size = int(row["selected_cover_center_image_size"])
        nonidentity_positions = tuple(
            int(value)
            for value in row["nonidentity_center_image_positions"].split(",")
            if value
        )
        explicit_zero_row = row["explicit_nonidentity_zero_row_available"] == "true"
        if row["explicit_nonidentity_zero_row_available"] not in ("true", "false"):
            raise AssertionError("invalid selected-cover zero-row flag")
        if center_image_size != expected["selected_cover_center_image_size"]:
            raise AssertionError("selected-cover center-image size changed")
        if center_image_size != 1 + len(nonidentity_positions):
            raise AssertionError("selected-cover center-image positions are incomplete")
        if explicit_zero_row != bool(nonidentity_positions):
            raise AssertionError("selected-cover zero-row flag disagrees with positions")
        if all_subgroups != expected["all_subgroups"]:
            raise AssertionError("exterior subgroup count changed")
        if normal_kernels != expected["normal_kernels"] or normal_kernels > all_subgroups:
            raise AssertionError("normal-kernel feasibility count changed")
        if row["direct_cutoff8_scan_feasibility"] != expected["feasibility"]:
            raise AssertionError("direct-scan feasibility class changed")
        if any(int(row[field]) < 0 for field in (
            "cover_ms", "pc_ms", "all_subgroups_ms", "normal_filter_ms"
        )):
            raise AssertionError("negative GAP runtime")
        records.append({
            "label": row["label"],
            "small_group": list(key),
            "structure": row["structure"],
            "abstract_q_adjacency_sha256": hashlib.sha256(
                adjacency_sha256_payload(adjacency)
            ).hexdigest(),
            "abstract_q_twin_quotient_order": len(reduced),
            "abstract_q_omega": clique.size,
            "abstract_q_clique": list(lifted_clique),
            "abstract_q_clique_search_nodes": clique.search_nodes,
            "center_order": int(row["q_center_order"]),
            "derived_order": derived_order,
            "multiplier_invariants": list(multiplier),
            "multiplier_order": multiplier_order,
            "exterior_order": exterior_identity,
            "cover_order": cover_order,
            "cover_kernel_order": cover_kernel_order,
            "exterior_structure": row["exterior_structure"],
            "exterior_abelian": row["exterior_abelian"] == "true",
            "exterior_generator_count": int(row["exterior_generator_count"]),
            "selected_cover_center_image_size": center_image_size,
            "nonidentity_center_image_positions": list(nonidentity_positions),
            "explicit_nonidentity_zero_row_available": explicit_zero_row,
            "all_exterior_subgroup_count": all_subgroups,
            "normal_kernel_count": normal_kernels,
            "direct_cutoff8_scan_feasibility": expected["feasibility"],
            "cutoff8_disposition": (
                "excluded_by_abstract_quotient_clique"
                if clique.size > 8
                else "requires_exterior_kernel_scan"
            ),
            "runtime_ms": {
                "schur_cover": int(row["cover_ms"]),
                "pc_conversion": int(row["pc_ms"]),
                "all_exterior_subgroups": int(row["all_subgroups_ms"]),
                "normal_kernel_filter": int(row["normal_filter_ms"]),
            },
        })
    if tuple(record["small_group"] for record in records) != (
        [96, 227], [108, 41], [144, 196]
    ):
        raise AssertionError("candidate rows are not in canonical order")
    return {
        "metadata": metadata,
        "candidate_count": 3,
        "records": records,
        "total_normal_kernel_count": sum(
            record["normal_kernel_count"] for record in records
        ),
        "scope_limitation": (
            "These are three literature-motivated quotient candidates beyond "
            "order 81. The inventory constructs their chosen Schur covers and "
            "first solves each abstract quotient noncommuting graph exactly, "
            "checks the image of each selected cover center, then counts normal "
            "exterior kernels. It performs no central-extension cutoff-eight "
            "graph scan and is not "
            "a complete inventory for nu<=8. A trivial selected-cover center image "
            "is recorded only as complementary feasibility data; no converse "
            "capability assertion is made."
        ),
    }


def verify_saved_document(document_path: Path, root: Path | None = None) -> None:
    root = root or Path.cwd()
    document = json.loads(document_path.read_text(encoding="utf-8"))
    for field in ("input", "gap_script", "gap_stdout", "producer"):
        path = Path(document[field])
        if not path.is_absolute():
            path = root / path
        if sha256(path) != document[field + "_sha256"]:
            raise AssertionError("post-81 feasibility artifact hash mismatch: " + field)
    input_path = Path(document["input"])
    if not input_path.is_absolute():
        input_path = root / input_path
    if document["certificate"] != exact_certificate(input_path):
        raise AssertionError("saved post-81 feasibility certificate changed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()
    certificate = exact_certificate(args.input)
    producer = Path(__file__)
    root = Path.cwd()
    document = {
        "schema_version": 1,
        "status": "[COMPUTED] feasibility-only post-81 candidate inventory; no cutoff graph scan or h(8) completeness claim",
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
    lines = [document["status"]]
    for record in certificate["records"]:
        lines.append(
            "Q=SmallGroup(%d,%d) abstract_omega=%d exterior=%d "
            "normal_kernels=%d disposition=%s feasibility=%s"
            % (
                record["small_group"][0], record["small_group"][1],
                record["abstract_q_omega"], record["exterior_order"],
                record["normal_kernel_count"], record["cutoff8_disposition"],
                record["direct_cutoff8_scan_feasibility"],
            )
        )
    lines.append("wrote %s" % args.output)
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
