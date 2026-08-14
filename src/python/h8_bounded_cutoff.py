#!/usr/bin/env python3
"""Canonical cutoff-eight certificate for center quotients of order at most 81.

This deliberately makes no global claim about ``h(8)``.  It reuses the
checksummed quotient inventory and raw cutoff-seven exports, but performs new
exact clique calculations on every formerly pruned ordinary graph and a new
target-nine invariant-subgroup BFS for the eleven generic dual quotients.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from functools import reduce
from pathlib import Path
from typing import Dict, Iterable, Mapping, Sequence, Tuple

from analyze_h7_capability_order64 import validate_capability_batches
from analyze_h7_exterior_batch import (
    parse_adjacency,
    parse_export,
    parse_vertices,
    verify_saved_batch,
)
from exact_invariants import (
    exact_chromatic_number,
    maximum_clique,
    verify_clique,
    verify_coloring,
)
import h7_c2_3_d8 as sg261
import h7_c4_2_c2_2 as sg192
from h8_order64_dual import (
    adjacency_sha256_payload,
    compress_independent_twins,
    exact_certificate as exact_dual_certificate,
    lift_clique,
    lift_coloring,
)


EXPECTED_GENERIC_IDS = (193, 195, 202, 203, 207, 211, 216, 226, 236, 242, 250)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _resolve(path: str | Path, root: Path) -> Path:
    value = Path(path)
    return value if value.is_absolute() else root / value


def _display_path(path: str | Path, root: Path) -> str:
    """Use a repository-relative path whenever the artifact is inside root."""

    value = _resolve(path, root).resolve()
    try:
        return str(value.relative_to(root.resolve()))
    except ValueError:
        return str(value)


def _distribution(counter: Counter) -> list[dict[str, int]]:
    return [
        {"omega": key, "count": value}
        for key, value in sorted(counter.items())
    ]


def _exact_graph_record(adjacency: Sequence[int]) -> Dict[str, object]:
    representatives, reduced, classes = compress_independent_twins(adjacency)
    clique = maximum_clique(reduced)
    lifted_clique = lift_clique(representatives, clique.vertices)
    if not verify_clique(adjacency, lifted_clique):
        raise AssertionError("invalid lifted exact clique")
    record: Dict[str, object] = {
        "adjacency_sha256": hashlib.sha256(
            adjacency_sha256_payload(adjacency)
        ).hexdigest(),
        "quotient_graph_order": len(adjacency),
        "twin_quotient_order": len(reduced),
        "twin_representatives": list(representatives),
        "omega": clique.size,
        "clique_search_nodes": clique.search_nodes,
    }
    if clique.size == 8:
        coloring = exact_chromatic_number(reduced, 8)
        lifted_coloring = lift_coloring(classes, coloring.colors)
        if not verify_coloring(adjacency, lifted_coloring):
            raise AssertionError("invalid lifted exact coloring")
        record.update({
            "clique": list(lifted_clique),
            "chi": coloring.size,
            "coloring": list(lifted_coloring),
            "commuting_color_classes": [
                [
                    vertex
                    for vertex, color in enumerate(lifted_coloring)
                    if color == selected
                ]
                for selected in range(coloring.size)
            ],
            "coloring_search_nodes_by_k": [
                list(item) for item in coloring.search_nodes_by_k
            ],
        })
    elif clique.size >= 9:
        witness = lifted_clique[:9]
        if not verify_clique(adjacency, witness):
            raise AssertionError("invalid nine-clique boundary witness")
        record["nine_clique"] = list(witness)
    else:
        raise AssertionError("cutoff-seven boundary graph has omega below eight")
    return record


def ordinary_certificate(
    batch_documents: Sequence[Path], root: Path,
) -> Dict[str, object]:
    """Solve every formerly pruned ordinary graph exactly."""

    graphs: Dict[Tuple[int, ...], list[dict[str, object]]] = {}
    verified_batches = []
    for document_path in batch_documents:
        comparisons = verify_saved_batch(document_path, root)
        document = json.loads(document_path.read_text(encoding="utf-8"))
        input_path = _resolve(document["input"], root)
        _, rows = parse_export(input_path)
        verified_batches.append({
            "document": _display_path(document_path, root),
            "document_sha256": sha256(document_path),
            "input": _display_path(input_path, root),
            "input_sha256": sha256(input_path),
            "base_comparisons": comparisons,
        })
        for row_number, row in enumerate(rows, 1):
            if row["status"] != "clique_ge_8":
                continue
            order = int(row["q_order"])
            adjacency = parse_adjacency(row["adjacency"], order)
            radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
            witness = parse_vertices(row["witness"])
            if radical != (0,) or len(witness) != 8 or not verify_clique(
                adjacency, witness
            ):
                raise AssertionError("malformed ordinary cutoff-seven boundary")
            graphs.setdefault(adjacency, []).append({
                "batch_document": _display_path(document_path, root),
                "input": _display_path(input_path, root),
                "row_number": row_number,
                "q_order": order,
                "q_id": int(row["q_id"]),
                "structure": row["structure"],
                "kernel_serial": int(row["kernel_serial"]),
                "kernel_order": int(row["kernel_order"]),
                "kernel_index": int(row["kernel_index"]),
            })

    records = []
    unique_distribution = Counter()
    row_distribution = Counter()
    new_candidates = []
    for adjacency, sources in graphs.items():
        record = _exact_graph_record(adjacency)
        record["sources"] = sources
        omega = int(record["omega"])
        unique_distribution[omega] += 1
        row_distribution[omega] += len(sources)
        records.append(record)
        if omega == 8:
            if record.get("chi") != 8:
                raise AssertionError("unexpected ordinary omega-eight chromatic number")
            new_candidates.extend(
                {
                    **source,
                    "omega": 8,
                    "chi": 8,
                    "adjacency_sha256": record["adjacency_sha256"],
                    "clique": record["clique"],
                    "coloring": record["coloring"],
                    "commuting_color_classes": record["commuting_color_classes"],
                }
                for source in sources
            )

    row_count = sum(len(sources) for sources in graphs.values())
    if row_count != 14989 or len(graphs) != 12266:
        raise AssertionError("unexpected ordinary cutoff-seven boundary census")
    expected_candidates = [
        (14, 1, 1, "D14"),
        (21, 1, 1, "C7 : C3"),
        (42, 1, 1, "C7 : C6"),
        (49, 2, 1, "C7 x C7"),
    ]
    observed_candidates = sorted(
        (
            record["q_order"], record["q_id"], record["kernel_serial"],
            record["structure"],
        )
        for record in new_candidates
    )
    if observed_candidates != expected_candidates:
        raise AssertionError("unexpected ordinary cutoff-eight candidate list")
    if unique_distribution[8] != 4 or row_distribution[8] != 4:
        raise AssertionError("wrong ordinary omega-eight multiplicity")
    if sum(value for key, value in unique_distribution.items() if key >= 9) != 12262:
        raise AssertionError("ordinary omega-nine boundary is incomplete")
    return {
        "verified_batches": verified_batches,
        "former_clique_ge_8_row_count": row_count,
        "distinct_stored_adjacency_count": len(graphs),
        "exact_omega_distribution_distinct_adjacencies": _distribution(
            unique_distribution
        ),
        "exact_omega_distribution_rows": _distribution(row_distribution),
        "omega_eight_row_count": len(new_candidates),
        "omega_at_least_nine_distinct_adjacency_count": 12262,
        "new_candidate_records": new_candidates,
        "graph_records": records,
    }


def _special_192(document_path: Path, root: Path) -> Dict[str, object]:
    document = json.loads(document_path.read_text(encoding="utf-8"))
    certificate = document["certificate"]
    sg192.verify_certificate(certificate)
    graphs: Dict[Tuple[int, ...], list[int]] = {}
    faithful_rows = 0
    for serial, parameter in enumerate(sg192.all_subgroups(), 1):
        adjacency = sg192.graph_from_kernel(parameter[3])
        if sg192.radical(adjacency) != (0,):
            continue
        faithful_rows += 1
        graphs.setdefault(adjacency, []).append(serial)
    unique_distribution = Counter()
    row_distribution = Counter()
    minimum_record = None
    for adjacency, serials in graphs.items():
        record = _exact_graph_record(adjacency)
        omega = int(record["omega"])
        unique_distribution[omega] += 1
        row_distribution[omega] += len(serials)
        if minimum_record is None or omega < minimum_record["omega"]:
            minimum_record = {
                "omega": omega,
                "serials": serials,
                "adjacency_sha256": record["adjacency_sha256"],
                "nine_clique": record.get("nine_clique", record.get("clique")),
            }
    expected = {
        12: 136, 13: 48, 14: 12, 17: 144, 18: 256, 19: 12,
        20: 624, 21: 414, 22: 18, 23: 288, 25: 85, 27: 1,
    }
    if faithful_rows != 2351 or len(graphs) != 2038:
        raise AssertionError("wrong SG(64,192) faithful graph census")
    if dict(sorted(unique_distribution.items())) != expected:
        raise AssertionError("wrong SG(64,192) exact clique distribution")
    return {
        "small_group": [64, 192],
        "delegated_document": _display_path(document_path, root),
        "delegated_document_sha256": sha256(document_path),
        "faithful_kernel_count": faithful_rows,
        "distinct_stored_adjacency_count": len(graphs),
        "minimum_omega": minimum_record["omega"],
        "minimum_record": minimum_record,
        "exact_omega_distribution_distinct_adjacencies": _distribution(
            unique_distribution
        ),
        "exact_omega_distribution_rows": _distribution(row_distribution),
    }


def _sg261_faithful_graphs(
    certificate: Mapping[str, object], export_path: Path,
) -> Tuple[int, Dict[Tuple[int, ...], list[int]]]:
    parsed = sg261.parse_export(export_path)
    orders = parsed["exterior_orders"]
    characters = tuple(itertools.product(*(range(order) for order in orders)))
    indices = {character: index for index, character in enumerate(characters)}
    scalar_graphs = tuple(
        sg261._scalar_graph(character, parsed["commutators"], orders)
        for character in characters
    )
    odd_base = tuple(certificate["odd_base_character"])
    double_base = int(certificate["twice_odd_base_code"])
    complement = tuple(int(value) for value in certificate["affine_coordinate_basis"])[1:]

    def hchar(code: int) -> Tuple[int, ...]:
        return tuple((code >> index) & 1 for index in range(9)) + (
            2 * ((code >> 9) & 1),
        )

    def lift(value: int) -> int:
        result = 0
        for index, vector in enumerate(complement):
            if value & (1 << index):
                result ^= vector
        return result

    graphs: Dict[Tuple[int, ...], list[int]] = {}
    faithful_rows = 0
    seen_subgroups = set()
    for expected_serial, record in enumerate(certificate["subgroup_records"], 1):
        if record["serial"] != expected_serial:
            raise AssertionError("SG261 subgroup serials are incomplete")
        quotient_basis = tuple(record["quotient_subspace_rref_basis"])
        representative = int(record["odd_coset_representative"])
        m_codes = sg261._binary_span(
            (double_base,) + tuple(lift(row) for row in quotient_basis)
        )
        shift = sg261._add(odd_base, hchar(lift(representative)), orders)
        subgroup = frozenset(
            {indices[hchar(code)] for code in m_codes}
            | {
                indices[sg261._add(shift, hchar(code), orders)]
                for code in m_codes
            }
        )
        if subgroup in seen_subgroups or len(subgroup) != record["subgroup_order"]:
            raise AssertionError("invalid SG261 affine subgroup parameters")
        seen_subgroups.add(subgroup)
        adjacency = tuple(
            reduce(
                int.__or__,
                (scalar_graphs[character][vertex] for character in subgroup),
                0,
            )
            for vertex in range(64)
        )
        radical = tuple(vertex for vertex, mask in enumerate(adjacency) if not mask)
        if radical == (0,):
            faithful_rows += 1
            graphs.setdefault(adjacency, []).append(expected_serial)
    if len(seen_subgroups) != 26387:
        raise AssertionError("SG261 affine subgroup census is incomplete")
    return faithful_rows, graphs


def _special_261(
    document_path: Path, export_path: Path, root: Path,
) -> Dict[str, object]:
    document = json.loads(document_path.read_text(encoding="utf-8"))
    certificate = document["certificate"]
    sg261.verify_certificate(certificate, export_path)
    faithful_rows, graphs = _sg261_faithful_graphs(certificate, export_path)
    unique_distribution = Counter()
    row_distribution = Counter()
    minimum_record = None
    for adjacency, serials in graphs.items():
        record = _exact_graph_record(adjacency)
        omega = int(record["omega"])
        unique_distribution[omega] += 1
        row_distribution[omega] += len(serials)
        if minimum_record is None or omega < minimum_record["omega"]:
            minimum_record = {
                "omega": omega,
                "serials": serials,
                "adjacency_sha256": record["adjacency_sha256"],
                "nine_clique": record.get("nine_clique", record.get("clique")),
            }
    expected = {
        13: 672, 17: 2352, 19: 504, 21: 1540, 25: 406,
        27: 128, 29: 224, 33: 29, 35: 7, 37: 7, 41: 1,
    }
    if faithful_rows != 22641 or len(graphs) != 5870:
        raise AssertionError("wrong SG(64,261) faithful graph census")
    if dict(sorted(unique_distribution.items())) != expected:
        raise AssertionError("wrong SG(64,261) exact clique distribution")
    return {
        "small_group": [64, 261],
        "delegated_document": _display_path(document_path, root),
        "delegated_document_sha256": sha256(document_path),
        "export": _display_path(export_path, root),
        "export_sha256": sha256(export_path),
        "faithful_subgroup_count": faithful_rows,
        "distinct_stored_adjacency_count": len(graphs),
        "minimum_omega": minimum_record["omega"],
        "minimum_record": minimum_record,
        "exact_omega_distribution_distinct_adjacencies": _distribution(
            unique_distribution
        ),
        "exact_omega_distribution_rows": _distribution(row_distribution),
    }


def _delegation_checks(paths: Mapping[str, Path], root: Path) -> Dict[str, object]:
    required = {
        "c2_5", "c2_6_rank6", "c2_6_rank4", "c3_4", "order64_zero_rows"
    }
    if set(paths) != required:
        raise AssertionError("wrong cutoff-eight delegation set")
    documents = {key: json.loads(path.read_text(encoding="utf-8")) for key, path in paths.items()}

    c2_5 = documents["c2_5"]["independent_python_certificate"]
    if c2_5["conclusion"] != "every zero-common-radical form subspace has clique number at least 9":
        raise AssertionError("C2^5 cutoff-eight delegation changed")
    c2_5_minimum = min(
        [record["omega"] for record in c2_5["pencil_orbits"]]
        + [c2_5["rank_two_radical_zero_orbit"]["omega"]]
    )
    if c2_5_minimum != 9:
        raise AssertionError("wrong C2^5 minimum clique number")

    rank6 = documents["c2_6_rank6"]["certificate"]
    if rank6["normalized_pencil_count"] != 16383 or rank6["minimum_omega"] != 9:
        raise AssertionError("C2^6 rank-six pencil delegation changed")
    rank4 = documents["c2_6_rank4"]["certificate"]
    faithful_rank4 = [
        record for record in rank4["orbits"] if record["common_radical"] == [0]
    ]
    rank4_minimum = min(record["omega"] for record in faithful_rank4)
    if rank4["normalized_pencil_count"] != 16383 or rank4_minimum != 11:
        raise AssertionError("C2^6 rank-four pencil delegation changed")
    if any(record["omega"] == 8 for record in rank4["orbits"]):
        raise AssertionError("unexpected C2^6 rank-four omega-eight orbit")

    c3 = documents["c3_4"]["certificate"]
    c3_eligible = [
        record for record in c3["weighted_invariant_distribution"]
        if record["omega"] <= 8
    ]
    if c3_eligible != [{"chi": 10, "omega": 7, "subspace_count": 234}]:
        raise AssertionError("C3^4 cutoff-eight delegation changed")

    zero_document = documents["order64_zero_rows"]
    zero_inputs = [_resolve(record["path"], root) for record in zero_document["inputs"]]
    zero_inventory = _resolve(zero_document["inventory"], root)
    for record, path in zip(zero_document["inputs"], zero_inputs):
        if sha256(path) != record["sha256"]:
            raise AssertionError("order-64 zero-row input hash mismatch")
    if sha256(zero_inventory) != zero_document["inventory_sha256"]:
        raise AssertionError("order-64 zero-row inventory hash mismatch")
    rebuilt_zero = validate_capability_batches(zero_inputs, zero_inventory)
    if rebuilt_zero != zero_document["certificate"]:
        raise AssertionError("order-64 zero-row delegated certificate changed")
    if len(rebuilt_zero["exterior_zero_excluded_ids"]) != 62:
        raise AssertionError("wrong order-64 exterior-zero exclusion count")

    return {
        "documents": {
            key: {"path": _display_path(path, root), "sha256": sha256(path)}
            for key, path in sorted(paths.items())
        },
        "c2_5": {
            "small_group": [32, 51],
            "minimum_omega_for_exact_center": c2_5_minimum,
            "common_radical_zero_pencil_count": c2_5[
                "common_radical_zero_pencil_count"
            ],
        },
        "c2_6": {
            "small_group": [64, 267],
            "rank_six_pencil_minimum_omega": rank6["minimum_omega"],
            "zero_radical_rank_four_pencil_minimum_omega": rank4_minimum,
            "rank_four_omega_eight_orbit_count": 0,
        },
        "c3_4": {
            "small_group": [81, 15],
            "eligible_at_cutoff_eight": c3_eligible,
        },
        "order64_exterior_zero": {
            "excluded_quotient_count": 62,
            "excluded_ids": rebuilt_zero["exterior_zero_excluded_ids"],
        },
    }


def exact_bounded_certificate(
    *,
    ordinary_batch_documents: Sequence[Path],
    generic_exports: Sequence[Path],
    sg192_document: Path,
    sg261_document: Path,
    sg261_export: Path,
    delegation_paths: Mapping[str, Path],
    root: Path,
) -> Dict[str, object]:
    ordinary = ordinary_certificate(ordinary_batch_documents, root)
    generic = [exact_dual_certificate(path) for path in generic_exports]
    if tuple(record["q_id"] for record in generic) != EXPECTED_GENERIC_IDS:
        raise AssertionError("generic dual exports are incomplete or out of order")
    generic_summary = {
        "quotient_count": len(generic),
        "retained_no_nine_subgroup_count": sum(
            record["retained_no_nine_subgroup_count"] for record in generic
        ),
        "pruned_boundary_subgroup_count": sum(
            record["pruned_boundary_subgroup_count"] for record in generic
        ),
        "faithful_candidate_count": sum(
            record["faithful_candidate_count"] for record in generic
        ),
        "certificates": generic,
    }
    observed_generic = (
        generic_summary["quotient_count"],
        generic_summary["retained_no_nine_subgroup_count"],
        generic_summary["pruned_boundary_subgroup_count"],
        generic_summary["faithful_candidate_count"],
    )
    if observed_generic != (11, 5206, 24551, 0):
        raise AssertionError("wrong aggregate generic cutoff-eight census")

    special_192 = _special_192(sg192_document, root)
    special_261 = _special_261(sg261_document, sg261_export, root)
    delegations = _delegation_checks(delegation_paths, root)
    return {
        "scope": "center quotients Q with |Q| <= 81 in the h7 inventory",
        "status": "[COMPUTED] center quotients |Q|<=81 only; no global h(8) upper bound",
        "ordinary": ordinary,
        "generic_order64_dual": generic_summary,
        "special_order64": [special_192, special_261],
        "delegations": delegations,
        "bounded_maximum_a_at_nu_at_most_eight": 10,
        "bounded_new_omega_eight_records": ordinary["new_candidate_records"],
        "bounded_example_with_a_greater_than_10_count": 0,
        "conclusion": (
            "Within the previously certified 738-type center-quotient inventory "
            "of order at most 81, the only graphs newly admitted when the clique "
            "cutoff rises from seven to eight are four ordinary (omega,chi)=(8,8) "
            "records. The bounded maximum remains 10, attained already at cutoff "
            "seven by the delegated C3^4 case. This does not bound center quotients "
            "for arbitrary groups with nu<=8 and therefore is not a global h(8) "
            "upper bound."
        ),
    }
