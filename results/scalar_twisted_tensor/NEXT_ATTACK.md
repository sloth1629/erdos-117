# NEXT ATTACK

## Starting point created by this bundle

`[PROVED]` Scalar-valued field-linear symplectic groups are now asymptotically exhausted: the binary field gives rate \(\sqrt2\), while the union of all nonbinary scalar fields is subexponential in \(\nu\).

`[PROVED]` Therefore the next lower-bound attack should not optimize \(q\) or search for larger scalar partial ovoids as its main objective. Such work can improve finite cutoffs, but cannot improve the global exponential base.

`[UNVERIFIED]` The most direct remaining lower-bound route is a genuinely higher-codomain alternating map.

---

# 1. Primary next direction: higher-codomain commutator geometry

Let \(V,W\) be finite vector spaces over \(\mathbb F_p\), and let

\[
\beta:V\times V\to W
\]

be alternating bilinear and radical-free. Define

\[
\omega(\beta)=
\max\{|X|:X\subseteq V,\ \beta(x,y)\ne0\text{ for distinct }x,y\},
\]

and let

\[
\tau(\beta)=
\min\{k:V=U_1\cup\cdots\cup U_k,\ \beta(U_i,U_i)=0\},
\]

where the \(U_i\) are additive subspaces.

`[PROVED]` A valid class-two group realization has \(\nu=\omega(\beta)\) and \(a=\tau(\beta)\). In characteristic two, one must choose a bilinear triangular cocycle \(c\) satisfying

\[
c(v,w)+c(w,v)=\beta(v,w),
\]

and use

