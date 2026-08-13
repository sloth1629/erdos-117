# Final Research-Pass Checklist

This is a release audit for an honest partial result, not a complete-solution
certificate.

## Complete-solution requirements

- [ ] Exact main theorem determining \(h(n)\) or its sharp asymptotic.
- [ ] Matching construction and universal upper bound at the optimal scale.
- [ ] Exact explanation of how the theorem completely settles Problem 117.

These boxes remain open, so no complete solution is claimed.

## Passed release checks

- [x] Definitions, boundary conventions, and \(n=1,2,3,4,5,6\) checked.
- [x] Arbitrary and finite groups distinguished and connected by a proved
  exact finite commutation model.
- [x] Central elements, central cosets, and the false quotient shortcut
  handled explicitly.
- [x] Every paper-level theorem has an internal proof; inaccessible sources
  are not load-bearing.
- [x] The \(S(3,2)\) counterexample has a full structural proof and an
  independent exact computation.
- [x] The computer-assisted proof of \(h(5)=5\) records its primary-source
  cover theorem, Schur-cover reduction, complete GAP export, checksums, and
  independently checked clique/coloring certificates.
- [x] The computer-assisted proof of \(h(6)=6\) records its repaired
  six-cover proof, independently reconstructed finite leaves, the structural
  \(C_2^5\) exclusion, complete exterior-square export, and independently
  checked radical/clique/coloring certificates.
- [x] Product and limit assertions audited without assuming one-shot
  multiplicativity.
- [x] Computational witnesses, configurations, versions, hashes, and
  independent verifiers committed.
- [x] Full verification suite passes; exact count, output, and runtime are
  committed for this milestone.
- [x] Proof dependency graph is acyclic.
- [x] Backward/forward source audit completed to the stated search boundary;
  negative novelty claims remain qualified.
- [x] `git diff --check`, JSON parsing, Python compilation, secret scan, and
  repository-size review pass.

## Known release limitations

- [ ] Pyber (1987) full theorem and proof acquired.
- [ ] Bertram (1983), printed p. 40, acquired.
- [ ] Manuscript PDF compiled and visually inspected. TeX was not installed;
  only the source artifact is delivered.
- [x] \(p=5,m=2\) and \(p=3,m=3\) scalar-symplectic clique numbers
  determined by symmetry-reduced exact searches.
