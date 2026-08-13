"""Exact noncommuting-graph and abelian-cover algorithms for small groups."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from finite_groups import FiniteGroup


def _bits(mask: int) -> Iterable[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def _popcount(mask: int) -> int:
    """Python 3.9-compatible population count."""

    return bin(mask).count("1")


@dataclass(frozen=True)
class CompressedNoncommutingGraph:
    """The noncommuting graph compressed along cosets of the center."""

    cosets: Tuple[Tuple[int, ...], ...]
    adjacency: Tuple[int, ...]

    @property
    def order(self) -> int:
        return len(self.cosets)

    def adjacent(self, x: int, y: int) -> bool:
        return bool(self.adjacency[x] & (1 << y))

    def validate(self) -> None:
        n = self.order
        if len(self.adjacency) != n:
            raise ValueError("wrong adjacency length")
        all_vertices = (1 << n) - 1
        for x, neighbors in enumerate(self.adjacency):
            if neighbors & ~all_vertices:
                raise ValueError("neighbor index out of range")
            if neighbors & (1 << x):
                raise ValueError("graph has a loop")
            for y in _bits(neighbors):
                if not self.adjacency[y] & (1 << x):
                    raise ValueError("adjacency is not symmetric")


def graph_or_product(left: Sequence[int], right: Sequence[int]) -> Tuple[int, ...]:
    """Return the disjunctive/OR product, on lexicographically paired vertices.

    Vertices ``(i,j)`` and ``(k,l)`` are adjacent exactly when ``i~k`` in the
    left graph OR ``j~l`` in the right graph.  This is the compressed
    noncommuting graph operation for direct products of groups.
    """

    n, m = len(left), len(right)
    adjacency = [0] * (n * m)
    for i in range(n):
        for j in range(m):
            vertex = i * m + j
            neighbors = 0
            for k in range(n):
                for ell in range(m):
                    target = k * m + ell
                    if target != vertex and ((left[i] & (1 << k)) or (right[j] & (1 << ell))):
                        neighbors |= 1 << target
            adjacency[vertex] = neighbors
    return tuple(adjacency)


def compressed_noncommuting_graph(group: FiniteGroup) -> CompressedNoncommutingGraph:
    """Construct and exhaustively check the central-coset compression.

    The check deliberately does not assume commutation descends to G/Z(G): for
    every pair of cosets it verifies that *all* element pairs have the same
    commutation truth value.  It also verifies that each individual coset is a
    commuting set.
    """

    cosets = group.center_cosets()
    n = len(cosets)
    adjacency = [0] * n
    for i, left in enumerate(cosets):
        if not group.is_abelian_subset(left):
            raise AssertionError("a center coset is not internally commuting")
        for j in range(i + 1, n):
            right = cosets[j]
            relations = {group.commute(x, y) for x in left for y in right}
            if len(relations) != 1:
                raise AssertionError("commutation is not invariant on the selected cosets")
            if not next(iter(relations)):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    graph = CompressedNoncommutingGraph(cosets, tuple(adjacency))
    graph.validate()
    return graph


@dataclass(frozen=True)
class CliqueResult:
    vertices: Tuple[int, ...]
    search_nodes: int

    @property
    def size(self) -> int:
        return len(self.vertices)


def maximum_clique(adjacency: Sequence[int]) -> CliqueResult:
    """Exact maximum clique by branch-and-bound with greedy-color bounds."""

    n = len(adjacency)
    all_vertices = (1 << n) - 1
    # A deterministic greedy clique gives the search a useful initial bound.
    seed_candidates = all_vertices
    best: List[int] = []
    while seed_candidates:
        vertex = max(
            _bits(seed_candidates),
            key=lambda x: (_popcount(seed_candidates & adjacency[x]), -x),
        )
        best.append(vertex)
        seed_candidates &= adjacency[vertex]
    nodes = 0

    def color_sort(candidates: int) -> Tuple[List[int], List[int]]:
        """Greedily color G[candidates], returning nondecreasing bounds."""

        order: List[int] = []
        bounds: List[int] = []
        remaining = candidates
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                vertex = max(
                    _bits(available),
                    key=lambda x: (_popcount(available & adjacency[x]), -x),
                )
                bit = 1 << vertex
                order.append(vertex)
                bounds.append(color)
                remaining &= ~bit
                available &= ~bit
                # Vertices in one greedy color class form an independent set.
                available &= ~adjacency[vertex]
        return order, bounds

    def search(clique: List[int], candidates: int) -> None:
        nonlocal best, nodes
        nodes += 1
        order, bounds = color_sort(candidates)
        while order:
            vertex = order.pop()
            bound = bounds.pop()
            if len(clique) + bound <= len(best):
                return
            bit = 1 << vertex
            extension = candidates & adjacency[vertex]
            if extension:
                search(clique + [vertex], extension)
            elif len(clique) + 1 > len(best):
                best = clique + [vertex]
            candidates &= ~bit

    search([], all_vertices)
    return CliqueResult(tuple(best), nodes)


def verify_clique(adjacency: Sequence[int], vertices: Sequence[int]) -> bool:
    return len(set(vertices)) == len(vertices) and all(
        adjacency[x] & (1 << y) for i, x in enumerate(vertices) for y in vertices[i + 1 :]
    )


@dataclass(frozen=True)
class ColoringResult:
    colors: Tuple[int, ...]
    search_nodes_by_k: Tuple[Tuple[int, int], ...]

    @property
    def size(self) -> int:
        return max(self.colors, default=-1) + 1


def _greedy_dsatur(adjacency: Sequence[int]) -> Tuple[int, ...]:
    n = len(adjacency)
    colors = [-1] * n
    for _ in range(n):
        uncolored = [v for v in range(n) if colors[v] < 0]
        vertex = max(
            uncolored,
            key=lambda v: (
                len({colors[u] for u in _bits(adjacency[v]) if colors[u] >= 0}),
                _popcount(adjacency[v]),
                -v,
            ),
        )
        forbidden = {colors[u] for u in _bits(adjacency[vertex]) if colors[u] >= 0}
        color = 0
        while color in forbidden:
            color += 1
        colors[vertex] = color
    return tuple(colors)


def _k_coloring(adjacency: Sequence[int], k: int) -> Tuple[Optional[Tuple[int, ...]], int]:
    n = len(adjacency)
    colors = [-1] * n
    nodes = 0

    def search(colored_count: int, used_count: int) -> bool:
        nonlocal nodes
        nodes += 1
        if colored_count == n:
            return True
        uncolored = [v for v in range(n) if colors[v] < 0]
        vertex = max(
            uncolored,
            key=lambda v: (
                len({colors[u] for u in _bits(adjacency[v]) if colors[u] >= 0}),
                _popcount(adjacency[v]),
                -v,
            ),
        )
        forbidden_mask = 0
        for neighbor in _bits(adjacency[vertex]):
            color = colors[neighbor]
            if color >= 0:
                forbidden_mask |= 1 << color

        # Existing colors are tried first.  All unused color names are
        # symmetric, so at most the first unused one needs to be considered.
        upper = min(k, used_count + 1)
        for color in range(upper):
            if forbidden_mask & (1 << color):
                continue
            colors[vertex] = color
            if search(colored_count + 1, max(used_count, color + 1)):
                return True
            colors[vertex] = -1
        return False

    found = search(0, 0)
    return (tuple(colors) if found else None), nodes


def exact_chromatic_number(adjacency: Sequence[int], clique_lower_bound: int = 0) -> ColoringResult:
    """Return an optimal coloring and exhaustive failed-search counts."""

    n = len(adjacency)
    if n == 0:
        return ColoringResult((), ())
    greedy = _greedy_dsatur(adjacency)
    upper = max(greedy) + 1
    lower = max(1, clique_lower_bound)
    searches = []
    for k in range(lower, upper):
        coloring, nodes = _k_coloring(adjacency, k)
        searches.append((k, nodes))
        if coloring is not None:
            return ColoringResult(coloring, tuple(searches))
    searches.append((upper, 0))
    return ColoringResult(greedy, tuple(searches))


def verify_coloring(adjacency: Sequence[int], colors: Sequence[int]) -> bool:
    return len(adjacency) == len(colors) and all(
        colors[x] != colors[y] for x, neighbors in enumerate(adjacency) for y in _bits(neighbors) if x < y
    )


def abelian_subgroups_from_coloring(
    group: FiniteGroup,
    graph: CompressedNoncommutingGraph,
    colors: Sequence[int],
) -> Tuple[Tuple[int, ...], ...]:
    """Generate one certified abelian subgroup from each graph color class."""

    if not verify_coloring(graph.adjacency, colors):
        raise ValueError("invalid coloring")
    subgroups = []
    for color in range(max(colors, default=-1) + 1):
        generators = [element for vertex, coset in enumerate(graph.cosets) if colors[vertex] == color for element in coset]
        subgroup = group.generated_subgroup(generators)
        if not group.is_abelian_subset(subgroup):
            raise AssertionError("color class did not generate an abelian subgroup")
        subgroups.append(subgroup)
    if set().union(*(set(x) for x in subgroups)) != set(range(group.order)):
        raise AssertionError("subgroups from coloring do not cover the group")
    return tuple(subgroups)


@dataclass(frozen=True)
class SetCoverResult:
    subgroups: Tuple[Tuple[int, ...], ...]
    candidate_count: int
    search_nodes: int

    @property
    def size(self) -> int:
        return len(self.subgroups)


def exact_abelian_subgroup_cover(group: FiniteGroup) -> SetCoverResult:
    """Independently minimize over all maximal abelian subgroups."""

    abelian = [frozenset(h) for h in group.all_subgroups() if group.is_abelian_subset(h)]
    maximal = sorted(
        (h for h in abelian if not any(h < other for other in abelian)),
        key=lambda h: (-len(h), tuple(sorted(h))),
    )
    masks = [sum(1 << x for x in subgroup) for subgroup in maximal]
    universe = (1 << group.order) - 1
    containing: List[List[int]] = [[] for _ in range(group.order)]
    for index, mask in enumerate(masks):
        for element in _bits(mask):
            containing[element].append(index)

    # A deterministic greedy cover supplies an initial finite upper bound.
    uncovered = universe
    greedy: List[int] = []
    while uncovered:
        candidate = max(range(len(masks)), key=lambda i: _popcount(masks[i] & uncovered))
        gain = masks[candidate] & uncovered
        if not gain:
            raise AssertionError("maximal abelian subgroups do not cover the group")
        greedy.append(candidate)
        uncovered &= ~masks[candidate]

    best = greedy[:]
    nodes = 0

    seen_depth: Dict[int, int] = {}

    def search(uncovered_mask: int, chosen: List[int]) -> None:
        nonlocal best, nodes
        nodes += 1
        if not uncovered_mask:
            if len(chosen) < len(best):
                best = chosen[:]
            return
        if len(chosen) >= len(best):
            return
        previous_depth = seen_depth.get(uncovered_mask)
        if previous_depth is not None and previous_depth <= len(chosen):
            return
        seen_depth[uncovered_mask] = len(chosen)
        max_gain = max(_popcount(mask & uncovered_mask) for mask in masks)
        if max_gain == 0:
            return
        lower = (_popcount(uncovered_mask) + max_gain - 1) // max_gain
        if len(chosen) + lower >= len(best):
            return

        uncovered_elements = tuple(_bits(uncovered_mask))
        element = min(
            uncovered_elements,
            key=lambda x: sum(1 for i in containing[x] if i not in chosen),
        )
        options = [i for i in containing[element] if i not in chosen]
        options.sort(key=lambda i: (-_popcount(masks[i] & uncovered_mask), i))
        for candidate in options:
            search(uncovered_mask & ~masks[candidate], chosen + [candidate])

    search(universe, [])

    chosen_subgroups = tuple(tuple(sorted(maximal[i])) for i in best)
    return SetCoverResult(chosen_subgroups, len(maximal), nodes)


def verify_abelian_cover(group: FiniteGroup, subgroups: Sequence[Sequence[int]]) -> bool:
    return (
        all(group.is_subgroup(h) and group.is_abelian_subset(h) for h in subgroups)
        and set().union(*(set(h) for h in subgroups)) == set(range(group.order))
    )


def commuting_probability(group: FiniteGroup) -> Fraction:
    commuting_pairs = sum(group.commute(x, y) for x in range(group.order) for y in range(group.order))
    return Fraction(commuting_pairs, group.order * group.order)


def color_classes(colors: Sequence[int]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(
        tuple(vertex for vertex, assigned in enumerate(colors) if assigned == color)
        for color in range(max(colors, default=-1) + 1)
    )


def analyze_group(group: FiniteGroup, independent_cover: bool = True) -> Dict[str, object]:
    """Compute exact invariants and serializable certificates for one group."""

    group.validate()
    graph = compressed_noncommuting_graph(group)
    clique = maximum_clique(graph.adjacency)
    if not verify_clique(graph.adjacency, clique.vertices):
        raise AssertionError("internal clique certificate failure")
    coloring = exact_chromatic_number(graph.adjacency, clique.size)
    if not verify_coloring(graph.adjacency, coloring.colors):
        raise AssertionError("internal coloring certificate failure")
    color_cover = abelian_subgroups_from_coloring(group, graph, coloring.colors)
    independent = exact_abelian_subgroup_cover(group) if independent_cover else None
    if independent is not None:
        if not verify_abelian_cover(group, independent.subgroups):
            raise AssertionError("internal subgroup-cover certificate failure")
        if independent.size != coloring.size:
            raise AssertionError("independent set cover and coloring disagree")

    labels = group.elements
    return {
        "group_id": group.group_id,
        "order": group.order,
        "elements": list(labels),
        "multiplication_table": [list(row) for row in group.table],
        "center": [labels[x] for x in group.center()],
        "central_cosets": [[labels[x] for x in coset] for coset in graph.cosets],
        "compressed_adjacency": [list(_bits(mask)) for mask in graph.adjacency],
        "nu": clique.size,
        "a": coloring.size,
        "commuting_probability": str(commuting_probability(group)),
        "clique_certificate": {
            "coset_vertices": list(clique.vertices),
            "representatives": [labels[graph.cosets[v][0]] for v in clique.vertices],
            "search_nodes": clique.search_nodes,
        },
        "coloring_certificate": {
            "colors_by_coset": list(coloring.colors),
            "color_classes": [list(x) for x in color_classes(coloring.colors)],
            "generated_abelian_subgroups": [[labels[x] for x in h] for h in color_cover],
            "search_nodes_by_k": [list(x) for x in coloring.search_nodes_by_k],
        },
        "independent_abelian_cover_certificate": None
        if independent is None
        else {
            "maximal_abelian_candidate_count": independent.candidate_count,
            "search_nodes": independent.search_nodes,
            "subgroups": [[labels[x] for x in h] for h in independent.subgroups],
        },
    }
