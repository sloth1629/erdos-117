#!/usr/bin/env python3
"""Dependency-free verifier for the dynamic-centralizer certificates.

Only the Python standard library is used.  The script verifies:
  * the two finite class-two group models and their centers;
  * exact clique numbers;
  * primal and dual LP certificates using fractions;
  * exact dynamic-centralizer values and fractional abelian covers;
  * the strict max-child/dynamic separation in the order-64 model;
  * all 28,672 natural one-pair extensions, each by an explicit 10-clique.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

REPOSITORY = Path(__file__).resolve().parents[2]
CERT_PATH = (
    REPOSITORY / "experiments" / "logs" / "dynamic_fractional_centralizer.json"
)

Vector = int
Matrix = Tuple[Tuple[int, ...], ...]
Centralizer = Tuple[int, ...]


def frac(value: str | int) -> Fraction:
    return Fraction(value)


def popcount(value: int) -> int:
    """Return the number of set bits, including on repository Python 3.9."""
    return bin(value).count("1")


def bit_vector(code: int, dimension: int) -> Tuple[int, ...]:
    return tuple((code >> i) & 1 for i in range(dimension))


def dot_mod2(left: Sequence[int], right: Sequence[int]) -> int:
    return sum(a * b for a, b in zip(left, right)) & 1


def matrix_vector(matrix: Matrix, vector: Sequence[int]) -> Tuple[int, ...]:
    return tuple(dot_mod2(row, vector) for row in matrix)


def bilinear_component(matrix: Matrix, left: int, right: int, dimension: int) -> int:
    lv = bit_vector(left, dimension)
    rv = bit_vector(right, dimension)
    return dot_mod2(lv, matrix_vector(matrix, rv))


def beta(matrices: Sequence[Matrix], left: int, right: int, dimension: int) -> int:
    value = 0
    for coordinate, matrix in enumerate(matrices):
        value |= bilinear_component(matrix, left, right, dimension) << coordinate
    return value


def cocycle(matrices: Sequence[Matrix], left: int, right: int, dimension: int) -> int:
    """Upper-triangular bilinear cocycle whose alternating part is beta."""
    lv = bit_vector(left, dimension)
    rv = bit_vector(right, dimension)
    value = 0
    for coordinate, matrix in enumerate(matrices):
        component = 0
        for i in range(dimension):
            for j in range(i + 1, dimension):
                component ^= lv[i] & matrix[i][j] & rv[j]
        value |= component << coordinate
    return value


def multiply_group_element(
    matrices: Sequence[Matrix], dimension: int, codomain_dimension: int, a: int, b: int
) -> int:
    mask = (1 << dimension) - 1
    av, az = a & mask, a >> dimension
    bv, bz = b & mask, b >> dimension
    cv = av ^ bv
    cz = az ^ bz ^ cocycle(matrices, av, bv, dimension)
    assert 0 <= cz < (1 << codomain_dimension)
    return cv | (cz << dimension)


def verify_group_model(
    matrices: Sequence[Matrix], dimension: int, codomain_dimension: int
) -> Tuple[int, int]:
    order = 1 << (dimension + codomain_dimension)
    elements = range(order)
    mul = lambda a, b: multiply_group_element(
        matrices, dimension, codomain_dimension, a, b
    )

    # Bilinearity of the cocycle makes associativity formal; the finite check is an
    # independent exhaustive validation of the encoded multiplication law.
    for a in elements:
        assert mul(0, a) == a and mul(a, 0) == a
    for a in elements:
        for b in elements:
            ab = mul(a, b)
            for c in elements:
                assert mul(ab, c) == mul(a, mul(b, c))

    for a in elements:
        assert any(mul(a, b) == 0 and mul(b, a) == 0 for b in elements)

    center = []
    for a in elements:
        if all(mul(a, b) == mul(b, a) for b in elements):
            center.append(a)

    # Check that the actual group commutator relation agrees with beta on V.
    for v in range(1 << dimension):
        for w in range(1 << dimension):
            group_commutes = mul(v, w) == mul(w, v)
            assert group_commutes == (beta(matrices, v, w, dimension) == 0)

    return order, len(center)


def adjacency_masks(matrices: Sequence[Matrix], dimension: int) -> List[int]:
    """Adjacency on the nonzero quotient vectors, indexed by code-1."""
    count = (1 << dimension) - 1
    adjacency = [0] * count
    for x in range(1, 1 << dimension):
        for y in range(x + 1, 1 << dimension):
            if beta(matrices, x, y, dimension) != 0:
                adjacency[x - 1] |= 1 << (y - 1)
                adjacency[y - 1] |= 1 << (x - 1)
    return adjacency


def maximum_clique(adjacency: Sequence[int], allowed: int | None = None) -> Tuple[int, ...]:
    """Exact branch-and-bound maximum clique with a greedy-color upper bound."""
    vertex_count = len(adjacency)
    if allowed is None:
        allowed = (1 << vertex_count) - 1
    best: Tuple[int, ...] = ()

    def color_sort(candidates: int) -> Tuple[List[int], List[int]]:
        order: List[int] = []
        bounds: List[int] = []
        color = 0
        remaining = candidates
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= remaining
                available &= ~adjacency[vertex]
        return order, bounds

    def search(chosen: Tuple[int, ...], candidates: int) -> None:
        nonlocal best
        if not candidates:
            if len(chosen) > len(best):
                best = chosen
            return
        order, bounds = color_sort(candidates)
        for index in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[index] <= len(best):
                return
            vertex = order[index]
            bit = 1 << vertex
            if candidates & bit:
                search(chosen + (vertex,), candidates & adjacency[vertex])
                candidates ^= bit

    search((), allowed)
    return tuple(vertex + 1 for vertex in best)


def clique_number_on_codes(adjacency: Sequence[int], codes: Iterable[int]) -> int:
    codes_tuple = tuple(sorted(set(codes)))
    allowed = 0
    has_edge = False
    for code in codes_tuple:
        if code == 0:
            continue
        bit = 1 << (code - 1)
        allowed |= bit
    probe = allowed
    while probe:
        bit = probe & -probe
        vertex = bit.bit_length() - 1
        if adjacency[vertex] & allowed:
            has_edge = True
            break
        probe ^= bit
    if not has_edge:
        return 0
    return len(maximum_clique(adjacency, allowed))


def is_clique(matrices: Sequence[Matrix], dimension: int, clique: Sequence[int]) -> bool:
    return all(
        beta(matrices, x, y, dimension) != 0
        for x, y in itertools.combinations(clique, 2)
    )


def is_isotropic(matrices: Sequence[Matrix], dimension: int, subset: Sequence[int]) -> bool:
    return all(
        beta(matrices, x, y, dimension) == 0
        for x, y in itertools.combinations(subset, 2)
    )


def is_linear_subspace(subset: Sequence[int]) -> bool:
    values = set(subset)
    return 0 in values and all((x ^ y) in values for x in values for y in values)


def centralizer_set(
    matrices: Sequence[Matrix], dimension: int, vector: int, universe: Iterable[int] | None = None
) -> Centralizer:
    if universe is None:
        universe = range(1 << dimension)
    return tuple(
        value
        for value in universe
        if beta(matrices, vector, value, dimension) == 0
    )


def unique_centralizers(matrices: Sequence[Matrix], dimension: int) -> Tuple[Centralizer, ...]:
    values = {
        centralizer_set(matrices, dimension, vector)
        for vector in range(1, 1 << dimension)
    }
    return tuple(sorted(values, key=lambda item: (-len(item), item)))


def radical_of_subspace(
    matrices: Sequence[Matrix], dimension: int, subspace: Sequence[int]
) -> Tuple[int, ...]:
    return tuple(
        value
        for value in subspace
        if all(beta(matrices, value, other, dimension) == 0 for other in subspace)
    )


def xor_cosets(subspace: Sequence[int], radical: Sequence[int]) -> Tuple[Tuple[int, ...], ...]:
    remaining = set(subspace)
    radical_set = set(radical)
    cosets: List[Tuple[int, ...]] = []
    while remaining:
        representative = min(remaining)
        coset = tuple(sorted(representative ^ r for r in radical_set))
        assert set(coset) <= remaining
        remaining -= set(coset)
        cosets.append(coset)
    return tuple(sorted(cosets, key=lambda item: (0 not in item, item)))


def verify_k3_child(
    matrices: Sequence[Matrix], dimension: int, subspace: Sequence[int]
) -> None:
    radical = radical_of_subspace(matrices, dimension, subspace)
    cosets = xor_cosets(subspace, radical)
    assert len(cosets) == 4
    nonzero_cosets = [coset for coset in cosets if 0 not in coset]
    assert len(nonzero_cosets) == 3
    representatives = [min(coset) for coset in nonzero_cosets]
    assert is_clique(matrices, dimension, representatives)

    # Each nonzero coset together with the radical is an abelian centralizer in
    # the child.  The three such sets give primal cost 3, while one unit on each
    # nonzero coset gives the matching dual cost 3.
    for representative, coset in zip(representatives, nonzero_cosets):
        child_centralizer = centralizer_set(
            matrices, dimension, representative, universe=subspace
        )
        assert set(child_centralizer) == set(radical) | set(coset)
        assert is_isotropic(matrices, dimension, child_centralizer)


def check_primal_cover(
    universe: Iterable[int],
    weights: Mapping[Centralizer, Fraction],
    costs: Mapping[Centralizer, Fraction],
) -> Fraction:
    universe_tuple = tuple(universe)
    for value in universe_tuple:
        coverage = sum(weight for subset, weight in weights.items() if value in subset)
        assert coverage >= 1, (value, coverage)
    return sum(weights[subset] * costs[subset] for subset in weights)


def check_dual_packing(
    centralizers: Sequence[Centralizer],
    vector_weights: Mapping[int, Fraction],
    costs: Mapping[Centralizer, Fraction],
) -> Fraction:
    for subset in centralizers:
        mass = sum(vector_weights.get(value, Fraction(0)) for value in subset)
        assert mass <= costs[subset], (subset, mass, costs[subset])
    return sum(vector_weights.values())


def certificate_weight_map(entries: Sequence[Mapping[str, object]]) -> Dict[Centralizer, Fraction]:
    result: Dict[Centralizer, Fraction] = {}
    for entry in entries:
        subset = tuple(int(value) for value in entry["set"])  # type: ignore[index]
        result[subset] = frac(entry["weight"])  # type: ignore[arg-type]
    return result


def certificate_vector_weights(entries: Sequence[Mapping[str, object]]) -> Dict[int, Fraction]:
    return {
        int(entry["vector"]): frac(entry["weight"])  # type: ignore[arg-type]
        for entry in entries
    }


def verify_fractional_abelian_cover(
    matrices: Sequence[Matrix],
    dimension: int,
    cover: Sequence[Sequence[int]],
    dual_clique: Sequence[int],
    expected: Fraction,
) -> None:
    universe = set(range(1 << dimension))
    cover_sets = [tuple(subset) for subset in cover]
    for subset in cover_sets:
        assert is_linear_subspace(subset)
        assert is_isotropic(matrices, dimension, subset)
    assert set().union(*(set(subset) for subset in cover_sets)) == universe
    assert is_clique(matrices, dimension, dual_clique)

    primal_value = Fraction(len(cover_sets))
    dual_value = Fraction(len(dual_clique))
    assert primal_value == dual_value == expected


def load_matrices(model: Mapping[str, object]) -> Tuple[Matrix, ...]:
    raw = model["alternating_matrices"]  # type: ignore[index]
    matrices: List[Matrix] = []
    for matrix in raw:  # type: ignore[assignment]
        rows = tuple(tuple(int(value) for value in row) for row in matrix)
        dimension = len(rows)
        assert all(len(row) == dimension for row in rows)
        assert all(rows[i][i] == 0 for i in range(dimension))
        assert all(rows[i][j] == rows[j][i] for i in range(dimension) for j in range(dimension))
        matrices.append(rows)
    return tuple(matrices)


def verify_scalar_model(model: Mapping[str, object]) -> None:
    dimension = int(model["dimension"])
    codomain_dimension = int(model["codomain_dimension"])
    matrices = load_matrices(model)
    order, center_order = verify_group_model(matrices, dimension, codomain_dimension)
    assert order == int(model["expected_group_order"])
    assert center_order == int(model["expected_center_order"])

    adjacency = adjacency_masks(matrices, dimension)
    maximum = maximum_clique(adjacency)
    expected_nu = int(model["expected_nu"])
    assert len(maximum) == expected_nu
    supplied_clique = tuple(int(value) for value in model["clique"])  # type: ignore[arg-type]
    assert len(supplied_clique) == expected_nu and is_clique(matrices, dimension, supplied_clique)

    centralizers = unique_centralizers(matrices, dimension)
    assert len(centralizers) == 15
    child_nus = {clique_number_on_codes(adjacency, subset) for subset in centralizers}
    assert child_nus == {int(model["expected_child_nu"])}
    for subset in centralizers:
        verify_k3_child(matrices, dimension, subset)

    universe = range(1 << dimension)
    tau_costs = {subset: Fraction(1) for subset in centralizers}
    tau_primal = {
        subset: frac(model["tau_primal_weight_all_nonzero"]) for subset in centralizers
    }
    tau_dual = {
        value: frac(model["tau_dual_weight_all_nonzero"])
        for value in range(1, 1 << dimension)
    }
    tau_primal_value = check_primal_cover(universe, tau_primal, tau_costs)
    tau_dual_value = check_dual_packing(centralizers, tau_dual, tau_costs)
    expected_tau = frac(model["expected_tau"])
    assert tau_primal_value == tau_dual_value == expected_tau

    kappa_costs = {subset: Fraction(1, 2) for subset in centralizers}
    kappa_primal = {
        subset: frac(model["kappa_primal_weight_all_nonzero"]) for subset in centralizers
    }
    kappa_dual = {
        value: frac(model["kappa_dual_weight_all_nonzero"])
        for value in range(1, 1 << dimension)
    }
    kappa_primal_value = check_primal_cover(universe, kappa_primal, kappa_costs)
    kappa_dual_value = check_dual_packing(centralizers, kappa_dual, kappa_costs)
    expected_kappa = frac(model["expected_kappa"])
    assert kappa_primal_value == kappa_dual_value == expected_kappa
    assert expected_kappa > 1

    child_dynamic = frac(model["child_dynamic_value"])
    dynamic_costs = {subset: child_dynamic for subset in centralizers}
    dynamic_primal_value = check_primal_cover(universe, tau_primal, dynamic_costs)
    dynamic_dual = {
        value: frac(model["dynamic_dual_weight_all_nonzero"])
        for value in range(1, 1 << dimension)
    }
    dynamic_dual_value = check_dual_packing(centralizers, dynamic_dual, dynamic_costs)
    expected_dynamic = frac(model["expected_dynamic_value"])
    assert dynamic_primal_value == dynamic_dual_value == expected_dynamic

    spread = model["spread"]  # type: ignore[assignment]
    verify_fractional_abelian_cover(
        matrices,
        dimension,
        spread,  # type: ignore[arg-type]
        supplied_clique,
        frac(model["expected_fractional_abelian_cover"]),
    )

    print(
        "[OK] scalar_symplectic_d2:",
        f"|G|={order}, |Z|={center_order}, nu={expected_nu},",
        f"tau={expected_tau}, kappa={expected_kappa}, R={expected_dynamic}",
    )


def verify_mixed_model(model: Mapping[str, object]) -> None:
    dimension = int(model["dimension"])
    codomain_dimension = int(model["codomain_dimension"])
    matrices = load_matrices(model)
    order, center_order = verify_group_model(matrices, dimension, codomain_dimension)
    assert order == int(model["expected_group_order"])
    assert center_order == int(model["expected_center_order"])

    adjacency = adjacency_masks(matrices, dimension)
    maximum = maximum_clique(adjacency)
    expected_nu = int(model["expected_nu"])
    assert len(maximum) == expected_nu
    supplied_clique = tuple(int(value) for value in model["clique"])  # type: ignore[arg-type]
    assert len(supplied_clique) == expected_nu and is_clique(matrices, dimension, supplied_clique)

    centralizers = unique_centralizers(matrices, dimension)
    expected_nonabelian = {
        tuple(int(value) for value in subset)
        for subset in model["centralizers_nonabelian"]  # type: ignore[assignment]
    }
    expected_abelian = {
        tuple(int(value) for value in subset)
        for subset in model["centralizers_abelian"]  # type: ignore[assignment]
    }
    assert set(centralizers) == expected_nonabelian | expected_abelian
    assert len(centralizers) == 9

    child_nu: Dict[Centralizer, int] = {
        subset: clique_number_on_codes(adjacency, subset) for subset in centralizers
    }
    assert {subset for subset, value in child_nu.items() if value == 3} == expected_nonabelian
    assert {subset for subset, value in child_nu.items() if value == 0} == expected_abelian
    for subset in expected_nonabelian:
        verify_k3_child(matrices, dimension, subset)
    for subset in expected_abelian:
        assert is_isotropic(matrices, dimension, subset)

    universe = range(1 << dimension)
    tau_costs = {subset: Fraction(1) for subset in centralizers}
    tau_primal = certificate_weight_map(model["tau_primal"])  # type: ignore[arg-type]
    tau_dual = certificate_vector_weights(model["tau_dual"])  # type: ignore[arg-type]
    tau_primal_value = check_primal_cover(universe, tau_primal, tau_costs)
    tau_dual_value = check_dual_packing(centralizers, tau_dual, tau_costs)
    expected_tau = frac(model["expected_tau"])
    assert tau_primal_value == tau_dual_value == expected_tau

    dynamic_costs = {
        subset: Fraction(3 if child_nu[subset] == 3 else 1) for subset in centralizers
    }
    dynamic_primal = certificate_weight_map(model["dynamic_primal"])  # type: ignore[arg-type]
    dynamic_dual = certificate_vector_weights(model["dynamic_dual"])  # type: ignore[arg-type]
    dynamic_primal_value = check_primal_cover(universe, dynamic_primal, dynamic_costs)
    dynamic_dual_value = check_dual_packing(centralizers, dynamic_dual, dynamic_costs)
    expected_dynamic = frac(model["expected_dynamic_value"])
    assert dynamic_primal_value == dynamic_dual_value == expected_dynamic

    # Exact kappa certificate.  Abelian children cost 2^{-3}=1/8.  The three
    # nonabelian children cost 2^{-3/2}=1/(2 sqrt(2)).  The dual puts 1/8 on six
    # vertices; each nonabelian centralizer contains only two of them, so its mass
    # is 1/4 <= 1/(2 sqrt(2)), verified exactly by squaring.
    kappa_primal = {subset: Fraction(1) for subset in expected_abelian}
    for value in universe:
        coverage = sum(weight for subset, weight in kappa_primal.items() if value in subset)
        assert coverage >= 1
    kappa_primal_value = Fraction(len(expected_abelian), 8)
    kappa_support = tuple(int(value) for value in model["kappa_dual_support"])  # type: ignore[arg-type]
    kappa_weight = frac(model["kappa_dual_weight"])
    for subset in centralizers:
        mass = sum(kappa_weight for value in kappa_support if value in subset)
        if subset in expected_abelian:
            assert mass <= Fraction(1, 8)
        else:
            assert mass * mass <= Fraction(1, 8)  # mass <= 1/(2 sqrt(2))
    kappa_dual_value = kappa_weight * len(kappa_support)
    expected_kappa = frac(model["expected_kappa"])
    assert kappa_primal_value == kappa_dual_value == expected_kappa

    maximal_isotropic = [
        tuple(int(value) for value in subset)
        for subset in model["maximal_isotropic_subspaces"]  # type: ignore[assignment]
    ]
    for subset in maximal_isotropic:
        assert is_linear_subspace(subset) and is_isotropic(matrices, dimension, subset)
    # Exhaustively enumerate all linear subspaces and confirm the supplied maximal list.
    all_subspaces = set()
    for generator_mask in range(1 << ((1 << dimension) - 1)):
        span = {0}
        for offset in range((1 << dimension) - 1):
            if (generator_mask >> offset) & 1:
                generator = offset + 1
                span |= {value ^ generator for value in tuple(span)}
        subset = tuple(sorted(span))
        if is_isotropic(matrices, dimension, subset):
            all_subspaces.add(subset)
    computed_maximal = {
        subset
        for subset in all_subspaces
        if not any(set(subset) < set(other) for other in all_subspaces)
    }
    assert computed_maximal == set(maximal_isotropic)

    abelian_cover = model["abelian_cover"]  # type: ignore[assignment]
    verify_fractional_abelian_cover(
        matrices,
        dimension,
        abelian_cover,  # type: ignore[arg-type]
        tuple(dynamic_dual.keys()),
        frac(model["expected_fractional_abelian_cover"]),
    )

    max_child = frac(model["expected_max_child_value"])
    path_majorant = expected_tau * max_child
    assert path_majorant == frac(model["expected_path_majorant"]) == 9
    assert expected_dynamic == 6 < 8 < path_majorant

    print(
        "[OK] mixed_order_64:",
        f"|G|={order}, |Z|={center_order}, nu={expected_nu},",
        f"tau={expected_tau}, R=a_f={expected_dynamic}, P={path_majorant}, kappa={expected_kappa}",
    )


def extension_adjacency(
    base_beta: Sequence[Sequence[int]],
    z_value: int,
    linear_values: Sequence[int],
    decoded: Sequence[Tuple[int, int, int]],
) -> List[int]:
    """Adjacency for the 6-dimensional projected one-pair extension."""
    vertex_count = 63
    adjacency = [0] * vertex_count
    for x in range(1, 64):
        a, alpha, beta_x = decoded[x]
        for y in range(x + 1, 64):
            b, gamma, beta_y = decoded[y]
            pairing = base_beta[a][b]
            if (alpha & beta_y) ^ (beta_x & gamma):
                pairing ^= z_value
            if beta_x:
                pairing ^= linear_values[b]
            if beta_y:
                pairing ^= linear_values[a]
            if pairing:
                adjacency[x - 1] |= 1 << (y - 1)
                adjacency[y - 1] |= 1 << (x - 1)
    return adjacency


def all_linear_value_tables() -> Tuple[Tuple[int, ...], ...]:
    tables: List[Tuple[int, ...]] = []
    for linear_map_code in range(1 << 12):
        images = tuple((linear_map_code >> (3 * i)) & 7 for i in range(4))
        values: List[int] = []
        for a in range(16):
            value = 0
            for i, image in enumerate(images):
                if (a >> i) & 1:
                    value ^= image
            values.append(value)
        tables.append(tuple(values))
    return tuple(tables)

def find_clique_of_size(adjacency: Sequence[int], target: int) -> Tuple[int, ...] | None:
    """Exact target-clique search, stopping immediately after a witness is found."""
    vertex_count = len(adjacency)

    def color_sort(candidates: int) -> Tuple[List[int], List[int]]:
        order: List[int] = []
        bounds: List[int] = []
        color = 0
        remaining = candidates
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= remaining
                available &= ~adjacency[vertex]
        return order, bounds

    def search(chosen: Tuple[int, ...], candidates: int) -> Tuple[int, ...] | None:
        if len(chosen) >= target:
            return chosen[:target]
        if popcount(candidates) < target - len(chosen):
            return None
        order, bounds = color_sort(candidates)
        for index in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[index] < target:
                return None
            vertex = order[index]
            bit = 1 << vertex
            if candidates & bit:
                result = search(chosen + (vertex,), candidates & adjacency[vertex])
                if result is not None:
                    return result
                candidates ^= bit
        return None

    result = search((), (1 << vertex_count) - 1)
    if result is None:
        return None
    return tuple(vertex + 1 for vertex in result)


def verify_extension_search(
    extension: Mapping[str, object], base_model: Mapping[str, object]
) -> str:
    base_matrices = load_matrices(base_model)
    required = int(extension["required_clique_size"])
    base_beta = [
        [beta(base_matrices, a, b, 4) for b in range(16)]
        for a in range(16)
    ]
    decoded = tuple(
        (code & 15, (code >> 4) & 1, (code >> 5) & 1)
        for code in range(64)
    )
    linear_tables = all_linear_value_tables()
    digest = hashlib.sha256()
    count = 0
    for z_value in extension["z_values"]:  # type: ignore[assignment]
        z = int(z_value)
        for code in range(int(extension["linear_map_codes_per_z"])):
            adjacency = extension_adjacency(base_beta, z, linear_tables[code], decoded)
            clique = find_clique_of_size(adjacency, required)
            assert clique is not None, (z, code)
            for left, right in itertools.combinations(clique, 2):
                assert adjacency[left - 1] & (1 << (right - 1))
            digest.update(bytes([z]))
            digest.update(code.to_bytes(2, "little"))
            digest.update(bytes(clique))
            count += 1
    assert count == int(extension["total_cases"])
    hexdigest = digest.hexdigest()
    expected_digest = extension.get("witness_digest_sha256")
    if expected_digest is not None:
        assert hexdigest == expected_digest
    print(
        "[OK] one-pair extension census:",
        f"{count} / {count} cases contain a {required}-clique, digest={hexdigest}",
    )
    return hexdigest



# ---------- Binary chain-ring Heisenberg family ----------

def ring_mul_binary(left: int, right: int, length: int) -> int:
    """Multiply in F_2[pi]/(pi^length), using low-to-high coefficient bits."""
    mask = (1 << length) - 1
    result = 0
    for shift in range(length):
        if (left >> shift) & 1:
            result ^= right << shift
    return result & mask


def ring_det_binary(
    left: Tuple[int, int], right: Tuple[int, int], length: int
) -> int:
    # Characteristic two turns subtraction into xor.
    return ring_mul_binary(left[0], right[1], length) ^ ring_mul_binary(
        right[0], left[1], length
    )


def ring_scale_binary(
    scalar: int, vector: Tuple[int, int], length: int
) -> Tuple[int, int]:
    return (
        ring_mul_binary(scalar, vector[0], length),
        ring_mul_binary(scalar, vector[1], length),
    )


def matrix_xor(
    left: Sequence[Sequence[int]], right: Sequence[Sequence[int]]
) -> List[List[int]]:
    return [
        [(int(a) ^ int(b)) & 1 for a, b in zip(row_left, row_right)]
        for row_left, row_right in zip(left, right)
    ]


def matrix_transpose(matrix: Sequence[Sequence[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*matrix)]


def matrix_multiply_mod2(
    left: Sequence[Sequence[int]], right: Sequence[Sequence[int]]
) -> List[List[int]]:
    right_t = matrix_transpose(right)
    return [
        [
            sum((int(a) & int(b)) for a, b in zip(row, column)) & 1
            for column in right_t
        ]
        for row in left
    ]


def matrix_congruence_mod2(
    form: Sequence[Sequence[int]], basis: Sequence[Sequence[int]]
) -> List[List[int]]:
    return matrix_multiply_mod2(
        matrix_multiply_mod2(matrix_transpose(basis), form), basis
    )


def verify_chain_ring_family(
    family: Mapping[str, object], mixed_model: Mapping[str, object]
) -> None:
    lengths = tuple(int(value) for value in family["verified_lengths"])  # type: ignore[index]
    for length in lengths:
        ring_size = 1 << length
        ideal = tuple(value for value in range(ring_size) if (value & 1) == 0)
        nonzero_vectors = tuple(
            (x, y)
            for x in range(ring_size)
            for y in range(ring_size)
            if x or y
        )

        first_representatives = tuple((1, a) for a in range(ring_size))
        second_representatives = tuple((b, 1) for b in ideal)
        clique = first_representatives + second_representatives
        expected = 3 * (1 << (length - 1))
        assert len(clique) == expected
        assert len(set(clique)) == expected
        for left, right in itertools.combinations(clique, 2):
            assert ring_det_binary(left, right, length) != 0

        lines: List[frozenset[Tuple[int, int]]] = []
        for generator in clique:
            line = frozenset(
                ring_scale_binary(scalar, generator, length)
                for scalar in range(ring_size)
            )
            assert len(line) == ring_size
            for left, right in itertools.combinations(line, 2):
                assert ring_det_binary(left, right, length) == 0
            lines.append(line)
        assert len(set(lines)) == expected
        covered = set().union(*lines)
        assert len(covered) == ring_size * ring_size

        deepest = 1 << (length - 1)
        primal_directions = ((deepest, 0), (0, deepest), (deepest, deepest))
        centralizers = [
            frozenset(
                vector
                for vector in ((x, y) for x in range(ring_size) for y in range(ring_size))
                if ring_det_binary(direction, vector, length) == 0
            )
            for direction in primal_directions
        ]
        assert set().union(*centralizers) == set(
            (x, y) for x in range(ring_size) for y in range(ring_size)
        )

        dual_support = ((1, 0), (0, 1), (1, 1))
        for vector in nonzero_vectors:
            incidence = sum(
                ring_det_binary(vector, support, length) == 0
                for support in dual_support
            )
            assert incidence <= 1

        # A valuation-k element has compressed centralizer model R_k^2.
        for child_length in range(length):
            x_vector = (1 << child_length, 0)
            centralizer = tuple(
                vector
                for vector in ((a, b) for a in range(ring_size) for b in range(ring_size))
                if ring_det_binary(x_vector, vector, length) == 0
            )
            expected_size = 1 << (length + child_length)
            assert len(centralizer) == expected_size
            child_mask = (1 << child_length) - 1
            shift = length - child_length

            def child_image(vector: Tuple[int, int]) -> Tuple[int, int]:
                a, b = vector
                if child_length == 0:
                    return (0, 0)
                assert b & ((1 << shift) - 1) == 0
                return (a & child_mask, (b >> shift) & child_mask)

            for left in centralizer:
                for right in centralizer:
                    original_zero = ring_det_binary(left, right, length) == 0
                    if child_length == 0:
                        child_zero = True
                    else:
                        child_zero = (
                            ring_det_binary(
                                child_image(left), child_image(right), child_length
                            )
                            == 0
                        )
                    assert original_zero == child_zero

        assert 3**length >= expected

    canonical = family["canonical_dual_number_forms"]  # type: ignore[index]
    b0 = [[int(value) for value in row] for row in canonical["B0"]]  # type: ignore[index]
    b1 = [[int(value) for value in row] for row in canonical["B1"]]  # type: ignore[index]
    basis = [
        [int(value) for value in row]
        for row in family["domain_basis_change_P"]  # type: ignore[index]
    ]
    mixed_matrices = load_matrices(mixed_model)
    transformed_b1 = matrix_congruence_mod2(b1, basis)
    transformed_sum = matrix_congruence_mod2(matrix_xor(b0, b1), basis)
    assert tuple(tuple(row) for row in transformed_b1) == mixed_matrices[0]
    assert tuple(tuple(row) for row in transformed_sum) == mixed_matrices[1]

    print(
        "[OK] binary chain-ring Heisenberg family:",
        f"m={lengths[0]}..{lengths[-1]}, nu=R=a_f=3*2^(m-1), tau=3, P=3^m",
    )

def main() -> None:
    with CERT_PATH.open("r", encoding="utf-8") as handle:
        certificate = json.load(handle)
    models = certificate["models"]
    verify_scalar_model(models["scalar_symplectic_d2"])
    verify_mixed_model(models["mixed_order_64"])
    verify_chain_ring_family(certificate["chain_ring_family"], models["mixed_order_64"])
    verify_extension_search(certificate["extension_search"], models["mixed_order_64"])
    print("[OK] all exact certificates verified with the Python standard library only")


if __name__ == "__main__":
    main()
