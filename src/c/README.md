# Exact C search

`scalar_symplectic_clique.c` is a dependency-free ISO C11 exact
branch-and-bound solver specialized to odd-prime scalar-symplectic projective
graphs. It uses transitivity on adjacent pairs and the four stabilizer orbits
for a third point to reduce a global clique exclusion to four residual graphs.

The canonical Python runner compiles it with strict warnings, verifies the
saved lower witness and isotropic spread independently, and records the source
hash and all search counts. The verification suite also solves every residual
graph with the separate Python maximum-clique implementation.

`h6_c2_5_pencils.c` is a second dependency-free ISO C11 verifier. It
enumerates all 174,251 two-dimensional subspaces of the ten-dimensional space
of alternating forms on \(\mathbb F_2^5\), retains the 156,240 pencils with
zero common radical, and constructs a nine-clique for every retained pencil.
The Python runner independently reconstructs the two transvection orbits and
all 1,892 subspaces whose nonzero forms have rank two.
