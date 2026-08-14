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
    quotient_vectors,
    scalar_symplectic_adjacency,
    symplectic_spread,
)
from h6_c2_5 import form_graph, independent_certificate  # noqa: E402
from analyze_f6_maximal_cover_audit import (  # noqa: E402
    parse_tsv as parse_f6_cover_tsv,
    verify_group_row as verify_f6_cover_group_row,
)
from analyze_h7_quotient_inventory import validate_inventory as validate_h7_inventory  # noqa: E402
from analyze_h7_exterior_batch import verify_saved_batch as verify_h7_batch  # noqa: E402
from analyze_h7_capability_order64 import (  # noqa: E402
    validate_capability_batches as validate_h7_capability_batches,
)
from h7_c2_6_pencils import exact_certificate as fresh_h7_c2_6_rank6_certificate  # noqa: E402
from h7_c2_6_rank4_pencils import exact_certificate as fresh_h7_c2_6_rank4_certificate  # noqa: E402
from h7_c4_2_c2_2 import (  # noqa: E402
    exact_certificate as fresh_h7_c4_2_c2_2_certificate,
    verify_certificate as verify_h7_c4_2_c2_2_certificate,
)
from h7_c2_3_d8 import (  # noqa: E402
    exact_certificate as fresh_h7_c2_3_d8_certificate,
    verify_certificate as verify_h7_c2_3_d8_certificate,
)
from h7_order64_dual import (  # noqa: E402
    exact_certificate as fresh_h7_order64_dual_certificate,
)
from h7_c3_4 import (  # noqa: E402
    exact_certificate as fresh_h7_c3_4_certificate,
    graph_from_subspace as h7_c3_4_graph,
    projective_vectors as h7_c3_4_vectors,
    scalar_form_graphs as h7_c3_4_scalar_graphs,
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
    def test_h6_c2_5_alternating_form_certificate(self):
        log_path = REPOSITORY / "experiments" / "logs" / "h6_c2_5.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        source_path = REPOSITORY / document["solver_source"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            document["solver_source_sha256"],
            hashlib.sha256(source_path.read_bytes()).hexdigest(),
        )
        c_record = document["c_exhaustive_certificate"]
        self.assertEqual((174251, 156240), (
            c_record["pencil_count"], c_record["common_radical_zero_pencil_count"]
        ))
        self.assertEqual({"244": 52080, "444": 104160}, c_record["rank_profile_counts"])
        self.assertEqual((9, 156240, 1482030, 36), (
            c_record["search"]["target_clique_size"],
            c_record["search"]["witness_count"],
            c_record["search"]["total_search_nodes"],
            c_record["search"]["maximum_search_nodes"],
        ))
        for representative in c_record["representatives"]:
            adjacency = form_graph(representative["pencil"])
            vertices = tuple(value - 1 for value in representative["clique_vectors"])
            self.assertEqual(9, len(vertices))
            self.assertTrue(verify_clique(adjacency, vertices))

        rebuilt = independent_certificate()
        saved = document["independent_python_certificate"]
        # Search-node counts and every saved witness are deterministic, so the
        # complete pure-Python reconstruction should match byte-level data
        # except for no runtime fields (none are stored in this subrecord).
        self.assertEqual(saved, rebuilt)
        self.assertEqual([(2, 4, 4, 52080, 11), (4, 4, 4, 104160, 9)], [
            tuple(record["rank_profile"]) + (record["pencil_count"], record["omega"])
            for record in rebuilt["pencil_orbits"]
        ])
        rank_two = rebuilt["rank_two_radical_zero_orbit"]
        self.assertEqual((31, 17, 17), (
            rank_two["subspace_count"], rank_two["omega"], rank_two["chi"]
        ))

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

    def test_p5_rank2_symmetry_reduced_certificate_and_spread(self):
        log_path = REPOSITORY / "experiments" / "logs" / "scalar_symplectic_extended.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        source_path = REPOSITORY / document["solver_source"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            document["solver_source_sha256"],
            hashlib.sha256(source_path.read_bytes()).hexdigest(),
        )
        record = document["records"][0]
        self.assertEqual((5, 2, 18, 26), (
            record["prime"], record["rank"], record["nu"], record["a"]
        ))
        vectors, adjacency = projective_symplectic_graph(5, 2)
        clique = tuple(record["clique_certificate"]["projective_vertices"])
        self.assertEqual(
            tuple(vectors[vertex] for vertex in clique),
            tuple(tuple(vector) for vector in record["clique_certificate"]["vectors"]),
        )
        self.assertTrue(verify_clique(adjacency, clique))
        upper = record["clique_upper_certificate"]
        self.assertEqual(4, len(upper["cases"]))
        self.assertEqual({18}, {case["maximum_at_most"] for case in upper["cases"]})
        self.assertEqual(117060, upper["total_search_nodes"])
        self.assertEqual(18, upper["maximum"])

        quotient, compressed = scalar_symplectic_adjacency(5, 2)
        spread = symplectic_spread(5, 2, quotient)
        spread_record = record["spread_certificate"]
        self.assertEqual(spread.subspaces, tuple(
            tuple(space) for space in spread_record["subspace_vertices"]
        ))
        self.assertEqual(spread.colors, tuple(spread_record["colors"]))
        self.assertEqual(26, len(spread.subspaces))
        self.assertEqual({25}, {len(space) for space in spread.subspaces})
        self.assertTrue(verify_coloring(compressed, spread.colors))

        # Independent Python upper checks on the four canonical residual
        # graphs.  These do not execute or import the C search implementation.
        for prime, rank, expected_orders, expected_maxima in [
            (5, 2, (75, 75, 80, 80), (15, 15, 15, 15)),
            (3, 3, (81, 81, 108, 108), (7, 7, 10, 10)),
        ]:
            canonical_vectors, canonical_adjacency = projective_symplectic_graph(prime, rank)
            index = {vector: vertex for vertex, vector in enumerate(canonical_vectors)}
            first = (1,) + (0,) * (2 * rank - 1)
            second = (0,) * rank + (1,) + (0,) * (rank - 1)
            nonsquare = next(
                value
                for value in range(2, prime)
                if pow(value, (prime - 1) // 2, prime) == prime - 1
            )
            observed_orders = []
            observed_maxima = []
            for nonzero_tail in (False, True):
                for scalar in (1, nonsquare):
                    third = [0] * (2 * rank)
                    third[0] = 1
                    third[rank] = scalar
                    if nonzero_tail:
                        third[1] = 1
                    prefix = (index[first], index[second], index[tuple(third)])
                    common = (1 << len(canonical_vectors)) - 1
                    for vertex in prefix:
                        common &= canonical_adjacency[vertex]
                    residual_vertices = tuple(
                        vertex
                        for vertex in range(len(canonical_vectors))
                        if common & (1 << vertex)
                    )
                    residual_adjacency = tuple(
                        sum(
                            1 << target
                            for target, full_target in enumerate(residual_vertices)
                            if canonical_adjacency[full_source] & (1 << full_target)
                        )
                        for full_source in residual_vertices
                    )
                    observed_orders.append(len(residual_vertices))
                    observed_maxima.append(maximum_clique(residual_adjacency).size)
            self.assertEqual(expected_orders, tuple(observed_orders))
            self.assertEqual(expected_maxima, tuple(observed_maxima))

        rank3 = document["records"][1]
        self.assertEqual((3, 3, 13, 28), (
            rank3["prime"], rank3["rank"], rank3["nu"], rank3["a"]
        ))
        rank3_vectors, rank3_adjacency = projective_symplectic_graph(3, 3)
        rank3_clique = tuple(rank3["clique_certificate"]["projective_vertices"])
        self.assertTrue(verify_clique(rank3_adjacency, rank3_clique))
        self.assertEqual(
            tuple(rank3_vectors[vertex] for vertex in rank3_clique),
            tuple(tuple(vector) for vector in rank3["clique_certificate"]["vectors"]),
        )
        rank3_upper = rank3["clique_upper_certificate"]
        self.assertEqual(13, rank3_upper["maximum"])
        self.assertEqual(111536, rank3_upper["total_search_nodes"])
        self.assertEqual({13}, {
            case["maximum_at_most"] for case in rank3_upper["cases"]
        })
        rank3_quotient, rank3_compressed = scalar_symplectic_adjacency(3, 3)
        rank3_spread = symplectic_spread(3, 3, rank3_quotient)
        self.assertEqual(28, len(rank3_spread.subspaces))
        self.assertTrue(verify_coloring(rank3_compressed, rank3_spread.colors))

    def test_p7_rank2_rigorous_bounded_record(self):
        log_path = REPOSITORY / "experiments" / "logs" / "scalar_symplectic_bounds.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        config_path = REPOSITORY / document["configuration"]
        self.assertEqual(
            document["configuration_sha256"],
            hashlib.sha256(config_path.read_bytes()).hexdigest(),
        )
        record = document["records"][0]
        self.assertEqual((7, 2, 33, 50, 50), (
            record["prime"], record["rank"], record["nu_lower_bound"],
            record["nu_upper_bound"], record["a"],
        ))
        vectors, adjacency = projective_symplectic_graph(7, 2)
        clique = tuple(record["clique_certificate"]["projective_vertices"])
        self.assertTrue(verify_clique(adjacency, clique))
        self.assertEqual(
            tuple(vectors[vertex] for vertex in clique),
            tuple(tuple(vector) for vector in record["clique_certificate"]["vectors"]),
        )
        parameters = record["strongly_regular_certificate"]
        self.assertEqual((343, 294, -7, 50), (
            parameters["degree"],
            parameters["common_neighbors_for_every_distinct_pair"],
            parameters["least_eigenvalue"],
            parameters["delsarte_clique_upper_bound"],
        ))
        quotient = quotient_vectors(7, 2)
        spread = symplectic_spread(7, 2, quotient)
        self.assertEqual(50, len(spread.subspaces))
        self.assertEqual({49}, {len(space) for space in spread.subspaces})

    def test_order128_small_n_prefilter_certificates(self):
        log_path = (
            REPOSITORY / "experiments" / "logs" / "gap_smallgroups_order128_nu_le6.json"
        )
        document = json.loads(log_path.read_text(encoding="utf-8"))
        input_path = REPOSITORY / document["input"]
        self.assertEqual(
            document["input_sha256"], hashlib.sha256(input_path.read_bytes()).hexdigest()
        )
        self.assertEqual((128, 2328, 6, 418, 1910), (
            document["order"], document["total_smallgroups"], document["clique_cutoff"],
            document["survivor_count"], document["excluded_count"],
        ))
        with input_path.open(newline="", encoding="utf-8") as handle:
            rows = {row["group_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual(418, len(rows))
        distribution = {}
        non_ac = {}
        for record in document["records"]:
            row = rows[record["group_id"]]
            raw_rows = row["adjacency"].split(";")
            adjacency = tuple(
                sum(1 << (int(value) - 1) for value in raw.split(",") if value)
                for raw in raw_rows
            )
            self.assertTrue(verify_clique(adjacency, record["clique_certificate"]))
            self.assertTrue(verify_coloring(adjacency, record["coloring_certificate"]))
            self.assertEqual(record["nu"], len(record["clique_certificate"]))
            self.assertEqual(record["a"], max(record["coloring_certificate"]) + 1)
            pair = (record["nu"], record["a"])
            distribution[pair] = distribution.get(pair, 0) + 1
            if not record["is_ac_group"]:
                non_ac[record["nu"]] = non_ac.get(record["nu"], 0) + 1
        self.assertEqual({(1, 1): 15, (3, 3): 60, (5, 5): 199, (6, 6): 144}, distribution)
        self.assertEqual({5: 21, 6: 144}, non_ac)
        self.assertEqual([], document["strict_a_greater_nu"])

    def test_h5_exterior_square_scan_certificates(self):
        log_path = REPOSITORY / "experiments" / "logs" / "h5_exterior.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        input_path = REPOSITORY / document["input"]
        gap_script = REPOSITORY / document["gap_script"]
        self.assertEqual(
            document["input_sha256"], hashlib.sha256(input_path.read_bytes()).hexdigest()
        )
        self.assertEqual(
            document["gap_script_sha256"], hashlib.sha256(gap_script.read_bytes()).hexdigest()
        )
        self.assertEqual({
            "GAP_VERSION": "4.16.0",
            "SMALLGRP_VERSION": "1.5.4",
            "MAX_Q_ORDER": "16",
        }, document["gap_metadata"])
        self.assertEqual((42, 2986, 2396, 5), (
            document["quotient_count"], document["record_count"],
            document["unique_graph_count"], document["clique_cutoff"],
        ))
        lines = [
            line
            for line in input_path.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("# ")
        ]
        rows = list(csv.DictReader(lines, delimiter="\t"))
        self.assertEqual(len(rows), len(document["records"]))
        serials = {}
        distribution = {}
        eligible = {}
        for row, record in zip(rows, document["records"]):
            self.assertEqual(int(row["q_order"]), record["q_order"])
            self.assertEqual(int(row["q_id"]), record["q_id"])
            raw_rows = row["adjacency"].split(";")
            adjacency = tuple(
                sum(1 << (int(value) - 1) for value in raw.split(",") if value)
                for raw in raw_rows
            )
            self.assertTrue(verify_clique(adjacency, record["clique_certificate"]))
            self.assertTrue(verify_coloring(adjacency, record["coloring_certificate"]))
            self.assertEqual(record["nu"], len(record["clique_certificate"]))
            self.assertEqual(record["a"], max(record["coloring_certificate"], default=-1) + 1)
            pair = (record["nu"], record["a"])
            distribution[pair] = distribution.get(pair, 0) + 1
            if record["nu"] <= 5:
                eligible[pair] = eligible.get(pair, 0) + 1
                self.assertLessEqual(record["a"], 5)
            key = (record["q_order"], record["q_id"])
            serials.setdefault(key, set()).add(record["kernel_serial"])
        for record in document["records"]:
            key = (record["q_order"], record["q_id"])
            self.assertEqual(
                set(range(1, record["normal_kernel_count"] + 1)), serials[key]
            )
        self.assertEqual({
            (1, 1): 42, (3, 3): 84, (4, 4): 4, (5, 5): 234,
            (6, 6): 215, (7, 7): 22, (8, 8): 1, (9, 9): 1492,
            (11, 11): 492, (13, 13): 315, (15, 15): 85,
        }, distribution)
        self.assertEqual({(1, 1): 42, (3, 3): 84, (4, 4): 4, (5, 5): 234}, eligible)
        self.assertEqual([], document["eligible_failure_rows"])

    def test_h6_exterior_square_scan_certificates(self):
        log_path = REPOSITORY / "experiments" / "logs" / "h6_exterior.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        input_path = REPOSITORY / document["input"]
        gap_script = REPOSITORY / document["gap_script"]
        c2_path = REPOSITORY / document["c2_5_certificate"]
        self.assertEqual(
            document["input_sha256"], hashlib.sha256(input_path.read_bytes()).hexdigest()
        )
        self.assertEqual(
            document["gap_script_sha256"], hashlib.sha256(gap_script.read_bytes()).hexdigest()
        )
        self.assertEqual(
            document["c2_5_certificate_sha256"], hashlib.sha256(c2_path.read_bytes()).hexdigest()
        )
        self.assertEqual({
            "GAP_VERSION": "4.16.0",
            "SMALLGRP_VERSION": "1.5.4",
            "MAX_Q_ORDER": "36",
            "CLIQUE_CUTOFF": "6",
            "SPECIAL_QUOTIENT": "SmallGroup(32,51)",
        }, document["gap_metadata"])
        self.assertEqual((162, 161, 23527, 314, 4045), (
            document["quotient_count"], document["gap_scanned_quotient_count"],
            document["normal_kernel_record_count"],
            document["status_distribution"]["candidate"],
            document["unique_faithful_graph_count"],
        ))
        lines = [
            line
            for line in input_path.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("# ")
        ]
        rows = list(csv.DictReader(lines, delimiter="\t"))
        self.assertEqual(23528, len(rows))
        candidate_records = {
            record["row_number"]: record for record in document["candidate_records"]
        }
        statuses = {}
        serials = {}
        normal_counts = {}
        eligible = {}
        special = []
        for row_number, row in enumerate(rows, 1):
            status = row["status"]
            statuses[status] = statuses.get(status, 0) + 1
            q_order = int(row["q_order"])
            key = (q_order, int(row["q_id"]))
            if status == "special_c2_5":
                special.append(key)
                self.assertEqual((32, 51), key)
                self.assertEqual("", row["adjacency"])
                continue
            count = int(row["normal_kernel_count"])
            normal_counts[key] = count
            serials.setdefault(key, set()).add(int(row["kernel_serial"]))
            adjacency = tuple(int(mask) for mask in row["adjacency"].split(","))
            self.assertEqual(q_order, len(adjacency))
            for source, mask in enumerate(adjacency):
                self.assertFalse(mask & (1 << source))
                for target in range(q_order):
                    self.assertEqual(
                        bool(mask & (1 << target)),
                        bool(adjacency[target] & (1 << source)),
                    )
            radical = tuple(vertex for vertex, mask in enumerate(adjacency) if mask == 0)
            self.assertEqual(int(row["radical_count"]), len(radical))
            witness = tuple(int(value) - 1 for value in row["witness"].split(",") if value)
            if status == "nonfaithful_radical":
                self.assertGreater(len(radical), 1)
                self.assertEqual(radical, witness)
            elif status == "clique_ge_7":
                self.assertEqual(7, len(witness))
                self.assertTrue(verify_clique(adjacency, witness))
            else:
                self.assertEqual("candidate", status)
                self.assertEqual(1, len(radical))
                record = candidate_records[row_number]
                clique = tuple(record["clique_certificate"])
                colors = tuple(record["coloring_certificate"])
                self.assertTrue(verify_clique(adjacency, clique))
                self.assertTrue(verify_coloring(adjacency, colors))
                self.assertEqual(record["nu"], len(clique))
                self.assertEqual(record["a"], max(colors, default=-1) + 1)
                pair = (record["nu"], record["a"])
                eligible[pair] = eligible.get(pair, 0) + 1
        self.assertEqual([(32, 51)], special)
        self.assertEqual({
            "candidate": 314,
            "clique_ge_7": 4982,
            "nonfaithful_radical": 18231,
            "special_c2_5": 1,
        }, statuses)
        self.assertEqual(23527, sum(normal_counts.values()))
        for key, count in normal_counts.items():
            self.assertEqual(set(range(1, count + 1)), serials[key])
        self.assertEqual({
            (1, 1): 1, (3, 3): 1, (4, 4): 2, (5, 5): 93, (6, 6): 217,
        }, eligible)
        self.assertEqual([], document["eligible_failure_rows"])

    def test_f6_maximal_cover_audit_certificates(self):
        log_path = REPOSITORY / "experiments" / "logs" / "f6_maximal_cover.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        inputs = document["inputs"]
        for name in ("gap_script", "class_tsv", "group_tsv", "gap_stdout"):
            path = REPOSITORY / inputs[name]
            self.assertEqual(
                inputs[name + "_sha256"], hashlib.sha256(path.read_bytes()).hexdigest()
            )
        class_path = REPOSITORY / inputs["class_tsv"]
        group_path = REPOSITORY / inputs["group_tsv"]
        class_metadata, class_rows = parse_f6_cover_tsv(class_path)
        group_metadata, group_rows = parse_f6_cover_tsv(group_path)
        self.assertEqual(class_metadata, group_metadata)
        self.assertEqual({
            "GAP_VERSION": "4.16.0",
            "SMALLGRP_VERSION": "1.5.4",
            "COVER_SIZE": "6",
        }, class_metadata)
        self.assertEqual((165, 48), (len(class_rows), len(group_rows)))

        # Re-run the dependency-free table verifier, including all subgroup
        # closures, all maximal subgroups, and all 5,545,351 six-subsets.
        independently_verified = {
            record["group_id"]: record
            for record in (verify_f6_cover_group_row(row) for row in group_rows)
        }
        self.assertEqual(48, len(independently_verified))
        self.assertEqual(5545351, sum(
            record["six_combinations"] for record in independently_verified.values()
        ))
        self.assertEqual((38, 0, 0), (
            independently_verified["36,10"]["cover_count"],
            independently_verified["36,10"]["irredundant_cover_count"],
            independently_verified["36,10"]["qualifying_count"],
        ))
        self.assertEqual((72, {1: 72}), (
            independently_verified["36,13"]["qualifying_count"],
            independently_verified["36,13"]["intersection_distribution"],
        ))
        positives = {
            group_id: (
                record["qualifying_count"], record["intersection_distribution"]
            )
            for group_id, record in independently_verified.items()
            if record["qualifying_count"]
        }
        self.assertEqual({
            "18,4": (234, {1: 234}),
            "24,14": (4, {1: 4}),
            "36,13": (72, {1: 72}),
            "50,4": (25, {2: 25}),
            "54,14": (6318, {2: 6318}),
            "100,11": (25, {4: 25}),
        }, positives)
        s4_ids = {
            row["group_id"] for row in class_rows
            if row["family"] == "auxiliary_S4_all"
        }
        self.assertEqual(9, len(s4_ids))
        self.assertTrue(all(
            independently_verified[group_id]["qualifying_count"] == 0
            for group_id in s4_ids
        ))
        self.assertEqual((5257, 100483, 10308, 6678), (
            document["total_subgroups_independently_enumerated"],
            document["total_covers"],
            document["total_irredundant_covers"],
            document["total_qualifying_covers"],
        ))

    def test_h7_quotient_inventory_and_c3_4_orbits(self):
        inventory_path = REPOSITORY / "experiments" / "logs" / "h7_quotient_inventory.json"
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        raw_inventory = REPOSITORY / inventory["inventory"]
        gap_script = REPOSITORY / inventory["configuration"]
        self.assertEqual(
            inventory["inventory_sha256"], hashlib.sha256(raw_inventory.read_bytes()).hexdigest()
        )
        self.assertEqual(
            inventory["configuration_sha256"], hashlib.sha256(gap_script.read_bytes()).hexdigest()
        )
        self.assertEqual((738, 150, 33), (
            inventory["quotient_count"], inventory["abelian_quotient_count"],
            inventory["elementary_abelian_quotient_count"],
        ))
        rebuilt_inventory = validate_h7_inventory(raw_inventory)
        self.assertEqual(738, len(rebuilt_inventory["rows"]))
        self.assertEqual(
            inventory["cumulative_exterior_order_tiers"], rebuilt_inventory["tier_counts"]
        )
        self.assertEqual(
            inventory["exterior_order_distribution"],
            {str(key): value for key, value in sorted(rebuilt_inventory["exterior_distribution"].items())},
        )
        explosions = [
            (record["q_order"], record["q_id"], record["exact_raw_kernel_count"])
            for record in rebuilt_inventory["exact_explosions"]
        ]
        self.assertEqual([
            (64, 267, 623476476706836148),
            (32, 51, 229755605),
            (64, 260, 229755605),
        ], explosions)

        log_path = REPOSITORY / "experiments" / "logs" / "h7_c3_4.json"
        document = json.loads(log_path.read_text(encoding="utf-8"))
        self.assertEqual(
            document["inventory_certificate_sha256"],
            hashlib.sha256((REPOSITORY / document["inventory_certificate"]).read_bytes()).hexdigest(),
        )
        certificate = document["certificate"]
        # This fresh full reconstruction enumerates all 56,632 subspaces,
        # repartitions all 55,941 faithful cases, checks every generator
        # transport, and recomputes the 16 exact graph records.
        self.assertEqual(certificate, fresh_h7_c3_4_certificate())
        self.assertEqual((56632, 55941, 691, 16, 55941), (
            certificate["raw_subspace_count"], certificate["faithful_subspace_count"],
            certificate["nonfaithful_subspace_count"], certificate["orbit_count"],
            certificate["orbit_size_sum"],
        ))
        self.assertEqual([4], certificate["eligible_orbit_indices"])
        self.assertEqual(10, certificate["maximum_a_at_nu_at_most_7"])
        scalar_graphs = h7_c3_4_scalar_graphs()
        self.assertEqual(40, len(h7_c3_4_vectors()))
        weighted = {}
        for index, record in enumerate(certificate["orbits"]):
            subspace = tuple(tuple(row) for row in record["representative_rref"])
            adjacency = h7_c3_4_graph(subspace, scalar_graphs)
            self.assertEqual(tuple(record["projective_adjacency"]), adjacency)
            clique = tuple(record["clique_certificate"])
            colors = tuple(record["coloring_certificate"])
            self.assertTrue(verify_clique(adjacency, clique))
            self.assertTrue(verify_coloring(adjacency, colors))
            self.assertEqual(record["omega"], len(clique))
            self.assertEqual(record["chi"], max(colors) + 1)
            pair = (record["omega"], record["chi"])
            weighted[pair] = weighted.get(pair, 0) + record["orbit_size"]
            if index == 4:
                self.assertEqual((7, 10, 234), (
                    record["omega"], record["chi"], record["orbit_size"],
                ))
        self.assertEqual({
            (7, 10): 234, (10, 10): 2106, (12, 12): 3120,
            (16, 16): 5265, (25, 25): 9360, (28, 28): 21100,
            (31, 31): 1560, (34, 34): 5265, (37, 37): 5590,
            (40, 40): 2341,
        }, weighted)

    def test_h7_bounded_batches_and_c2_6_pencil_certificates(self):
        expected_batches = {
            "h7_exterior_1_36.json": (
                162, 161, 23527,
                {"candidate": 317, "clique_ge_8": 4979, "nonfaithful_radical": 18231},
                4045,
            ),
            "h7_exterior_37_63.json": (
                157, 157, 9657,
                {"clique_ge_8": 2933, "nonfaithful_radical": 6724},
                2419,
            ),
            "h7_exterior_65_80.json": (
                137, 137, 9816,
                {"clique_ge_8": 2884, "nonfaithful_radical": 6932},
                2356,
            ),
            "h7_exterior_81.json": (
                15, 14, 368,
                {"clique_ge_8": 197, "nonfaithful_radical": 171},
                121,
            ),
            "h7_exterior_64_1_191.json": (
                191, 191, 12602,
                {"clique_ge_8": 3996, "nonfaithful_radical": 8606},
                3637,
            ),
        }
        batch_documents = {}
        for filename, expected in expected_batches.items():
            path = REPOSITORY / "experiments" / "logs" / filename
            batch_documents[filename] = json.loads(path.read_text(encoding="utf-8"))
            rebuilt = verify_h7_batch(path, REPOSITORY)
            self.assertEqual(expected, (
                rebuilt["quotient_row_count"], rebuilt["scanned_quotient_count"],
                rebuilt["kernel_record_count"], rebuilt["status_distribution"],
                rebuilt["unique_faithful_graph_count"],
            ))
            self.assertEqual([], rebuilt["failure_rows"])
        self.assertEqual([{
            "small_group": [81, 15],
            "path": "experiments/logs/h7_c3_4.json",
            "sha256": hashlib.sha256(
                (REPOSITORY / "experiments/logs/h7_c3_4.json").read_bytes()
            ).hexdigest(),
        }], batch_documents["h7_exterior_81.json"]["delegated_certificates"])
        first_batch = batch_documents["h7_exterior_1_36.json"]
        omega_seven = sorted(
            (record["q_order"], record["q_id"], record["kernel_serial"])
            for record in first_batch["candidate_records"] if record["nu"] == 7
        )
        self.assertEqual([(8, 5, 1), (12, 3, 1), (12, 4, 1)], omega_seven)

        rank_six_path = REPOSITORY / "experiments/logs/h7_c2_6_rank6_pencils.json"
        rank_six = json.loads(rank_six_path.read_text(encoding="utf-8"))["certificate"]
        self.assertEqual(rank_six, fresh_h7_c2_6_rank6_certificate())
        self.assertEqual((16383, 14, 6, 9), (
            rank_six["normalized_pencil_count"],
            rank_six["all_raw_form_orbit_count_including_zero_and_beta"],
            rank_six["symplectic_pencil_orbit_count"], rank_six["minimum_omega"],
        ))
        self.assertEqual([9, 11, 12, 15, 15, 15], sorted(
            record["omega"] for record in rank_six["pencil_orbits"]
        ))

        rank_four_path = REPOSITORY / "experiments/logs/h7_c2_6_rank4_pencils.json"
        rank_four = json.loads(rank_four_path.read_text(encoding="utf-8"))["certificate"]
        self.assertEqual(rank_four, fresh_h7_c2_6_rank4_certificate())
        self.assertEqual((16383, 5471, 12, 7, [1, 76]), (
            rank_four["normalized_pencil_count"], rank_four["no_rank_six_pencil_count"],
            rank_four["stabilizer_orbit_count"], rank_four["relevant_orbit_count"],
            rank_four["low_orbit_representatives"],
        ))
        self.assertEqual({
            "clique_ge_8": 5450,
            "common_radical_equals_beta_radical": 21,
        }, rank_four["direct_dichotomy_distribution"])

    def test_h7_c4_2_c2_2_exterior_kernel_certificate(self):
        path = REPOSITORY / "experiments/logs/h7_c4_2_c2_2.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        inventory_path = REPOSITORY / document["inventory_certificate"]
        self.assertEqual(
            document["inventory_certificate_sha256"],
            hashlib.sha256(inventory_path.read_bytes()).hexdigest(),
        )
        for field in ("producer", "runner"):
            source_path = REPOSITORY / document[field]
            self.assertEqual(
                document[field + "_sha256"],
                hashlib.sha256(source_path.read_bytes()).hexdigest(),
            )
        certificate = document["certificate"]
        # First rebuild the entire producer output. This independently repeats
        # the RREF/coset subgroup classification and all 5,276 graph checks.
        self.assertEqual(certificate, fresh_h7_c4_2_c2_2_certificate())
        # Then parse every saved record again and reconstruct its subgroup,
        # radical, and saved clique/radical witness without trusting aggregates.
        rebuilt = verify_h7_c4_2_c2_2_certificate(certificate)
        self.assertEqual((5276, 2351, 2925, 0), (
            rebuilt["subgroup_count"],
            rebuilt["status_distribution"]["clique_ge_8"],
            rebuilt["status_distribution"]["nonfaithful_radical"],
            rebuilt["cutoff_seven_candidate_count"],
        ))
        self.assertEqual({"full": 2451, "two": 2451, "zero": 374},
                         rebuilt["subgroup_projection_distribution"])
        self.assertEqual(2038, rebuilt["unique_faithful_graph_count"])

    def test_h7_order64_capability_certificate(self):
        path = REPOSITORY / "experiments/logs/h7_capability_order64.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        gap_script = REPOSITORY / document["gap_script"]
        inventory = REPOSITORY / document["inventory"]
        self.assertEqual(document["gap_script_sha256"], hashlib.sha256(gap_script.read_bytes()).hexdigest())
        self.assertEqual(document["inventory_sha256"], hashlib.sha256(inventory.read_bytes()).hexdigest())
        inputs = []
        for record in document["inputs"]:
            input_path = REPOSITORY / record["path"]
            self.assertEqual(record["sha256"], hashlib.sha256(input_path.read_bytes()).hexdigest())
            inputs.append(input_path)
        for record in document["gap_stdout"]:
            stdout_path = REPOSITORY / record["path"]
            self.assertEqual(record["sha256"], hashlib.sha256(stdout_path.read_bytes()).hexdigest())
        rebuilt = validate_h7_capability_batches(inputs, inventory)
        self.assertEqual(document["certificate"], rebuilt)
        self.assertEqual((76, {"1": 14, "2": 30, "4": 32}), (
            rebuilt["quotient_count"],
            rebuilt["epicentre_size_distribution"],
        ))
        self.assertEqual([
            192, 193, 195, 202, 203, 207, 211,
            216, 226, 236, 242, 250, 261, 267,
        ], rebuilt["trivial_center_image_ids"])
        self.assertEqual(62, len(rebuilt["exterior_zero_excluded_ids"]))
        self.assertTrue(all(
            any(record["q_exponents"])
            and all(
                not any(vector)
                for vector in record["universal_exterior_commutator_row"]
            )
            for record in rebuilt["nonidentity_epicentre_witnesses"]
        ))
        for q_id in range(262, 267):
            witness = next(
                record for record in rebuilt["nonidentity_epicentre_witnesses"]
                if record["q_id"] == q_id
            )
            self.assertEqual((7, [0, 0, 0, 0, 0, 1]), (
                witness["epicentre_position"], witness["q_exponents"],
            ))
            self.assertTrue(all(not any(vector) for vector in witness["cover_generator_commutators"]))

    def test_h7_global_quotient_partition(self):
        inventory_document = json.loads((
            REPOSITORY / "experiments/logs/h7_quotient_inventory.json"
        ).read_text(encoding="utf-8"))
        inventory = validate_h7_inventory(
            REPOSITORY / inventory_document["inventory"]
        )
        inventory_keys = set(inventory["indexed"])

        ordinary = set()
        for filename in (
            "h7_exterior_1_36.json",
            "h7_exterior_37_63.json",
            "h7_exterior_64_1_191.json",
            "h7_exterior_65_80.json",
            "h7_exterior_81.json",
        ):
            document = json.loads((
                REPOSITORY / "experiments/logs" / filename
            ).read_text(encoding="utf-8"))
            ordinary.update(
                (record["q_order"], record["q_id"])
                for record in document["quotients"]
            )
        delegates = {(32, 51), (81, 15)}

        exterior_zero_document = json.loads((
            REPOSITORY / "experiments/logs/h7_capability_order64.json"
        ).read_text(encoding="utf-8"))
        exterior_zero = {
            (64, q_id) for q_id in
            exterior_zero_document["certificate"]["exterior_zero_excluded_ids"]
        }
        generic_document = json.loads((
            REPOSITORY / "experiments/logs/h7_order64_dual.json"
        ).read_text(encoding="utf-8"))
        generic = {
            (64, int(certificate["metadata"]["Q_ID"]))
            for certificate in generic_document["certificates"]
        }
        specials = {(64, 192), (64, 261), (64, 267)}

        parts = (ordinary, delegates, exterior_zero, generic, specials)
        self.assertEqual([660, 2, 62, 11, 3], list(map(len, parts)))
        for left, right in itertools.combinations(parts, 2):
            self.assertTrue(left.isdisjoint(right))
        self.assertEqual(inventory_keys, set().union(*parts))

    def test_h7_order64_generic_dual_certificates(self):
        path = REPOSITORY / "experiments/logs/h7_order64_dual.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        for field in ("gap_script", "inventory_certificate", "producer", "runner"):
            source_path = REPOSITORY / document[field]
            self.assertEqual(
                document[field + "_sha256"],
                hashlib.sha256(source_path.read_bytes()).hexdigest(),
            )
        input_paths = []
        for record in document["inputs"]:
            input_path = REPOSITORY / record["path"]
            self.assertEqual(
                record["sha256"], hashlib.sha256(input_path.read_bytes()).hexdigest()
            )
            input_paths.append(input_path)
        for record in document["gap_stdout"]:
            stdout_path = REPOSITORY / record["path"]
            self.assertEqual(
                record["sha256"], hashlib.sha256(stdout_path.read_bytes()).hexdigest()
            )

        expected = {
            193: (192, 498, 4053, {"4": 334, "8": 128, "16": 35, "64": 1}),
            195: (64, 450, 1765, {"4": 294, "8": 120, "16": 35, "64": 1}),
            202: (224, 498, 2609, {"4": 330, "8": 132, "16": 35, "64": 1}),
            203: (128, 482, 2141, {"4": 318, "8": 128, "16": 35, "64": 1}),
            207: (96, 466, 1953, {"4": 306, "8": 124, "16": 35, "64": 1}),
            211: (288, 498, 2453, {"4": 330, "8": 132, "16": 35, "64": 1}),
            216: (96, 466, 1953, {"4": 306, "8": 124, "16": 35, "64": 1}),
            226: (128, 482, 2141, {"4": 318, "8": 128, "16": 35, "64": 1}),
            236: (64, 450, 1765, {"4": 294, "8": 120, "16": 35, "64": 1}),
            242: (64, 450, 1765, {"4": 294, "8": 120, "16": 35, "64": 1}),
            250: (96, 466, 1953, {"4": 306, "8": 124, "16": 35, "64": 1}),
        }
        self.assertEqual(11, len(document["certificates"]))
        for input_path, saved in zip(input_paths, document["certificates"]):
            # This fresh no-orbit BFS rechecks every retained subgroup and
            # every saved scalar/boundary eight-clique before exact equality.
            rebuilt = fresh_h7_order64_dual_certificate(input_path)
            self.assertEqual(saved, rebuilt)
            q_id = int(rebuilt["metadata"]["Q_ID"])
            self.assertEqual(expected[q_id], (
                rebuilt["good_character_count"],
                rebuilt["retained_no_eight_subgroup_count"],
                rebuilt["pruned_boundary_subgroup_count"],
                rebuilt["radical_size_distribution"],
            ))
            self.assertEqual(
                {"nonfaithful_radical": rebuilt["retained_no_eight_subgroup_count"]},
                rebuilt["retained_status_distribution"],
            )
            self.assertEqual(0, rebuilt["faithful_candidate_count"])

    def test_h7_c2_3_d8_affine_dual_certificate(self):
        path = REPOSITORY / "experiments/logs/h7_c2_3_d8.json"
        document = json.loads(path.read_text(encoding="utf-8"))
        for field in (
            "input", "gap_script", "gap_stdout", "inventory_certificate",
            "producer", "runner",
        ):
            source_path = REPOSITORY / document[field]
            self.assertEqual(
                document[field + "_sha256"],
                hashlib.sha256(source_path.read_bytes()).hexdigest(),
            )
        input_path = REPOSITORY / document["input"]
        certificate = document["certificate"]
        # Freshly repeat the complete affine RREF census and graph checks.
        self.assertEqual(certificate, fresh_h7_c2_3_d8_certificate(input_path))
        # Independently reconstruct every one of the 26,387 saved subgroups
        # and its stored radical or eight-clique witness.
        rebuilt = verify_h7_c2_3_d8_certificate(certificate, input_path)
        self.assertEqual((26387, 22641), (
            rebuilt["subgroup_count"], rebuilt["faithful_subgroup_count"],
        ))
        self.assertEqual({
            "clique_ge_8": 26323,
            "nonfaithful_radical": 64,
        }, rebuilt["status_distribution"])
        self.assertEqual((1152, 1024, 128, 0), (
            certificate["good_character_count"],
            certificate["even_good_character_count"],
            certificate["odd_good_character_count"],
            certificate["faithful_candidate_count"],
        ))
        obstruction = certificate["all_even_obstruction"]
        self.assertTrue(any(obstruction["quotient_pc_exponents"]))
        self.assertEqual([[0] * 10, [0] * 9 + [2]], obstruction["commutator_values"])


if __name__ == "__main__":
    unittest.main()
