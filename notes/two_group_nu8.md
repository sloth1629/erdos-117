# The finite \(2\)-group branch at cutoff eight

This note records two finite-only reductions that were intermediate steps in
the \(2\)-group branch.  By themselves they neither classify the branch nor
determine \(h(8)\); the later closure is in
`notes/two_group_q128_symplectic_attack.md`.

## A core bound for an eight-subgroup cover

### [PROVED] Core-free irredundant eight-covers of finite \(2\)-groups

Let \(Q\) be a finite \(2\)-group with an irredundant cover

\[
  Q=A_1\cup\cdots\cup A_8,
  \qquad \bigcap_{i=1}^8 A_i=1.
\]

Then

\[
  |Q|\le 2^{11}=2048.
  \tag{T2.1}
\]

**Proof.**  The factorial intersection lemma proved in
`notes/known_bounds.md`, applied with eight cover members and trivial total
intersection, says that an intersection of \(t\) chosen cover members has
order at most \((8-t)!\).  Since every such order is a power of two, the
rounded bounds for \(t=1,\ldots,8\) are

\[
  4096,\ 512,\ 64,\ 16,\ 4,\ 2,\ 1,\ 1.
  \tag{T2.2}
\]

We shall also use repeatedly the elementary lower bound

\[
 \left|\bigcap_{j=1}^t B_j\right|
 \ge { |Q|\over \prod_{j=1}^t[Q:B_j]}
 \tag{T2.3}
\]

for subgroups \(B_j\le Q\).  It follows inductively from
\([H:H\cap K]\le[Q:K]\).

Put \(N=|Q|\), and order the cover so that \(|A_1|\) is largest.  Counting
the identity only once gives

\[
  N\le \sum_i|A_i|-7<8|A_1|,
\]

so \([Q:A_1]\in\{2,4\}\).  At least one more cover member has index at
most four.  Indeed, suppose that all \(A_i\), \(i>1\), have index at least
eight.  Irredundancy implies \(A_i\nleq A_1\) for \(i>1\), since otherwise
\(A_i\) itself would be redundant.  If \([Q:A_1]=2\), each \(A_i\)
therefore contributes exactly \(|A_i|/2\), and in particular at most
\(|A_i|/2\le N/16\) points outside \(A_1\), and seven such contributions do
not cover the complement of size \(N/2\).  If \([Q:A_1]=4\), each contributes
at most \(3|A_i|/4\le3N/32\) points outside \(A_1\), so the whole union has
size at most

\[
  {N\over4}+7{3N\over32}={29N\over32}<N.
\]

Choose two cover members \(A,B\) of index at most four.  Equations (T2.2)
and (T2.3) give

\[
  {N\over16}\le |A\cap B|\le512,
\]

and hence \(N\le8192\).

Suppose first that \(N=8192\).  Neither \(A\) nor \(B\) can have index two,
since then (T2.3) would give \(|A\cap B|\ge1024\).  Thus both have index
four and \(|A\cap B|=512\).  Every other cover member has index at least
eight: a third member of index at most four would have triple intersection
of order at least \(8192/4^3=128\), contrary to (T2.2).  If \(K\) is one of
the other six members, inclusion--exclusion inside \(K\) gives

\[
\begin{aligned}
 |K\setminus(A\cup B)|
 &=|K|-|K\cap A|-|K\cap B|+|K\cap A\cap B|\\
 &\le {|K|\over2}+64\le576.
\end{aligned}
\]

But \(|Q\setminus(A\cup B)|=8192-(2048+2048-512)=4608\), while the six
remaining members contribute at most \(6\cdot576=3456\).  This excludes
\(N=8192\).

It remains to exclude \(N=4096\).  First suppose that some cover member
\(A\) has index two.  A second member \(B\) of index at most four cannot also
have index two, by the pair-intersection bound, so it has index four and
\(|A\cap B|=512\).  Every other member has index at least eight, since a
third index-at-most-four member would have triple intersection of order at
least \(4096/(2\cdot4\cdot4)=128>64\).  For any remaining \(K\),

\[
 |K\setminus(A\cup B)|
 \le {|K|\over4}+64\le192.
\]

The complement of \(A\cup B\) has size
\(4096-(2048+1024-512)=1536\), greater than \(6\cdot192\).  Hence no cover
member has index two.

Let \(t\) be the number of index-four cover members; then \(t\ge2\).  Fix
two of them, \(A,B\).  Since \(|A\cap B|\ge256\), the complement of their
union has size at least \(2304\).  Each further index-four member contributes
at most \(576\) points to this complement, and each member of index at least
eight contributes at most \(320\).  Thus

\[
 |Q\setminus(A\cup B)|
 \le (t-2)576+(8-t)320.
\]

