# Failed and Superseded Approaches

## Quotienting by the center

[DISPROVED] Replacing \(G\) by \(G/Z(G)\) does not preserve commutation.
The quotient only detects whether \([x,y]\in Z(G)\), not whether
\([x,y]=1\). For \(D_8\), the quotient is abelian while the exact
central-coset graph is an isolated vertex plus a triangle.

Reusable replacement: compress elements into central cosets while retaining
the original zero/nonzero commutator relation.

## A finite transversal generates a finite group

[DISPROVED] If \(T\) is a transversal for \(Z(G)\), the subgroup
\(\langle T\rangle\) need not be finite. In
\(Q_8\times\langle z\rangle\), a representative such as \((i,z)\) may
generate a nontrivial infinite central power.

Reusable replacement: the generated subgroup is finitely generated and
central-by-finite; quotient a finitely generated central subgroup by a
carefully chosen finite-index subgroup avoiding the finitely many relevant
commutators.

## Arbitrary finite quotients preserve commutation

[DISPROVED] A finite quotient can kill a nontrivial commutator and create new
commuting pairs. The finite-model proof must explicitly avoid every nonzero
commutator among central-transversal representatives.

## Direct-product multiplicativity

[DISPROVED] The noncommuting graph of \(G\times H\) is an OR product, but
clique and chromatic numbers are not generally multiplicative for OR
products. At graph level,
\[
(\omega,\chi)(C_5)=(2,3),\qquad
(\omega,\chi)(C_5\vee C_5)=(5,8),
\]
not \((4,9)\).

Reusable replacement: use fractional chromatic number and complementary
Shannon capacity for direct-power rates. Fixed-seed powers give only a
polynomial relation between \(a\) and \(\nu\), not an exponential lower
bound for \(h(n)\).

## Binary symplectic groups are exact extremizers

[DISPROVED] The proposal
\[
h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}
\]
fails first at \(n=1,2\), and its restriction to \(n\geq3\) fails at
\(n=7\): the group \(S(3,2)\) has \((\nu,a)=(7,10)\), while the formula
gives 9.

Reusable lesson: even scalar-valued alternating commutator maps in odd
characteristic can outperform the binary family at finite parameters.

## Using inaccessible quantitative sources as proof

[DISPROVED] The official abstract of Pyber's 1987 paper
supports a fixed-base finite-group center-index bound, but not its detailed
constant or proof. The explicit expression found in a dissertation remains
secondary evidence and is not a load-bearing repository theorem.

## Bounding a capable quotient from its own clique number

[DISPROVED] The proposed cutoff-eight reduction

\[
Q\text{ finite, solvable and capable},\quad \nu(Q)\leq8
\quad\Longrightarrow\quad |Q|\leq108
\]

is false, even with \(8\) replaced by \(4\). For any prime \(p\), let \(E_p\)
be an extraspecial group of order \(p^3\). Then

\[
Z(E_p)\cong C_p,\qquad E_p/Z(E_p)\cong C_p^2.
\]

Since \(S_3\) is centerless, the group \(E_p\times S_3\) has central quotient

\[
(E_p\times S_3)/Z(E_p\times S_3)\cong C_p^2\times S_3.
\]

Thus \(Q_p=C_p^2\times S_3\) is finite, solvable, and capable for every
prime \(p\). Its abelian direct factor has no effect on commutation, so
\(\nu(Q_p)=\nu(S_3)=4\), whereas \(|Q_p|=6p^2\) is unbounded.

Reusable replacement: a cutoff argument must retain the commutator map of
the **particular exact central extension** \(G\to Q=G/Z(G)\) and the
hypothesis \(\nu(G)\leq8\); capability and \(\nu(Q)\) alone discard precisely
the information that can control central chief factors. For example, in the
displayed witness extension, a \((p+1)\)-clique in \(E_p\) and a four-clique
in \(S_3\) have Cartesian product a \(4(p+1)\)-clique in \(E_p\times S_3\).
This is only the general OR-product lower bound obtained by multiplying two
explicit cliques, not a claim of clique-number multiplicativity.

## A local centralizer-index drop

[DISPROVED] The tempting inequality

\[
[G:C_G(x)]\leq \nu(G)-\nu(C_G(x))
\]

does not hold in general.  The canonical complete-table certificate in
`notes/h8_local_inequality_counterexample.md` takes
\(G=\operatorname{SmallGroup}(48,15)\) and an involution \(x\) whose
centralizer is abelian of order four.  It verifies

\[
\nu(G)=12,\qquad \nu(C_G(x))=1,
\qquad [G:C_G(x)]=12>11.
\]

