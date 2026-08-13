"""Independent regression checks for the exact finite-group computation."""

from __future__ import annotations

import itertools
import hashlib
import json
import csv
import sys
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY / "src" / "python"))

from exact_invariants import (  # noqa: E402
    abelian_subgroups_from_coloring,
    compressed_noncommuting_graph,
    exact_abelian_subgroup_cover,
    exact_chromatic_number,
    graph_or_product,
    maximum_clique,
    verify_abelian_cover,
    verify_clique,
    verify_coloring,
)
from finite_groups import (  # noqa: E402
    FiniteGroup,
    cyclic_group,
    dihedral_group,
    direct_product,
    extraspecial_prime_group,
    extraspecial_two_group,
    quaternion_group,
    symmetric_group,
)
from scalar_symplectic import (  # noqa: E402
    fixed_size_clique,
    multiplication_table_sha256,
    projective_symplectic_graph,
    scalar_symplectic_adjacency,
    symplectic_spread,
)


def brute_force_clique(adjacency):
    n = len(adjacency)
    for size in range(n, -1, -1):
        for vertices in itertools.combinations(range(n), size):
            if verify_clique(adjacency, vertices):
                return vertices
    raise AssertionError("empty set should always be a clique")


def brute_force_coloring(adjacency):
    n = len(adjacency)
    if n == 0:
        return ()
    for k in range(1, n + 1):
        colors = [-1] * n

        def search(vertex):
            if vertex == n:
                return tuple(colors)
            for color in range(k):
                if all(colors[u] != color for u in range(vertex) if adjacency[vertex] & (1 << u)):
                    colors[vertex] = color
                    result = search(vertex + 1)
                    if result is not None:
                        return result
            colors[vertex] = -1
            return None

        result = search(0)
        if result is not None:
            return result
    raise AssertionError("every finite graph is n-colorable")


class GroupConstructionTests(unittest.TestCase):
    def test_group_axioms_and_basic_centers(self):
        cases = [
            (cyclic_group(1), 1),
            (cyclic_group(5), 5),
            (symmetric_group(3), 1),
            (dihedral_group(4), 2),
            (quaternion_group(), 2),
        ]
        for group, expected_center in cases:
            with self.subTest(group=group.group_id):
                group.validate()
                self.assertEqual(expected_center, len(group.center()))

    def test_center_cosets_partition_and_commutation_invariance(self):
        for group in [symmetric_group(3), dihedral_group(4), quaternion_group(), extraspecial_two_group(2)]:
            with self.subTest(group=group.group_id):
                cosets = group.center_cosets()
                self.assertEqual(set(range(group.order)), set().union(*(set(coset) for coset in cosets)))
                self.assertEqual(group.order, sum(map(len, cosets)))
                for left in cosets:
                    self.assertTrue(group.is_abelian_subset(left))
                    for right in cosets:
                        relations = {group.commute(x, y) for x in left for y in right}
                        self.assertEqual(1, len(relations))


