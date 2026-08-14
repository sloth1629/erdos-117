"""Exact exterior-kernel certificate for ``Q = C4^2 x C2^2``.

Write ``Q = <e0,e1>_4 x <e2,e3>_2``.  Its exterior square is

``E = C4<t=e0^e1> x C2^5<e0^e2,e0^e3,e1^e2,e1^e3,e2^e3>``.

Every subgroup of ``E`` is listed once by its image in the ``C4`` factor:

* image zero: ``0 x N``;
* image ``2C4``: ``(0 x N) + <(2,u)>``;
* image ``C4``: ``(0 x N) + <(1,u)>``;

where ``N <= F2^5`` and, in the last two cases, ``u`` runs through
``F2^5/N``.  This gives all 5,276 subgroups without GAP's ``AllSubgroups``.
For each subgroup the module constructs the 64-vertex commutator graph,
records its full radical if nonfaithful, and otherwise records a checked
eight-clique.  Thus no exact-center quotient at clique cutoff seven occurs.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from typing import Dict, Iterator, Sequence, Tuple

from exact_invariants import verify_clique


Q_ELEMENT_COUNT = 64
H_DIMENSION = 5
EXTERIOR_ELEMENT_COUNT = 128
Basis = Tuple[int, ...]
KernelRecord = Tuple[str, Basis, int, Tuple[int, ...]]


def rref_subspaces() -> Iterator[Basis]:
    """Yield every subspace of ``F2^5`` once as bit-coded RREF rows."""

    for dimension in range(H_DIMENSION + 1):
        for pivots in combinations(range(H_DIMENSION), dimension):
            pivot_set = set(pivots)
            free_positions = [
                (row, column)
                for column in range(H_DIMENSION)
                if column not in pivot_set
                for row, pivot in enumerate(pivots)
                if pivot < column
            ]
            for values in product(range(2), repeat=len(free_positions)):
                rows = [1 << pivot for pivot in pivots]
                for value, (row, column) in zip(values, free_positions):
                    if value:
                        rows[row] |= 1 << column
                yield tuple(rows)


def subspace_elements(basis: Sequence[int]) -> Tuple[int, ...]:
    result = [0]
    for row in basis:
        result += [value ^ row for value in result]
    return tuple(sorted(result))


def quotient_representatives(subspace: Sequence[int]) -> Tuple[int, ...]:
    """Return the least element of every coset of ``subspace`` in ``F2^5``."""

    subspace_set = set(subspace)
    seen = set()
    representatives = []
    for value in range(1 << H_DIMENSION):
        if value not in seen:
            coset = {value ^ member for member in subspace_set}
            representatives.append(min(coset))
            seen.update(coset)
    if len(seen) != 1 << H_DIMENSION:
        raise AssertionError("coset representatives do not cover F2^5")
    return tuple(representatives)


def exterior_add(left: int, right: int) -> int:
    """Add encodings ``t + 4*h`` in ``C4 x F2^5``."""

    return ((left + right) & 3) + 4 * ((left // 4) ^ (right // 4))


def quotient_add(left: int, right: int) -> int:
    """Add bit encodings in ``C4^2 x C2^2``."""

    x0, x1, x2, x3 = decode_quotient(left)
    y0, y1, y2, y3 = decode_quotient(right)
    return (
        ((x0 + y0) & 3)
        | (((x1 + y1) & 3) << 2)
        | ((x2 ^ y2) << 4)
        | ((x3 ^ y3) << 5)
    )


def subgroup_elements(
    projection: str, subspace: Sequence[int], coset_representative: int = 0
) -> Tuple[int, ...]:
    """Construct one subgroup in the three-case classification above."""

    if projection == "zero":
        if coset_representative:
            raise ValueError("zero-projection subgroup has no coset parameter")
        return tuple(4 * member for member in subspace)
    if projection == "two":
        return tuple(sorted(
            [4 * member for member in subspace]
            + [2 + 4 * (coset_representative ^ member) for member in subspace]
        ))
    if projection == "full":
        return tuple(sorted(
            t + 4 * ((coset_representative if t & 1 else 0) ^ member)
            for t in range(4) for member in subspace
        ))
    raise ValueError("unknown C4 projection")


def all_subgroups() -> Tuple[KernelRecord, ...]:
    records = []
    for basis in rref_subspaces():
        subspace = subspace_elements(basis)
        records.append(("zero", basis, 0, subgroup_elements("zero", subspace)))
        for representative in quotient_representatives(subspace):
            records.append((
                "two", basis, representative,
                subgroup_elements("two", subspace, representative),
            ))
            records.append((
                "full", basis, representative,
                subgroup_elements("full", subspace, representative),
            ))
    return tuple(records)


def decode_quotient(value: int) -> Tuple[int, int, int, int]:
    if not 0 <= value < Q_ELEMENT_COUNT:
        raise ValueError("quotient element code is out of range")
    return value & 3, (value >> 2) & 3, (value >> 4) & 1, (value >> 5) & 1


def wedge(left: int, right: int) -> int:
    """Return ``left ^ right`` in the ``C4 x F2^5`` encoding."""

    x0, x1, x2, x3 = decode_quotient(left)
    y0, y1, y2, y3 = decode_quotient(right)
    cyclic = (x0 * y1 - x1 * y0) & 3
    binary = (
        (((x0 & 1) * y2) ^ (x2 * (y0 & 1)))
        | ((((x0 & 1) * y3) ^ (x3 * (y0 & 1))) << 1)
        | ((((x1 & 1) * y2) ^ (x2 * (y1 & 1))) << 2)
        | ((((x1 & 1) * y3) ^ (x3 * (y1 & 1))) << 3)
        | (((x2 * y3) ^ (x3 * y2)) << 4)
    )
    return cyclic + 4 * binary


WEDGES = tuple(
    tuple(wedge(left, right) for right in range(Q_ELEMENT_COUNT))
    for left in range(Q_ELEMENT_COUNT)
)


def graph_from_kernel(kernel: Sequence[int]) -> Tuple[int, ...]:
    kernel_set = set(kernel)
    return tuple(
        sum(
            1 << target for target, exterior_value in enumerate(row)
            if exterior_value not in kernel_set
        )
        for row in WEDGES
    )


def radical(adjacency: Sequence[int]) -> Tuple[int, ...]:
    return tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)


def greedy_target_clique(
    adjacency: Sequence[int], target: int = 8
) -> Tuple[int, ...]:
    """Deterministic multi-start greedy search used by the GAP batches."""

    starts = sorted(
        range(len(adjacency)),
        key=lambda vertex: (-bin(adjacency[vertex]).count("1"), vertex),
    )
    for start in starts:
        clique = [start]
        candidates = adjacency[start]
        while candidates and len(clique) < target:
            vertices = tuple(
                vertex for vertex in range(len(adjacency))
                if candidates & (1 << vertex)
            )
            vertex = min(
                vertices,
                key=lambda choice: (
                    -bin(candidates & adjacency[choice]).count("1"), choice
                ),
            )
            clique.append(vertex)
            candidates &= adjacency[vertex]
        if len(clique) == target:
            return tuple(clique)
    return ()


def _validate_subgroup(kernel: Sequence[int]) -> None:
    kernel_set = set(kernel)
    if 0 not in kernel_set or len(kernel_set) != len(kernel):
        raise AssertionError("subgroup encoding is not a set containing zero")
    if any(not 0 <= value < EXTERIOR_ELEMENT_COUNT for value in kernel):
        raise AssertionError("subgroup element is outside the exterior square")
    if any(
        exterior_add(left, right) not in kernel_set
        for left in kernel for right in kernel
    ):
        raise AssertionError("parameterized set is not closed under addition")


def exact_certificate() -> Dict[str, object]:
    subspaces = tuple(rref_subspaces())
    if len(subspaces) != 374 or len(set(subspaces)) != 374:
        raise AssertionError("wrong F2^5 subspace enumeration")
    subspace_dimension_distribution = Counter(map(len, subspaces))
    if subspace_dimension_distribution != {0: 1, 1: 31, 2: 155, 3: 155, 4: 31, 5: 1}:
        raise AssertionError("wrong F2^5 subspace dimension distribution")

    subgroup_parameters = all_subgroups()
    if len(subgroup_parameters) != 5276:
        raise AssertionError("wrong exterior subgroup count")
    encoded_subgroups = [record[3] for record in subgroup_parameters]
    if len(set(encoded_subgroups)) != len(encoded_subgroups):
        raise AssertionError("subgroup parametrization is not injective")

    # Independent subgroup count from the Gaussian-binomial numbers of F2^5.
    # Each N contributes one zero-image subgroup and 2^(5-dim N) subgroups in
    # each of the other two projection cases.
    classified_count = sum(
        count * (1 + 2 * (1 << (H_DIMENSION - dimension)))
        for dimension, count in subspace_dimension_distribution.items()
    )
    if classified_count != len(subgroup_parameters):
        raise AssertionError("three-case subgroup classification count is incomplete")

    # Check the coordinate formula independently on generators and every pair.
    quotient_generators = (1, 4, 16, 32)
    expected_generator_wedges = {
        (0, 1): 1, (0, 2): 4, (0, 3): 8,
        (1, 2): 16, (1, 3): 32, (2, 3): 64,
    }
    for (left, right), expected in expected_generator_wedges.items():
        if wedge(quotient_generators[left], quotient_generators[right]) != expected:
            raise AssertionError("wrong exterior basis coordinate")
    if any(WEDGES[x][x] != 0 for x in range(Q_ELEMENT_COUNT)):
        raise AssertionError("wedge is not alternating")
    # In characteristic four, skew symmetry means t changes sign while the
    # five binary coordinates are unchanged.
    for left in range(Q_ELEMENT_COUNT):
        for right in range(Q_ELEMENT_COUNT):
            value = WEDGES[left][right]
            negative = ((-value) & 3) + 4 * (value // 4)
            if WEDGES[right][left] != negative:
                raise AssertionError("wedge is not skew-symmetric")
            for third in range(Q_ELEMENT_COUNT):
                if WEDGES[quotient_add(left, right)][third] != exterior_add(
                    WEDGES[left][third], WEDGES[right][third]
                ):
                    raise AssertionError("wedge is not additive in the first variable")

    projection_counts = Counter()
    subgroup_order_counts = Counter()
    status_counts = Counter()
    status_by_projection = {key: Counter() for key in ("zero", "two", "full")}
    status_by_kernel_order = {}
    radical_size_counts = Counter()
    unique_graphs = set()
    unique_faithful_graphs = set()
    records = []
    for serial, (projection, basis, representative, kernel) in enumerate(
        subgroup_parameters, 1
    ):
        _validate_subgroup(kernel)
        projection_counts[projection] += 1
        subgroup_order_counts[len(kernel)] += 1
        adjacency = graph_from_kernel(kernel)
        if any(
            bool(adjacency[left] & (1 << right))
            != bool(adjacency[right] & (1 << left))
            for left in range(Q_ELEMENT_COUNT)
            for right in range(Q_ELEMENT_COUNT)
        ):
            raise AssertionError("commutator graph is not simple and symmetric")
        common_radical = radical(adjacency)
        radical_size_counts[len(common_radical)] += 1
        unique_graphs.add(adjacency)
        record = {
            "serial": serial,
            "projection_to_c4": projection,
            "binary_intersection_rref_basis": list(basis),
            "coset_representative": representative,
            "kernel_order": len(kernel),
        }
        if common_radical != (0,):
            status = "nonfaithful_radical"
            witness = common_radical
        else:
            status = "clique_ge_8"
            unique_faithful_graphs.add(adjacency)
            witness = greedy_target_clique(adjacency, 8)
            if len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("faithful kernel has no verified eight-clique")
        status_counts[status] += 1
        status_by_projection[projection][status] += 1
        status_by_kernel_order.setdefault(len(kernel), Counter())[status] += 1
        record.update({"status": status, "witness": list(witness)})
        records.append(record)

    expected_projection_counts = {"full": 2451, "two": 2451, "zero": 374}
    expected_order_counts = {1: 1, 2: 63, 4: 683, 8: 1891, 16: 1891, 32: 683, 64: 63, 128: 1}
    expected_status_counts = {"clique_ge_8": 2351, "nonfaithful_radical": 2925}
    if dict(projection_counts) != expected_projection_counts:
        raise AssertionError("wrong subgroup projection distribution")
    if dict(subgroup_order_counts) != expected_order_counts:
        raise AssertionError("wrong subgroup order distribution")
    if dict(status_counts) != expected_status_counts:
        raise AssertionError("wrong faithful/clique distribution")

    return {
        "quotient": "C4 x C4 x C2 x C2",
        "small_group": [64, 192],
        "quotient_element_count": Q_ELEMENT_COUNT,
        "exterior_structure": "C4 x C2^5",
        "exterior_order": EXTERIOR_ELEMENT_COUNT,
        "binary_subspace_count": len(subspaces),
        "binary_subspace_dimension_distribution": {
            str(key): value for key, value in sorted(subspace_dimension_distribution.items())
        },
        "subgroup_count": len(subgroup_parameters),
        "subgroup_projection_distribution": dict(sorted(projection_counts.items())),
        "subgroup_order_distribution": {
            str(key): value for key, value in sorted(subgroup_order_counts.items())
        },
        "status_distribution": dict(sorted(status_counts.items())),
        "status_by_projection": {
            key: dict(sorted(value.items()))
            for key, value in sorted(status_by_projection.items())
        },
        "status_by_kernel_order": {
            str(key): dict(sorted(value.items()))
            for key, value in sorted(status_by_kernel_order.items())
        },
        "radical_size_distribution": {
            str(key): value for key, value in sorted(radical_size_counts.items())
        },
        "unique_graph_count": len(unique_graphs),
        "unique_faithful_graph_count": len(unique_faithful_graphs),
        "cutoff_seven_candidate_count": 0,
        "records": records,
    }


def verify_certificate(certificate: Dict[str, object]) -> Dict[str, object]:
    """Rebuild and validate every saved subgroup, radical, and clique witness."""

    if certificate["small_group"] != [64, 192]:
        raise AssertionError("wrong quotient in saved certificate")
    if certificate["exterior_structure"] != "C4 x C2^5":
        raise AssertionError("wrong exterior structure in saved certificate")
    parameters = all_subgroups()
    records = certificate["records"]
    if len(parameters) != 5276 or len(records) != len(parameters):
        raise AssertionError("saved subgroup records are incomplete")

    projection_counts = Counter()
    subgroup_order_counts = Counter()
    status_counts = Counter()
    status_by_projection = {key: Counter() for key in ("zero", "two", "full")}
    status_by_kernel_order = {}
    radical_size_counts = Counter()
    unique_graphs = set()
    unique_faithful_graphs = set()
    encoded_subgroups = set()
    for serial, (parameter, record) in enumerate(zip(parameters, records), 1):
        projection, basis, representative, kernel = parameter
        expected_parameters = (
            record["serial"], record["projection_to_c4"],
            tuple(record["binary_intersection_rref_basis"]),
            record["coset_representative"], record["kernel_order"],
        )
        if expected_parameters != (
            serial, projection, basis, representative, len(kernel)
        ):
            raise AssertionError("saved subgroup parameters disagree with reconstruction")
        _validate_subgroup(kernel)
        if kernel in encoded_subgroups:
            raise AssertionError("saved subgroup parametrization is not injective")
        encoded_subgroups.add(kernel)
        adjacency = graph_from_kernel(kernel)
        common_radical = radical(adjacency)
        witness = tuple(record["witness"])
        status = record["status"]
        if status == "nonfaithful_radical":
            if len(common_radical) <= 1 or witness != common_radical:
                raise AssertionError("invalid saved radical witness")
        elif status == "clique_ge_8":
            if common_radical != (0,) or len(witness) != 8 or not verify_clique(adjacency, witness):
                raise AssertionError("invalid saved faithful clique witness")
            unique_faithful_graphs.add(adjacency)
        else:
            raise AssertionError("unknown saved record status")
        projection_counts[projection] += 1
        subgroup_order_counts[len(kernel)] += 1
        status_counts[status] += 1
        status_by_projection[projection][status] += 1
        status_by_kernel_order.setdefault(len(kernel), Counter())[status] += 1
        radical_size_counts[len(common_radical)] += 1
        unique_graphs.add(adjacency)

    rebuilt = {
        "subgroup_count": len(parameters),
        "subgroup_projection_distribution": dict(sorted(projection_counts.items())),
        "subgroup_order_distribution": {
            str(key): value for key, value in sorted(subgroup_order_counts.items())
        },
        "status_distribution": dict(sorted(status_counts.items())),
        "status_by_projection": {
            key: dict(sorted(value.items()))
            for key, value in sorted(status_by_projection.items())
        },
        "status_by_kernel_order": {
            str(key): dict(sorted(value.items()))
            for key, value in sorted(status_by_kernel_order.items())
        },
        "radical_size_distribution": {
            str(key): value for key, value in sorted(radical_size_counts.items())
        },
        "unique_graph_count": len(unique_graphs),
        "unique_faithful_graph_count": len(unique_faithful_graphs),
        "cutoff_seven_candidate_count": 0,
    }
    for key, value in rebuilt.items():
        if certificate[key] != value:
            raise AssertionError("saved certificate aggregate mismatch: " + key)
    return rebuilt