Reusable lesson: a centralizer chain cannot obtain a multiplicative
center-index bound by charging the whole index at a step to the decrease in
noncommuting clique number.  Any replacement needs additional hypotheses or
a different local quantity.  No minimal-counterexample claim is made.

## Forcing an extra drop among clique-member centralizers

[DISPROVED] Even when \(x_1,\ldots,x_m\) form a maximum noncommuting set,
it need not be true that one of their centralizers has clique number below
the universal bound \(m-2\).  In the binary scalar symplectic group
\(E_3\), the repository proves \(\nu(G)=7\).  Write
\(V=G/Z(G)\cong\mathbf F_2^6\) with its nondegenerate alternating form.
For every noncentral \(x\), represented by \(0\ne v\in V\),

\[
C_G(x)/Z(G)=v^\perp.
\]

The restriction to \(v^\perp\) has radical \(\langle v\rangle\), and the
quotient is a four-dimensional nondegenerate binary symplectic space.
The proved formula \(\nu(E_r)=2r+1\) in
`notes/class_two_geometry.md` therefore gives

\[
\nu(C_G(x))=5=\nu(G)-2.
\]

Thus every member of every maximum seven-clique has the simultaneously
sharp signature \((5,5,5,5,5,5,5)\).  Any useful sum or product constraint
at cutoff eight must exploit something special to that cutoff; it cannot
follow merely by summing strengthened individual centralizer drops.

## Replacing several centralizers by their private cells for free

[DISPROVED] The one-private-cell cover does not extend by simply replacing
an arbitrary collection of centralizers with the abelian subgroups generated
by their private cells.  The same group \(E_3\) gives a transparent
counterexample.  Choose its standard seven-clique
\(v_1,\ldots,v_7\) with

\[
B(v_i,v_j)=1\quad(i\ne j),
\qquad \sum_{i=1}^7v_i=0.
\]

The injective signature map

\[
V\longrightarrow\mathbf F_2^7,
\qquad
u\longmapsto\bigl(B(u,v_1),\ldots,B(u,v_7)\bigr)
\]

has image exactly the even-weight subspace.  A private cell for index \(i\)
has the signature that is zero at \(i\) and one elsewhere, so its generated
subgroup maps to the line \(\langle v_i\rangle\).  For any prescribed
three-element set \(J\), however, the vector that is zero on \(J\) and one
off \(J\) has even weight four and therefore is the signature of some
\(u\in V\).  This element commutes with exactly the three clique members
indexed by \(J\), lies in none of their private generated lines, and lies
outside all the other centralizers.

### [PROVED] Reusable multi-private-cell cover

Let \(P_j=C_G(x_j)\setminus\bigcup_{k\ne j}C_G(x_k)\). For every
\(J\subseteq\{1,\ldots,m\}\), the valid cover is

\[
G=\bigcup_{i\notin J}C_G(x_i)
 \ \cup\ \bigcup_{j\in J}\langle P_j\rangle
 \ \cup\ \bigcup_{\{j,k\}\subseteq J}
       \bigl(C_G(x_j)\cap C_G(x_k)\bigr).
\]

Indeed, an element outside every \(C_G(x_i)\) with \(i\notin J\) commutes
with at least one \(x_j\), since otherwise it would extend the maximum
clique. If it commutes with exactly one such member, it lies in \(P_j\); if
it commutes with at least two, it lies in one of the displayed pairwise
intersections.

The intersection terms cannot be discarded without additional structure;
in the binary symplectic example they can themselves retain the full
\(m-2\) clique bound.

## A withdrawn exponential abelian-cover theorem

[DISPROVED] Theorem 1.1 of Nagy--Pach--Tomon,
*Irredundant hyperplane covers*, arXiv:2205.03389v1, cannot be used as a
proof that every irredundant \(k\)-coset cover of an abelian group has
intersection index \(2^{O(k)}\).  The official current arXiv record is v2,
withdrawn on 31 October 2022.  Its comments identify an error in Claim 4.5
of Section 4.2 and state that the error invalidates most of the paper.
Consequently neither the theorem nor the appendix's proposed numerical
base 20 is load-bearing.

This false lead was especially tempting because, combined with the valid
Guralnick--Maróti BFC derived-subgroup theorem and the repository's
class-two centralizer reduction, it would have reproduced a fixed-base
exponential center-index bound.  Reading only the still-accessible v1 PDF
is insufficient; current withdrawal metadata must be checked before a
preprint is promoted.

Reusable replacement: the authors' earlier, unwithdrawn manuscript
*Additive bases, coset covers, and non-vanishing linear maps*,
arXiv:2111.13658, states only the weaker
\(\exp(O(k\log\log k))\) abelian intersection bound.  That separate theorem
requires its own proof audit before use and cannot yield a fixed-base
constant by itself.
