# The solvable nonnilpotent branch at cutoff eight

## [PROVED] Scope and result boundary

This note treats a finite group \(G\) with

\[
\nu(G)=8,
\qquad Q=G/Z(G)
\]

such that \(Q\) is solvable and nonnilpotent.  The exact finite-model
theorem justifies the finite scope for the extremal problem.  The quotient
\(Q\) is always the **particular exact center quotient** of \(G\); no
capability criterion and no value of \(\nu(Q)\) is substituted for the
commutation data of \(G\).

The main reduction below closes the branch in which maximalizing the
clique-centralizer cover introduces no common normal core.  At this
intermediate stage, the other branch identified that core, rather than a
large affine chief factor, as the precise obstruction.  The later notes
`common_core_frattini_reduction.md`,
`common_core_binary_semidirect.md`, and
`common_core_coprime_closure.md` close that obstruction without descending
the exact commutator pairing through the core quotient.

## [PROVED] The exact cover and its maximal skeleton

Choose a maximum noncommuting set

\[
X=\{x_1,\ldots,x_8\},
\qquad C_i=C_G(x_i),
\qquad H_i=C_i/Z(G)\leq Q.
\tag{NR.1}
\]

The structural-reduction theorem gives

\[
Q=\bigcup_{i=1}^8H_i,
\qquad \bigcap_{i=1}^8H_i=1,
\tag{NR.2}
\]

and this cover is irredundant.  Notice that \(H_i\) is the image of the
**exact** centralizer \(C_G(x_i)\).  It can be strictly smaller than
\(C_Q(x_iZ(G))\).

Choose a maximal subgroup above every \(H_i\), remove duplicates, and then
remove redundant members.  This gives an irredundant cover

\[
Q=M_1\cup\cdots\cup M_k,
\qquad 3\leq k\leq8,
\tag{NR.3}
\]

by maximal subgroups.  Put

\[
D=\bigcap_{i=1}^kM_i,
\qquad R=D_Q=\bigcap_{q\in Q}D^q,
\qquad L=Q/R.
\tag{NR.4}
\]

The lower bound \(k\geq3\) is elementary.  One proper subgroup cannot cover
a group.  If two incomparable proper subgroups did, the product of one
element private to each would lie in neither; if they are comparable, their
union is just the larger proper subgroup.

Then the images \(\overline M_i=M_i/R\) form an irredundant maximal-subgroup
cover of \(L\), and

\[
\left(\bigcap_i\overline M_i\right)_L=1.
\tag{NR.5}
\]

Also

\[
\Phi(L)=1.
\tag{NR.6}
\]

Indeed, the Frattini subgroup is normal and is contained in every maximal
subgroup, hence in \(\bigcap_i\overline M_i\); (NR.5) then makes it trivial.
Every noncommuting set in \(L\) lifts to a noncommuting set in \(Q\), and
every noncommuting set in \(Q\) lifts to one in \(G\).  Thus only the safe
one-way inequalities are used:

\[
\nu(L)\leq\nu(Q)\leq\nu(G)=8.
\tag{NR.7}
\]

No converse inequality is asserted.

## [PROVED] Every minimal normal factor of the skeleton has order at most eight

Let \(U\ne1\) be a minimal normal subgroup of \(L\).  Solvability makes
\(U\) elementary abelian.  It cannot be contained in
\(\bigcap_i\overline M_i\), because a normal subgroup contained there lies
in the core (NR.5).  Let \(s\) of the \(k\) cover members contain \(U\), and
put \(t=k-s\).

For every \(j\) with \(U\nleq\overline M_j\), maximality gives

\[
L=U\overline M_j.
\]

Moreover \(U\cap\overline M_j\) is normalized by \(\overline M_j\), and it
is normalized by the abelian group \(U\).  It is therefore normal in \(L\).
Minimality of \(U\) gives

\[
U\cap\overline M_j=1.
\tag{NR.8}
\]

Fix such a \(j\), and choose a private point

\[
y\in\overline M_j\mathbin{\big\backslash}
       \bigcup_{i\ne j}\overline M_i.
\]