\[
(v,z)(v',z')=(v+v',z+z'+c(v,v')).
\]

## Target construction

### HC target `[CONJECTURE]`

Find an explicit infinite family \(\beta_i:V_i\times V_i\to W_i\) with

\[
\omega(\beta_i)\to\infty
\]

and some \(\varepsilon>0\) such that

\[
\log_2\tau(\beta_i)
\ge
\left(\frac12+\varepsilon\right)\omega(\beta_i)-o(\omega(\beta_i)).
\tag{HC.1}
\]

`[PROVED]` Such a family would beat the binary lower exponential base for the full problem.

### HC barrier target `[CONJECTURE]`

As a meaningful negative alternative, prove for all radical-free maps with \(\dim W\le d\), for one fixed \(d\ge2\), that

\[
\log_2\tau(\beta)
\le
\frac12\omega(\beta)+o(\omega(\beta)).
\tag{HC.2}
\]

`[PROVED]` Even the case \(d=2\) would remove the first genuinely nonscalar layer and sharply narrow possible extremizers.

## Structural language to use

Choose a basis of \(W^*\). The dual map identifies \(\beta\) with a subspace

\[
\mathcal L\le\operatorname{Alt}(V)
\]

of alternating forms. Then

\[
\beta(v,w)=0
\quad\Longleftrightarrow\quad
B(v,w)=0\text{ for every }B\in\mathcal L.
\]

`[CONJECTURE]` A promising family should combine two opposing properties:

1. every large subspace of \(V\) is detected nontrivially by some form in \(\mathcal L\), forcing small common-isotropic subspaces and hence a large cover number;
2. the common nonorthogonality graph has no large clique, perhaps because low-rank combinations in \(\mathcal L\) impose many structured orthogonality relations.

Rank-metric codes, alternating matrix pencils, subspace designs, and tensor contractions are appropriate concrete languages. The scalar theorem shows that a one-dimensional pencil cannot work asymptotically.

---

# 2. Smallest falsification experiment

## Binary codomain-two census

### Experiment E1 `[CONJECTURE]`

Classify radical-free two-dimensional subspaces

\[
\mathcal L\le\operatorname{Alt}(\mathbb F_2^6)
\]

up to \(\operatorname{GL}(6,2)\times\operatorname{GL}(2,2)\), and compute the exact pair

\[
(\omega(\beta),\tau(\beta))
\]

for one representative of every orbit.

The raw Grassmannian has too many pencils for an unaudited brute-force scan. The orbit reduction should use the congruence classification of alternating pencils, Pfaffian/rank profiles, and explicit stabilizers.

## Decision criteria

- `[COMPUTED]` A representative with \(\tau(\beta)>2^{\omega(\beta)/2}\), together with exact certificates, falsifies the pointwise scalar barrier in the first higher-codomain layer and identifies a geometry worth amplifying.
- `[COMPUTED]` Exhaustion showing \(\tau(\beta)\le2^{\omega(\beta)/2}\) for every orbit would not prove HC.2 asymptotically, but would eliminate the smallest plausible counterexample and provide orbit invariants for an inductive theorem.
- `[PROVED]` A lone finite seed cannot by ordinary direct powers yield an exponential-in-\(\nu\) construction; any positive seed must be accompanied by a dimension-varying family or a new composition with proved invariant formulas.

## Required certificate format

For every retained orbit, save:

1. basis matrices for \(\mathcal L\);
2. a radical-freeness certificate;
3. an exact clique witness and an independently checkable upper certificate for \(\omega\);
4. an isotropic-subspace cover of size \(\tau\);
5. an exact lower certificate for the cover number, not merely optimizer output;
6. the triangular cocycle and group presentation in characteristic two;
7. software versions, hashes, raw logs, and an independent verifier that does not share the optimizer's code path.

`[PROVED]` A coloring alone proves only an upper bound for \(\tau\), and a clique alone proves only a lower bound for \(\omega\). Both directions require certificates before an efficiency claim is exact.

---

# 3. Family mechanisms to test before a census becomes too large

## 3.1 Tensor contraction with expanding codomain

### Candidate T1 `[CONJECTURE]`

Start from the twisted tensor vectors in this bundle, but replace the scalar norm pairing by several independent contractions into a codomain \(W_t\). Seek a map for which distinct parametrized points have a nonzero vector-valued pairing, while common-isotropic subspaces are much smaller than Lagrangians.

**Falsifier:** prove that every such contraction contains a scalar functional whose induced scalar symplectic form already controls the cover number, reducing the construction to the scalar barrier.

## 3.2 Alternating rank-metric pencils

### Candidate R1 `[CONJECTURE]`

Choose \(\mathcal L\le\operatorname{Alt}(V)\) so that every nonzero form has high rank, analogous to an MRD code. High rank may constrain common-isotropic subspaces.

**First obstruction:** high rank of individual forms does not by itself bound the clique number of the common nonorthogonality graph, and the exterior-product map shows that tiny isotropic spaces can coexist with a very large clique.

## 3.3 Subspace-design duality

### Candidate D1 `[CONJECTURE]`

Construct a family of kernels \(v^{\perp_\beta}=\{w:\beta(v,w)=0\}\) forming a subspace design: every low-dimensional test subspace should have controlled total intersection with these kernels. Translate that control into both a clique upper bound and an isotropic-cover lower bound.

**First obstruction:** a design bound usually controls average intersections, whereas \(\omega\) and \(\tau\) are worst-case integral parameters. An entropy or fractional-cover bridge must be proved rather than assumed.

---

# 4. Backup upper-bound direction

The packet proves for a finite class-two \(p\)-group \(P\), with \(m=\nu(P)\), that every abelian \(A\ge Z(P)\) satisfies

\[
[A:Z(P)]\le p^{m/p}.
\]

The uncontrolled factor is \([P:A]\).

## Aggregate charging target

### AC target `[CONJECTURE]`

Find a chain of exact centralizers

\[
P=H_0>H_1>\cdots>H_s
\]

and a potential \(\Psi\) such that

\[
\sum_{i=1}^s \log[H_{i-1}:H_i]
\le C\,\nu(P)
\]

while the terminal subgroup has a controlled abelian layer.

`[DISPROVED]` The summand cannot be charged only to the individual drop \(\nu(H_{i-1})-\nu(H_i)\); the packet's class-two counterexamples and the binary drop-two family rule that out.

`[CONJECTURE]` A viable potential must amortize several centralizer steps at once, perhaps through the rank growth of the combined commutator map

\[
P/Z(P)\longrightarrow\prod_i [x_i,P],
\qquad gZ(P)\longmapsto([x_i,g])_i,
\]

while controlling cancellation and dependencies among the coordinates.

## Structured coset-cover target

### CC target `[CONJECTURE]`

Prove a fixed-base intersection-index theorem only for abelian coset covers whose subgroups are kernels of commutator homomorphisms arising from one group. The theorem must use a property absent from arbitrary irredundant covers; otherwise it would run into the packet's withdrawn-preprint warning.

---

# 5. Historical cutoff-eight laboratory

`[PROVED]` The two branches below were open in the source packet used for
this research run.  The surrounding repository subsequently closed both and
proved \(h(8)=10\).  The proposed mechanisms remain recorded only as
superseded stress tests; they are no longer open dependencies.

## Binary all-nonmaximal branch

### H8-B target `[CONJECTURE]`

Use the odd-circuit normals of the maximalized cover to recover one exact feature lost under maximalization: either a true maximal clique centralizer, an exact private cell, or a bounded family of pairwise intersections sufficient for a ten-subgroup cover.

**Smallest falsifier:** construct a finite \(2\)-group with \(\nu=8\), all eight maximum-clique centralizers nonmaximal, and a certified abelian-cover number above ten.

## Solvable nontrivial-core branch

### H8-S target `[CONJECTURE]`

Exploit the restricted affine quotient action on the core \(R\). Prove that the eight external fixed subgroups induced on \(R\) either reduce to exact centralizers in a controlled extension or admit a bounded abelian refinement.

**Smallest falsifier:** one explicit action/core pair from the seven affine skeletons whose induced fixed-subgroup cover is irredundant and cannot be refined to ten abelian subgroups.

`[PROVED]` Work at cutoff eight should be judged by whether it produces a reusable cover/core invariant; a census with no structural extraction would not address the global asymptotic obstruction.

---

# 6. Recommended order of attack

1. `[PROVED]` Begin with the codomain-two orbit problem in dimension six, because it is the smallest genuinely nonscalar setting not ruled out by the new theorem.
2. `[CONJECTURE]` Use its orbit invariants to formulate either a codomain-two barrier theorem or a dimension-varying construction.
3. `[CONJECTURE]` In parallel, test tensor contractions and alternating rank-metric pencils for a family-level mechanism, not isolated seeds.
4. `[CONJECTURE]` Return to the aggregate centralizer potential only after identifying an invariant that survives the binary drop-two counterfamily.
5. `[CONJECTURE]` Use the now-closed \(h(8)\) proof branches as adversarial finite tests for any proposed cover/core invariant.

---

# 7. Exact next decision

`[UNVERIFIED]` **The next decisive question is:** does codomain two already permit an asymptotic efficiency above \(\log2/2\), or can one prove a scalar-strength barrier for every radical-free alternating pencil?
