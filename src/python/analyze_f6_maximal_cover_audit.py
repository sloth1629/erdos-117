#!/usr/bin/env python3
"""Independently verify the finite maximal six-cover audit.

The GAP producer exports complete multiplication tables and its chosen maximal
subgroups as integer bit masks.  This verifier does not call GAP: it checks the
group axioms, enumerates every subgroup from the tables, recovers the complete
set of maximal subgroups, and recomputes every six-subset cover test, including
irredundancy and the core of the intersection.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import platform
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

from finite_groups import FiniteGroup


csv.field_size_limit(10_000_000)


EXPECTED_FAMILY_CLASS_COUNTS = {
    "auxiliary_C2S3square_all": 69,
    "auxiliary_S4_all": 11,
    "lemma_1a_C2C3S3": 1,
    "lemma_1a_S3cube": 1,
    "lemma_1b_S3cube_order72": 3,
    "lemma_1b_S3cube_order108": 7,
    "lemma_1c_S4square_order48": 21,
    "lemma_1c_S4square_order96": 15,
    "lemma_2_order50": 5,
    "lemma_2_order100": 16,
    "lemma_3_S3cube_subdirect": 14,
    "semisimple_A5": 1,
    "semisimple_S5": 1,
}

EXPECTED_FAMILY_CONCRETE_COUNTS = {
    "auxiliary_C2S3square_all": 206,
    "auxiliary_S4_all": 30,
    "lemma_1a_C2C3S3": 1,
    "lemma_1a_S3cube": 1,
    "lemma_1b_S3cube_order72": 9,
    "lemma_1b_S3cube_order108": 7,
    "lemma_1c_S4square_order48": 88,
    "lemma_1c_S4square_order96": 44,
    "lemma_2_order50": 5,
    "lemma_2_order100": 16,
    "lemma_3_S3cube_subdirect": 90,
    "semisimple_A5": 1,
    "semisimple_S5": 1,
}

# These duplicate distributions make the conjugacy-class enumeration auditable
# without depending on the order in which GAP happens to return its classes.
EXPECTED_KEY_FAMILY_IDS = {
    "auxiliary_S4_all": {
        "1,1": 1, "2,1": 2, "3,1": 1, "4,1": 1, "4,2": 2,
        "6,1": 1, "8,3": 1, "12,3": 1, "24,12": 1,
    },
    "lemma_1b_S3cube_order72": {"72,46": 3},
    "lemma_1b_S3cube_order108": {"108,38": 3, "108,39": 3, "108,40": 1},
    "lemma_1c_S4square_order48": {
        "48,30": 2, "48,31": 2, "48,38": 2,
        "48,48": 10, "48,49": 4, "48,50": 1,
    },
    "lemma_1c_S4square_order96": {
        "96,186": 2, "96,187": 2, "96,195": 4,
        "96,197": 2, "96,226": 4, "96,227": 1,
    },
    "lemma_3_S3cube_subdirect": {
        "6,1": 1, "18,4": 4, "36,10": 3, "54,14": 1,
        "108,39": 3, "108,40": 1, "216,162": 1,
    },
}

EXPECTED_POSITIVE_GROUPS = {
    "18,4": (234, {1: 234}),
    "24,14": (4, {1: 4}),
    "36,13": (72, {1: 72}),
    "50,4": (25, {2: 25}),
    "54,14": (6318, {2: 6318}),
    "100,11": (25, {4: 25}),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_tsv(path: Path) -> Tuple[Dict[str, str], List[Dict[str, str]]]:
    metadata: Dict[str, str] = {}
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            key, value = line[2:].split("=", 1)
            metadata[key] = value
        elif line:
            lines.append(line)
    if not lines:
        raise ValueError("empty TSV: %s" % path)
    return metadata, list(csv.DictReader(lines, delimiter="\t"))


def parse_integer_list(raw: str, offset: int = 0) -> Tuple[int, ...]:
    if not raw:
        return ()
    return tuple(int(value) + offset for value in raw.split(","))


def bit_vertices(mask: int) -> Iterable[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def popcount(mask: int) -> int:
    # The repository's baseline interpreter is Python 3.9, before int.bit_count.
    return bin(mask).count("1")


def parse_group(row: Mapping[str, str]) -> FiniteGroup:
    order = int(row["order"])
    table_rows = row["multiplication_table"].split(";")
    if not row["elements"] or len(table_rows) != order:
        raise ValueError("wrong multiplication-table dimensions for %s" % row["group_id"])
    table = tuple(
        tuple(value - 1 for value in parse_integer_list(table_row))
        for table_row in table_rows
    )
    # GAP's human-readable permutation labels themselves contain commas, so
    # they are deliberately non-load-bearing.  The canonical table positions
    # are the element identities used throughout the independent verifier.
    elements = tuple("element_%d" % (index + 1) for index in range(order))
    group = FiniteGroup(row["group_id"], elements, table)
    group.validate(check_associativity=True)
    return group


def inverses(group: FiniteGroup) -> Tuple[int, ...]:
    return tuple(group.inverse(vertex) for vertex in range(group.order))


def generated_mask(
    group: FiniteGroup,
    generators: Sequence[int],
    inverse: Sequence[int],
) -> int:
    steps = tuple(dict.fromkeys(tuple(generators) + tuple(inverse[x] for x in generators)))
    mask = 1 << group.identity
    queue = deque([group.identity])
    while queue:
        vertex = queue.popleft()
        for step in steps:
            product = group.table[vertex][step]
            if not mask & (1 << product):
                mask |= 1 << product
                queue.append(product)
    return mask


def enumerate_subgroups(group: FiniteGroup) -> Dict[int, Tuple[int, ...]]:
    """Enumerate all subgroups, keeping one exact generating tuple per mask.

    For a known subgroup H, one representative of each left coset Hx suffices,
    since <H,hx>=<H,x>.  This is a pruning identity, not a classification input.
    """

    inverse = inverses(group)
    full = (1 << group.order) - 1
    trivial = 1 << group.identity
    generating_sets: Dict[int, Tuple[int, ...]] = {trivial: ()}
    queue = deque([trivial])
    while queue:
        subgroup = queue.popleft()
        generators = generating_sets[subgroup]
        remaining = full ^ subgroup
        while remaining:
            representative_bit = remaining & -remaining
            representative = representative_bit.bit_length() - 1
            coset = 0
            for element in bit_vertices(subgroup):
                coset |= 1 << group.table[element][representative]
            remaining &= ~coset
            extension_generators = generators + (representative,)
            extension = generated_mask(group, extension_generators, inverse)
            if extension & subgroup != subgroup:
                raise AssertionError("generated extension lost its base subgroup")
            if extension not in generating_sets:
                generating_sets[extension] = extension_generators
                queue.append(extension)
    return generating_sets


def maximal_subgroup_masks(
    group: FiniteGroup,
    subgroup_generators: Mapping[int, Sequence[int]],
) -> Tuple[int, ...]:
    full = (1 << group.order) - 1
    proper = tuple(mask for mask in subgroup_generators if mask != full)
    result = []
    for subgroup in proper:
        if not any(
            subgroup != larger and subgroup & ~larger == 0
            for larger in proper
        ):
            result.append(subgroup)
    return tuple(sorted(result))


def core_mask(group: FiniteGroup, subgroup: int, inverse: Sequence[int]) -> int:
    core = 0
    for element in bit_vertices(subgroup):
        normal_in_subgroup = True
        for conjugator in range(group.order):
            conjugate = group.table[group.table[inverse[conjugator]][element]][conjugator]
            if not subgroup & (1 << conjugate):
                normal_in_subgroup = False
                break
        if normal_in_subgroup:
            core |= 1 << element
    return core


def parse_distribution(raw: str) -> Counter:
    distribution = Counter()
    if raw:
        for entry in raw.split(","):
            order, count = entry.split(":")
            distribution[int(order)] = int(count)
    return distribution


def parse_qualifying(raw: str) -> Tuple[Tuple[Tuple[int, ...], int, int], ...]:
    records = []
    if raw:
        for entry in raw.split(";"):
            combination, order, mask = entry.split("@")
            records.append((parse_integer_list(combination), int(order), int(mask)))
    return tuple(records)


def verify_group_row(row: Mapping[str, str]) -> Dict[str, object]:
    group = parse_group(row)
    order = group.order
    full = (1 << order) - 1
    inverse = inverses(group)
    exported_maximals = parse_integer_list(row["maximal_masks"])
    exported_orders = parse_integer_list(row["maximal_orders"])
    if int(row["maximal_count"]) != len(exported_maximals):
        raise AssertionError("wrong maximal count for %s" % group.group_id)
    if len(exported_orders) != len(exported_maximals):
        raise AssertionError("wrong maximal-order list for %s" % group.group_id)
    if len(set(exported_maximals)) != len(exported_maximals):
        raise AssertionError("duplicate maximal masks for %s" % group.group_id)
    for mask, expected_order in zip(exported_maximals, exported_orders):
        if mask <= 0 or mask & ~full or mask == full:
            raise AssertionError("invalid proper-subgroup mask")
        if popcount(mask) != expected_order:
            raise AssertionError("maximal order disagrees with its mask")
        if not group.is_subgroup(bit_vertices(mask)):
            raise AssertionError("exported maximal mask is not a subgroup")

    subgroup_generators = enumerate_subgroups(group)
    independent_maximals = maximal_subgroup_masks(group, subgroup_generators)
    if set(exported_maximals) != set(independent_maximals):
        raise AssertionError("independent maximal-subgroup set disagrees for %s" % group.group_id)
    for maximal in exported_maximals:
        generators = subgroup_generators[maximal]
        for outside in range(order):
            if not maximal & (1 << outside):
                if generated_mask(group, generators + (outside,), inverse) != full:
                    raise AssertionError("exported subgroup is not maximal")

    combination_count = math.comb(len(exported_maximals), 6) if len(exported_maximals) >= 6 else 0
    cover_count = 0
    irredundant_count = 0
    qualifying: List[Tuple[Tuple[int, ...], int, int]] = []
    intersection_distribution = Counter()
    core_cache: Dict[int, int] = {}
    for zero_based in itertools.combinations(range(len(exported_maximals)), 6):
        masks = tuple(exported_maximals[index] for index in zero_based)
        if masks[0] | masks[1] | masks[2] | masks[3] | masks[4] | masks[5] != full:
            continue
        cover_count += 1
        irredundant = True
        for omitted in range(6):
            union_of_others = 0
            for position, mask in enumerate(masks):
                if position != omitted:
                    union_of_others |= mask
            if not masks[omitted] & ~union_of_others & full:
                irredundant = False
                break
        if not irredundant:
            continue
        irredundant_count += 1
        intersection = masks[0] & masks[1] & masks[2] & masks[3] & masks[4] & masks[5]
        if intersection not in core_cache:
            core_cache[intersection] = core_mask(group, intersection, inverse)
        if core_cache[intersection] != 1 << group.identity:
            continue
        intersection_order = popcount(intersection)
        intersection_distribution[intersection_order] += 1
        combination = tuple(index + 1 for index in zero_based)
        qualifying.append((combination, intersection_order, intersection))

    expected_qualifying = parse_qualifying(row["qualifying_covers"])
    comparisons = {
        "six_combinations": combination_count,
        "cover_count": cover_count,
        "irredundant_cover_count": irredundant_count,
        "qualifying_count": len(qualifying),
    }
    for field, actual in comparisons.items():
        if int(row[field]) != actual:
            raise AssertionError("%s disagrees for %s" % (field, group.group_id))
    if parse_distribution(row["intersection_distribution"]) != intersection_distribution:
        raise AssertionError("intersection distribution disagrees for %s" % group.group_id)
    if tuple(qualifying) != expected_qualifying:
        raise AssertionError("qualifying cover certificates disagree for %s" % group.group_id)

    return {
        "group_id": group.group_id,
        "structure": row["structure"],
        "order": order,
        "case_tags": row["case_tags"].split(";") if row["case_tags"] else [],
        "subgroup_count": len(subgroup_generators),
        "maximal_count": len(exported_maximals),
        "six_combinations": combination_count,
        "cover_count": cover_count,
        "irredundant_cover_count": irredundant_count,
        "qualifying_count": len(qualifying),
        "intersection_distribution": dict(sorted(intersection_distribution.items())),
        "qualifying_certificate_sha256": hashlib.sha256(
            row["qualifying_covers"].encode("utf-8")
        ).hexdigest(),
    }


def audit_class_rows(rows: Sequence[Mapping[str, str]]) -> Tuple[List[Dict[str, object]], Dict[str, set]]:
    by_family = defaultdict(list)
    selected_tags = defaultdict(set)
    for row in rows:
        family = row["family"]
        by_family[family].append(row)
        group_order = int(row["group_id"].split(",", 1)[0])
        if int(row["subgroup_order"]) != group_order:
            raise AssertionError("SmallGroup order and subgroup order disagree")
        center_order = int(row["center_order"])
        if center_order < 1 or group_order % center_order:
            raise AssertionError("invalid center order")
        selected = row["selected_for_cover"] == "true"
        if row["selected_for_cover"] not in ("true", "false"):
            raise AssertionError("invalid selection flag")
        if family.startswith("lemma_2_order") and selected != (center_order == 1):
            raise AssertionError("order-50/100 selection is not exactly centerlessness")
        if not family.startswith("lemma_2_order") and not selected:
            raise AssertionError("an ambient subgroup class was unexpectedly skipped")
        if selected:
            selected_tags[row["group_id"]].add(family)
        projections = parse_integer_list(row["projection_sizes"])
        if family == "lemma_3_S3cube_subdirect":
            if projections != (6, 6, 6):
                raise AssertionError("a purported S3^3 subdirect is not surjective")
        elif projections:
            raise AssertionError("unexpected projection metadata")

    if {family: len(records) for family, records in by_family.items()} != EXPECTED_FAMILY_CLASS_COUNTS:
        raise AssertionError("ambient conjugacy-class counts changed")
    concrete_counts = {
        family: sum(int(row["class_size"]) for row in records)
        for family, records in by_family.items()
    }
    if concrete_counts != EXPECTED_FAMILY_CONCRETE_COUNTS:
        raise AssertionError("ambient concrete-subgroup counts changed")
    for family, records in by_family.items():
        serials = sorted(int(row["class_serial"]) for row in records)
        if serials != list(range(1, len(records) + 1)):
            raise AssertionError("incomplete class serials for %s" % family)
    for family, expected in EXPECTED_KEY_FAMILY_IDS.items():
        actual = Counter(row["group_id"] for row in by_family[family])
        if actual != Counter(expected):
            raise AssertionError("isomorphism-ID distribution changed for %s" % family)

    summaries = []
    for family in sorted(by_family):
        records = by_family[family]
        ids = Counter(row["group_id"] for row in records)
        summaries.append(
            {
                "family": family,
                "ambient": sorted(set(row["ambient"] for row in records)),
                "conjugacy_class_count": len(records),
                "concrete_subgroup_count": sum(int(row["class_size"]) for row in records),
                "isomorphism_type_count": len(ids),
                "duplicate_class_count": len(records) - len(ids),
                "id_multiplicities": dict(sorted(ids.items())),
                "class_serials_complete": True,
            }
        )
    return summaries, selected_tags


def assert_case_results(group_records: Mapping[str, Mapping[str, object]]) -> None:
    positives = {
        group_id: (
            int(record["qualifying_count"]),
            {int(order): int(count) for order, count in record["intersection_distribution"].items()},
        )
        for group_id, record in group_records.items()
        if int(record["qualifying_count"])
    }
    if positives != EXPECTED_POSITIVE_GROUPS:
        raise AssertionError("positive-group distribution changed: %r" % positives)

    def zero_for_tag(tag: str) -> None:
        for record in group_records.values():
            if tag in record["case_tags"] and int(record["qualifying_count"]):
                raise AssertionError("unexpected qualifying cover in %s" % tag)

    for tag in (
        "auxiliary_S4_all",
        "lemma_1a_C2C3S3",
        "lemma_1a_S3cube",
        "lemma_1b_S3cube_order72",
        "lemma_1b_S3cube_order108",
        "lemma_1c_S4square_order48",
        "lemma_1c_S4square_order96",
        "semisimple_A5",
        "semisimple_S5",
    ):
        zero_for_tag(tag)

    subdirect_positive = {
        group_id for group_id, record in group_records.items()
        if "lemma_3_S3cube_subdirect" in record["case_tags"]
        and int(record["qualifying_count"])
    }
    if subdirect_positive != {"18,4", "54,14"}:
        raise AssertionError("wrong S3^3 subdirect classification")
    if (
        int(group_records["36,10"]["cover_count"]) != 38
        or int(group_records["36,10"]["irredundant_cover_count"]) != 0
        or int(group_records["36,10"]["qualifying_count"]) != 0
    ):
        raise AssertionError("SmallGroup(36,10) regression failed")
    if (
        int(group_records["36,13"]["qualifying_count"]) != 72
        or group_records["36,13"]["intersection_distribution"] != {1: 72}
    ):
        raise AssertionError("SmallGroup(36,13) regression failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--classes", type=Path, required=True)
    parser.add_argument("--groups", type=Path, required=True)
    parser.add_argument("--gap-script", type=Path, required=True)
    parser.add_argument("--gap-stdout", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()

    class_metadata, class_rows = parse_tsv(args.classes)
    group_metadata, group_rows = parse_tsv(args.groups)
    if class_metadata != group_metadata:
        raise AssertionError("GAP metadata differs between exported files")
    if class_metadata.get("COVER_SIZE") != "6":
        raise AssertionError("this verifier is specific to six-covers")
    class_summaries, selected_tags = audit_class_rows(class_rows)

    raw_group_ids = [row["group_id"] for row in group_rows]
    if len(raw_group_ids) != len(set(raw_group_ids)):
        raise AssertionError("duplicate group rows")
    if set(raw_group_ids) != set(selected_tags):
        raise AssertionError("selected class IDs do not equal audited group IDs")

    verified = []
    for row in group_rows:
        record = verify_group_row(row)
        if set(record["case_tags"]) != selected_tags[row["group_id"]]:
            raise AssertionError("case-tag deduplication disagrees for %s" % row["group_id"])
        verified.append(record)
    by_id = {record["group_id"]: record for record in verified}
    if len(by_id) != 48:
        raise AssertionError("wrong number of distinct audited group types")
    assert_case_results(by_id)

    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "gap_metadata": class_metadata,
        "inputs": {
            "gap_script": str(args.gap_script),
            "gap_script_sha256": sha256(args.gap_script),
            "class_tsv": str(args.classes),
            "class_tsv_sha256": sha256(args.classes),
            "group_tsv": str(args.groups),
            "group_tsv_sha256": sha256(args.groups),
            "gap_stdout": str(args.gap_stdout),
            "gap_stdout_sha256": sha256(args.gap_stdout),
        },
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "verification": {
            "group_axioms": "exhaustive multiplication-table check",
            "subgroups": "independent closure enumeration from each table",
            "maximality": "independent complete maximal-subgroup recovery",
            "six_subsets": "independent exhaustive combinations",
            "cover": "bitwise union equals the full group",
            "irredundancy": "each member has a private element",
            "corefree": "all conjugates of every intersection element checked",
        },
        "ambient_class_record_count": len(class_rows),
        "ambient_families": class_summaries,
        "audited_isomorphism_type_count": len(verified),
        "total_subgroups_independently_enumerated": sum(int(r["subgroup_count"]) for r in verified),
        "total_six_subsets": sum(int(r["six_combinations"]) for r in verified),
        "total_covers": sum(int(r["cover_count"]) for r in verified),
        "total_irredundant_covers": sum(int(r["irredundant_cover_count"]) for r in verified),
        "total_qualifying_covers": sum(int(r["qualifying_count"]) for r in verified),
        "positive_groups": [record for record in verified if int(record["qualifying_count"])],
        "groups": verified,
        "case_conclusions": {
            "lemma_4_1_1a": "no qualifying covers in S3^3 or C2xC3xS3",
            "lemma_4_1_1b": "no qualifying covers in order-72/108 subgroups of S3^3",
            "lemma_4_1_1c": "no qualifying covers in order-48/96 subgroups of S4^2",
            "lemma_4_1_2d": "SmallGroup(50,4): 25 qualifying covers, all |D|=2",
            "lemma_4_1_2e": "SmallGroup(100,11): 25 qualifying covers, all |D|=4",
            "lemma_4_1_3": "S3^3 subdirect positives are exactly SmallGroup(18,4) and SmallGroup(54,14)",
            "semisimple": "A5 and S5 have no qualifying covers",
            "S4_subgroup_gap": "all 11 conjugacy classes, 30 subgroups, and 9 isomorphism types have no qualifying covers",
        },
        "corrections": [
            "SmallGroup(36,10)=S3xS3 has 38 six-covers but none is irredundant; it is not the index-36 witness.",
            "SmallGroup(36,13)=C2x((C3xC3):C2) has 72 qualifying covers with trivial intersection and is the audited index-36 witness.",
            "SmallGroup IDs and exact subgroup masks replace the dissertation's inconsistent L_i indexing on page 59.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "ambient_class_records=%d audited_group_types=%d"
        % (len(class_rows), len(verified)),
        "independent_subgroups=%d six_subsets=%d covers=%d irredundant=%d qualifying=%d"
        % (
            output["total_subgroups_independently_enumerated"],
            output["total_six_subsets"],
            output["total_covers"],
            output["total_irredundant_covers"],
            output["total_qualifying_covers"],
        ),
        "positive_groups=%r"
        % [
            (r["group_id"], r["qualifying_count"], r["intersection_distribution"])
            for r in output["positive_groups"]
        ],
        "S4_subgroups=11_classes/30_concrete/9_types; all qualifying=0",
        "regressions=SmallGroup(36,10):0; SmallGroup(36,13):72",
        "input_hashes=%r" % output["inputs"],
        "wrote independent certificate to %s" % args.output,
    ]
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
