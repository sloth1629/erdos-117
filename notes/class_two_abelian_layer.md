# The abelian layer in a class-two \(p\)-group

## A charged centralizer-chain bound

[PROVED] Let \(P\) be a finite \(p\)-group of nilpotency class at most two,
put \(m=\nu(P)\), and let \(A\leq P\) be abelian with \(Z(P)\leq A\).  Then

\[
 [A:Z(P)]\leq p^{m/p}\leq 3^{m/3}.
\tag{AL.1}
\]

If \(A=Z(P)\), there is nothing to prove.  Otherwise set \(K_0=A\).  Since

\[
 Z(P)=A\cap Z(P)=\bigcap_{x\in P}C_A(x)
\]

and \(P\) is finite, elements \(x_1,\ldots,x_t\in P\) can be chosen so that

\[
 K_i=K_{i-1}\cap C_A(x_i),\qquad
 K_0>K_1>\cdots>K_t=Z(P).
\]

Write

\[
 q_i=[K_{i-1}:K_i]=p^{e_i},\qquad e_i\geq1.
\tag{AL.2}
\]

We prove inductively that \(P\) contains a noncommuting set \(S_i\) of size

\[
 |S_i|=q_1+\cdots+q_i
\tag{AL.3}
\]

which is centralized by \(K_i\).  Take \(S_0=\varnothing\).  Suppose that
\(S_{i-1}\) has been constructed, put \(K=K_{i-1}\), \(x=x_i\), and choose
a transversal \(T\subseteq K\) for

\[
 K_i=C_K(x).
\]

The set

\[
 B_i=\{xt:t\in T\}
\tag{AL.4}
\]

is a \(q_i\)-clique.  Indeed, the class-two commutator identities and the
commutativity of \(K\leq A\) give, for distinct \(t,u\in T\),

\[
 [xt,xu]=[x,u][t,x],
\]

which is nontrivial because \(t\) and \(u\) represent different cosets of
\(C_K(x)\).

For each \(s\in S_{i-1}\), choose \(a_s\in K\) such that

\[
 [s a_s,x]\neq1.
\tag{AL.5}
\]

This is always possible: the homomorphism
\(a\mapsto[a,x]\) on \(K\) has \(q_i\geq2\) values, while at most one value
can cancel \([s,x]\).  Because \(K\) centralizes \(S_{i-1}\) and is abelian,
replacing every \(s\) by \(s a_s\) preserves every old noncommuting pair.
Moreover, for every \(t\in T\),

\[
 [s a_s,xt]=[s,x][a_s,x]\neq1;
\]

the right side is independent of \(t\).  Thus the modified old set together
with \(B_i\) is a clique of the size in (AL.3).  Finally, \(K_i\) centralizes
the modified old vertices and all of \(B_i\), so the induction invariant is
preserved.

At \(i=t\), (AL.3) and the definition of \(m\) imply

\[
 \sum_{i=1}^t q_i\leq m.
\tag{AL.6}
\]

On the other hand, the subgroup chain and (AL.2) give

\[
 [A:Z(P)]=\prod_{i=1}^tq_i=p^{\sum_i e_i}.
\]

For every \(e\geq1\), one has \(e\leq p^{e-1}\), and hence
\(e_i\leq q_i/p\).  Equation (AL.6) now gives

\[
 \sum_i e_i\leq\frac1p\sum_iq_i\leq\frac mp,
\]

which proves the first inequality in (AL.1).  Finally,
\(p^{1/p}\leq3^{1/3}\) for every prime \(p\): the function
\((\log x)/x\) decreases for \(x\geq3\), and the remaining comparison is
\(2^{1/2}<3^{1/3}\).  This proves the second inequality.  \(\square\)

## Consequence for commuting subsets

[PROVED] If \(B\leq P\) is any abelian subgroup, then \(BZ(P)\) is abelian
and

\[
 [B:B\cap Z(P)]=[BZ(P):Z(P)]\leq p^{m/p}.
\tag{AL.7}
\]

Equivalently, every isotropic subgroup of the central commutator model
\(P/Z(P)\) has order at most \(p^{m/p}\).

## A relative-center version

[PROVED] More generally, let \(H\leq P\) contain \(Z(P)\), and put
\(r=\nu(H)\).  Then

\[
 [Z(H):Z(P)]
 \leq p^{(m-r)/p}
 \leq 3^{(m-r)/3}.
\tag{AL.8}
\]

Choose an \(r\)-clique \(Y\) in \(H\), set \(A=Z(H)\), and run the
centralizer chain used above from \(K_0=A\) down to \(Z(P)\).  The same
block induction starts with \(S_0=Y\), rather than the empty set: \(K_0\)
centralizes \(Y\), and every later \(K_i\) centralizes the modified old
vertices by the induction invariant.  It therefore produces a clique of
size

\[
 r+\sum_iq_i.
\]

Consequently \(\sum_iq_i\leq m-r\).  The index calculation from (AL.2)
through (AL.6), with \(m\) replaced by \(m-r\), proves (AL.8).

## Exact remaining gap

[UNVERIFIED] Bound (AL.1) controls the \(A/Z(P)\) side of a maximal abelian
subgroup, but it does not control \([P:A]\).  In higher-codomain commutator
maps the latter index need not be bounded by \([A:Z(P)]\); the exterior-product
map already has maximal isotropic subspaces of dimension one in arbitrarily
large ambient dimension.  A fixed-base proof for \([P:Z(P)]\) therefore still
needs a separate argument charging the non-isotropic quotient \(P/A\).

[UNVERIFIED] The relative estimate (AL.8) isolates a possible induction
target.  For \(x\in P\), put \(H=C_P(x)\) and \(r=\nu(H)\).  An absolute
bound

\[
 [P:H]\leq C^{\,m-r}
\tag{AL.9}
\]

would combine with (AL.8) and induction on \(m\) to prove the desired
fixed-base estimate for all finite class-two \(p\)-groups.  The existing
quadratic conjugacy-class estimate gives only
\([P:H]\leq4m^2\), which does not have the required dependence on the
drop \(m-r\).

[DISPROVED] The withdrawn manuscript Nagy--Pach--Tomon,
arXiv:2205.03389, cannot supply that missing argument.  Its current official
arXiv record says that an error in Claim 4.5, Section 4.2 invalidates most of
the paper, and the manuscript was withdrawn.  Consequently its advertised
\(2^{O(k)}\) irredundant-cover theorem, including the proposed numerical base
\(20\), is not load-bearing evidence.  The later published hyperplane-cover
paper is a weaker result and does not restore this implication.