This is a new private point of the minimal maximal cover; it is not assumed
to be the image of \(x_j\).  A member containing \(U\) misses the whole
coset \(Uy\), since an element \(uy\) in such a member would also put \(y\)
in it.  By (NR.8), every member not containing \(U\) meets \(Uy\) in at most
one point.  The \(t\) latter members cover \(Uy\), so

\[
|U|\leq t=k-s\leq8.
\tag{NR.9}
\]

Consequently every minimal normal subgroup of \(L\) has one of the orders

\[
2,3,4,5,7,8.
\tag{NR.10}
\]

This is the exact place where private points are used.  It does not assume
that all eight original centralizers were maximal.

## [PROVED] Fitting structure of the Frattini-free skeleton

Let \(F=F(L)\).  Then

\[
F=\operatorname {Soc}(L)
\]

is an abelian direct product of minimal normal subgroups, and

\[
C_L(F)=F.
\tag{NR.11}
\]

Here is a self-contained proof.  Every minimal normal subgroup of a finite
solvable group is elementary abelian and lies in \(F\).  If
\(U\leq F\) is minimal normal, then \(U\leq Z(F)\): inside the relevant
normal Sylow subgroup of \(F\), the nontrivial intersection with its center
is normal in \(L\), and minimality gives all of \(U\).  Since
\(\Phi(L)=1\), there is a maximal subgroup \(T\) not containing \(U\).
As above,

\[
L=U\rtimes T,
\qquad U\cap T=1.
\]

It follows that

\[
F=U\times(F\cap T),
\]

and \(F\cap T\) is normal in \(L\): it is normalized by \(T\), while the
central subgroup \(U\leq Z(F)\) also normalizes it.  Induction on \(|F|\)
decomposes \(F\) as a direct product of minimal normal subgroups.  In
particular, \(F\) is abelian.

Now \(C=C_L(F)\) is normal and contains \(F\).  If \(C>F\), choose
\(F<N\leq C\) with \(N/F\) minimal normal in \(L/F\).  Then \(N/F\) is an
elementary abelian \(p\)-group and \(F\leq Z(N)\).  For a Sylow
\(p\)-subgroup \(P\) of \(N\), the equality \(N=FP\) shows that \(N\) is the
product of \(P\) with the central Sylow subgroups of \(F\) of order prime to
\(p\).  Hence \(N\) is nilpotent.  This contradicts the maximality of the
normal nilpotent subgroup \(F\), proving (NR.11).

In particular, conjugation gives a faithful embedding

\[
L/F\hookrightarrow
 \prod_{U\text{ minimal normal in }L}\operatorname {Aut}(U).
\tag{NR.12}
\]

The factors in (NR.10) show, for example, that every prime divisor of this
Frattini-free skeleton belongs to \(\{2,3,5,7\}\).  This prime restriction is
for \(L\), not automatically for the common core \(R\) or for \(Q\).

## [PROVED] The abelian-normal-fiber clique

Let \(V\triangleleft K\) be abelian and let \(g\in K\) act nontrivially on
\(V\).  With \(v^g=g^{-1}vg\), the map

\[
\delta_g:V\longrightarrow V,
\qquad \delta_g(v)=v^{-1}v^g
\]

is a homomorphism.  If \(T\) is a transversal for its kernel, direct
multiplication gives

\[
gv\text{ commutes with }gw
 \quad\Longleftrightarrow\quad
\delta_g(v)=\delta_g(w).
\]

Thus \(\{gt:t\in T\}\) is a clique of size
\([V:C_V(g)]\).  If \(u\in V\) is moved by \(g\), then \(u\) fails to
commute with every \(gt\), independently of \(t\).  Therefore

\[
\nu(K)\geq [V:C_V(g)]+1.
\tag{NR.13}
\]

More generally, if \(g_1,\ldots,g_m\) have pairwise noncommuting images in
\(K/V\), the corresponding fiber cliques are completely joined.  Hence

\[
\nu(K)\geq
 \sum_{i=1}^m[V:C_V(g_i)].
\tag{NR.14}
\]

