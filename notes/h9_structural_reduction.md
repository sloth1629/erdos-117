# Cutoff Nine: Structural Reduction and the Binary Residual

## Scope and status

This note studies the first unresolved cutoff after the proved value
\(h(8)=10\).  It does **not** claim the value of \(h(9)\).

[PROVED] The scalar binary symplectic group \(E_4\) from
`notes/class_two_geometry.md` has

\[
   (\nu(E_4),a(E_4))=(9,17),
\]

so \(h(9)\ge 17\).

[PROVED] Subject only to the same primary-verified CFSG-dependent
solvability input used for \(h(8)\), the reductions below give

\[
   \boxed{17\le h(9)\le 73.}
\tag{H9.1}
\]

More precisely, a hypothetical group with \(\nu\le9\) and \(a>17\) has an
exact finite commutation model which is a finite \(2\)-group \(P\) satisfying

\[
 \boxed{
 \nu(P)=9,\qquad [P:Z(P)]\le128,\qquad
 \text{some maximum-clique centralizer is nonmaximal in }P.}
\tag{H9.2}
\]

[PROVED] The order-\(256\) boundary is closed exactly at the lower
construction:

\[
 \nu(P)=9,\quad [P:Z(P)]=256
 \quad\Longrightarrow\quad a(P)\le17.
\tag{H9.2a}
\]

The all-maximal case is scalar symplectic directly.  The nonmaximal case
uses the exact cutoff-five commutator geometries and the central-product
argument below.  Thus (H9.2), rather than an unrestricted group, is the
exact structural residual left by this note.

[PROVED] The nonnilpotent branch is sharper: every finite exact model \(G\)
with \(\nu(G)=9\) and nonnilpotent \(G/Z(G)\) satisfies

\[
   a(G)\le15.
\tag{H9.3}
\]

The proof of (H9.3), including the new equality action on \(C_2^2\), the
Frattini-complement contradiction, and the final odd-coset cover, was
independently reconstructed from the statements and arguments in this note.

## [PROVED] The unconditional private-cell bound and its binary saving

For arbitrary groups the private-cell recurrence in
`notes/known_bounds.md` says

\[
 h(n)\le1+(n-1)h(n-2).
\]

Since \(h(7)=10\), it gives the immediate cutoff-nine bound

\[
 h(9)\le1+8\cdot10=81.
\tag{H9.4}
\]

There is a useful saving for finite \(2\)-groups.  The certified binary
part of the cutoff-seven inventory has

\[
 \nu(T)\le7, T\text{ a finite }2\text{-group}
 \quad\Longrightarrow\quad a(T)\le9.
\tag{H9.5}
\]

Indeed the seven-cover theorem first gives
\([T:Z(T)]\le81\), hence the binary rounding gives at most \(64\).  The
complete cutoff-seven exterior-kernel inventory gives at most seven colors
on all ordinary binary rows; the only surviving exceptional quotient is
the scalar \(C_2^6\) graph, with \((\nu,a)=(7,9)\).

Now let \(P\) be a finite \(2\)-group with \(\nu(P)=9\), choose a maximum
clique \(x_1,\ldots,x_9\), and put \(H_i=C_P(x_i)\).  Fix \(j\), and let

\[
 \mathcal P_j=H_j\setminus\bigcup_{i\ne j}H_i.
\]

The private-cell argument proves that \(\mathcal P_j\) is pairwise
commuting, hence \(A_j=\langle\mathcal P_j\rangle\) is abelian, and

\[
 P=A_j\cup\bigcup_{i\ne j}H_i.
\]

The two-step centralizer drop gives \(\nu(H_i)\le7\).  Applying (H9.5) to
the eight displayed centralizers yields

\[
 \boxed{a(P)\le1+8\cdot9=73.}
\tag{H9.6}
\]

No assertion about replacing two or more centralizers by private-cell
subgroups is used here.

## Inclusion-maximal centralizers in a finite \(p\)-group

### [PROVED] The local center-layer inequality

Let \(P\) be a finite \(p\)-group with \(\nu(P)=m\).  Let
\(C=C_P(y)\) be inclusion-maximal among the proper element centralizers and
put \(r=\nu(C)\).  If \(C\) is maximal in \(P\), set \(K=P\).  Otherwise the
normalizer condition supplies

\[
 C\triangleleft K<P,\qquad [K:C]=p.
\]

In either case \(C=C_K(y)\), \([K:C]=p\), and

\[
 Z(K)=Z(P).
\tag{H9.7}
\]

For if \(z\in Z(K)\setminus Z(P)\), then
\(C<K\le C_P(z)<P\), contrary to the inclusion-maximality of \(C\).

Put

\[
 q=[Z(C):Z(P)].
\]

Then \(q\ge p\) and

\[
 \boxed{r+q\le m.}
\tag{H9.8}
\]

To see this, choose \(g\in K\setminus C\).  Conjugation by \(g\) on
\(Z(C)\) has fixed subgroup \(Z(K)=Z(P)\).  Thus the map
\(a\mapsto[a,g]\) has fibers of size \(|Z(P)|\), and a transversal gives a
\(q\)-clique in \(gZ(C)\).  Twisting a maximum \(r\)-clique of \(C\) by
suitable elements of \(Z(C)\) joins it to that \(q\)-clique.  Also
\(y\in Z(C)\setminus Z(K)\), so \(q>1\), hence \(q\ge p\).

### [PROVED] The primes five and seven

Let \(m=9\) and \(p\in\{5,7\}\).  The centralizer drop gives \(r\le7\).
If \(C\) were nonabelian, the standard \(p\)-group lower bound would give
\(r\ge p+1\), while (H9.8) gives \(q\ge p\).  Hence
\(r+q\ge2p+1>9\), impossible.  Thus every inclusion-maximal element
centralizer is abelian.  In that case \(Z(C)=C\), so

\[
 [C:Z(P)]=q=p,
\]

because \(1+q\le9\) and \(q\) is a positive power of \(p\).

Nine such centralizer images cover \(Q=P/Z(P)\), whence

\[
 |Q|\le1+9(p-1).
\]

Power-of-\(p\) rounding gives \(|Q|\le25\) for \(p=5\) and
\(|Q|\le49\) for \(p=7\).  A nonabelian exact center quotient is not cyclic,
so the only possibility is \(Q\cong C_p^2\).  Its commutator form has
one-dimensional image and zero radical; it is the scalar symplectic plane,
which has

\[
 \nu(P)=a(P)=p+1,
\]

not nine.  Therefore no finite \(5\)- or \(7\)-group has clique number
nine.  Together with the already proved small-cutoff \(p\)-group results,
the cutoff-nine possibilities are \((1,1),(6,6)\) for \(p=5\), and
\((1,1),(8,8)\) for \(p=7\).

### The prime three

[PROVED] There is no finite \(3\)-group of clique number six.  If
\(m=6\), (H9.8) gives \(r\le4\).  A nonabelian \(C\) would have
\(r\ge4\), and then \(r+q\ge4+3>6\).  Hence all inclusion-maximal
centralizers are abelian, with \(q=3\).  Six order-three images cover
\(Q=P/Z(P)\), so