class ExactGraphTests(unittest.TestCase):
    def test_algorithms_against_brute_force_all_graphs_through_six_vertices(self):
        # Up to six vertices there are 2^15=32768 labeled simple graphs.  This
        # exhaustive test is an independent small-instance check of both exact
        # optimizers and catches subtle pruning errors.
        for n in range(7):
            edges = list(itertools.combinations(range(n), 2))
            for edge_mask in range(1 << len(edges)):
                adjacency = [0] * n
                for bit, (x, y) in enumerate(edges):
                    if edge_mask & (1 << bit):
                        adjacency[x] |= 1 << y
                        adjacency[y] |= 1 << x
                exact_clique = maximum_clique(adjacency)
                brute_clique = brute_force_clique(adjacency)
                self.assertEqual(len(brute_clique), exact_clique.size)
                self.assertTrue(verify_clique(adjacency, exact_clique.vertices))
                exact_coloring = exact_chromatic_number(adjacency, exact_clique.size)
                brute_coloring = brute_force_coloring(adjacency)
                self.assertEqual(max(brute_coloring, default=-1) + 1, exact_coloring.size)
                self.assertTrue(verify_coloring(adjacency, exact_coloring.colors))

    def test_named_group_invariants_and_independent_covers(self):
        cases = [
            (cyclic_group(1), (1, 1)),
            (cyclic_group(5), (1, 1)),
            (symmetric_group(3), (4, 4)),
            (dihedral_group(4), (3, 3)),
            (quaternion_group(), (3, 3)),
        ]
        for group, expected in cases:
            with self.subTest(group=group.group_id):
                graph = compressed_noncommuting_graph(group)
                clique = maximum_clique(graph.adjacency)
                coloring = exact_chromatic_number(graph.adjacency, clique.size)
                self.assertEqual(expected, (clique.size, coloring.size))
                generated_cover = abelian_subgroups_from_coloring(group, graph, coloring.colors)
                self.assertTrue(verify_abelian_cover(group, generated_cover))
                independent = exact_abelian_subgroup_cover(group)
                self.assertEqual(coloring.size, independent.size)
                self.assertTrue(verify_abelian_cover(group, independent.subgroups))

    def test_direct_product_is_graph_or_product(self):
        pairs = [
            (dihedral_group(4), symmetric_group(3)),
            (quaternion_group(), cyclic_group(2)),
        ]
        for left, right in pairs:
            with self.subTest(left=left.group_id, right=right.group_id):
                direct = compressed_noncommuting_graph(direct_product(left, right))
                left_graph = compressed_noncommuting_graph(left)
                right_graph = compressed_noncommuting_graph(right)
                expected_cosets = tuple(
                    tuple(sorted(x * right.order + y for x in left_coset for y in right_coset))
                    for left_coset in left_graph.cosets
                    for right_coset in right_graph.cosets
                )
                # Match each product coset to the corresponding lexicographic
                # pair, independent of the constructor's coset enumeration.
                direct_index = {frozenset(coset): i for i, coset in enumerate(direct.cosets)}
                product_graph = graph_or_product(left_graph.adjacency, right_graph.adjacency)
                for source, coset in enumerate(expected_cosets):
                    i = direct_index[frozenset(coset)]
                    for target, other in enumerate(expected_cosets):
                        j = direct_index[frozenset(other)]
                        self.assertEqual(
                            bool(product_graph[source] & (1 << target)),
                            bool(direct.adjacency[i] & (1 << j)),
                        )

    def test_or_product_multiplicativity_fails_for_general_graphs(self):
        cycle = tuple((1 << ((i - 1) % 5)) | (1 << ((i + 1) % 5)) for i in range(5))
        product = graph_or_product(cycle, cycle)
        cycle_clique = maximum_clique(cycle)
        cycle_coloring = exact_chromatic_number(cycle, cycle_clique.size)
        product_clique = maximum_clique(product)
        product_coloring = exact_chromatic_number(product, product_clique.size)
        self.assertEqual((2, 3), (cycle_clique.size, cycle_coloring.size))
        self.assertEqual((5, 8), (product_clique.size, product_coloring.size))
        self.assertGreater(product_clique.size, cycle_clique.size ** 2)
        self.assertLess(product_coloring.size, cycle_coloring.size ** 2)
        self.assertTrue(verify_clique(product, product_clique.vertices))
        self.assertTrue(verify_coloring(product, product_coloring.colors))


