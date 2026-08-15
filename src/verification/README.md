# Independent verification

`test_exact_computation.py` checks group axioms, central-coset partitions and
commutation invariance, witness validity, exact named-group records, direct
product/OR-product compatibility, and the symplectic quotient model for
extraspecial 2-groups.  As an implementation-independent optimizer check it
also compares both exact graph algorithms against naive enumeration on every
labeled simple graph with at most six vertices. Saved GAP logs at orders 8,
32, and 64 are reparsed from their checksummed TSV sources: all 323
multiplication tables, compressed graphs, clique/coloring witnesses, candidate
bounds, and generated abelian subgroup covers are rechecked.

The scalar-symplectic test reconstructs the order-243 group and its 81-vertex
graph, reruns exact clique and coloring, independently excludes an 8-clique on
the 40 projective twin classes, and checks every finite-field spread subspace
and both saved abelian subgroup covers.

`test_f5_small_hyperplane_cover.py` independently rebuilds the finite
certificate used to close the \(5\)-group branch at cutoff eight.  After
normalizing independent hyperplane normals to the coordinate points, it
exhausts every torus-covering subfamily in dimensions two through four and
checks that each cover contains all six normals of a projective line.

`test_h8_sg261_target9_scalar_bridge.py` repairs and independently checks the
scalar-completeness link for `SmallGroup(64,261)`: it exact-solves all 2,048
scalar graphs, rechecks the 896 saved nine-cliques, and verifies that the
target-nine good set is exactly the 1,152-character affine universe used by
the cutoff-seven and cutoff-eight subgroup certificates.

`test_dynamic_fractional_centralizer.py` verifies the saved exact
dynamic-centralizer bundle using only the Python standard library.  It
reconstructs both finite class-two multiplication tables and centers,
checks the clique and rational primal/dual certificates, verifies the
chain-ring family through length four, and reruns all 28,672 one-pair
extension target-clique searches with a fixed witness digest.

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 -m unittest discover -s src/verification -p 'test_*.py' -v
```