\[
 |Q|\le1+6(3-1)=13,
\]

and power-of-three rounding gives \(|Q|\le9\).  The nonabelian case is
therefore the scalar plane \(Q=C_3^2\), which has clique number four, a
contradiction.

[CITED-VERIFIED] The audited small \(p\)-group equality theorem excludes clique
number five.  Consequently, for \(m\in\{8,9\}\), an
inclusion-maximal centralizer has \(r=1\) or \(4\): the values five and six
are absent, while \(r=7\) contradicts \(r+q\le m\) and \(q\ge3\).
In the \(r=4\) equality case the exact center quotient of \(C\) has order
nine.  Hence every inclusion-maximal centralizer satisfies

\[
 [C:Z(P)]\le27.
\]

The covering count gives

\[
 |P:Z(P)|\le1+m(27-1)\le235,
\]

so power-of-three rounding gives

\[
 |P:Z(P)|\le81.
\tag{H9.9}
\]

[COMPUTED] The canonical order-at-most-\(81\) exterior-kernel artifacts,
together with the complete \(C_3^4\) orbit certificate, have no faithful
exact-center graph of clique number eight or nine.  The ordinary records of
orders \(9,27,81\) are either at most seven or at least ten; the
\(C_3^4\) orbit distribution has the unique \((7,10)\) orbit and all other
orbits have clique number at least ten.  This finite filter was independently
reconstructed from the saved adjacencies.  Combining it with (H9.9) proves
that no finite \(3\)-group has clique number eight or nine.

Thus every odd-primary nilpotent contribution at cutoff nine has
abelian-cover number at most ten.

## [PROVED] The nilpotent partition

Let \(G\) be finite and nilpotent.  Its Sylow subgroups are direct factors.
A nonabelian \(p\)-group has clique number at least \(p+1\), and maximum
cliques in two direct factors form their Cartesian product.  Thus two
nonabelian Sylow factors at distinct primes give at least

\[
 (2+1)(3+1)=12
\]

pairwise noncommuting elements.  At cutoff nine there is therefore at most
one nonabelian Sylow factor; all other Sylow factors are abelian direct
factors and preserve both \(\nu\) and \(a\).  Primes at least eleven are
impossible, and the preceding sections dispose of the odd primes.  Hence a
nilpotent exact model with \(a>17\) must be a finite \(2\)-group.

## A complement-free chief-action lemma at cutoff nine

### [PROVED] Statement

Let \(K\) be finite solvable with \(\nu(K)\le9\), and let
\(V\triangleleft K\) be a noncentral minimal normal subgroup.  Put

\[
 A=K/C_K(V).
\]

Then \(V\) is elementary abelian, \(A\) acts faithfully and irreducibly,
and exactly one of the following holds:

1. \(A\) is cyclic and fixed-point-free, with

\[
 (V,A)\in\{
 (C_3,C_2),(C_2^2,C_3),(C_5,C_2),(C_5,C_4),
 (C_7,C_2),(C_7,C_3),(C_7,C_6),(C_2^3,C_7)
 \};
\tag{H9.10}
\]

2. \(V=C_2^2\) and \(A=S_3\cong\mathrm{GL}(2,2)\) in its natural action.

No complement for \(V\) is assumed.

### [PROVED] Fiber and rank proof

For \(g\in K\), the coset \(gV\) contains a clique of size

\[
 [V:C_V(g)].
\tag{H9.11}
\]

Fiber cliques over noncommuting quotient elements are completely joined.
Moreover, a vector moved by all their actions is noncommuting with every
member of all the chosen fibers.

If \(A\) is abelian, a finite abelian irreducible linear group is cyclic.
A generator has no nonzero fixed vector, and (H9.11), together with one
moved vector, gives \(|V|+1\le9\).  Listing the nontrivial cyclic
irreducible subgroups gives (H9.10).

Suppose \(A\) is nonabelian and choose noncommuting \(a,b\in A\).  The
actions \(a,b,ab\) are nontrivial.  Write

\[
 r(c)=\operatorname{codim}C_V(c).
\]

Their three completely joined fiber cliques give

\[
 p^{r(a)}+p^{r(b)}+p^{r(ab)}\le9.
\tag{H9.12}
\]

For \(p\ge3\), three proper fixed subspaces do not cover \(V\), so one can
adjoin a vector moved by all three.  This excludes \(p\ge3\).  For \(p=2\),
if one of the three ranks is at least two, the same fixed-space count
supplies such a vector.  Equation (H9.12) then forces the rank multiset

\[
 \{r(a),r(b),r(ab)\}=\{1,1,2\}.
\tag{H9.13}
\]

The alternative of three rank-one actions is impossible: an invertible
rank-one perturbation of the identity over \(\mathbf F_2\) is an involution,
and if \(a,b,ab\) were all involutions then \(a\) and \(b\) would commute.

It remains to classify the equality case.  First \(O_2(A)=1\): a normal
\(2\)-subgroup has a nonzero fixed vector in characteristic two, whose
\(A\)-invariant fixed space would contradict irreducibility and faithfulness.
Let \(N=C_r^k\) be a minimal normal subgroup of \(A\); then \(r\) is odd.

If \(N\le Z(A)\), (H9.13) supplies a noncentral rank-one element \(x\).
Because \(x\) commutes with \(N\), the line
\(\operatorname{im}(x-1)\) is \(N\)-invariant.  But
\(\mathrm{GL}(1,2)=1\), so \(N\) fixes this line pointwise.  This contradicts
\(C_V(N)=0\), which follows from normality, irreducibility, and faithful
nontrivial action.

Thus \(N\) is noncentral.  Minimality gives \(C_N(A)=1\), so every
\(1\ne n\in N\) is noncentral and has rank at most two.  Odd semisimplicity
over \(\mathbf F_2\) forces \(r=3\), with exactly one nontrivial
two-dimensional \(C_3\)-block.  More explicitly, a faithful
\(C_3^k\)-module is a sum of two-dimensional \(\mathbf F_4\)-character
blocks.  A repeated block, or two distinct characters, gives an element
nontrivial on two blocks and hence rank at least four.  A single character
is faithful only when \(k=1\).  Since \(C_V(N)=0\), it follows that

\[
 V=C_2^2,\qquad N=C_3,\qquad A\le\mathrm{GL}(2,2)=S_3.
\]

Nonabelianness now gives \(A=S_3\), proving the lemma.

## [PROVED] The Frattini-free skeleton

Let \(Q=G/Z(G)\) be finite, solvable, nonnilpotent, and satisfy
\(\nu(G)=9\).  Put \(P=\Phi(Q)\).  The finite-group argument in
`notes/common_core_frattini_reduction.md` shows that \(P\) is nilpotent and
that \(Q/P\) remains nonnilpotent.

The Frattini-free Fitting argument from
`notes/h8_nonnilpotent_reduction.md` applies with the preceding chief-action
lemma.  In a Frattini-free group every minimal normal factor is
complemented.  The exceptional natural action would therefore give the
affine quotient