class ExtraspecialGeometryTests(unittest.TestCase):
    @staticmethod
    def quotient_vector(label):
        # label format is (aaa;bbb;c); the central coordinate is discarded.
        left, right, _ = label.strip("()").split(";")
        return tuple(map(int, left + right))

    @staticmethod
    def symplectic(x, y):
        m = len(x) // 2
        return sum(x[i] * y[m + i] + y[i] * x[m + i] for i in range(m)) % 2

    def test_symplectic_adjacency_and_exact_m_1_to_3(self):
        expected = {1: (3, 3), 2: (5, 5), 3: (7, 9)}
        for m in range(1, 4):
            with self.subTest(rank=m):
                group = extraspecial_two_group(m)
                group.validate()
                graph = compressed_noncommuting_graph(group)
                vectors = [self.quotient_vector(group.elements[coset[0]]) for coset in graph.cosets]
                self.assertEqual(1 << (2 * m), len(vectors))
                for i, x in enumerate(vectors):
                    for j, y in enumerate(vectors):
                        self.assertEqual(
                            self.symplectic(x, y) == 1,
                            bool(graph.adjacency[i] & (1 << j)),
                        )
                clique = maximum_clique(graph.adjacency)
                coloring = exact_chromatic_number(graph.adjacency, clique.size)
                self.assertEqual(expected[m], (clique.size, coloring.size))
                self.assertTrue(verify_clique(graph.adjacency, clique.vertices))
                self.assertTrue(verify_coloring(graph.adjacency, coloring.colors))


