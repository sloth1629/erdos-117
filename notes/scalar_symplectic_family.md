# Scalar Symplectic Groups over Arbitrary Finite Fields

This note places both the binary family and the order-\(3^5\) counterexample
in one exact framework. It also identifies the unresolved parameter as a
standard finite-geometric extremal number.

## Construction and commutation geometry

Let \(q\) be a prime power and \(m\geq1\). On

\[
S(q,m)=\mathbb F_q^m\times\mathbb F_q^m\times\mathbb F_q
\]

define

\[
(x,y,z)(x',y',z')
=
(x+x',\,y+y',\,z+z'+x\mathbin\cdot y').
\]

### Theorem SS.1 [PROVED]

This operation makes \(S(q,m)\) a finite group of order \(q^{2m+1}\), with

\[
Z(S(q,m))=\{(0,0,z):z\in\mathbb F_q\}.
\]

On the central quotient
\(V=\mathbb F_q^m\oplus\mathbb F_q^m\), commutation is orthogonality for the
nondegenerate alternating form

\[
B((x,y),(x',y'))=x\mathbin\cdot y'-x'\mathbin\cdot y.
\]

**Proof.** Bilinearity of the cocycle \(x\cdot y'\) proves associativity,
\((0,0,0)\) is the identity, and

\[
(x,y,z)^{-1}=(-x,-y,-z+x\mathbin\cdot y).
\]

Direct multiplication gives the displayed commutator form. Its radical is
zero: pairing \((x,y)\) first with all \((0,y')\), then with all \((x',0)\),
forces \(x=y=0\). The asserted center and commutation rule follow. \(\square\)

Let \(\pi(q,m)\) denote the largest number of one-dimensional subspaces of
the symplectic space \(V\) that are pairwise nonorthogonal. In finite-geometry
language, this is the maximum size of a partial ovoid of
\(W(2m-1,q)\).

### Corollary SS.2 [PROVED]

\[
\nu(S(q,m))=\pi(q,m).
\]

**Proof.** Nonzero scalar multiples are mutually orthogonal and have the
same orthogonality relations with every other vector, so a nonorthogonal set
uses at most one vector from each projective point. Conversely, choose one
nonzero representative from every point of a partial ovoid and then choose
arbitrary representatives of the corresponding central cosets. \(\square\)

## Exact abelian-cover number

### Theorem SS.3 [PROVED]

For every prime power \(q\) and \(m\geq1\),

\[
a(S(q,m))=q^m+1.
\]

**Proof.** The image \(U\) of an abelian subgroup in \(V\) is an additive
subgroup on which \(B\) vanishes. Its \(\mathbb F_q\)-linear span is still
totally isotropic, by bilinearity. A totally isotropic subspace lies in its
orthogonal complement, and nondegeneracy gives dimension at most \(m\).
Thus \(U\) has at most \(q^m\) vectors, of which at most \(q^m-1\) are
nonzero. Covering the \(q^{2m}-1\) nonzero central cosets therefore needs at
least

\[
\frac{q^{2m}-1}{q^m-1}=q^m+1
\]

abelian subgroups.

For equality, identify \(V\), up to symplectic isometry, with
\(\mathbb F_{q^m}^2\) equipped with

\[
((u,v),(u',v'))
\longmapsto
\operatorname{Tr}_{\mathbb F_{q^m}/\mathbb F_q}(uv'-u'v).
\]

Here the trace pairing is nondegenerate: if \(u\ne0\), choose \(w\) with
\(\operatorname{Tr}(w)\ne0\) (the trace map is a nonzero
\(\mathbb F_q\)-linear functional for finite separable fields) and take
\(v'=u^{-1}w\); the other coordinate is identical. Thus the displayed form
is nondegenerate alternating. The usual symplectic-basis induction shows
that any two nondegenerate alternating forms of dimension \(2m\) over
\(\mathbb F_q\) are isometric.

The \(q^m+1\) one-dimensional \(\mathbb F_{q^m}\)-subspaces of
\(\mathbb F_{q^m}^2\) are \(m\)-dimensional totally isotropic
\(\mathbb F_q\)-subspaces, meet pairwise only in zero, and partition the
nonzero vectors. Their full preimages in \(S(q,m)\) are abelian subgroups
forming a cover of the required size. \(\square\)

## General clique construction and exact special cases

### Proposition SS.4 [PROVED]

\[
\pi(q,m)\geq mq+1.
\]

**Proof.** A symplectic plane has a set of \(q+1\) pairwise
nonorthogonal projective points, one from each one-dimensional subspace;
choose one nonzero vector representative for every point below.
If \(A\) and \(C\) are nonorthogonal sets in orthogonal symplectic summands
\(V_1,V_2\), fix \(c_0\in C\) and form

\[
\{(a,c_0):a\in A\}
\ \cup\
\{(0,c):c\in C\setminus\{c_0\}\}.
\]

The first part is nonorthogonal because \(A\) is, the second because \(C\)
is, and every cross-pair has nonzero pairing
\(B_2(c_0,c)\). Its size is \(|A|+|C|-1\). Induction over an orthogonal
sum of \(m\) symplectic planes gives \(m(q+1)-(m-1)=mq+1\). \(\square\)

The following values are proved elsewhere in the repository:

- [PROVED] \(\pi(2,m)=2m+1\), by the Gram-rank argument in
  notes/class_two_geometry.md.
- [PROVED] \(\pi(q,1)=q+1\), since distinct projective points in a
  symplectic plane are nonorthogonal.
- [PROVED] \(\pi(3,2)=7\), by the normalized four-direction case analysis
  in notes/candidate_bound.md.

Consequently,

\[
(\nu,a)(S(2,m))=(2m+1,2^m+1),
\qquad
(\nu,a)(S(3,2))=(7,10).
\]

## Twisted-tensor scalar barrier

### Theorem SS.5 [PROVED]

For every prime power \(q\) and every odd \(t\ge1\),

\[
\pi(q,2^{t-1})\ge q^t+1.
\]

The proof in
`results/scalar_twisted_tensor/GLOBAL_RESEARCH_REPORT.md` descends the
\(t\)-fold tensor power of the determinant form from
\(\mathbb F_{q^t}\) to a \(2^t\)-dimensional \(\mathbb F_q\)-space.  The
Frobenius-twisted image of \(\operatorname{PG}(1,q^t)\) has pairings
\(N_{\mathbb F_{q^t}/\mathbb F_q}(ad-bc)\), so its \(q^t+1\) points are
pairwise nonorthogonal.  The characteristic-two zero-diagonal issue and the
fixed-space dimension are handled explicitly there.

Combining these seeds with Proposition SS.4's orthogonal gluing gives the
following exact asymptotic conclusion for the scalar family:

\[
\log h_{\mathrm{sc},\ne2}(n)=o(n),
\qquad
\lim_{n\to\infty}h_{\mathrm{sc}}(n)^{1/n}=\sqrt2.
\]

Moreover, except for \((q,m)=(2,1)\),

\[
q^m+1\le2^{\pi(q,m)/2}.
\]

Thus the order-\(3^5\) example beats the proposed exact binary formula at the
finite cutoff seven, but no scalar-valued field-linear symplectic family can
beat the binary asymptotic base.  Any asymptotic improvement must leave this
class.

## What remains open in this family

[UNVERIFIED] Exact values of \(\pi(q,m)\) remain difficult in general.  The
new theorem determines the exponential optimization of the whole scalar
envelope, but it does not determine the full finite table or provide a
universal upper bound for higher-codomain commutator maps or arbitrary
groups.
