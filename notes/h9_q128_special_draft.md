# Cutoff Nine at Center Quotient Order \(128\): Special-Case Draft

## Scope

This isolated note is not integrated into the cutoff-nine reduction.
It records the proved structural part of two special order-\(128\)
quotients, promotes the \(C_2^4\times D_8\) restriction census, and states
the remaining \(C_2^7\) finite certificate exactly.  It does not claim
\(h(9)=17\).

## The elementary quotient \(C_2^7\)

Let \(V=\mathbb F_2^7\), let \(W\) be an elementary abelian \(2\)-group,
and let

\[
 B:V\times V\longrightarrow W
\]

be alternating and bilinear.  Write

\[
 B_v(x)=B(v,x),\qquad
 \operatorname{rad}B=\{v:B_v=0\}.
\]

For an exact center quotient, \(\operatorname{rad}B=0\).

### [PROVED] An exact six-dimensional restriction exists

There is a hyperplane \(H<V\) such that

\[
 \operatorname{rad}(B|_{H\times H})=0.
\tag{S128.1}
\]

Suppose instead that every hyperplane is inexact.  For each hyperplane
\(H\), choose \(0\ne v_H\in H\) with \(B(v_H,H)=0\).  Exactness gives
\(B_{v_H}\ne0\), while \(H\le\ker B_{v_H}\).  Hence

\[
 \ker B_{v_H}=H,\qquad \operatorname{rank}B_{v_H}=1.
\tag{S128.2}
\]

There are \(127\) hyperplanes and \(127\) nonzero vectors in \(V\).  The
map

\[
 \{0\ne v:\operatorname{rank}B_v=1\}
 \longrightarrow\{\text{hyperplanes of }V\},\qquad
 v\longmapsto\ker B_v
\]

is surjective by (S128.2).  Therefore every \(0\ne v\in V\) has
\(\operatorname{rank}B_v=1\).

The contractions

\[
 \mathcal M=\{B_v:v\in V\}\le\operatorname{Hom}(V,W)
\]

form a linear space all of whose nonzero members have rank one.  Such a
space has either a common image line or a common kernel.  Indeed, two
rank-one maps with both different image lines and different kernels have
rank-two sum.  Thus every pair has the same image or the same kernel.
If one pair has different images, it has a common kernel \(K\); comparison
with that pair forces every other nonzero map to have kernel \(K\).
If no pair has different images, all images are the same line.

A common kernel is contained in \(\operatorname{rad}B\), contradicting
exactness.  A common image line makes \(B\) a scalar alternating form.
Every scalar alternating form in odd dimension has nonzero radical.
This is the other contradiction and proves (S128.1).

### Dual form-space notation

Put

\[
 L=\operatorname{im}\bigl(B^*:W^*\to\operatorname{Alt}(V)\bigr).
\]

Then two vertices \(x,y\in V\) are adjacent exactly when
\(\beta(x,y)=1\) for some \(\beta\in L\), and exactness says that the
members of \(L\) have zero common radical.  Let \(U\) be a hyperplane
given by (S128.1), choose \(e\notin U\), and set

\[
 R=\operatorname{res}_U L\le\operatorname{Alt}(U),\qquad
 T=\ker(\operatorname{res}_U:L\to R)\le U^*.
\tag{S128.3}
\]

Here \(t\in U^*\) represents the cross form \(e^*\wedge t\).
Choose a linear section of the restriction map.  It has the form

\[
 r\longmapsto r+e^*\wedge f(r)
\]

for a linear map \(f:R\to U^*\), and

\[
 L=
 \{\,r+e^*\wedge(f(r)+t):r\in R,\ t\in T\,\}.
\tag{S128.4}
\]

Changing the section replaces \(f\) by
\(f+g\), where \(g\in\operatorname{Hom}(R,T)\).  Replacing \(e\) by
\(e+u\) replaces \(f\) by

\[
 f+j_u,\qquad j_u(r)=r(u,-).
\tag{S128.5}
\]

### [PROVED] Exactness and section normalization