class LogCertificateTests(unittest.TestCase):
    def test_exact_small_group_log_is_self_consistent(self):
        log_path = REPOSITORY / "experiments" / "logs" / "exact_small_groups.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        for record in document["records"]:
            with self.subTest(group=record["group_id"]):
                group = FiniteGroup(
                    record["group_id"],
                    tuple(record["elements"]),
                    tuple(tuple(row) for row in record["multiplication_table"]),
                )
                group.validate()
                graph = compressed_noncommuting_graph(group)
                logged_adjacency = tuple(
                    sum(1 << neighbor for neighbor in neighbors)
                    for neighbors in record["compressed_adjacency"]
                )
                self.assertEqual(graph.adjacency, logged_adjacency)
                clique_vertices = tuple(record["clique_certificate"]["coset_vertices"])
                colors = tuple(record["coloring_certificate"]["colors_by_coset"])
                self.assertTrue(verify_clique(logged_adjacency, clique_vertices))
                self.assertTrue(verify_coloring(logged_adjacency, colors))
                exact_clique = maximum_clique(logged_adjacency)
                exact_coloring = exact_chromatic_number(logged_adjacency, exact_clique.size)
                self.assertEqual(record["nu"], exact_clique.size)
                self.assertEqual(record["a"], exact_coloring.size)
                index = group.index
                generated_cover = tuple(
                    tuple(index[label] for label in subgroup)
                    for subgroup in record["coloring_certificate"]["generated_abelian_subgroups"]
                )
                self.assertTrue(verify_abelian_cover(group, generated_cover))
                independent = record["independent_abelian_cover_certificate"]
                if independent is not None:
                    cover = tuple(
                        tuple(index[label] for label in subgroup)
                        for subgroup in independent["subgroups"]
                    )
                    self.assertEqual(record["a"], len(cover))
                    self.assertTrue(verify_abelian_cover(group, cover))

    def test_graph_product_log_certificates(self):
        log_path = REPOSITORY / "experiments" / "logs" / "graph_products.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        for record in document["records"]:
            with self.subTest(experiment=record["id"]):
                for part in ("left", "right", "or_product"):
                    certificate = record[part]
                    adjacency = tuple(
                        sum(1 << neighbor for neighbor in neighbors)
                        for neighbors in certificate["adjacency"]
                    )
                    clique = tuple(certificate["clique_vertices"])
                    colors = tuple(certificate["colors"])
                    self.assertTrue(verify_clique(adjacency, clique))
                    self.assertTrue(verify_coloring(adjacency, colors))
                    exact_clique = maximum_clique(adjacency)
                    exact_coloring = exact_chromatic_number(adjacency, exact_clique.size)
                    self.assertEqual(certificate["omega"], exact_clique.size)
                    self.assertEqual(certificate["chi"], exact_coloring.size)

    def test_gap_smallgroups_logs(self):
        for order in (8, 32, 64):
            log_path = (
                REPOSITORY
                / "experiments"
                / "logs"
                / ("gap_smallgroups_order%d.json" % order)
            )
            document = json.loads(log_path.read_text(encoding="utf-8"))
            export_path = REPOSITORY / document["gap_export"]
            self.assertEqual(
                document["gap_export_sha256"],
                hashlib.sha256(export_path.read_bytes()).hexdigest(),
            )
            self.assertEqual(str(order), document["gap_metadata"]["ORDER"])
            self.assertEqual(int(document["gap_metadata"]["COUNT"]), len(document["records"]))
            data_lines = [
                line
                for line in export_path.read_text(encoding="utf-8").splitlines()
                if line and not line.startswith("# ")
            ]
            export_rows = {
                row["group_id"]: row
                for row in csv.DictReader(data_lines, delimiter="\t")
            }
            self.assertEqual(len(document["records"]), len(export_rows))
            for record in document["records"]:
                with self.subTest(group=record["group_id"]):
                    export_row = export_rows[record["group_id"]]
                    self.assertEqual(tuple(record["elements"]), tuple(export_row["elements"].split(",")))
                    if "multiplication_table" in record:
                        table = tuple(tuple(row) for row in record["multiplication_table"])
                    else:
                        raw_table = export_row["multiplication_table"]
                        table = tuple(
                            tuple(int(value) - 1 for value in raw_row.split(","))
                            for raw_row in raw_table.split(";")
                        )
                    group = FiniteGroup(
                        record["group_id"],
                        tuple(record["elements"]),
                        table,
                    )
                    group.validate()
                    graph = compressed_noncommuting_graph(group)
                    logged_adjacency = tuple(
                        sum(1 << neighbor for neighbor in neighbors)
                        for neighbors in record["compressed_adjacency"]
                    )
                    self.assertEqual(graph.adjacency, logged_adjacency)
                    clique = maximum_clique(logged_adjacency)
                    coloring = exact_chromatic_number(logged_adjacency, clique.size)
                    self.assertEqual(record["nu"], clique.size)
                    self.assertEqual(record["a"], coloring.size)
                    candidate_bound = max(
                        int(record["nu"]),
                        2 ** ((int(record["nu"]) - 1) // 2) + 1,
                    )
                    if "candidate_bound" in record:
                        self.assertEqual(candidate_bound, record["candidate_bound"])
                        self.assertEqual(
                            candidate_bound - int(record["a"]),
                            record["candidate_bound_slack"],
                        )
                    self.assertLessEqual(int(record["a"]), candidate_bound)
                    if order == 64:
                        self.assertEqual(record["nu"], record["a"])
                    self.assertTrue(
                        verify_clique(
                            logged_adjacency,
                            tuple(record["clique_certificate"]["coset_vertices"]),
                        )
                    )
                    self.assertTrue(
                        verify_coloring(
                            logged_adjacency,
                            tuple(record["coloring_certificate"]["colors_by_coset"]),
                        )
                    )
                    index = group.index
                    generated_cover = tuple(
                        tuple(index[label] for label in subgroup)
                        for subgroup in record["coloring_certificate"]["generated_abelian_subgroups"]
                    )
                    self.assertEqual(record["a"], len(generated_cover))
                    self.assertTrue(verify_abelian_cover(group, generated_cover))


class ScalarSymplecticLogTests(unittest.TestCase):
    def test_p3_rank2_group_graph_clique_coloring_and_spread(self):
        log_path = REPOSITORY / "experiments" / "logs" / "scalar_symplectic_p3_m2.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        self.assertEqual(1, len(document["records"]))
        record = document["records"][0]
        self.assertEqual((3, 2), (record["prime"], record["rank"]))
        self.assertEqual((243, 3, 81), (
            record["group_order"],
            record["center_order"],
            record["compressed_vertex_count"],
        ))
        self.assertEqual("83/243", record["commuting_probability"])

        group = extraspecial_prime_group(3, 2)
        group.validate()
        self.assertEqual(record["multiplication_table_sha256"], multiplication_table_sha256(group))
        graph = compressed_noncommuting_graph(group)
        vectors, direct_adjacency = scalar_symplectic_adjacency(3, 2)
        logged_vectors = tuple(tuple(vector) for vector in record["quotient_vectors"])
        logged_adjacency = tuple(
            sum(1 << neighbor for neighbor in neighbors)
            for neighbors in record["compressed_adjacency"]
        )
        self.assertEqual(vectors, logged_vectors)
        self.assertEqual(graph.adjacency, direct_adjacency)
        self.assertEqual(graph.adjacency, logged_adjacency)

        clique = tuple(record["clique_certificate"]["vertices"])
        exact_colors = tuple(record["exact_coloring_certificate"]["colors"])
        self.assertEqual(7, len(clique))
        self.assertEqual(10, max(exact_colors) + 1)
        self.assertEqual(
            tuple(vectors[vertex] for vertex in clique),
            tuple(tuple(vector) for vector in record["clique_certificate"]["vectors"]),
        )
        self.assertTrue(verify_clique(logged_adjacency, clique))
        self.assertTrue(verify_coloring(logged_adjacency, exact_colors))
        recomputed_clique = maximum_clique(logged_adjacency)
        recomputed_coloring = exact_chromatic_number(logged_adjacency, recomputed_clique.size)
        self.assertEqual((7, 10), (recomputed_clique.size, recomputed_coloring.size))

        projective_vectors, projective_adjacency = projective_symplectic_graph(3, 2)
        exclusion_record = record["projective_clique_exclusion"]
        self.assertEqual(40, len(projective_vectors))
        self.assertEqual(
            projective_vectors,
            tuple(tuple(vector) for vector in exclusion_record["representatives"]),
        )
        logged_projective_adjacency = tuple(
            sum(1 << neighbor for neighbor in neighbors)
            for neighbors in exclusion_record["adjacency"]
        )
        self.assertEqual(projective_adjacency, logged_projective_adjacency)
        independent_exclusion = fixed_size_clique(projective_adjacency, 8)
        self.assertFalse(independent_exclusion.exists)
        self.assertFalse(exclusion_record["exists"])
        self.assertEqual(8, exclusion_record["excluded_clique_size"])

        spread = symplectic_spread(3, 2, vectors)
        spread_record = record["spread_certificate"]
        self.assertEqual(spread.modulus, tuple(spread_record["field_modulus_low_to_high"]))
        self.assertEqual(spread.trace_gram, tuple(tuple(row) for row in spread_record["trace_gram"]))
        self.assertEqual(spread.subspaces, tuple(tuple(space) for space in spread_record["subspace_vertices"]))
        self.assertEqual(spread.colors, tuple(spread_record["colors"]))
        self.assertEqual(10, len(spread.subspaces))
        self.assertEqual({9}, {len(space) for space in spread.subspaces})
        self.assertTrue(verify_coloring(logged_adjacency, spread.colors))

        spread_cover = tuple(
            tuple(subgroup)
            for subgroup in spread_record["abelian_subgroup_element_indices"]
        )
        generated_cover = tuple(
            tuple(subgroup)
            for subgroup in spread_record["generated_abelian_subgroup_element_indices"]
        )
        self.assertEqual({27}, {len(subgroup) for subgroup in spread_cover})
        self.assertTrue(verify_abelian_cover(group, spread_cover))
        self.assertTrue(verify_abelian_cover(group, generated_cover))
        self.assertEqual(10, record["isotropic_counting_lower_bound"])

        candidate_bound = max(record["nu"], 2 ** ((record["nu"] - 1) // 2) + 1)
        self.assertEqual(9, candidate_bound)
        self.assertEqual(candidate_bound, record["candidate_bound"])
        self.assertEqual(-1, record["candidate_bound_slack"])
        self.assertEqual("[DISPROVED]", record["candidate_bound_status"])
        self.assertGreater(record["a"], candidate_bound)


if __name__ == "__main__":
    unittest.main()