Both statements are made inside \(K\); no quotient is assumed to preserve
commutation in the opposite direction.

## [PROVED] The only possible noncentral minimal-normal action

Let \(U\leq F(L)\) be minimal normal and noncentral.  A complement \(T\) to
\(U\) exists by \(\Phi(L)=1\).  Put

\[
A=L/C_L(U)\leq\operatorname {Aut}(U).
\]

Equivalently, if \(K=C_T(U)\), then \(K\triangleleft L\) and

\[
L/K\cong U\rtimes A.
\tag{NR.15}
\]

Indeed, \(C_T(U)\) is normal in \(T\) and is centralized by \(U\), so it is
normal in \(L=UT\).  Conversely, every normal subgroup of \(L\) contained
in \(T\) centralizes \(U\), because its commutator with \(U\) lies in the
trivial intersection with \(U\).  Thus \(K\) is the core of \(T\), and
(NR.15) follows.  Minimality makes the action of \(A\) on \(U\) faithful and
irreducible.

The possibilities in (NR.10) now reduce as follows.

- \(U\cong C_2\) cannot be noncentral because its automorphism group is
  trivial.
- If \(U\cong C_3,C_5\), or \(C_7\), then \(A\) is a nontrivial subgroup of
  the cyclic group \(\mathbf F _p^\times\).
- If \(U\cong C_2^2\), an irreducible subgroup of
  \(\mathrm {GL}(2,2)\cong S_3\) has order three or six.  The order-six case
  makes (NR.15) the affine group \(C_2^2:S_3\cong S_4\), which already has a
  ten-clique.  Explicitly, in \(S_4\) take

  \[
  (12),(13),(14);
  \quad(123),(124),(134),(234);
  \quad(1234),(1243),(1324).
  \]

  The three transpositions are pairwise noncommuting.  A \(3\)-cycle has
  centralizer its order-three subgroup, and a \(4\)-cycle has centralizer its
  order-four subgroup.  The displayed \(3\)- and \(4\)-cycles use distinct
  such cyclic subgroups, so all ten displayed elements are pairwise
  noncommuting.  Thus only \(A\cong C_3\) survives.
- \(U\cong C_2^3\) is impossible.  To see this without a subgroup
  classification, suppose that a solvable irreducible
  \(A\leq\mathrm {GL}(3,2)\) had no element of order seven.  Since
  \(|\mathrm {GL}(3,2)|=168\), a minimal normal subgroup \(N\) of \(A\)
  would be an elementary abelian \(2\)- or \(3\)-group.  In the first case,
  the fixed space \(C_U(N)\) is nonzero (orbit counting for a \(2\)-group on
  the eight vectors) and is \(A\)-invariant; irreducibility would make \(N\)
  act trivially, contradicting faithfulness.  In the second case,
  \(3^2\nmid168\), so \(N\cong C_3\).  An order-three operator on a
  three-dimensional binary space has a one-dimensional fixed space, again
  a forbidden \(A\)-invariant subspace.  Therefore \(A\) contains an
  element of order seven.  Such an element fixes no nonzero vector, since a
  nonzero-vector stabilizer in \(\mathrm {GL}(3,2)\) has order \(24\).
  The affine quotient (NR.15) then has, by (NR.13), a clique of size
  \(8+1=9\), contradicting (NR.7).

It follows that the affine quotient belonging to a noncentral minimal normal
subgroup is one of exactly seven groups:

\[
S_3,\quad A_4,\quad C_5:C_2,\quad C_5:C_4,\quad
C_7:C_2,\quad C_7:C_3,\quad C_7:C_6.
\tag{NR.16}
\]

Here \(A_4=C_2^2:C_3\); the other six descriptions are the fixed-point-free
one-dimensional affine actions.

## [PROVED] At most one minimal normal factor is noncentral

Write \(F=\prod_jU_j\) as in (NR.11).  For every \(g\in L\),

\[
[F:C_F(g)]=\prod_j[U_j:C_{U_j}(g)].
\tag{NR.17}
\]