Assume \(R\) contains a nondegenerate alternating form.  Then

\[
 J=\{j_u:u\in U\}\le\operatorname{Hom}(R,U^*)
\]

has order \(64\).  If \(T=0\), the global form space \(L\) is inexact
exactly when \(f\in J\): in that case \(e+u\) is a common radical vector
for \(f=j_u\), and the converse follows by evaluating a common radical
vector outside \(U\) on every \(x\in U\).  If \(T\ne0\), no vector outside
\(U\) can lie in the common radical, because a nonzero cross form
\(e^*\wedge t\) detects it; exactness on \(U\) handles vectors in \(U\).

Consequently, for a fixed \(d\)-dimensional restriction space \(R\), the
\(T=0\) exact sections number

\[
 2^{6d}-64.
\tag{S128.6}
\]

### [PROVED] A nondegenerate restriction branch has dimension at most three

Suppose \(R\le\operatorname{Alt}(\mathbb F_2^6)\) has a union graph
with no ten-clique and contains a nondegenerate form \(\beta\).  For any
\(\gamma\notin\langle\beta\rangle\), the pencil
\(\langle\beta,\gamma\rangle\) is a subspace of \(R\).  The canonical
rank-six-pencil certificate exhausts all such pencils and has only one
orbit of clique number at most nine: its rank profile is \((6,6,6)\)
and its clique number is nine.  Hence every nonzero member of \(R\) is
nondegenerate.

Let \(p\) be the Pfaffian of a six-dimensional alternating form.  Its
restriction to the \(d\)-space \(R\) is a polynomial of degree at most
three satisfying

\[
 p(0)=0,
 \qquad
 p(r)=1\quad(0\ne r\in R).
\]

As a Boolean function on \(\mathbb F_2^d\), the right-hand side is the
nonzero indicator.  Its unique algebraic normal form is

\[
 1+\prod_{i=1}^d(1+x_i),
\]

which has degree \(d\).  Therefore \(d\le3\).  Thus the nondegenerate
branch of the finite input below only needs to classify the unique
\((6,6,6)\) pencil and its three-dimensional extensions; no form space
of dimension at least four can occur.

### [UNVERIFIED] The finite six-dimensional input awaiting promotion

Current scratch computations report that every exact
\(R\le\operatorname{Alt}(\mathbb F_2^6)\) whose union graph has clique
number at most nine is, up to \(\mathrm{GL}_6(2)\), one of:

1. \(R_1=\langle2180\rangle\), a nondegenerate scalar line;
2. \(R_2=\langle2180,728\rangle\), the rank profile \(6,6,6\) pencil;
3. \(R_3=\langle728,1484,2180\rangle\), an all-nondegenerate
   three-space.

The same scratch scan reports that every exact \(T=0\) section over
\(R_2\) or \(R_3\) has a ten-clique.  The exact state count is

\[
 (2^{12}-64)+(2^{18}-64)=4032+262080=266112.
\tag{S128.7}
\]

These assertions require a canonical artifact, complete witness checks,
and an independent unit test before they can be cited as [COMPUTED].

### [PROVED] Conditional completion of the section argument

Assume the finite statement above.  Then no exact \(L\) over \(C_2^7\)
has clique number at most nine.

First let \(R\in\{R_2,R_3\}\).  If \(T=0\), (S128.7) gives a ten-clique.
Suppose \(T\ne0\).  The graph of every section

\[
 L_g=\{r+e^*\wedge g(r):r\in R\},\qquad
 g\in\operatorname{Hom}(R,T),
\]

is a subgraph of the graph of \(L\).  The finite section statement says
that a no-ten-clique section must have \(g\in J\).  After (S128.5), take
the initial section to be zero.  Thus no-ten-clique would force

\[
 \operatorname{Hom}(R,T)\le J.
\tag{S128.8}
\]

Choose \(0\ne t\in T\), a nondegenerate \(r_0\in R\), and a nonzero
functional \(\lambda\in R^*\) with \(\lambda(r_0)=0\); this is possible
because \(\dim R\ge2\).  The nonzero map

