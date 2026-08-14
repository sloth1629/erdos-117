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

[DISPROVED AS METHODOLOGY] The official abstract of Pyber's 1987 paper
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
