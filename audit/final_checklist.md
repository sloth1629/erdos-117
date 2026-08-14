# Final Research-Pass Checklist

This is a release audit for an honest partial result, not a complete-solution
certificate.

## Complete-solution requirements

- [ ] Exact main theorem determining \(h(n)\) or its sharp asymptotic.
- [ ] Matching construction and universal upper bound at the optimal scale.
- [ ] Exact explanation of how the theorem completely settles Problem 117.

These boxes remain open, so no complete solution is claimed.

## Passed release checks

- [x] Definitions, boundary conventions, and \(n=1,2,3,4,5,6,7\) checked.
- [x] Arbitrary and finite groups distinguished and connected by a proved
  exact finite commutation model.
- [x] Central elements, central cosets, and the false quotient shortcut
  handled explicitly.
- [x] Every load-bearing external theorem has a proof-bearing primary source
  read at the stated pages; inaccessible sources are not load-bearing.
- [x] The CFSG-dependent subfactorial upper bound records the exact
  Guralnick--Maróti and Nagy--Pach--Tomon inputs, retains the CFSG
  dependency, and excludes the withdrawn fixed-base preprint.
- [x] The \(S(3,2)\) counterexample has a full structural proof and an
  independent exact computation.
- [x] The computer-assisted proof of \(h(5)=5\) records its primary-source
  cover theorem, Schur-cover reduction, complete GAP export, checksums, and
  independently checked clique/coloring certificates.
- [x] The computer-assisted proof of \(h(6)=6\) records its repaired
  six-cover proof, independently reconstructed finite leaves, the structural
  \(C_2^5\) exclusion, complete exterior-square export, and independently
  checked radical/clique/coloring certificates.
- [x] The computer-assisted proof of \(h(7)=10\) records the verified
  seven-cover input, the complete 738-type partition, all ordinary and
  character-dual scans, explicit exterior-zero rows, special quotient
  certificates, final hashes, and independent reconstruction tests.
- [x] The finite \(5\)-group cutoff-eight theorem records Berkovich
  Proposition 4.5 at its exact pages, the complete normalized
  \(\mathbf F _5\) hyperplane certificate, the arbitrary-dimensional
  incidence reduction, and two independent audits.  Its scope is explicitly
  separated from the still-open global value of \(h(8)\).
- [x] The finite \(3\)-group cutoff-eight theorem records the exact
  Berkovich inputs, maximal-centralizer amplification, the \(J\)-versus-\(H'\)
  twelve-clique dichotomy, the scalar-symplectic obstruction, and the final
  private-cell abelian cover.  It proves \(\nu(P)=8\Rightarrow a(P)=8\)
  only for finite \(3\)-groups and explicitly does not determine \(h(8)\).
- [x] The finite \(2\)-group cutoff-eight reduction records the rounded
  factorial intersection bounds, exact order-\(8192\) and order-\(4096\)
  exclusions, the Bonferroni arithmetic, and the Frattini odd-circuit
  argument.  Its conclusion \([P:Z(P)]\le2048\) is finite-only, and the
  binary classification remains open.
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
