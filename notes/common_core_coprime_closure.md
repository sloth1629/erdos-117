# Coprime closure of the nonnilpotent cutoff-eight residual

## [PROVED] Scope and conclusion

This note starts from the independently audited reductions
notes/common_core_frattini_reduction.md and
notes/common_core_binary_semidirect.md, at respective frozen SHA-256
values

    951a907c096e4a68b7dcc850954db04c051ea5fd7eeb3f830cd9fc1a1f92c4c6
    748f9aecc695bc3a18a3e3a43bf37ec1fc6b63e493ac1d84d9aa39641d61696e

Thus a finite exact model \(E\) in the unresolved solvable nonnilpotent
branch, with \(\nu(E)=8\) and \(a(E)>10\), has

\[
 Q:=E/Z(E)\cong C_3\rtimes_\chi S,
 \qquad \chi:S\twoheadrightarrow C_2,
\tag{CC.1}
\]

where \(S\) is a finite \(2\)-group. No commutator pairing is descended
through a quotient here. The conclusion is stronger than needed:

\[
 \boxed{\nu(E)=8\Longrightarrow a(E)=8}
\tag{CC.2}
\]

under (CC.1).

## [PROVED] Removing the exact central extension

Let \(T\cong C_3\) be the normal subgroup in (CC.1), let
\(\pi:E\to Q\) be the quotient map, put \(Z=Z(E)\), and set
\(N=\pi^{-1}(T)\). Since \(N/Z\) is cyclic and \(Z\le Z(N)\), \(N\) is
abelian: all its elements have the form \(x^iz\) for one fixed \(x\) and
\(z\in Z\). Also \(N\triangleleft E\).

First remove irrelevant primes. The product \(C\) of the Sylow
\(r\)-subgroups of \(Z\) for \(r\notin\{2,3\}\) contains the full
\(r\)-part of \(E\), since \(Q\) is a \(\{2,3\}\)-group. Thus \(C\) is
a central normal Hall subgroup. Schur--Zassenhaus and centrality give

\[
 E=C\times E_0.
\tag{CC.3}
\]

Direct product with an abelian group preserves both invariants, so
\[
 \nu(E)=\nu(E_0),\qquad a(E)=a(E_0).
\tag{CC.4}
\]
Moreover \(E_0/Z(E_0)\cong E/Z(E)\). We may therefore replace \(E\) by
\(E_0\) and assume that only the primes two and three divide \(|E|\).

Let \(A\) be the Sylow \(3\)-subgroup of the abelian normal group \(N\).
It is characteristic in \(N\), hence normal in \(E\). Since
\(E/N\cong S\) is a \(2\)-group, \(A\) is a normal Hall \(3\)-subgroup
of \(E\). Schur--Zassenhaus gives a Sylow \(2\)-subgroup \(U\) with
\[
 E=A\rtimes U.
\tag{CC.5}
\]
Because \(A\) is abelian,
\[
 C_A(U)=A\cap Z(E).
\tag{CC.6}
\]
Indeed, an element fixed by \(U\) commutes with both factors in (CC.5).
Also
\[
 |A:C_A(U)|=|\pi(A)|=|T|=3.
\tag{CC.7}
\]
Here \(\pi(A)=T\) explicitly: in the Sylow decomposition of the abelian
group \(N\), every primary factor other than \(A\) has trivial image in
the \(3\)-group \(N/Z=T\), while \(\pi(N)=T\). Thus the \(3\)-part \(A\)
maps onto \(T\).

