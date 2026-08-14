# The finite \(5\)-group branch at cutoff eight

## A small hyperplane-cover lemma

`[PROVED]` (computer-assisted) Let \(V\) be a finite-dimensional vector
space over \(\mathbf F _5\). If at most eight distinct hyperplanes cover \(V\),
then six of them are the full pencil through a common codimension-two
subspace. Equivalently, their six projective normal vectors are all the
points of one projective line.

Here is a self-contained reduction to the finite certificate. Let \(B\) be
the set of projective normal vectors, let \(d=\dim\langle B\rangle\), choose
\(d\) independent members of \(B\), and change coordinates so that they are
the coordinate points \(e_1,\ldots,e_d\). The cover property descends to the
span of \(B\): every hyperplane of that span is the kernel of evaluation at
some vector in the original primal space. Thus it is enough to work in
\(\mathbf F _5^d\).

The coordinate hyperplanes cover every projective vector having a zero
coordinate. The remaining projective torus has

\[
  4^{d-1}
\]

points. If an additional normal has support one, it covers no torus point.
Otherwise normalize at a nonzero coefficient, choose a second nonzero
coefficient, and fix the other \(d-2\) nonzero coordinates. The orthogonality
equation determines at most one value of the remaining coordinate, so one
additional hyperplane covers at most \(4^{d-2}\) torus points. For \(d\ge5\),

\[
  (8-d)4^{d-2}<4^{d-1},
\]

so no cover exists. Dimension one is also impossible. The zero-dimensional
case has no projective normal and is vacuous.

`[COMPUTED]` The verifier
`src/verification/verify_f5_small_hyperplane_cover.py` exhausts the remaining
dimensions \(d=2,3,4\). It normalizes the independent members to the
coordinate points, represents the torus zero sets as bit masks, enumerates
every possible subfamily of size at most \(8-d\), and checks directly that
every covering subfamily contains all six points of a projective line. The
exact census is:

| \(d\) | torus points | candidates actually enumerated | subfamilies checked | covers | covers without a line |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 4 | 16 | 1 | 0 |
| 3 | 16 | 28 | 122,438 | 87 | 0 |
| 4 | 64 | 24 | 10,626 | 6 | 0 |

For \(d=4\), all 152 non-coordinate normals are first checked. A normal
vanishes on at most 16 torus points, and exactly 24 attain 16. A cover by at
most four extras must therefore use exactly four of those 24 maximum masks;
this explains the smaller enumerated candidate column without omitting a
possible cover. The regression test rebuilds the enumeration rather than
trusting a saved list of covers.

The six normals on a projective line do cover \(V\): evaluation at any vector
has a nonzero kernel on their two-dimensional span. Their hyperplanes have a
common codimension-two intersection \(D\), and every vector outside \(D\)
lies in exactly one member of the pencil.

## Excluding clique number eight

`[CITED-VERIFIED]` Berkovich, *Glasnik Mat.* 45 (2010), Proposition 4.5,
printed pp. 425--426, states that if a finite \(p\)-group is covered by
\(k\le2p\) proper subgroups, then at least \(p\) cover members are maximal;
when \(p>3\) and \(p+2<k<2p\), at least \(p+1\) are maximal. The paper's
standing convention on printed p. 415 is that all groups are finite.

`[PROVED]` No finite \(5\)-group has \(\nu(P)=8\). Suppose otherwise and
choose a maximum clique \(x_1,\ldots,x_8\). Its distinct proper centralizers

\[
  H_i=C_P(x_i)
\]

form an irredundant cover: maximality of the clique gives the cover, and
\(x_i\) is not in any \(H_j\) with \(j\ne i\). Proposition 4.5, with
\(p=5\) and \(k=8\), says that at least six of the \(H_i\) are maximal.

Enlarge each of the at most two nonmaximal \(H_i\) to a maximal subgroup
\(M_i\). Maximal subgroups of a finite \(5\)-group contain \(\Phi(P)\), so the
resulting cover is a cover by at most eight hyperplanes of
\(P/\Phi(P)\). The preceding lemma supplies a six-member pencil. At least one
pencil member \(M\) is not an original \(H_i\), since otherwise six original
members already cover \(P\), contradicting irredundancy. Notice also that an
enlargement of a nonmaximal \(H_i\) cannot equal another original \(H_j\):
then \(H_i\subseteq H_j\), again contradicting irredundancy.

Let \(D\) be the common intersection of the pencil. Choose one original index
for each of the five pencil hyperplanes other than \(M\). On intersecting the
original eight-member cover with \(M\), those five chosen original subgroups
contribute only subsets of \(D\). Hence

\[
  M=D\mathbin{\cup}
    \bigcup_{i\in I}(M\cap H_i),
  \qquad |I|\le3.
\]

All displayed subgroups are proper in \(M\). Indeed, \(D\) has index five in
each pencil member, and \(M\cap H_i=M\) would force \(H_i=M\) because \(M\)
is maximal in \(P\), contrary to the choice of \(M\) as a genuinely new
enlargement. Thus the finite \(5\)-group \(M\) is covered by at most four
proper subgroups. This is impossible: after enlarging any such subgroups to
maximal ones, each has at most \(|M|/5-1\) nonidentity elements, so five or
fewer cover at most

\[
  1+5(|M|/5-1)=|M|-4
\]

elements.

`[PROVED]` Combining this exclusion with Berkovich's verified Lemma 1.2,
Theorem 2.3, and Theorem 4.4 gives the exact finite \(5\)-group cutoff:
if \(\nu(P)\le8\), then either \(P\) is abelian and
\((\nu(P),a(P))=(1,1)\), or

\[
  (\nu(P),a(P))=(6,6).
\]

The lower bound \(\nu(P)\ge6\) for nonabelian \(5\)-groups is Lemma 1.2;
Theorem 4.4 excludes \(\nu=7=p+2\); the argument above excludes \(\nu=8\);
and Theorem 2.3 gives \(P=HZ(P)\), where \(H\) is minimal nonabelian. The
centralizers in \(H\) of a maximum six-clique are six proper subgroups
covering \(H\); every proper subgroup of the minimal nonabelian group \(H\)
is abelian. Adjoining the central subgroup \(Z(P)\) therefore gives six
abelian subgroups covering \(P\). Since every abelian cover has at least
\(\nu(P)=6\) members, this proves \(a(P)=6\). This closes the finite
\(5\)-group branch only; by itself it neither classified the finite
\(2\)-group branch nor controlled the nonnilpotent solvable branch.  Those
later branches are closed separately in the exact proof of \(h(8)=10\).

## Reproduction

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-f5-hyperplane-pycache \
python3 -m unittest src.verification.test_f5_small_hyperplane_cover -v
PYTHONPYCACHEPREFIX=/tmp/erdos117-f5-hyperplane-pycache \
python3 src/verification/verify_f5_small_hyperplane_cover.py
```

`[COMPUTED]` The saved targeted transcript is
`experiments/logs/f5_small_hyperplane_cover_verification.txt`. The verifier
uses only the Python standard library and runs in substantially less than one
second on the recorded environment.
