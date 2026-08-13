#!/usr/bin/env python3
"""Write rigorous clique intervals and spread witnesses for larger cases."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

from exact_invariants import verify_clique
from scalar_symplectic import (
    projective_symplectic_graph,
    quotient_vectors,
    symplectic_spread,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stdout-log", type=Path)
    args = parser.parse_args()

    raw = args.config.read_bytes()
    configuration = json.loads(raw)
    records = []
    lines = []
    start = time.monotonic()
    for entry in configuration["groups"]:
        prime, rank = int(entry["prime"]), int(entry["rank"])
        projective_vectors, adjacency = projective_symplectic_graph(prime, rank)
        clique = tuple(int(vertex) for vertex in entry["clique_projective_vertices"])
        if not verify_clique(adjacency, clique):
            raise AssertionError("configured clique witness failed")

        # Independently check the strongly regular parameters used by the
        # Delsarte/Hoffman upper bound.  Since lambda=mu, the two restricted
        # eigenvalues are +/-sqrt(k-mu)=+/-p^(m-1).
        degrees = {bin(mask).count("1") for mask in adjacency}
        if len(degrees) != 1:
            raise AssertionError("projective graph is not regular")
        degree = next(iter(degrees))
        common_counts = {
            bin(adjacency[left] & adjacency[right]).count("1")
            for left in range(len(adjacency))
            for right in range(left + 1, len(adjacency))
        }
        if len(common_counts) != 1:
            raise AssertionError("common-neighbor count is not constant")
        common_neighbors = next(iter(common_counts))
        negative_eigenvalue = -(prime ** (rank - 1))
        if degree - common_neighbors != negative_eigenvalue ** 2:
            raise AssertionError("strongly regular parameters and eigenvalue disagree")
        upper_bound = 1 - degree // negative_eigenvalue

        vectors = quotient_vectors(prime, rank)
        spread = symplectic_spread(prime, rank, vectors)
        a_value = prime ** rank + 1
        if len(spread.subspaces) != a_value:
            raise AssertionError("spread has the wrong size")
        record = {
            "status": "[COMPUTED]",
            "exact_nu": False,
            "prime": prime,
            "rank": rank,
            "group_order": prime ** (2 * rank + 1),
            "center_order": prime,
            "compressed_vertex_count": prime ** (2 * rank),
            "projective_vertex_count": len(projective_vectors),
            "nu_lower_bound": len(clique),
            "nu_upper_bound": upper_bound,
            "a": a_value,
            "log_a_over_nu_upper_bound_from_witness": math.log(a_value) / len(clique),
            "clique_certificate": {
                "projective_vertices": list(clique),
                "vectors": [list(projective_vectors[vertex]) for vertex in clique],
            },
            "strongly_regular_certificate": {
                "degree": degree,
                "common_neighbors_for_every_distinct_pair": common_neighbors,
                "least_eigenvalue": negative_eigenvalue,
                "delsarte_clique_upper_bound": upper_bound,
            },
            "spread_certificate": {
                "field_modulus_low_to_high": list(spread.modulus),
                "trace_gram": [list(row) for row in spread.trace_gram],
                "subspace_vertices": [list(space) for space in spread.subspaces],
                "colors": list(spread.colors),
            },
        }
        records.append(record)
        lines.append(
            "p=%d m=%d: %d<=nu<=%d, a=%d, projective_vertices=%d"
            % (prime, rank, len(clique), upper_bound, a_value, len(projective_vectors))
        )

    output = {
        "schema_version": 1,
        "status": "[COMPUTED]",
        "configuration": str(args.config),
        "configuration_sha256": hashlib.sha256(raw).hexdigest(),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "external_dependencies": [],
        },
        "elapsed_wall_seconds": time.monotonic() - start,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines.append("wrote %d bounded records to %s" % (len(records), args.output))
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.stdout_log:
        args.stdout_log.parent.mkdir(parents=True, exist_ok=True)
        args.stdout_log.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