For each surviving noncentral factor in (NR.16), a nontrivial action moves
at least three points in the index sense: the index is \(3,5\), or \(7\) in
the odd one-dimensional cases and \(4\) on \(C_2^2\).  If one element acted
nontrivially on two such factors, (NR.17) and the fiber clique would give a
clique of size at least \(3\cdot3=9\).

If two factors \(U,V\) were noncentral but no element acted on both, choose
\(g\) acting on \(U\) and \(h\) acting on \(V\).  The preceding observation
forces \(g\) to act trivially on \(V\) and \(h\) trivially on \(U\); then
\(gh\) acts nontrivially on both, the same contradiction.  Hence at most one
minimal normal factor is noncentral.

All other minimal normal factors are central.  To make the direct-product
step explicit, choose a central minimal normal subgroup \(A\cong C_p\).
Since \(A\nleq\Phi(L)\), some maximal subgroup \(M\) avoids \(A\), and

\[
L=A\times M.
\]

The complement is normal because \(A\) is central, and
\(\Phi(M)=1\) because the Frattini subgroup of this direct product is
\(\Phi(A)\times\Phi(M)\).  Minimal normal subgroups of \(M\) are also
minimal normal in \(L\).  Iterating removes all central minimal factors.
If the final direct factor has no noncentral minimal normal factor, (NR.11)
makes it equal to its central Fitting subgroup and hence abelian.  Otherwise
its Fitting subgroup is the unique noncentral minimal normal subgroup \(U\);
(NR.11) and a complement to \(U\) identify that final factor with the
faithful affine group \(U\rtimes A\) already listed in (NR.16).  This gives
the following complete skeleton description:

\[
\boxed{
  L\text{ is either abelian, or }L=C\times H,
}
\tag{NR.18}
\]

where \(C\) is central and is a direct product of elementary abelian
\(2\)-, \(3\)-, \(5\)-, and \(7\)-groups, and \(H\) is one of the seven
groups in (NR.16).  In the abelian case, \(L\) is itself a direct product of
elementary abelian groups at those four primes.  The numerical cutoff also
retains

\[
|L|\leq |Q|\leq40{,}320.
\tag{NR.19}
\]

Thus (NR.18), rather than an unrestricted solvable group of order at most
\(40{,}320\), is the maximal-cover skeleton that remains.

## [PROVED] Exact pairing collapses the core-free case to eight quotients

Assume now that

\[
R=1.
\tag{NR.20}
\]

Then \(L=Q\), so the exact central-extension pairing of \(G\to Q\) is
available.  Since \(Q\) is nonnilpotent, (NR.18) gives \(Q=C\times H\) with
\(H\) in (NR.16).  Each such \(H\) is centerless.  The proved exact-center
restrictions give

\[
\dim_{\mathbf F_2}C_2\leq2,
\qquad
\dim_{\mathbf F_3}C_3\leq2,
\qquad
\dim_{\mathbf F_5}C_5\leq2,
\qquad C_7=1.
\tag{NR.21}
\]

If a Sylow component \(A\leq C\) has order coprime to
\(((C/A)\times H)_{\rm ab}\), the proved coprime central-direct-factor lemma
gives

\[
\nu(G)\geq3\nu((C/A)\times H)\geq12.
\]

The final inequality is immediate from (NR.13): every listed affine group
\(H=V:B\) has \(\nu(H)\geq |V|+1\geq4\), and the central direct factor
\(C/A\) does not change commutation in \(H\).

Consequently only primes dividing \(|H_{\rm ab}|\) can occur in \(C\).

It remains to treat such a prime \(p\).  Write the Frobenius group in
(NR.16) as

\[
H=V:B,
\]

where \(B\) is cyclic and fixed-point-free on \(V\), and choose a generator
\(b\) of \(B\).  Let \(A=C_p^r\) be the full \(p\)-part of \(C\), where
\(1\leq r\leq2\).  Write the subgroup of \(p\)-torsion values in \(Z(G)\)
additively as an \(\mathbf F_p\)-space.  For lifts to \(G\), define the exact
central pairing

