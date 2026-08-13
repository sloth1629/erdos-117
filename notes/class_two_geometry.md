# A Self-Contained Class-Two Lower-Bound Construction

This note gives an independent construction; the historical attribution remains a separate source-audit question.

## The groups

Fix \(m\geq1\). Let

\[
E_m=\mathbb F_2^m\times\mathbb F_2^m\times\mathbb F_2
\]

with multiplication

\[
(a,b,c)(a',b',c')=(a+a',\ b+b',\ c+c'+b\mathbin\cdot a').
\]

Bilinearity of the dot product proves associativity.  The identity is
\((0,0,0)\), and

\[
(a,b,c)^{-1}=(a,b,c+b\mathbin\cdot a),
\]

so this operation does define a group. Direct calculation gives

\[
[(a,b,c),(a',b',c')]=(0,0,\ b\cdot a'+b'\cdot a).
\]

Hence

\[
Z(E_m)=\{(0,0,c):c\in\mathbb F_2\},
\]

and the central quotient is the \(2m\)-dimensional vector space

\[
V=\mathbb F_2^m\times\mathbb F_2^m
\]

with nondegenerate alternating form

\[
B((a,b),(a',b'))=b\cdot a'+b'\cdot a.
\]

Thus two central cosets commute exactly when their vectors are orthogonal under \(B\).

## Maximum pairwise-noncommuting set

### Theorem C2.1 `[PROVED]`

\[
\nu(E_m)=2m+1.
\]

**Proof.** Suppose \(v_1,\ldots,v_r\in V\) are pairwise nonorthogonal. Over \(\mathbb F_2\), this means \(B(v_i,v_j)=1\) for all \(i\ne j\). Their Gram matrix is the \(r\times r\) matrix \(A_r\) with zero diagonal and one off the diagonal. Its rank over \(\mathbb F_2\) is \(r\) for even \(r\) and \(r-1\) for odd \(r\): if \(s=\sum_jx_j\), then \((A_rx)_i=s+x_i\), which describes the kernel immediately. Since a Gram matrix in \(V\) has rank at most \(2m\), we get \(r\leq2m+1\).

For equality, \(A_{2m}\) is a nondegenerate alternating matrix. The standard symplectic-basis induction shows that all nondegenerate alternating forms of dimension \(2m\) over \(\mathbb F_2\) are isometric. Therefore there are \(v_1,\ldots,v_{2m}\in V\) with Gram matrix \(A_{2m}\). Put \(v_{2m+1}=v_1+\cdots+v_{2m}\). For every \(j\),

\[
B(v_j,v_{2m+1})=2m-1=1\pmod2.
\]

So these \(2m+1\) vectors, and arbitrary representatives of their central cosets, are pairwise noncommuting. \(\square\)

## Minimum abelian cover

### Theorem C2.2 `[PROVED]`

\[
a(E_m)=2^m+1.
\]

**Proof.** The image in \(V\) of any abelian subgroup is a totally isotropic subspace. Conversely, the full preimage of every totally isotropic subspace is abelian. More generally, every pairwise commuting set of cosets spans a totally isotropic subspace. If \(L\) is totally isotropic, then \(L\subseteq L^\perp\), so \(\dim L\leq m\). Thus a commuting color class contains at most \(2^m-1\) nonzero vectors. Since the \(2^{2m}-1\) nonzero vectors must all be colored,

\[
a(E_m)=\chi(\Gamma_{E_m})
\geq\frac{2^{2m}-1}{2^m-1}=2^m+1.
\]

For the reverse inequality, put \(q=2^m\), identify \(V\) with \(\mathbb F_q^2\) over \(\mathbb F_2\), and use the isometric symplectic form

\[
((x,y),(x',y'))\longmapsto
\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(xy'+x'y).
\]

The \(q+1\) subspaces

\[
L_t=\{(x,tx):x\in\mathbb F_q\}\quad(t\in\mathbb F_q),
\qquad
L_\infty=\{(0,y):y\in\mathbb F_q\}
\]

are being viewed through a symplectic isometry with the original form. To
justify it explicitly, the finite-field trace pairing is nondegenerate: for
\(x\ne0\), choose \(w\) with \(\operatorname{Tr}(w)=1\) and put
\(y=x^{-1}w\). The displayed alternating form is therefore nondegenerate,
and the symplectic-basis induction identifies it with every other
nondegenerate alternating form of dimension \(2m\) over \(\mathbb F_2\).
The subspaces are totally isotropic, meet pairwise only in zero, and
partition \(V\setminus\{0\}\). Their preimages in \(E_m\) are \(q+1\)
abelian subgroups covering \(E_m\). \(\square\)

## Consequence for \(h(n)\)

### Corollary C2.3 `[PROVED]`

For every \(m\geq1\),

\[
h(2m+1)\geq2^m+1.
\]

In particular,

\[
\liminf_{n\to\infty}h(n)^{1/n}\geq\sqrt2.
\]

**Proof.** The first assertion follows from Theorems C2.1 and C2.2. Monotonicity of \(h\) transfers the odd-index bounds to intervening even indices, and taking roots gives the limit inferior. \(\square\)

## Structural lesson

`[PROVED]` The direct product \(E_1^m\) has a vector-valued, coordinatewise commutator constraint and its compressed graph is an OR power. The group \(E_m\) instead combines the \(m\) coordinate commutators into one scalar symplectic form. This central-product phenomenon keeps \(\nu\) linear in \(m\) while making \(a\) exponential in \(m\).