The standard coprime-action decomposition for an abelian \(3\)-group
acted on by a \(2\)-group is
\[
 A=C_A(U)\times[A,U].
\tag{CC.8}
\]
Here is the full argument for possibly noncyclic \(U\). Write \(A\)
additively, put \(m=|U|\), and choose an integer \(n\) such that
\(nm\equiv1\pmod{\exp A}\). Define the averaging endomorphism
\[
 e(a)=n\sum_{u\in U}u(a).
\]
Then \(e^2=e\) and \(\operatorname {im}e=C_A(U)\). Every difference
\((u-1)a\) lies in \(\ker e\), so \([A,U]\le\ker e\). Conversely, \(U\)
acts trivially on \(A/[A,U]\), where \(e\) therefore acts as multiplication
by \(nm\), hence as the identity. Thus \(e(a)=0\) forces
\(a\in[A,U]\). Consequently
\[
 \ker e=[A,U],\qquad A=C_A(U)\times[A,U],
\]
proving (CC.8) without a cyclicity assumption. Equation (CC.7) implies
\[
 T_0:=[A,U]\cong C_3.
\tag{CC.9}
\]
The \(U\)-action on \(T_0\) is nontrivial, since modulo the central factor
it is the inversion action of (CC.1). Write
\[
 \varepsilon(u)=(-1)^{\chi_0(u)},\qquad
 \chi_0:U\twoheadrightarrow C_2.
\tag{CC.10}
\]
Equations (CC.5)--(CC.9) give an actual central direct product
\[
 E=C_A(U)\times H,\qquad H:=T_0\rtimes_{\chi_0}U.
\tag{CC.11}
\]
Together with (CC.3)--(CC.4), this proves
\[
 \boxed{\nu(E)=\nu(H),\qquad a(E)=a(H).}
\tag{CC.12}
\]
Thus the central extension was removed by central direct factors, not by
assuming commutation descends through \(Q\to Q/\Phi(Q)\).

## [PROVED] Exact commutation and clique formula

Write \(T_0\) additively as \(\mathbf F_3\). Elements of \(H\) are
\((a,u)\in\mathbf F_3\times U\), with
\[
 (a,u)(b,v)=\bigl(a+\varepsilon(u)b,uv\bigr).
\tag{CC.13}
\]
Consequently they commute exactly when
\[
 uv=vu,\qquad
 (1-\varepsilon(v))a=(1-\varepsilon(u))b
 \quad\text{in }\mathbf F_3.
\tag{CC.14}
\]

Put \(K=\ker\chi_0\), \(\Omega=U\setminus K\), and let
\(\omega_\Omega\) be the maximum size of a pairwise noncommuting subset
of \(U\) contained in \(\Omega\). Since \(\chi_0\) is onto,
\(\omega_\Omega\ge1\). When the \(U\)-coordinates commute, (CC.14) says:

1. for two members of \(K\), all \(\mathbf F_3\)-coordinates commute;
2. for \(u\in K,v\in\Omega\), commutation holds exactly when the even
   coordinate \(a\) is zero;
3. for two members of \(\Omega\), commutation holds exactly when their
   \(\mathbf F_3\)-coordinates are equal.

These cases give the exact equality
\[
 \boxed{\nu(H)=\nu(K)+3\omega_\Omega.}
\tag{CC.15}
\]

For the upper bound, let \(\mathcal X\) be a clique in \(H\). Above a
fixed \(u\in K\), at most one vertex can occur, and the distinct even
projections are pairwise noncommuting in \(K\). Hence there are at most
\(\nu(K)\) even vertices. Partition the odd vertices by their three
\(\mathbf F_3\)-coordinates. In one fixed coordinate layer the projection
is injective and pairwise noncommuting in \(\Omega\), so each layer has at
most \(\omega_\Omega\) vertices.

Conversely choose maximum cliques \(X\subseteq K\) and
\(Y\subseteq\Omega\). Then
\[
 \{(1,x):x\in X\}\ \cup\
 \{(a,y):a\in\mathbf F_3,\ y\in Y\}
\tag{CC.16}
\]
is a clique. Pairs with noncommuting projections are automatic; the three
vertices over one odd projection are pairwise noncommuting by case 3; and
every even--odd cross pair is noncommuting because case 2 has even
coordinate \(1\ne0\). This proves the lower bound, including the allowed
threefold projection collisions over an odd element.

## [PROVED] Clique eight has an eight-subgroup abelian cover