For \(t=2,3\) the right side is smaller than \(2304\), so \(t\ge4\).

For any index-four members in this last case, (T2.2)--(T2.3) now force every
triple intersection to have order \(64\), every fourfold intersection to
have order \(16\), and every fivefold intersection to have order \(4\).
Every pair intersection has order \(256\): after intersecting the pair with
a third index-four member, its index can drop by at most four, while the
resulting triple has order \(64\).  In particular,
\(|Q\setminus(A\cup B)|=2304\).

For every other index-four member \(K\), put
\(S_K=K\setminus(A\cup B)\).  The exact intersection sizes just obtained
give

\[
 |S_K|=576,\qquad
 |S_K\cap S_L|=144,\qquad
 |S_K\cap S_L\cap S_M|=36
 \tag{T2.4}
\]

for distinct remaining index-four members.  If \(j=t-2\), the three-term
Bonferroni upper bound and the bound \(320\) for each of the other
\(8-t\) members give

\[
 \left|Q\setminus(A\cup B)\right|
 \le j576-{j\choose2}144+{j\choose3}36+(8-t)320.
\]

For \(t=4,5,6,7,8\), the right side is respectively

\[
  2288,\ 2292,\ 2224,\ 2120,\ 2016,
\]

always smaller than \(2304\).  This contradiction excludes \(N=4096\).
Since \(N\) is a power of two and \(N\le8192\), (T2.1) follows. \(\square\)

### [PROVED] Center-index consequence at clique cutoff eight

Let \(P\) be a finite \(2\)-group with \(\nu(P)=8\).  Then

\[
  [P:Z(P)]\le2048.
  \tag{T2.5}
\]

Indeed, for a maximum noncommuting set \(x_1,\ldots,x_8\), the subgroups
\(C_P(x_i)\) form an irredundant cover and their intersection is \(Z(P)\).
After quotienting by \(Z(P)\), the preceding theorem applies to the eight
proper subgroups \(C_P(x_i)/Z(P)\) of the finite \(2\)-group \(P/Z(P)\).

This improves, for this branch, the general factorial consequence
\([P:Z(P)]\le8!\), whose power-of-two rounding only gives \(32768\).  It is
still a reduction rather than a classification: no assertion is made that
the bound \(2048\) is attained by a centralizer cover.

## The Frattini-quotient shape of a maximalized cover

### [PROVED] Odd-circuit reduction over \(\mathbf F _2\)

Let \(V\) be a finite-dimensional \(\mathbf F _2\)-space covered by at most
eight distinct hyperplanes.  Some inclusion-minimal subcover has size

\[
  3,\quad5,\quad\text{or}\quad7,
  \tag{T2.6}
\]

and its normal vectors form a circuit: their sum is zero and every proper
subfamily is linearly independent.  Consequently their common intersection
has codimension respectively \(2,4\), or \(6\).

To prove this, write the hyperplanes as \(\ker b\), with distinct nonzero
\(b\in V^*\).  A subfamily covers \(V\) exactly when the simultaneous system

\[
  b(v)=1
\]

has no solution.  Linear-system consistency over \(\mathbf F _2\) says that
this happens exactly when the normals have an odd-cardinality zero-sum
subfamily.  Choose one with minimal support.  Its size is odd, at least three,
and at most eight, proving (T2.6).  It has no proper dependency: a proper odd
dependency contradicts minimality directly, while subtracting a proper even
dependency from the chosen odd relation produces a smaller odd dependency.
Thus it is a circuit and has rank one less than its cardinality.

### [PROVED] Consequence for maximum centralizers

Let \(P\) be a finite \(2\)-group with \(\nu(P)=8\), and enlarge each member
of its irredundant maximum-clique centralizer cover to a maximal subgroup.
After duplicates are removed, the corresponding hyperplanes of
\(P/\Phi(P)\) contain a minimal subcover of size \(3,5\), or \(7\), as in
(T2.6).  For each circuit member choose an original centralizer whose chosen
maximal enlargement is that member, choosing an equal source whenever one
exists.  At least one chosen inclusion is strict.  Otherwise those at most
seven original centralizers would already cover \(P\), contradicting
irredundancy.

In particular, the eight maximum-clique centralizers cannot all be maximal
subgroups of \(P\).  More precisely, the normals belonging to those
centralizers which are maximal contain no odd dependency.  Equivalently,
there is a coset of \(\Phi(P)\) outside all maximal centralizers in the cover;
every lift of that coset must be caught by a nonmaximal centralizer.

These statements isolate the remaining binary cases but do not turn the
maximal subgroups in the odd circuit into abelian subgroups, and therefore do
not yet bound \(a(P)\) sharply enough to settle the finite \(2\)-group branch.