\[
 C_2^2:S_3\cong S_4,
\]

which has an explicit ten-clique, so it is excluded.  Every surviving
noncentral minimal factor is one of the fixed-point-free cyclic cases in
(H9.10).

There is at most one such noncentral factor.  Indeed, an element moving two
minimal factors gives a fiber clique of size at least \(3\cdot3=9\), and a
vector moved by it adjoins a tenth vertex.  If initially separate elements
move the two factors, either one already moves both or their product does.
The remaining central minimal factors split directly.  Consequently

\[
 \boxed{Q/P=C\times H,}
\tag{H9.14}
\]

where \(C\le Z(Q/P)\) is a direct product of elementary abelian
\(2\)-, \(3\)-, \(5\)-, and \(7\)-parts, and

\[
 H\in\{S_3,A_4,C_5:C_2,C_5:C_4,
 C_7:C_2,C_7:C_3,C_7:C_6,C_2^3:C_7\}.
\tag{H9.15}
\]

Write every member as \(H=V:B\), where \(B\) is cyclic and acts
fixed-point-freely on \(V\).  Then \(H_{\rm ab}=B\) and

\[
 \nu(H)=a(H)=|V|+1.
\tag{H9.16}
\]

## [PROVED] The Frattini-free exact branch has \(a\le15\)

Assume first that \(P=1\), so the exact center quotient itself is
\(Q=C\times H\).

Let \(A=C_p^d\) be a nontrivial Sylow component of \(C\).  If
\(p\nmid|H_{\rm ab}|\), the exact coprime central-direct-factor lemma gives

\[
 \nu(G)\ge3\nu(H)\ge12,
\]

a contradiction.  Thus every prime occurring in \(C\) divides \(|B|\).

Fix such a prime \(p\), let \(b\) generate \(B\), and write the exact
commutator pairing on \(A\) as \(\beta\), with cross-evaluation

\[
 T_b(a)=[\widetilde a,\widetilde b].
\]

