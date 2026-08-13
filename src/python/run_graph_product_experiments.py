#!/usr/bin/env python3
"""Produce exact certificates for configured disjunctive graph products."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Sequence, Tuple

from exact_invariants import (
    compressed_noncommuting_graph,
    exact_chromatic_number,
    graph_or_product,
    maximum_clique,
    verify_clique,
    verify_coloring,
)
from finite_groups import named_group


def cycle_graph(n: int) -> Tuple[int, ...]:
    if n < 3:
        raise ValueError("cycle length must be at least three")
    return tuple((1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) for i in range(n))


def configured_graph(specification: Dict[str, object]) -> Tuple[int, ...]:
    graph_type = specification["type"]
    if graph_type == "cycle":
        return cycle_graph(int(specification["n"]))
    if graph_type == "compressed_group":
        return compressed_noncommuting_graph(named_group(str(specification["id"]))).adjacency
    raise ValueError("unknown graph type: %s" % graph_type)


def analyze(adjacency: Sequence[int]) -> Dict[str, object]:
    clique = maximum_clique(adjacency)
    coloring = exact_chromatic_number(adjacency, clique.size)
    if not verify_clique(adjacency, clique.vertices) or not verify_coloring(adjacency, coloring.colors):
        raise AssertionError("certificate verification failed")
    return {
        "vertex_count": len(adjacency),
        "adjacency": [[v for v in range(len(adjacency)) if mask & (1 << v)] for mask in adjacency],
        "omega": clique.size,
        "chi": coloring.size,
        "clique_vertices": list(clique.vertices),
        "colors": list(coloring.colors),
        "clique_search_nodes": clique.search_nodes,
        "coloring_search_nodes_by_k": [list(item) for item in coloring.search_nodes_by_k],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.config.read_bytes()
    config = json.loads(raw)
    records = []
    for experiment in config["experiments"]:
        left_graph = configured_graph(experiment["left"])
        right_graph = configured_graph(experiment["right"])
        product_graph = graph_or_product(left_graph, right_graph)
        records.append(
            {
                "id": experiment["id"],
                "left": analyze(left_graph),
                "right": analyze(right_graph),
                "or_product": analyze(product_graph),
            }
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
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for record in records:
        left, right, product = record["left"], record["right"], record["or_product"]
        print(
            "%s: (omega,chi)=(%d,%d) OR (%d,%d) -> (%d,%d)"
            % (
                record["id"],
                left["omega"],
                left["chi"],
                right["omega"],
                right["chi"],
                product["omega"],
                product["chi"],
            )
        )


if __name__ == "__main__":
    main()