\[
\beta(a,a')=[\widetilde a,\widetilde {a'}],
\qquad T_q(a)=[\widetilde a,\widetilde q].
\]

Because \(V=H'\), the second-variable factorization through the
abelianization gives

\[
T_{vb}=T_b\qquad(v\in V).
\tag{NR.22}
\]

The common kernel of \(\beta(a,A)\) and \(T_b(a)\) is zero.  Indeed, values
against central components of order prime to \(p\) vanish, and \(b\)
generates \(H_{\rm ab}/H_{\rm ab}^p\); a vector in that common kernel would
therefore be in the forbidden left radical of the exact center pairing.

The exact same-fiber formula is

\[
[\widetilde a\widetilde q,
  \widetilde {a'}\widetilde q]
=\beta(a,a')+T_q(a)-T_q(a').
\tag{NR.23}
\]

If \(r=1\), then \(\beta=0\) and \(T_b\) is injective, so every \(A(vb)\)
fiber contains a \(p\)-clique.  If \(r=2\) and \(\beta=0\), the same argument
gives a \(p^2\)-clique.  If \(r=2\) and \(\beta\ne0\), choose a scalar
functional on its image that makes \(\beta\) a nondegenerate alternating
form on \(A\).  The scalarization of (NR.23) is a translate of that
symplectic form.  More explicitly, write the scalarized form as \(B\) and
the scalarized evaluation as \(\ell\).  There is a \(t\in A\) with
\(\ell(a)=B(t,a)\), and the scalarization of (NR.23) is exactly

\[
B(a-t,a'-t).
\]

One point from each of the \(p+1\) projective lines, translated by \(t\),
then gives a \((p+1)\)-clique.  A nonzero scalarized commutator is also a
nonzero actual commutator.

Finally, the \(|V|\) elements \(vb\) are pairwise noncommuting in \(H\), so
the corresponding fiber cliques are completely joined in \(G\).  For
\(r\geq1\), this gives the uniform lower bound

\[
\nu(G)\geq p|V|.
\tag{NR.24}
\]

For \(r=2\), the lower bound is \((p+1)|V|\) when \(\beta\ne0\), and
\(p^2|V|\) when \(\beta=0\).

The resulting elimination is explicit:

| \(H\) | \(|V|\) | \(H_{\rm ab}\) | possible \(p\) before (NR.24) | lower bound |
|:---|---:|:---:|---:|---:|
| \(S_3=C_3:C_2\) | \(3\) | \(C_2\) | \(2\) | \(6\) |
| \(A_4=C_2^2:C_3\) | \(4\) | \(C_3\) | \(3\) | \(12\) |
| \(C_5:C_2\) | \(5\) | \(C_2\) | \(2\) | \(10\) |
| \(C_5:C_4\) | \(5\) | \(C_4\) | \(2\) | \(10\) |
| \(C_7:C_2\) | \(7\) | \(C_2\) | \(2\) | \(14\) |
| \(C_7:C_3\) | \(7\) | \(C_3\) | \(3\) | \(21\) |
| \(C_7:C_6\) | \(7\) | \(C_6\) | \(2\) or \(3\) | \(14\) or \(21\) |

Thus every nontrivial \(C\) is excluded except possibly \(C=C_2\) when
\(H=S_3\).  In that exceptional row, \(r=2\) would give at least
\(3|V|=9\), so only \(r=1\) survives.  Therefore (NR.20) forces

\[
Q\in\{
S_3,A_4,C_5:C_2,C_5:C_4,C_7:C_2,C_7:C_3,C_7:C_6,
C_2\times S_3
\}.
\tag{NR.25}
\]

In particular,

\[
|Q|\leq42.
\tag{NR.26}
\]

## [COMPUTED] The core-free maximalization branch has \(a(G)\leq10\)

The committed certificate in notes/h8_bounded_cutoff.md exhausts every
exact central-extension graph with \(|Q|\leq81\) at clique cutoff eight and
finds abelian-cover number at most ten.  All eight quotients in (NR.25) have
order at most \(42\).  Consequently

\[
R=1\quad\Longrightarrow\quad a(G)\leq10.
\tag{NR.27}
\]

This invokes only the already certified bounded census; it does not turn
that census into a global \(|Q|\leq81\) reduction.

## [PROVED] Exact description of the intermediate obstruction

At this stage, the only unresolved solvable nonnilpotent branch had

\[
1\ne R=\left(\bigcap_{i=1}^kM_i\right)_Q,
\tag{NR.28}
\]

where the \(M_i\) arise from a minimal maximalization of the exact
clique-centralizer cover.  Its quotient satisfies the sharp alternative

\[
Q/R\text{ is abelian, or }Q/R=C\times H
\tag{NR.29}
\]

with \(C\) and \(H\) as in (NR.18), and \(|Q/R|\leq40{,}320\).

The original exact centralizers still cut the core in a genuine cover:

\[
R=\bigcup_{i=1}^8(R\cap H_i),
\qquad
\bigcap_{i=1}^8(R\cap H_i)=1.
\tag{NR.30}
\]

If \(\widetilde R\) is the preimage of \(R\) in \(G\), then

\[
R\cap H_i=
\bigl(C_{\widetilde R}(x_i)Z(G)\bigr)/Z(G).
\tag{NR.31}
\]

These are exact fixed subgroups for the actions of the possibly external
elements \(x_i\).  They need not be element-centralizers of the abstract
group \(R\), the cover (NR.30) need not be irredundant, and its members need
not inherit private points.

For comparison, the original private cell

\[
P_j=C_j\mathbin{\big\backslash}\bigcup_{i\ne j}C_i
\]

is pairwise commuting and generates an abelian subgroup \(A_j\), giving the
valid cover

\[
G=A_j\cup\bigcup_{i\ne j}C_i.
\tag{NR.32}
\]

But the maximal members \(M_i\) are not exact centralizers, and replacing
several \(C_i\) by private-cell subgroups is known to require the pairwise
intersection terms recorded in notes/failed_approaches.md.  Thus neither
(NR.30) nor (NR.32) removes \(R\) for free.

Most importantly, the exact pairing used in (NR.21)--(NR.24) does not
descend through the generally noncentral quotient \(Q\to Q/R\).  Quotienting
can kill a nontrivial commutator and create a commuting pair.  If \(Q/R\) is
abelian, all nonnilpotence can also be hidden in \(R\) and its conjugation
action.  These are the exact reasons that (NR.28), rather than any of the
small affine factors, was the load-bearing gap left by this intermediate
reduction.

## [PROVED] Subsequent closure of the historical remaining task

This note alone did not control the nontrivial common core \(R\) in
(NR.28).  The later Frattini and binary-semidir reductions force the exact
center quotient into the form \(C_3\rtimes_\chi S\), with \(S\) a finite
\(2\)-group.  The coprime closure then removes central direct factors and
proves the exact identity
\(\nu(C_3\rtimes_\chi U)=\nu(\ker\chi)+3\omega(U\setminus\ker\chi)\).
At clique number eight this gives a five-plus-three abelian cover and closes
the branch.  Together with the exhaustive nilpotent alternatives, the later
argument proves \(h(8)=10\).

## [PROVED] Adversarial scope checks

1. Only \(\nu(Q/R)\leq\nu(Q)\leq\nu(G)\) is used; equality with a quotient
   clique number is never assumed.
2. The affine groups in (NR.16) arise from complements to actual minimal
   normal subgroups of the Frattini-free skeleton, not from capability.
3. The eight original clique-centralizers are not assumed maximal.  The
   argument explicitly allows a smaller minimal maximal subcover of size
   \(k\leq8\) and records the resulting core \(R\).
4. The private point used in (NR.9) belongs to the minimal maximal cover and
   is not silently identified with an original clique element.
5. Exact center-pairing arguments are used only after imposing \(R=1\).
   They are not transferred to the abstract quotient \(Q/R\).
6. The final computational invocation is restricted to the eight quotients
   of order at most \(42\) in (NR.25), inside the stated order-at-most-\(81\)
   certificate.
