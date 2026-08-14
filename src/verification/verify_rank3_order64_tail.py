#!/usr/bin/env python3
"""Independently verify the order-64 tail in the binary rank-three reduction.

The structural argument reduces a hypothetical rank-three case at cutoff
eight to a quotient ``Q`` of order 64 with the following quotient-level
properties.  The group is nonabelian of class two, ``A = Omega_1(Z(Q))`` has
order eight, and ``Q/A`` is elementary abelian of order eight.  This verifier
derives the corresponding SmallGroup IDs directly from the committed Cayley
tables, then joins that list to the already canonical h7/h8 exterior-kernel
certificates.

This file deliberately does not use GAP or the SmallGroups library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from run_h8_bounded_cutoff import verify_saved_document as verify_h8_document  # noqa: E402


ORDER64_TABLE = "experiments/logs/gap_smallgroups_order64.tsv"
ORDER64_TABLE_SHA256 = "4047bc195b59a9e3c631a31499bf93bf0f4c577dbbded558249bc5f3dda54b27"
ORDER64_JSON = "experiments/logs/gap_smallgroups_order64.json"
ORDER64_JSON_SHA256 = "6e134f170949c437b8a0c640f27a86c465fa6d3807f2a2e109301503d1c32576"
H7_ORDINARY_JSON = "experiments/logs/h7_exterior_64_1_191.json"
H7_ORDINARY_JSON_SHA256 = "69f3e4e39543ffb316798dec5df3dd220bdbd61b11a67c0bd07bdccdbdaa70a0"
H7_ORDINARY_TSV = "experiments/logs/h7_exterior_64_1_191.tsv"
H7_ORDINARY_TSV_SHA256 = "dee1fcdc02b633ac5eba9f708522e96117f1d997edbf3de38bee50ce984249d6"
H7_CAPABILITY_JSON = "experiments/logs/h7_capability_order64.json"
H7_CAPABILITY_JSON_SHA256 = "bb8e8f416e6b19ec0fdb9586b7fa1e04579aa66baa5554769c62a4fcdbd6198e"
H8_BOUNDED_JSON = "experiments/logs/h8_bounded_cutoff.json"
H8_BOUNDED_JSON_SHA256 = "052036975d9a6d30d920873ae8f171dbaa010eec6c7852b3180a918050b0ae61"

GENERIC_EXPORT_SHA256 = {
    195: "4ee0f3c9807f07f69200fad377566c5a1aee1abba85513c75122e704e5d99db6",
    202: "2c8e09f73162c3b55db2525406407ec8dad7328db7eaa968419c3722bcc8e040",
    203: "c33dba5d4a53c191efe3a767e7b5f04a8e16be8ec30be67c81adb9578d200949",
    207: "08667e416c98cdf4314d9faeeabc8e574f55d635aa73890dbb1aa9d419036dc7",
    211: "c73de1ce8c01a2248059dcbf39f2b35b681cb6d345f841d232095fe094c2d967",
}

EXPECTED_BASE_IDS = (
    17, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 87, 103,
    195, 196, 197, 202, 203, 204, 205, 207, 208, 209, 211, 212, 247, 263,
)
EXPECTED_NON_ELEMENTARY_QUOTIENT_IDS = (17, 84, 87, 103, 247)
EXPECTED_STRUCTURAL_IDS = tuple(
    identifier
    for identifier in EXPECTED_BASE_IDS
    if identifier not in EXPECTED_NON_ELEMENTARY_QUOTIENT_IDS
)

EXPECTED_ORDINARY_MINIMUM_OMEGA = {
    57: 20, 58: 12, 59: 19, 60: 12, 61: 17, 62: 12, 63: 19,
    64: 20, 67: 12, 68: 14, 69: 14, 71: 14, 72: 14, 73: 14,
    74: 14, 75: 14, 77: 14, 78: 14, 82: 14,
}
EXPECTED_ORDINARY_ALL_NONFAITHFUL = (65, 66, 70, 76, 79, 80, 81)
EXPECTED_GENERIC = (195, 202, 203, 207, 211)
EXPECTED_GENERIC_COUNTS = {
    195: (64, 450, 1765, 0),
    202: (224, 498, 2609, 0),
    203: (128, 482, 2141, 0),
    207: (96, 466, 1953, 0),
    211: (288, 498, 2453, 0),
}
EXPECTED_EXTERIOR_ZERO = (196, 197, 204, 205, 208, 209, 212, 263)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_path(root: Path, relative: str, expected_hash: str) -> Path:
    path = root / relative
    observed = sha256(path)
    if observed != expected_hash:
        raise AssertionError(
            "source hash mismatch for %s: expected %s, observed %s"
            % (relative, expected_hash, observed)
        )
    return path


def parse_order64_tables(path: Path):
    metadata = {}
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("\t", 1)
            metadata[key] = value
        elif line:
            lines.append(line)
    if metadata != {
        "GAP_VERSION": "4.16.0",
        "SMALLGRP_VERSION": "1.5.4",
        "ORDER": "64",
        "COUNT": "267",
    }:
        raise AssertionError("unexpected order-64 table metadata")
    rows = list(csv.DictReader(lines, delimiter="\t"))
    if len(rows) != 267:
        raise AssertionError("order-64 table must contain 267 groups")
    return metadata, rows


def parse_table(row: Mapping[str, str], expected_id: int) -> Tuple[Tuple[int, ...], ...]:
    match = re.fullmatch(r"SmallGroup\(64,(\d+)\)", row["group_id"])
    if match is None or int(match.group(1)) != expected_id:
        raise AssertionError("SmallGroup rows are incomplete or out of order")
    if int(row["element_count"]) != 64:
        raise AssertionError("wrong element count")
    elements = tuple(int(value) for value in row["elements"].split(","))
    if elements != tuple(range(1, 65)):
        raise AssertionError("unexpected element enumeration")
    table = tuple(
        tuple(int(value) - 1 for value in raw_row.split(","))
        for raw_row in row["multiplication_table"].split(";")
    )
    if len(table) != 64 or any(len(raw_row) != 64 for raw_row in table):
        raise AssertionError("multiplication table has wrong shape")
    allowed = set(range(64))
    if any(set(raw_row) != allowed for raw_row in table):
        raise AssertionError("multiplication table row is not a permutation")
    if any({table[x][y] for x in range(64)} != allowed for y in range(64)):
        raise AssertionError("multiplication table column is not a permutation")
    return table


def group_data(table: Sequence[Sequence[int]]) -> Dict[str, object]:
    size = len(table)
    identities = [
        element for element in range(size)
        if all(table[element][x] == x and table[x][element] == x for x in range(size))
    ]
    if len(identities) != 1:
        raise AssertionError("multiplication table has no unique identity")
    identity = identities[0]
    inverse = []
    for x in range(size):
        candidates = [
            y for y in range(size)
            if table[x][y] == identity and table[y][x] == identity
        ]
        if len(candidates) != 1:
            raise AssertionError("multiplication table has no unique two-sided inverse")
        inverse.append(candidates[0])

    # Full associativity is inexpensive here (267 * 64^3 comparisons) and
    # prevents the structural census from trusting GAP beyond the raw table.
    for x in range(size):
        row_x = table[x]
        for y in range(size):
            left = table[row_x[y]]
            row_y = table[y]
            for z in range(size):
                if left[z] != row_x[row_y[z]]:
                    raise AssertionError("multiplication table is not associative")

    center = {
        x for x in range(size)
        if all(table[x][y] == table[y][x] for y in range(size))
    }

    def commutator(x: int, y: int) -> int:
        value = table[inverse[x]][inverse[y]]
        value = table[value][x]
        return table[value][y]

    commutators = {commutator(x, y) for x in range(size) for y in range(size)}
    class_at_most_two = commutators <= center
    nonabelian = len(center) != size
    omega_one = {x for x in center if table[x][x] == identity}
    if identity not in omega_one:
        raise AssertionError("Omega_1 omitted the identity")
    if any(table[x][y] not in omega_one for x in omega_one for y in omega_one):
        raise AssertionError("central involutions are not closed")
    if any(inverse[x] not in omega_one for x in omega_one):
        raise AssertionError("central involutions are not inverse closed")
    quotient_elementary = (
        len(omega_one) == 8
        and commutators <= omega_one
        and all(table[x][x] in omega_one for x in range(size))
    )
    return {
        "identity": identity,
        "center_order": len(center),
        "omega_one_order": len(omega_one),
        "nonabelian": nonabelian,
        "class_at_most_two": class_at_most_two,
        "quotient_by_omega_one_elementary_abelian": quotient_elementary,
    }


def structural_census(table_path: Path) -> Dict[str, object]:
    _, rows = parse_order64_tables(table_path)
    base_ids = []
    structural_ids = []
    records = []
    for expected_id, row in enumerate(rows, 1):
        data = group_data(parse_table(row, expected_id))
        base = (
            data["nonabelian"]
            and data["class_at_most_two"]
            and data["omega_one_order"] == 8
        )
        selected = base and data["quotient_by_omega_one_elementary_abelian"]
        if base:
            base_ids.append(expected_id)
        if selected:
            structural_ids.append(expected_id)
        if base:
            records.append({
                "q_id": expected_id,
                "center_order": data["center_order"],
                "q_over_omega_one_elementary_abelian": bool(selected),
            })
    if tuple(base_ids) != EXPECTED_BASE_IDS:
        raise AssertionError("unexpected base rank-three order-64 census")
    eliminated = tuple(identifier for identifier in base_ids if identifier not in structural_ids)
    if eliminated != EXPECTED_NON_ELEMENTARY_QUOTIENT_IDS:
        raise AssertionError("unexpected non-elementary Q/A tail")
    if tuple(structural_ids) != EXPECTED_STRUCTURAL_IDS:
        raise AssertionError("unexpected structural rank-three order-64 census")
    return {
        "base_predicate_count": len(base_ids),
        "base_predicate_ids": base_ids,
        "q_over_A_non_elementary_ids": list(eliminated),
        "structural_predicate_count": len(structural_ids),
        "structural_predicate_ids": structural_ids,
        "base_records": records,
    }


def tsv_rows(path: Path):
    lines = [
        line for line in path.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("# ")
    ]
    return list(csv.DictReader(lines, delimiter="\t"))


def validate_inventory_document(root: Path) -> None:
    path = checked_path(root, ORDER64_JSON, ORDER64_JSON_SHA256)
    document = json.loads(path.read_text(encoding="utf-8"))
    if document["gap_export"] != ORDER64_TABLE:
        raise AssertionError("order-64 JSON points to the wrong table")
    if document["gap_export_sha256"] != ORDER64_TABLE_SHA256:
        raise AssertionError("order-64 JSON table hash changed")
    if document["multiplication_tables_embedded"] is not False:
        raise AssertionError("order-64 JSON unexpectedly embeds duplicate tables")
    if len(document["records"]) != 267:
        raise AssertionError("order-64 JSON record count changed")


def ordinary_partition(
    root: Path, h8_certificate: Mapping[str, object],
) -> Dict[str, object]:
    h7_json_path = checked_path(root, H7_ORDINARY_JSON, H7_ORDINARY_JSON_SHA256)
    h7_tsv_path = checked_path(root, H7_ORDINARY_TSV, H7_ORDINARY_TSV_SHA256)
    h7_document = json.loads(h7_json_path.read_text(encoding="utf-8"))
    if h7_document["input"] != H7_ORDINARY_TSV:
        raise AssertionError("ordinary batch points to the wrong TSV")
    if h7_document["input_sha256"] != H7_ORDINARY_TSV_SHA256:
        raise AssertionError("ordinary batch TSV hash changed")

    status_by_id = defaultdict(Counter)
    faithful_serials = defaultdict(set)
    for row in tsv_rows(h7_tsv_path):
        q_id = int(row["q_id"])
        if not 57 <= q_id <= 82:
            continue
        status = row["status"]
        status_by_id[q_id][status] += 1
        if status != "nonfaithful_radical":
            if status != "clique_ge_8":
                raise AssertionError("unexpected ordinary rank-three row status")
            faithful_serials[q_id].add(int(row["kernel_serial"]))

    faithful_ids = tuple(sorted(identifier for identifier in range(57, 83) if faithful_serials[identifier]))
    all_nonfaithful = tuple(sorted(identifier for identifier in range(57, 83) if not faithful_serials[identifier]))
    if faithful_ids != tuple(EXPECTED_ORDINARY_MINIMUM_OMEGA):
        raise AssertionError("unexpected ordinary faithful-ID partition")
    if all_nonfaithful != EXPECTED_ORDINARY_ALL_NONFAITHFUL:
        raise AssertionError("unexpected ordinary all-nonfaithful partition")
    if any(not status_by_id[identifier]["nonfaithful_radical"] for identifier in all_nonfaithful):
        raise AssertionError("an all-nonfaithful quotient has no saved kernel rows")

    exact_by_source = {}
    graph_records = h8_certificate["ordinary"]["graph_records"]
    for graph in graph_records:
        omega = int(graph["omega"])
        if omega >= 9 and len(graph.get("nine_clique", ())) != 9:
            raise AssertionError("ordinary exact graph lacks a K9 witness")
        for source in graph["sources"]:
            if source["q_order"] != 64 or not 57 <= source["q_id"] <= 82:
                continue
            key = (int(source["q_id"]), int(source["kernel_serial"]))
            if key in exact_by_source:
                raise AssertionError("duplicate ordinary exact source")
            exact_by_source[key] = omega
    expected_sources = {
        (q_id, serial)
        for q_id, serials in faithful_serials.items()
        for serial in serials
    }
    if set(exact_by_source) != expected_sources:
        raise AssertionError("h8 exact ordinary records do not cover every faithful kernel")
    minima = {
        q_id: min(omega for (source_id, _), omega in exact_by_source.items() if source_id == q_id)
        for q_id in faithful_ids
    }
    if minima != EXPECTED_ORDINARY_MINIMUM_OMEGA:
        raise AssertionError("ordinary per-ID exact omega minima changed")
    if min(minima.values()) != 12:
        raise AssertionError("ordinary rank-three tail minimum is not 12")
    return {
        "faithful_ids": list(faithful_ids),
        "all_nonfaithful_ids": list(all_nonfaithful),
        "faithful_kernel_count_by_id": {
            str(q_id): len(faithful_serials[q_id]) for q_id in faithful_ids
        },
        "minimum_exact_omega_by_id": {
            str(q_id): minima[q_id] for q_id in faithful_ids
        },
        "minimum_exact_omega": min(minima.values()),
    }


def generic_partition(
    root: Path, h8_document: Mapping[str, object], h8_certificate: Mapping[str, object],
) -> Dict[str, object]:
    input_records = {Path(record["path"]).stem: record for record in h8_document["inputs"]["generic_exports"]}
    for q_id, expected_hash in GENERIC_EXPORT_SHA256.items():
        relative = "experiments/logs/h7_order64_dual_%d.tsv" % q_id
        record = input_records.get(Path(relative).stem)
        if record != {"path": relative, "sha256": expected_hash}:
            raise AssertionError("generic export input record changed for %d" % q_id)
        checked_path(root, relative, expected_hash)

    certificates = {
        int(record["q_id"]): record
        for record in h8_certificate["generic_order64_dual"]["certificates"]
    }
    counts = {}
    for q_id in EXPECTED_GENERIC:
        record = certificates[q_id]
        observed = (
            int(record["good_character_count"]),
            int(record["retained_no_nine_subgroup_count"]),
            int(record["pruned_boundary_subgroup_count"]),
            int(record["faithful_candidate_count"]),
        )
        if observed != EXPECTED_GENERIC_COUNTS[q_id]:
            raise AssertionError("generic cutoff-nine census changed for %d" % q_id)
        if any(len(boundary["nine_clique"]) != 9 for boundary in record["boundary_records"]):
            raise AssertionError("generic boundary record lacks a K9 witness")
        counts[str(q_id)] = {
            "good_character_count": observed[0],
            "retained_no_nine_subgroup_count": observed[1],
            "pruned_boundary_subgroup_count": observed[2],
            "faithful_candidate_count": observed[3],
        }
    if h8_certificate["generic_order64_dual"]["faithful_candidate_count"] != 0:
        raise AssertionError("generic aggregate has a faithful cutoff-eight candidate")
    return {"ids": list(EXPECTED_GENERIC), "counts": counts}


def exterior_zero_partition(
    root: Path, h8_document: Mapping[str, object], h8_certificate: Mapping[str, object],
) -> Dict[str, object]:
    checked_path(root, H7_CAPABILITY_JSON, H7_CAPABILITY_JSON_SHA256)
    input_record = h8_document["inputs"]["delegations"]["order64_zero_rows"]
    if input_record != {
        "path": H7_CAPABILITY_JSON,
        "sha256": H7_CAPABILITY_JSON_SHA256,
    }:
        raise AssertionError("order-64 exterior-zero input record changed")
    excluded = set(
        h8_certificate["delegations"]["order64_exterior_zero"]["excluded_ids"]
    )
    observed = tuple(identifier for identifier in EXPECTED_STRUCTURAL_IDS if identifier in excluded)
    if observed != EXPECTED_EXTERIOR_ZERO:
        raise AssertionError("rank-three exterior-zero partition changed")
    return {"ids": list(observed)}


def verify_rank3_order64_tail(
    root: Path = REPOSITORY, rebuild_dependencies: bool = True,
) -> Dict[str, object]:
    table_path = checked_path(root, ORDER64_TABLE, ORDER64_TABLE_SHA256)
    validate_inventory_document(root)
    h8_path = checked_path(root, H8_BOUNDED_JSON, H8_BOUNDED_JSON_SHA256)
    if rebuild_dependencies:
        # This reparses every h7 ordinary row, reruns every generic cutoff-nine
        # BFS, validates the exterior-zero delegation, and exactly rebuilds the
        # entire saved h8 certificate before the joins below are trusted.
        verify_h8_document(h8_path, root)
    h8_document = json.loads(h8_path.read_text(encoding="utf-8"))
    h8_certificate = h8_document["certificate"]

    structural = structural_census(table_path)
    ordinary = ordinary_partition(root, h8_certificate)
    generic = generic_partition(root, h8_document, h8_certificate)
    exterior_zero = exterior_zero_partition(root, h8_document, h8_certificate)

    parts = (
        set(ordinary["faithful_ids"]),
        set(ordinary["all_nonfaithful_ids"]),
        set(generic["ids"]),
        set(exterior_zero["ids"]),
    )
    if any(parts[left] & parts[right] for left in range(4) for right in range(left)):
        raise AssertionError("rank-three order-64 partition overlaps")
    if set().union(*parts) != set(EXPECTED_STRUCTURAL_IDS):
        raise AssertionError("rank-three order-64 partition is incomplete")

    return {
        "status": "[COMPUTED] exact order-64 structural-tail join; no global h(8) claim",
        "scope": "all 267 committed order-64 multiplication tables and their canonical exact-center extension certificates",
        "source_sha256": {
            ORDER64_TABLE: ORDER64_TABLE_SHA256,
            ORDER64_JSON: ORDER64_JSON_SHA256,
            H7_ORDINARY_JSON: H7_ORDINARY_JSON_SHA256,
            H7_ORDINARY_TSV: H7_ORDINARY_TSV_SHA256,
            H7_CAPABILITY_JSON: H7_CAPABILITY_JSON_SHA256,
            H8_BOUNDED_JSON: H8_BOUNDED_JSON_SHA256,
            **{
                "experiments/logs/h7_order64_dual_%d.tsv" % q_id: digest
                for q_id, digest in sorted(GENERIC_EXPORT_SHA256.items())
            },
        },
        "structural_census": structural,
        "partition": {
            "ordinary_faithful_exact_omega_at_least_12": ordinary,
            "generic_no_faithful_candidate": generic,
            "exterior_zero": exterior_zero,
        },
        "conclusion": (
            "Exactly 39 order-64 quotients satisfy the proved rank-three normal-form "
            "predicates. Their complete canonical extension records contain no faithful "
            "graph with clique number at most eight."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=REPOSITORY)
    parser.add_argument(
        "--skip-dependency-rebuild", action="store_true",
        help="only for a quick repeat after the full dependency rebuild has passed",
    )
    args = parser.parse_args()
    result = verify_rank3_order64_tail(
        args.root.resolve(), rebuild_dependencies=not args.skip_dependency_rebuild
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