Since \(V=H'\), all \(vb\) have the same evaluation \(T_b\).  If
\(T_b\ne0\), choose a line in \(A\) on which it is nonzero.  The exact
same-fiber formula gives a \(p\)-clique in each of the \(|V|\) fibers
\(A(vb)\), and the fibers are completely joined.  Hence

\[
 p|V|\le9.
\tag{H9.17}
\]

If \(T_b=0\), exactness makes the internal alternating pairing on \(A\)
radical-free.  A noncommuting pair and its product give a three-clique in
\(A\); copying it over a maximum clique in \(H\) gives at least
\(3(|V|+1)\ge12\) vertices.  Thus this case is impossible.

The table (H9.15) and (H9.17) leave only

\[
 p=2,\qquad H=S_3.
\]

Therefore either \(C=1\), or \(Q=C_2^d\times S_3\).

If \(C=1\), there is a direct fifteen-subgroup cover which works in every
central extension.  The Frobenius group \(V:B\) is covered by its
\(|V|\) conjugate cyclic complements and by the one-dimensional subgroups
of \(V\).  The preimage in \(G\) of a cyclic subgroup of \(Q=G/Z(G)\) is
abelian.  The number of covering subgroups is

\[
 |V|+\frac{|V|-1}{p-1}\in\{4,7,6,8,15\},
\]

for \(V=C_3,C_2^2,C_5,C_7,C_2^3\), respectively.

If \(Q=C_2^d\times S_3\), rewrite it as

\[
 Q=C_3\rtimes_\chi C_2^{d+1}
\]

with inversion action.  The exact-extension removal and the cover in the
final semidirect section below apply and give \(a(G)\le15\).  Hence every
Frattini-free nonnilpotent exact model has \(a\le15\).

## Minimal layers inside the Frattini subgroup

Assume now that \(P=\Phi(Q)\ne1\), and let \(1\ne U\le P\) be minimal
normal in \(Q\).  Since \(P\) is nilpotent, the usual center intersection
argument gives

\[
 U\le Z(P).
\tag{H9.18}
\]

Thus the action on \(U\) factors through the skeleton (H9.14).

### [PROVED] Central and cyclic-action layers

Suppose first that \(U=\langle u\rangle\cong C_p\) is central in \(Q\).
Exactness of \(Q=G/Z(G)\) gives a nonzero homomorphism

\[
 \varphi_u:Q\longrightarrow Z(G),\qquad
 \varphi_u(q)=[\widetilde u,\widetilde q].
\tag{H9.19}
\]

If \(\varphi_u(P)\ne0\), every chosen element of \(Q/P\) has a lift on
which \(\varphi_u\) is nonzero.  If the descended map is nonzero on \(C\),
the same adjustment is made with a central factor.  Applying it to the
\((|V|+1)\)-clique in \(H\) gives

\[
 p(|V|+1)\le9.
\tag{H9.20}
\]

In the remaining case the map descends, vanishes on \(C\), and is nonzero
on \(H_{\rm ab}=B\).  The \(|V|\) complement fibers give

\[
 p|V|\le9.
\tag{H9.21}
\]

The complete table leaves only

\[
 U=C_2,\qquad H=S_3.
\tag{H9.22}
\]

Suppose next that the action on \(U\) is a cyclic fixed-point-free action
from (H9.10).  If it is nontrivial on \(C\), adjust every member of a
maximum \(H\)-clique to act nontrivially; the joined fiber cliques have
size at least

\[
 |U|(|V|+1)\ge12.
\]

If it is trivial on \(C\), choose \(b\in B\) acting nontrivially.  The
\(|V|\) joined \(U\)-fiber cliques, together with one moved vector in \(U\),
have size

\[
 |U||V|+1\ge3\cdot3+1=10.
\]

Both are impossible.

The only remaining noncentral possibility is therefore

\[
 U=C_2^2,\qquad Q/C_Q(U)=S_3
\tag{H9.23}
\]

in the natural action.  The central factor \(C\) maps trivially because
\(Z(S_3)=1\), and among (H9.15) only \(H=S_3\) can map onto \(S_3\).

Equations (H9.22)--(H9.23) show that \(H=S_3\) and that every minimal
\(Q\)-normal subgroup in \(P\) is binary.  Hence

\[
 P\text{ is a }2\text{-group}.
\tag{H9.24}
\]

### [PROVED] The possible \(P\)-chief factors

Refine \(P\) to a \(Q\)-chief series

\[
 1=P_0<P_1<\cdots<P_t=P.
\]

Each factor lies in the center of the corresponding quotient of \(P\).
Applying the chief-action lemma in \(Q/P_{j-1}\) shows that a factor is one
of

\[
 C_2\text{ central},\quad C_2^2:C_3,\quad C_2^3:C_7,\quad
 C_2^2:S_3\text{ natural}.
\tag{H9.25}
\]

The cyclic \(C_3\)- and \(C_7\)-actions must come from the corresponding
central factor of \(C\) in \(Q/P=C\times S_3\).  Multiplying a four-clique
in \(S_3\) by one such acting element gives four joined fiber cliques, of
total size \(16\) or \(32\).  Thus the two cyclic cases are excluded.
Every \(P\)-chief factor is central \(C_2\) or natural \(C_2^2:S_3\).

### [PROVED] Odd central factors vanish

Let a nontrivial odd component \(C_r\) occur in \(C\), and take its full
preimage with \(P\).  Schur--Zassenhaus supplies a Sylow \(r\)-complement
\(R\).  The group \(R\) acts trivially on every \(P\)-chief factor: it acts
trivially on central factors, and the natural action map
\(C\times S_3\to S_3\) kills \(C\).

Automorphisms of a finite \(2\)-group which stabilize a central chief series
and act trivially on every order-two factor form a \(2\)-group.  Therefore
the odd group \(R\) centralizes \(P\).  It follows that \(R\) is the unique
Sylow \(r\)-subgroup of its normal preimage and hence is normal in \(Q\).
Since \(C_r\) is central modulo \(P\),

\[
 [Q,R]\le P\cap R=1,
\]

so \(R\le Z(Q)\).  A central minimal subgroup of \(R\) has odd prime order,
contradicting the central-layer forcing (H9.20)--(H9.22).  Hence

\[
 C=C_2^a.
\tag{H9.26}
\]

### [PROVED] A natural chief factor would be complemented

Suppose that a natural factor occurs, and choose the highest such factor.
After quotienting by the preceding term of the chief series, write it as

\[
 U\cong C_2^2\le\overline P=\Phi(\overline Q).
\]

Every factor of \(\overline P/U\) is central of order two, and

\[
 \overline Q/\overline P=C_2^a\times S_3.
\]

Let \(B\) be the full preimage of \(C_2^a\times1\).  Then \(B\) is a normal
\(2\)-group.  Let \(R_0\) be the preimage of \(C_2^a\times A_3\), and choose
a Sylow three-subgroup \(T\cong C_3\), so \(R_0=B\rtimes T\).  The action of
\(T\) on \(U\) is fixed-point-free, while its action on \(B/U\) is trivial:
the latter action is trivial on every factor of a central series, so its
image is simultaneously a \(3\)-group and a \(2\)-group.

Coprime fixed-point lifting gives

\[
 B=U B_0,\qquad B_0=C_B(T),\qquad
 U\cap B_0=C_U(T)=1.
\tag{H9.27}
\]

In fact \(B\) centralizes \(U\), so this is a direct product.

Choose a lift \(s\) of a transposition.  Sylow conjugacy inside \(R_0\)
allows multiplication by an element of \(B\) so that the adjusted lift
\(t\) normalizes \(T\).  It then normalizes \(B_0\), and

\[
 t^2\in B\cap C_B(T)=B_0.
\]

Put

\[
 M=\langle B_0,T,t\rangle.
\]

The subgroup \(B_0\times T\) is normal in \(M\), with quotient of order two,
so

\[
 |M|=6|B_0|.
\]

On the other hand, (H9.27) and the images of \(T,t\) show that
\(MU=\overline Q\), while

\[
 |\overline Q/U|=6|B_0|.
\]

Therefore \(M\to\overline Q/U\) is an isomorphism and \(M\cap U=1\).
This complements the nontrivial subgroup \(U\le\Phi(\overline Q)\), which
is impossible: a complement is contained in a maximal subgroup, and that
maximal subgroup also contains \(U\).  Thus no natural factor occurs.

Consequently every \(P\)-chief factor is central of order two.

## [PROVED] The canonical nonnilpotent residual

Every odd-order subgroup of \(Q\) now centralizes \(P\), because its action
on a central order-two chief series has image in a \(2\)-group.  The normal
\(A_3\) in \(Q/P=C_2^a\times S_3\) therefore lifts to a normal subgroup
\(T\cong C_3\).  If \(S\) is a Sylow \(2\)-subgroup, then

\[
 \boxed{Q=C_3\rtimes_\chi S,\qquad
 \chi:S\twoheadrightarrow C_2,}
\tag{H9.28}
\]

where the action is inversion.

The maximal-subgroup argument from
`notes/common_core_binary_semidirect.md` applies verbatim and gives

\[
 \boxed{\Phi(Q)=\Phi(S)=P.}
\tag{H9.29}
\]

Briefly, every maximal \(M<S\) makes \(C_3M\) maximal in \(Q\), giving
\(P\le\Phi(S)\).  Conversely \(\Phi(S)\le\ker\chi\), and it lies both in
the maximal subgroups containing \(C_3\) and in every conjugate Sylow
\(2\)-complement; hence it lies in \(\Phi(Q)\).

## [PROVED] Clique nine in the \(C_3\)-by-\(2\) residual has a 15-cover

The exact central-extension removal in
`notes/common_core_coprime_closure.md` is independent of the cutoff.  It
splits off central Hall factors and reduces both invariants exactly to

\[
 H=\mathbf F_3\rtimes_\chi U,
\tag{H9.30}
\]

where \(U\) is a finite \(2\)-group and \(\chi:U\twoheadrightarrow C_2\).
Put

\[
 K=\ker\chi,\qquad \Omega=U\setminus K,
\]

and let \(\omega_\Omega\) be the largest size of a pairwise noncommuting
subset of \(U\) contained in \(\Omega\).  The exact multiplication and
commutation calculation gives

\[
 \boxed{\nu(H)=\nu(K)+3\omega_\Omega.}
\tag{H9.31}
\]

At clique number nine, the only arithmetic possibilities are

\[
 (\nu(K),\omega_\Omega)=(6,1)\quad\text{or}\quad(3,2).
\tag{H9.32}
\]

If the pair is \((6,1)\), six abelian subgroups cover \(K\), and each of the
three fixed-coordinate odd layers is internally pairwise commuting.  They give a
nine-subgroup cover of \(H\).

It remains to treat \((3,2)\).  Let \(x_1,x_2,x_3\) be a maximum clique in
\(K\).  The three centralizers \(A_i=C_K(x_i)\) are abelian by the two-step
centralizer drop, cover \(K\), and have intersection \(Z(K)\).  For
completeness, an irredundant cover of a group by three proper subgroups has
pairwise intersections equal to the total intersection and quotient
\(C_2^2\): if an element lay in two but not the third, multiplying it by a
private element of the third gives a contradiction; then multiplying a
fixed private element by all private elements in another member shows that
each member has exactly two intersection cosets.  Hence

\[
 K/Z(K)\cong C_2^2,
\tag{H9.33}
\]

and the \(A_i\) are its three abelian index-two line preimages.

Choose \(t\in\Omega\).  Conjugation by \(t\) permutes these three subgroups.
Its square is conjugation by \(t^2\in K\), which acts trivially on
\(K/Z(K)\).  Thus the induced permutation has square one and fixes at least
one line preimage \(A\).  Since \(A\triangleleft K\), this gives
\(A\triangleleft U\).

The odd coset \(\Omega=tK\) is the union of two \(A\)-cosets.  For any
\(r\in\Omega\), define

\[
 \delta_r:A\longrightarrow A,\qquad
 \delta_r(a)=a^{-1}a^r.
\]

Because \(A\) is abelian and \(r\) normalizes it, \(\delta_r\) is a
homomorphism.  A direct multiplication gives

\[
 ra\text{ commutes with }rb
 \quad\Longleftrightarrow\quad
 \delta_r(a)=\delta_r(b).
\tag{H9.34}
\]

One representative from every fiber value is an \(\Omega\)-clique, so

\[
 |\operatorname{im}\delta_r|\le\omega_\Omega=2.
\]

Each of the two \(A\)-cosets in \(\Omega\) is therefore covered by at most
two pairwise commuting fibers.  Thus \(\Omega\) is covered by four
pairwise commuting sets.  In each of the three \(\mathbf F_3\)-coordinate
layers these generate at most four abelian subgroups, while the even fibers
are covered by the three abelian subgroups over the \(A_i\).  Therefore

\[
 \boxed{a(H)\le3+3\cdot4=15.}
\tag{H9.35}
\]

Equations (H9.28)--(H9.35) prove the nonnilpotent bound (H9.3).

## The finite binary reduction

The remaining argument is internal to finite \(2\)-groups.  Its conclusion
is stated first; the local rigidity and counting proof follows.

### [PROVED] Binary center-index theorem at cutoff nine

Let \(P\) be a finite \(2\)-group with \(\nu(P)=9\).  Then

\[
 \boxed{[P:Z(P)]\le256.}
\tag{H9.36}
\]

If the centralizers of the members of some maximum nine-clique are all
maximal subgroups of \(P\), then

\[
 P/Z(P)\cong C_2^8
\]

and the commutator map is a scalar nondegenerate symplectic form.  Hence

\[
 (\nu(P),a(P))=(9,17).
\tag{H9.37}
\]

The non-all-maximal case is not classified by this theorem.

### [PROVED] The all-maximal case

Let \(x_1,\ldots,x_9\) be a maximum clique and put
\(H_i=C_P(x_i)\).  Their images in \(Q=P/Z(P)\) form an irredundant
nine-cover with trivial intersection.  If all \(H_i\) are maximal, then
\(\Phi(P)\le Z(P)\), so \(Q\) is elementary abelian.  The nine hyperplane
normals form a minimal odd circuit over \(\mathbf F_2\); hence they are the
unique nine-circuit and

\[
 Q\cong C_2^8.
\]

Let \(B:\Lambda^2Q\to W\) be the exact commutator map.  For each clique
vector \(v_i=x_iZ(P)\), the kernel of \(B(v_i,-)\) is the corresponding
hyperplane, so its image is a line \(D_i\le W\).  Since
\(B(v_i,v_j)\ne0\) for \(i\ne j\), one has

\[
 0\ne B(v_i,v_j)\in D_i\cap D_j,
\]

and all \(D_i\) are one common line \(D\).  The circuit normals span
\(Q^*\); exactness makes \(v\mapsto B(v,-)\) injective, and the \(v_i\)
span \(Q\).  Bilinearity therefore gives \(\operatorname{im}B=D\) on all
of \(Q\times Q\).  Thus \(B\) is a scalar nondegenerate alternating form on
an eight-dimensional binary space.  The symplectic clique and Lagrangian
spread calculation in `notes/class_two_geometry.md` gives (H9.37).

### Local rigidity input

[PROVED] The following boundary lemma is used in the center-index count.
Let \(C=C_K(y)\triangleleft K\) satisfy

\[
 [K:C]=2,\quad Z(K)=Z,\quad [Z(C):Z]=2,\quad
 C/Z(C)\cong C_2^6
\]

with scalar nondegenerate symplectic commutator, and suppose
\(\nu(K)\le9\).  Then

\[
 K/Z\cong C_2^8
\]

with scalar nondegenerate symplectic commutator, and
\((\nu(K),a(K))=(9,17)\).

[PROVED] Moreover, if such a scalar \(K/Z\cong C_2^8\) is normal of index
two in a group \(L\), with \(Z(K)=Z(L)\), then \(\nu(L)\ge10\).

Here is the complete equality analysis.  Put \(A=Z(C)\) and
\(V=C/A\cong\mathbf F_2^6\), and write \(b\) for its scalar symplectic
form.  First

\[
 C'=\langle d\rangle\le Z.
\tag{H9.38}
\]

Indeed, the kernel of
\(b:\Lambda^2V\to\mathbf F_2\) is spanned by isotropic decomposable
vectors.  In a symplectic basis, the only generators which are not
immediate are

\[
 e_i\wedge f_i+e_1\wedge f_1
 =(e_i+e_1)\wedge(f_i+f_1)
   +e_i\wedge f_1+e_1\wedge f_i.
\]

Thus the actual commutator map factors through \(b\), so \(C'\) is the
order-two scalar line.  It is characteristic in \(C\), and conjugation
fixes it because \(\operatorname{Aut}(C_2)=1\), proving (H9.38).

Choose \(t\in K\setminus C\).  Its induced action \(\alpha\) on \(V\) is
an involutory symplectic transformation.  Put

\[
 N=\alpha-1,\qquad s=\operatorname{rank}N,\qquad
 F=\ker N=(\operatorname{im}N)^\perp.
\]

Then \(s\le3\).  Representatives of \(V/F\), each doubled by the element
\(y\in A\setminus Z\), give an outer clique of size \(2^{s+1}\).  Distinct
representatives are noncommuting modulo \(A\), while each pair
\(tu,tuy\) is noncommuting because \([t,y]\ne1\).

If \(s>0\), a scalar six-clique can be chosen outside \(F\) and joins this
outer clique.  After a symplectic change of basis with
\(e_1\in\operatorname{im}N\), one exact list, in coordinates
\((e_1,e_2,e_3,f_1,f_2,f_3)\), is

\[
 000100, 110100, 100110, 111110, 110111, 111111.
\tag{H9.39}
\]

Every vector in (H9.39) has \(f_1=1\), hence lies outside \(F\), and every
pair has scalar product one.  For \(s=1\) this gives \(4+6=10\) vertices,
and larger \(s\) only increases the outer part.  Therefore \(\alpha=1\).

Now define

\[
 \phi:V\longrightarrow A/Z,\qquad \phi(v)=[t,v]Z.
\]

If \(\phi\ne0\), two representatives in opposite \(\phi\)-fibers, each
doubled by \(y\), give an outer four-clique.  A transported copy of
(H9.39) outside \(\ker\phi\) joins it, giving ten vertices.  Hence
\([t,C]\le Z\), and \(K\) has class at most two.

Write the commutator map on \(W=K/Z\) additively as \(B\).  Let
\(a=A/Z\), put

\[
 e=B(a,t)\ne0,\qquad L(u)=B(t,u)\quad(u\in U:=C/Z).
\]

If \(L(u)\notin\langle e\rangle\), then

\[
 \{t,t+a,t+u,t+u+a\}
\tag{H9.40}
\]

is an outer four-clique.  It joins a scalar six-clique chosen in the affine
set \(b(x,u)=1\).  When \(e\ne d\), toggling each scalar vector \(x\) by
\(a\) changes its \(L\)-value by \(e\), so the six lifts may be chosen to
avoid the two bad values; when \(e=d\), use a transported six-clique outside
the kernel of \(L\) modulo \(\langle d\rangle\).  Thus (H9.40) would extend
to a ten-clique, and consequently

\[
 L(U)\le\langle e\rangle.
\tag{H9.41}
\]

Since \(L(a)=e\), its kernel \(J\) has order \(64\), intersects
\(\langle a\rangle\) trivially, and maps isomorphically onto \(V\).  Hence
\(J\) is an elementary scalar symplectic six-space.  If \(e\ne d\), the
Cartesian sums of a scalar seven-clique in \(J\) with

\[
 \{a,t,a+t\}
\]

give \(21\) pairwise noncommuting points: the three possible cross-values
are the distinct nonzero elements \(d,e,d+e\).  Therefore \(e=d\).  By
(H9.41), every commutator in \(K\) now lies in \(\langle d\rangle\).
Exactness says that \(B\) has zero radical.  But \(2W\) lies in that radical,
so \(2W=0\).  Thus \(W=\mathbf F_2^8\) with a scalar nondegenerate
alternating form, proving the first rigidity statement.

For the index-two statement, let \(K\triangleleft L\), choose
\(t\in L\setminus K\), and put \(V=K/Z\cong\mathbf F_2^8\).  Again let
\(N=\alpha-1\), \(F=\ker N\), and \(s=\operatorname{rank}N\le4\).  An
outer transversal gives a \(2^s\)-clique.  It extends to ten vertices as
follows:

- \(s=4\): the outer clique already has size \(16\);
- \(s=3\): adjoin two nonorthogonal scalar vectors outside \(F\);
- \(s=2\): adjoin a scalar six-clique outside \(F\);
- \(s=1\): adjoin the following scalar eight-clique outside \(F\), after
  taking \(F\subseteq\{f_1=0\}\):

\[
\begin{split}
 &00001000, 11001000, 10001100, 11101100,\\
 &11001110, 11111110, 11101111, 11111111,
\end{split}
\tag{H9.42}
\]

where the coordinates are
\((e_1,e_2,e_3,e_4,f_1,f_2,f_3,f_4)\).  The same outer-inner commutator
calculation as above verifies every join.

It remains that \(s=0\).  Put \(T(v)=[t,v]\).  The image of \(T\) cannot
lie in the scalar line \(\langle d\rangle\): otherwise exactness would make
\(L/Z\) elementary with a nondegenerate scalar alternating form in odd
dimension nine.  Thus \(T\) induces a nonzero functional

\[
 \ell:V\longrightarrow Z/\langle d\rangle.
\]

Two outer representatives in \(\ker\ell\) can be chosen noncommuting.  If
the scalar component of \(T\) is nonzero on \(\ker\ell\), use \(0,u\) with
nonzero scalar value; otherwise use a \(b\)-nonorthogonal pair.  A third
representative outside \(\ker\ell\) is noncommuting with both.  A symplectic
transport of (H9.42) into the affine hyperplane \(\ell=1\) joins this outer
three-clique, producing eleven vertices.  This proves \(\nu(L)\ge10\) in
the last case and completes both rigidity lemmas.

### [PROVED] The center-index count

Return to an inclusion-maximal element centralizer \(C=C_P(y)\), put
\(r=\nu(C)\), \(q=[Z(C):Z(P)]\), and let \(K\) be the index-two
intermediate subgroup from (H9.7).  The possible local bounds are

| \(r\) | \([C:Z(C)]\) | \(q\) | \([C:Z(P)]\) |
|:---:|---:|---:|---:|
| \(1\) | \(1\) | \(8\) | \(8\) |
| \(3\) | \(4\) | \(4\) | \(16\) |
| \(4\) | \(8\) | \(4\) | \(32\) |
| \(5\) | \(16\) | \(4\) | \(64\) |
| \(6\) | \(16\) | \(2\) | \(32\) |
| \(7\) | \(64\) | \(2\) | \(128\) |

Here \(r=2\) never occurs, finite binary groups of clique number eight were
already excluded, (H9.8) gives the \(q\)-column, and the other column uses
the exact binary center-quotient bounds through cutoff seven.

If \(C\) is maximal in \(P\), then \(K=P\), so the last column gives
\([P:Z(P)]\le256\).  Suppose every inclusion-maximal element centralizer
is nonmaximal.  Nine of their images \(A_i=C_i/Z(P)\) cover
\(Q=P/Z(P)\), and the table first gives

\[
 |Q|\le1+9(128-1)=1144.
\]

Thus \(|Q|\le1024\).

If \(|Q|=1024\), at least eight \(A_i\) have order \(128\); otherwise

\[
 |Q|\le1+7(128-1)+2(64-1)=1016.
\]

For any order-\(128\) image the table is sharp in the row \(r=7,q=2\).
The exact cutoff-seven equality case makes
\(C/Z(C)\cong C_2^6\) scalar symplectic, and the local rigidity lemma makes
\(K/Z(P)\cong C_2^8\) scalar symplectic.  Normalize \(K\) upward to an
index-two subgroup \(K\triangleleft L<P\).  If \(Z(L)=Z(P)\), scalar
index-two rigidity gives a ten-clique.  If \(Z(L)>Z(P)\), choose
\(z\in Z(L)\setminus Z(P)\).  Since
\[
 L\le C_P(z)<P,\qquad [P:L]=2,
\]
one has \(C_P(z)=L\).  The two-step centralizer drop gives
\(\nu(L)\le7\), whereas the scalar subgroup \(K\) has clique number nine,
again a contradiction.  Hence \(|Q|\ne1024\).

It remains to exclude \(|Q|=512\).  An image \(A_i\) of order \(128\)
would already give a scalar \(K/Z(P)\) of order \(256\), now normal of
index two in \(P\), contrary to scalar index-two rigidity.  Hence
\(|A_i|\le64\) for all \(i\).

At least eight images have order \(64\), since with at most seven,

\[
 1+7(64-1)+2(32-1)=504<512.
\]

Suppose exactly eight have order \(64\), and the ninth has order
\(s\le32\).  For \(x\in Q\), let
\[
 m_x=|\{i:x\in A_i\}|.
\]
Writing
\[
 S_1=\sum_i|A_i|=512+s,\qquad
 E=S_1-|Q|=\sum_x(m_x-1)=s,
\]
and
\[
 S_2=\sum_{i<j}|A_i\cap A_j|
     =\sum_x\binom{m_x}{2},
\]
the pointwise inequality
\(\binom m2\le\frac92(m-1)\) gives \(S_2\le\frac92s\).
On the other hand, the subgroup product formula gives intersection at
least \(8\) for each of the \(28\) large-large pairs and at least
\(s/8\) for each of the eight large-small pairs.  Therefore
\[
 S_2\ge224+s>\frac92s,
\]
a contradiction.  All nine \(A_i\) consequently have order \(64\).

Now \(S_1=576\) and \(E=64\).  All \(36\) pair intersections have order at
least eight, so
\[
 288\le S_2\le\frac92E=288.
\]
Equality holds throughout.  Thus every pair intersection has order eight,
and every repeated point has multiplicity nine: apart from \(m=1\), equality
in \(\binom m2\le\frac92(m-1)\) occurs only at \(m=9\).  Consequently all
pair intersections are the same subgroup
\[
 D=\bigcap_iA_i,\qquad |D|=8,
\]
and
\[
 Q=D\ \dot\cup\ \bigdotcup_{i=1}^9(A_i\setminus D).
\tag{H9.43}
\]

Let \(B_i=C_P(x_i)/Z(P)\le A_i\) be the original maximum-clique
centralizer images.  They still cover \(Q\).  Every point of the private
cell \(A_i\setminus D\) must therefore lie in \(B_i\), so
\[
 A_i=B_i\cup D.
\]
A group cannot be the union of two proper subgroups.  Since
\(|D|<|A_i|\), it follows that \(B_i=A_i\) and \(D\le B_i\) for every
\(i\).  But the exact maximum-clique cover has
\(\bigcap_iB_i=1\), contradicting \(|D|=8\).  This excludes \(512\) and
proves (H9.36).

### [PROVED] The order-\(256\) boundary closure

Assume \(|Q|=256\) and \(a(P)>17\).  No inclusion-maximal element
centralizer can be maximal in \(P\): its image would have order \(128\),
and the sharp \(r=7,q=2\) local boundary would make \(P/Z(P)\) scalar
symplectic, with \(a(P)=17\).  Thus all nine labelled IMC enlargements are
nonmaximal and have order at most \(64\).

At least one image has order \(64\).  Otherwise all have order at most
\(32\).  As in the \(512\)-count, at least eight would have order \(32\),
because
\[
 1+7(32-1)+2(16-1)=248<256.
\]
If exactly eight have order \(32\) and the ninth has order \(s\le16\),
the multiplicity calculation gives \(E=s\) and
\[
 S_2\le\frac92s,
\]
whereas the \(28\) large-large and eight large-small intersections give
\[
 S_2\ge28\cdot4+8\frac{s}{8}=112+s>\frac92s.
\]
Thus all nine have order \(32\).  Equality then forces a common
intersection \(D\) of order four and a disjoint partition off \(D\).
The original private-cell argument used after (H9.43) again gives
\(B_i=A_i\) and \(1\ne D\le\bigcap_iB_i=1\), a contradiction.

Suppose exactly one image, say \(A_1\), has order \(64\), while the other
eight have order at most \(32\).  The complement \(Q\setminus A_1\) has
\(192\) points.  For \(j\ge2\), the subgroup product formula gives
\[
 |A_j\setminus A_1|
 \le |A_j|-\frac{|A_j||A_1|}{|Q|}
 =\frac34|A_j|\le24.
\]
The eight sets cover \(Q\setminus A_1\), so equality holds everywhere:
all \(|A_j|=32\), all \(|A_j\cap A_1|=8\), and the eight outside cells
are disjoint.  Every point of \(A_j\setminus A_1\) is then private to the
original \(B_j\), whence
\[
 A_j=B_j\cup(A_j\cap A_1).
\]
The union-of-two-subgroups lemma gives \(B_j=A_j\).  Moreover
\(A_j\setminus A_1\) generates \(A_j\): for
\(h\in A_j\cap A_1\) and \(x\notin A_1\), both \(x\) and \(hx\) lie in
the outside cell.  Its lifts lie in one original private cell, which is
pairwise commuting, so the full centralizer \(C_P(x_j)\) is abelian for
each \(j=2,\ldots,9\).

The remaining centralizer \(C_P(x_1)\) is a finite \(2\)-group of clique
number at most seven and is covered by at most nine abelian subgroups.
Together with the other eight abelian centralizers this gives
\[
 a(P)\le9+8=17,
\]
again a contradiction.  Hence at least two labelled IMC images have order
\(64\).

The order-\(64\) rows of the local table are \(r=5,q=4\), or
\(r=7,q=2\) with \([C:Z(C)]=32\).  [COMPUTED] The complete cutoff-seven certificate
has no exact binary clique-seven group with center quotient of order \(32\):
all ordinary quotient types of that order have an eight-clique, while the
delegated \(C_2^5\) case has a proved nine-clique.  Therefore every surviving
order-\(64\) IMC \(C\) has

\[
 \boxed{\nu(C)=5,\qquad [Z(C):Z(P)]=4,\qquad
 [C:Z(C)]=16.}
\tag{H9.44}
\]

Writing \(Z=Z(P)\) and \(A=Z(C)\), the normalizer construction gives

\[
 C\triangleleft K\triangleleft P,\qquad
 [K:C]=[P:K]=2.
\]

### [COMPUTED] The exact cutoff-five local dichotomy

The complete exterior-square certificate
`experiments/logs/h5_exterior.json` contains \(225\) rows with quotient
order \(16\) and clique number five.  Exactness of \(A=Z(C)\) means that
the identity is the only isolated quotient vertex.  Filtering by this
condition leaves \(84\) rows, all with

\[
 C/A\cong C_2^4.
\]

They have exactly two commutator geometries:

1. \(28\) scalar rows, where \(C'\cong C_2\) and the form on \(C_2^4\)
   is nondegenerate symplectic;
2. \(56\) determinant rows, where \(C'\cong C_2^2\), the five commuting
   two-spaces form a spread, and every nonzero contraction of the
   commutator map is onto \(C'\).

The focused reconstruction
`src/verification/verify_h9_h5_local_dichotomy.py`, its unit test, and
`experiments/logs/h9_h5_local_dichotomy.json` independently parse the
canonical TSV and JSON inputs and verify the split

\[
 225\longrightarrow84=28+56.
\tag{H9.45}
\]

This is the additional cutoff-five computer-assisted input in the
order-\(256\) closure below.

### [PROVED] A transversal centralizer and the central product

For every \(g\notin C\),

\[
 C_A(g)=Z.
\tag{H9.46}
\]

Indeed, if \(a\in A\setminus Z\) commuted with \(g\), then
\(C<C_P(a)\).  Inclusion-maximality of \(C\) among proper element
centralizers would force \(C_P(a)=P\), contrary to \(a\notin Z\).
Consequently every set \(gT\), for a transversal \(T\) of \(Z\) in \(A\),
is a four-clique.  Indeed two members differ on the right by an element
of \(A\), and \(x\) commutes with \(xd\) exactly when it commutes with
\(d\); (H9.46) applies to every nontrivial class \(dZ\).

Fix \(p\in P\setminus K\).  For every \(h\in K\setminus C\), exactly one
\(Z\)-coset in \(hA\) centralizes \(p\).  There is at most one by
\(C_A(p)=Z\).  If there were none, take a five-clique \(Y\subset C\).
For each \(y\in Y\), twisting \(y\) by \(A/Z\) leaves at most one forbidden
class for commutation with \(p\), and at most one for commutation with the
whole four-clique \(hT\).  The latter condition is independent of the
member of \(T\), because \(A=Z(C)\).  One of the four classes therefore
makes the twist noncommute with both \(p\) and every member of \(hT\).
The five independent twists remain a clique and, together with
\(\{p\}\cup hT\), give ten vertices, a contradiction.

There are \([C:A]=16\) such \(A\)-cosets in \(K\setminus C\).  Put

\[
 H=C_P(p),\qquad D=C\cap H.
\]

The one-coset count, followed by the two index-two crossings, gives

\[
 |D|=|C|/4,\qquad |C_K(p)|=|C|/2,\qquad
 |H|=|C|,\qquad |H/Z|=64.
\tag{H9.47}
\]

Every IMC has image of order at most \(64\) in the present
\(a(P)>17\) branch.  Hence \(H\) is itself an IMC and has the local
signature (H9.44).  Put \(B=Z(H)\).  Since \(C_A(p)=Z\), orders give

\[
 D\cap A=Z,\qquad DA=C.
\]

An element of \(Z(D)\) then centralizes both \(D\) and \(A\), hence all of
\(C\), so \(Z(D)=D\cap A=Z\).  The map \(D/Z\to C/A\) preserves
commutators and has one of the two geometries in (H9.45).  Since \(B\)
centralizes \(D\), it follows that \(D\cap B=Z\), and orders give \(DB=H\).
Finally,

\[
 |CH|=\frac{|C||H|}{|D|}=|P|,
\]

so \(P=CH\).  The decompositions \(C=DA\) and \(H=DB\) make \(D\) normal
in both factors and hence in \(P\).  For \(S=\langle A,B\rangle\) we obtain

\[
 \boxed{P=DS,\qquad [D,S]=1,\qquad D\cap S=Z,\qquad
 Z(S)=Z,\qquad |S/Z|=16.}
\tag{H9.48}
\]

For the center assertion, an element of \(Z(S)\) centralizes both factors
of \(P=DS\), so it lies in \(Z(P)=Z\).

### [PROVED] The central product is scalar

Put \(U=D'\le Z\), and let \(X\) be a five-clique in \(D\).  If
\(s,t\in S\) had \([s,t]\notin Z\), the ten distinct elements

\[
 X\{s,t\}=\{xs,xt:x\in X\}
\]

would form a clique: a central \(D\)-commutator cannot cancel a noncentral
\(S\)-commutator.  The same grid is a ten-clique when
\([s,t]\in Z\setminus U\), because every \(D\)-commutator lies in \(U\).
Distinctness uses \(D\cap S=Z\) and the fact that the members of \(X\)
represent distinct \(Z\)-cosets.  Therefore

\[
 1\ne S'\le U\le Z;
\tag{H9.49}
\]

the first inequality follows from \(Z(S)=Z<S\).

Suppose \(D\) has the determinant geometry.  Choose
\(1\ne e=[s,t]\in S'\), and a nonzero functional
\(\lambda:U\to C_2\) with kernel \(\langle e\rangle\).  Composing the
determinant form with \(\lambda\) gives a nondegenerate scalar alternating
form: every nonzero determinant contraction is onto \(U\).  Its standard
five-clique \(X\) has all actual determinant labels outside
\(\{1,e\}\).  Hence \(X\{s,t\}\) is again a ten-clique, a contradiction.

Thus \(D\) has the scalar geometry and \(U\cong C_2\).  Equation (H9.49)
gives \(S'=U\).  Since \(S'\le Z\) has exponent two,

\[
 [s^2,r]=[s,r]^2=1
\]

for all \(r,s\in S\).  Exactness gives \(s^2\in Z(S)=Z\), so
\(S/Z\cong C_2^4\).  Its scalar commutator form has zero radical and is
nondegenerate.  The central product (H9.48) is therefore the orthogonal
sum of two scalar symplectic four-spaces:

\[
 P/Z\cong (D/Z)\perp(S/Z)\cong C_2^8.
\]

The standard scalar calculation gives \(a(P)=17\), contradicting the
standing assumption \(a(P)>17\).  This proves the boundary theorem
(H9.2a).

## [PROVED] Global synthesis

Let \(G\) be arbitrary with \(\nu(G)\le9\).  The exact finite-model theorem
gives a finite group \(F\) with
\[
 (\nu(F),a(F))=(\nu(G),a(G)).
\]
If \(\nu(F)\le8\), the proved cutoff-eight theorem gives \(a(F)\le10\).
Otherwise \(\nu(F)=9\), and the primary-verified finite solvability theorem
applies; this is the CFSG-dependent input declared at the start of the note.

Put \(Q=F/Z(F)\).  If \(Q\) is nilpotent, then \(F\) is nilpotent: the upper
central series of \(Q\) lifts to a central series of \(F\).  The nilpotent
partition gives \(a(F)\le10\) in the odd-primary case and (H9.6) gives
\(a(F)\le73\) in the binary case.  If \(Q\) is nonnilpotent, (H9.3) gives
\(a(F)\le15\).  This proves the upper bound in (H9.1).

Finally, if \(a(F)>17\), only the binary nilpotent branch remains.
The center-index theorem gives \([F:Z(F)]\le256\), while (H9.2a) excludes
the order-\(256\) boundary.  Hence \([F:Z(F)]\le128\).  The all-maximal
theorem would give \(a(F)=17\), so some maximum-clique centralizer is
nonmaximal.  This proves (H9.2).

### [PROVED] Exact remaining reduction

Combining the preceding reductions, the only branch not closed at
seventeen is:

\[
 \boxed{
 \begin{gathered}
 P\text{ a finite }2\text{-group},\qquad \nu(P)=9,\\
 |P/Z(P)|\in\{4,8,16,32,64,128\},\\
 \text{not all nine maximum-clique centralizers are maximal},\\
 18\le a(P)\le73.
 \end{gathered}}
\tag{H9.50}
\]

[UNVERIFIED]
No computation presently classifies every exact commutator kernel over all
binary quotient types of order \(128\).  In particular, random form
pencils, a determinant-module census, or the order-at-most-\(81\)
certificate do not prove that every group in (H9.50) has \(a\le17\).

## [DISPROVED] The tempting maximal-cover shortcut

Maximalizing the nine original centralizer images and retaining a minimal
binary hyperplane cover gives an odd circuit of size
\(k\in\{3,5,7,9\}\).  It is tempting to argue that every private coset of a
retained maximal subgroup must contain three original private sources and
hence that \(3k\le9\).  This argument is invalid.

An original centralizer image \(B_j\) which meets a private cell need not be
contained in the associated retained maximal subgroup; it may satisfy
\(B_jD=Q\), where \(D\) is the common intersection.  Even at the level of
binary circuit geometry, for odd \(k\ge5\) the standard private vectors

\[
 v_i=\mathbf1+e_i\quad(i<k),\qquad v_k=\mathbf1
\]

have two-dimensional spans meeting multiple private cells while lying in
neither corresponding hyperplane.  No current centralizer-specific lemma
rules out the analogous crossing.  Therefore neither \(3k\le9\) nor a
\(k=3\) reduction is used anywhere in this note.