\[
 g(r)=\lambda(r)t
\]

cannot equal \(j_u\).  Indeed \(g(r_0)=0\) would give
\(r_0(u,-)=0\), hence \(u=0\), while \(g\ne0\).  This contradicts
(S128.8).

It remains to handle \(R_1\).  If \(T=0\), every \(f:R_1\to U^*\) equals
\(j_u\) for a unique \(u\), since the generator \(2180\) is
nondegenerate.  Thus the global form is inexact.  If \(T\ne0\), normalize
\(f=0\) and choose \(0\ne t\in T\).  The symplectic group of \(2180\) is
transitive on nonzero covectors, so \(L\) contains a copy of

\[
 \langle2180,\ e^*\wedge e_0^*\rangle.
\]

In the seven-bit encoding with \(e\) in coordinate six, the ten vertices

\[
 3,9,17,19,65,75,89,91,12,40
\tag{S128.9}
\]

are pairwise adjacent.  Direct evaluation checks all \(45\) pairs:
\(29\) have signature \((1,0)\), \(12\) have \((0,1)\), and \(4\) have
\((1,1)\).  This closes the scalar branch without computation beyond the
displayed witness.

## The quotient \(C_2^4\times D_8\)

Let

\[
 Q=C_2^4\times D_8=\operatorname{SmallGroup}(128,2320),
\]

and choose the index-two subgroup

\[
 Q_0=C_2^3\times D_8=\operatorname{SmallGroup}(64,261).
\]

### [PROVED] The all-even restriction cannot be repaired

The canonical \(Q_0\) export identifies its all-even obstruction as
quotient vertex \(v_6\), with pc exponent vector

\[
 (0,0,0,0,0,1).
\]

Every all-even exterior character annihilates the full commutator row of
\(v_6\), so \(v_6\) lies in the radical of every all-even restricted
graph.  Moreover, the saved quotient conjugation and exponent data show
that

\[
 v_6\in Q_0'.
\tag{S128.10}
\]

Concretely, the first exported conjugation sends quotient vertex \(2\),
whose pc exponent vector is \((0,1,0,0,0,0)\), to vertex \(15\), whose
normal form has exponent vector \((0,1,0,0,0,1)\).  If \(q\in Q_0\)
induces this saved conjugation, then

\[
 [v_2,q]=v_2^{-1}v_2^q=v_6,
\]

which proves (S128.10).

Now let \(G/Z(G)=Q\), let \(H\) be the inverse image of \(Q_0\), and
let \(t\) lift the extra central direct-factor generator.  The map

\[
 \Delta:H\longrightarrow Z(G),\qquad x\longmapsto[t,x]
\]