Assume \(\nu(H)=8\). Equation (CC.15) gives
\[
 8=\nu(K)+3\omega_\Omega.
\tag{CC.17}
\]
A group never has clique number two: if \(x,y\) do not commute, then
\(x,y,xy\) are pairwise noncommuting; an abelian group has clique number
one. Therefore the possibilities in (CC.17) are exhaustive:

- \(\omega_\Omega=1\) gives \(\nu(K)=5\);
- \(\omega_\Omega=2\) gives the impossible value \(\nu(K)=2\);
- \(\omega_\Omega\ge3\) is numerically impossible.

In particular, \(\nu(K)=1,3,4\) with \(\omega_\Omega=1\) would give
\(\nu(H)=4,6,7\), respectively. The unique cutoff-eight possibility is
\[
 \nu(K)=5,\qquad \omega_\Omega=1.
\tag{CC.18}
\]

The proved value \(h(5)=5\) supplies abelian subgroups
\(A_1,\ldots,A_5\le K\) covering \(K\). Since \(K\) acts trivially on
\(T_0\), the five subgroups
\[
 T_0\times A_i\le H
\tag{CC.19}
\]
are abelian and cover every even fiber \(\mathbf F_3\times K\).

Equation (CC.18) says that the set \(\Omega\) is pairwise commuting in
\(U\). For each \(a\in\mathbf F_3\), let
\[
 Y_a=\{(a,u):u\in\Omega\}.
\]
Case 3 says that \(Y_a\) is a pairwise commuting set in \(H\). Therefore
\(B_a=\langle Y_a\rangle\) is an abelian subgroup; this explicitly uses
that a pairwise commuting set generates an abelian subgroup. The three
subgroups \(B_0,B_1,B_2\) cover all odd fibers. Together with (CC.19),
\[
 a(H)\le5+3=8.
\tag{CC.20}
\]
Since always \(a(H)\ge\nu(H)=8\), equations (CC.12) and (CC.20) prove
the conclusion (CC.2).

## [PROVED] Global corollary from the audited dependency chain

Using the already independently audited upstream reductions and
certificates listed below, this closes the last nonnilpotent branch and gives
\[
 \boxed{h(8)=10.}
\tag{CC.21}
\]
The lower bound is the existing group \(S(3,2)\) with
\((\nu,a)=(7,10)\). For the upper bound, the exact finite-model theorem
preserves both invariants for arbitrary groups; the primary-verified
solvability reduction handles the finite model; the nilpotent partition
uses the audited \(p\)-group closures; and (CC.2) handles the solvable
nonnilpotent branch. The proved \(h(7)=10\) handles smaller clique number.

The load-bearing dependency ledger is:

1. the arbitrary-to-finite isoclinic model preserving \(\nu\) and \(a\),
   in notes/structural_reductions.md;
2. the primary-verified, CFSG-dependent solvability input and the exhaustive
   nilpotent/nonnilpotent partition;
3. the proved \(h(5)=5\), used in (CC.19), and \(h(7)=10\), used at the
   global boundary, including their saved exact computations;
4. the audited \(3\)-, \(5\)-, and \(7\)-group cutoff-eight closures;
5. the audited binary closure in
   notes/two_group_inclusion_maximal_centralizers.md and
   notes/two_group_q128_symplectic_attack.md, whose computational inputs
   are the exact binary cutoff-six certificate and universal
   order-at-most-\(81\) cutoff-eight exterior-kernel certificate;
6. the two audited common-core reductions at the frozen hashes above.

No new computation is used here.

## [PROVED] Independent audit status

An independent from-scratch audit checked the frozen pre-clarification
payload at SHA-256

    d99f47b8b28eb78bbe5e1b7012852124f3525c8a618666035c3857e826f9b3e6

and returned PASS with no edits. It reconstructed the central Hall
factorization, the noncyclic-\(U\) coprime decomposition, both directions
of (CC.15) including projection collisions, the complete arithmetic in
(CC.17), the eight-subgroup cover, and the global exhaustive dependency
chain. A separately assigned second auditor independently reconstructed
the same argument and also returned PASS. The only recommended additions
were the explicit averaging proof and the justification of \(\pi(A)=T\);
both have been inserted above without changing the mathematical argument.