is a homomorphism and is trivial on both \(H'\) and \(Z(G)\).  It
therefore factors through \(Q_0/Q_0'\), so it cannot remove the radical
element in (S128.10).  Thus an exact global graph cannot have an
all-even restriction.

Consequently, under the no-ten-clique hypothesis, the restriction
contains an odd character.  The repaired scalar bridge says that every
one of its characters belongs to the same target-ten good universe

\[
 H_{\mathrm{even}}\ \cup\ (x+U)
\]

used by the canonical affine enumeration.  The subgroup argument from
the cutoff-seven certificate then places the restriction among its
\(26{,}387\) action-invariant affine subgroups.

### [PROVED] The restriction must have a small nontrivial radical

For an exact central extension at clique cutoff nine, the restriction to
\(Q_0\) cannot be exact.  The canonical bounded cutoff certificate for
\(\operatorname{SmallGroup}(64,261)\) has minimum clique number \(13\)
over all exact-center graphs.  Let \(H\) be the inverse image of \(Q_0\)
in \(G\).  Its restricted radical

\[
 R_0=Z(H)/Z(G)
\]

is therefore nontrivial.

Let \(t\in G\) lift the extra central direct-factor element.  The map

\[
 R_0\longrightarrow Z(G),\qquad rZ(G)\longmapsto[t,r]
\]

is injective: here \(r\in Z(H)\), and its kernel would be a global
central element.  Since representatives of \(R_0\) centralize \(H\),
the coset set

\[
 tR_0=\{trZ(G):rZ(G)\in R_0\}
\]

is a clique.  Hence a cutoff-nine graph forces

\[
 2\le |R_0|\le8.
\tag{S128.11}
\]

### [PROVED] Radical-twist amplification

Let \(G\) be an exact central extension with \(G/Z(G)=Q\), let \(H\)
be the inverse image of \(Q_0\), and let \(t\in G\) lift the extra
central direct-factor generator.  Put

\[
 R=Z(H)/Z(G).
\]

Then

\[
 \nu(G)\ge |R|+\nu(H).
\tag{S128.12}
\]

Indeed, since \(tZ(G)\) is central in \(G/Z(G)\), the map

\[
 \Delta:H\longrightarrow Z(G),\qquad x\longmapsto[t,x]
\]

is a homomorphism.  Its restriction to \(Z(H)\) induces an injective
map on \(R\): an element of its kernel centralizes both \(H\) and
\(t\), while \(G=\langle H,t\rangle\), so it lies in \(Z(G)\).
Consequently the \(|R|\) cosets

\[
 \{trZ(G):rZ(G)\in R\}
\]

are pairwise noncommuting: for distinct \(rZ(G),sZ(G)\in R\),

\[
 [tr,ts]=\Delta(s)\Delta(r)^{-1}\ne1.
\]

Now take representatives in \(H\) of a maximum clique in the restricted
extension graph on the \(Z(G)\)-cosets of \(H\), equivalently a maximum
noncommuting set \(X\) in \(H\).  This is the stored restricted value
\(\nu(H)\); no ordinary quotient-group commutation graph is being used.
Multiplying each representative independently by an element of \(Z(H)\)
does not change any commutator inside \(X\).  For a fixed representative
\(x\), at most one coset \(rZ(G)\in R\) satisfies

\[
 \Delta(xr)=1,
\]

because \(\Delta|_R\) is injective.  Since \(|R|>1\), choose a twist
outside that exceptional coset for every member of \(X\).  Every
twisted member then fails to commute with every member of \(tR\),
because elements of \(Z(H)\) commute with all of \(H\), and explicitly

\[
 [xr_x,tr]=[xr_x,t]=\Delta(xr_x)^{-1}\ne1.
\]

Their union is the clique asserted in (S128.12).
There are no hidden collisions: two twisted members cannot coincide
modulo \(Z(G)\), since their original representatives would then differ
by an element of \(Z(H)\) and would commute; the members of \(tR\) are
distinct by the chosen \(Z(G)\)-cosets; and \(tR\) is disjoint from the
twisted set because their images in \(Q_0\times\langle e\rangle\) have
different \(e\)-coordinates.

### [COMPUTED] Exact restriction census and completion

The saved target-ten restriction census and its independent verifier
exhaust all \(26{,}387\) affine invariant dual subgroups for \(Q_0\).
Precisely \(204\) restrictions survive without a ten-clique, with
signatures

\[
\begin{array}{c|c|c}
 \nu(H)&|Z(H):Z(G)|&\text{number}\\
 \hline
 9&4&140\\
 6&4&56\\
 5&8&8.
\end{array}
\tag{S128.13}
\]

The repaired scalar bridge independently shows that the affine universe
is complete at target ten.  The canonical artifact stores a checked
ten-clique for every eliminated boundary record, exact clique witnesses
for the \(204\) survivors, source hashes, and the four automorphism
orbits of sizes \(8,28,56,112\).  Combining (S128.13) with (S128.12)
gives cliques of sizes \(13\), \(10\), and \(13\), respectively.  Thus
the quotient \(C_2^4\times D_8\) is eliminated at cutoff nine without
enumerating the five new exterior coordinates.

The saved certificate can be checked independently by either command

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
  python3 src/verification/verify_h9_sg261_target10_restrictions.py --verify
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
  python3 -m unittest src.verification.test_h9_sg261_target10_restrictions -v
```
