# A maximal-centralizer reduction in the finite binary branch

This note continues `notes/two_group_nu8.md`.  It treats the case in which
one member of a maximum-clique centralizer cover is a maximal subgroup.  It
does not assert that such a member always exists.

## A center layer charged to the centralizer drop

### [PROVED] The maximal-centralizer center-layer inequality

Let \(P\) be a finite \(2\)-group with \(\nu(P)=8\), let \(x\in P\setminus
Z(P)\), and suppose that

\[
  H=C_P(x)
\]

is maximal in \(P\).  Put \(r=\nu(H)\).  Then

\[
 [Z(H):Z(P)]\le 8-r.
 \tag{T2N.1}
\]

**Proof.**  The subgroup \(H\) is normal of index two.  Put \(A=Z(H)\),
choose \(g\in P\setminus H\), and let conjugation by \(g\) act on \(A\).
Since \(g^2\in H\) and \(A\le Z(H)\), this action is an involution.  Its
fixed subgroup is exactly

\[
 C_A(g)=Z(P).
 \tag{T2N.2}
\]

Indeed, an element of \(A\) fixed by \(g\) commutes with both \(H\) and
\(g\), which generate \(P\); the reverse inclusion is immediate.

With the convention \([u,v]=u^{-1}v^{-1}uv\), define

\[
 \delta:A\longrightarrow A,
 \qquad \delta(a)=[a,g]=a^{-1}a^g.
\]

This is a homomorphism because \(A\) is abelian, and (T2N.2) says that its
kernel is \(Z(P)\).  Thus

\[
 q:=|\operatorname{im}\delta|=[A:Z(P)].
 \tag{T2N.3}
\]

Moreover \(q\ge2\): the element \(x\in Z(H)\) is not fixed by \(g\), since
\(C_P(x)=H\).

Let \(T\) be a transversal for \(Z(P)=\ker\delta\) in \(A\).  The set

\[
 \{gt:t\in T\}
 \tag{T2N.4}
\]

is a \(q\)-clique.  For \(t,u\in A\), direct multiplication gives

\[
 (gt)(gu)=g^2t^gu,
 \qquad
 (gu)(gt)=g^2u^gt,
\]

so \(gt\) and \(gu\) commute exactly when
\(\delta(t)=\delta(u)\).  Distinct transversal representatives have
distinct images.

Now take a maximum \(r\)-clique \(s_1,\ldots,s_r\) in \(H\).  For each
\(j\), choose \(a_j\in A\) such that

\[
 [s_ja_j,g]=[s_j,g]\delta(a_j)\ne1.
 \tag{T2N.5}
\]

Such a choice exists: as \(\delta(a)\) ranges over a set of \(q\ge2\)
values, at most one value can cancel \([s_j,g]\).  Multiplying the old
vertices by elements of \(Z(H)\) preserves all old noncommuting pairs.
Also every \(s_ja_j\) commutes with every \(t\in T\), and
\([s_ja_j,g]\in H\) is centralized by \(t\in Z(H)\).  Equivalently, direct
cancellation shows

\[
 s_ja_j\text{ commutes with }gt
 \quad\Longleftrightarrow\quad
 s_ja_j\text{ commutes with }g.
\]

Consequently

\[
 \{s_1a_1,\ldots,s_ra_r\}\ \cup\ \{gt:t\in T\}
\]

is a clique of size \(r+q\) in \(P\).  Since \(\nu(P)=8\), one has
\(r+q\le8\).  Equation (T2N.3) now proves (T2N.1). \(\square\)

## Consequences for the exact center quotient

### [PROVED] A maximal clique-centralizer forces center index at most \(128\)

Let \(P\) be as above, and suppose that \(H=C_P(x)\) is maximal for some
member \(x\) of a maximum noncommuting set.  Then

\[
 [P:Z(P)]\le128.
 \tag{T2N.6}
\]

More precisely, the possible bounds by \(r=\nu(H)\) are

| \(r\) | bound for \([H:Z(H)]\) | bound for \([Z(H):Z(P)]\) | bound for \([P:Z(P)]\) |
|:---:|---:|---:|---:|
| \(1\) | \(1\) | \(4\) | \(8\) |
| \(3\) | \(4\) | \(4\) | \(32\) |
| \(4\) | \(8\) | \(4\) | \(64\) |
| \(5\) | \(16\) | \(2\) | \(64\) |
| \(6\) | \(32\) | \(2\) | \(128\) |

To justify the table, the preliminary centralizer-drop theorem gives
\(r\le6\).  A group with clique number below three is abelian, so
\(r\in\{1,3,4,5,6\}\).  For \(r=1\), \(H\) is abelian.  For
\(r=3,4,5,6\), the repository's exact three-, four-, five-, and six-cover
bounds give respectively

\[
 [H:Z(H)]\le4,9,16,36.
\]

Because \(H/Z(H)\) is a \(2\)-group, these round down to the powers of two
\(4,8,16,32\) displayed in the table.  Theorem (T2N.1), together with the
fact that \(Z(H)/Z(P)\) is a nontrivial \(2\)-group, gives the second numeric
column.  Finally,

\[
 [P:Z(P)]
 =2[H:Z(H)][Z(H):Z(P)],
\]

which proves the last column and (T2N.6).

### [PROVED] The exact binary cutoff-six scan removes the boundary

If \(K\) is a finite \(2\)-group with \(\nu(K)\le6\), then

\[
 [K:Z(K)]\le16.
 \tag{T2N.7}
\]

Here is the exact scope of the computational input.  If \(\nu(K)\le5\),
the exact lower-cutoff cover bounds already give \([K:Z(K)]\le16\).
It remains to take \(\nu(K)=6\).  The six-cover theorem then gives
\([K:Z(K)]\le36\), so the only power of two above \(16\) that could occur
is \(32\).  The complete certificate
`experiments/logs/h6_exterior.json` contains all 51 abstract groups of order
\(32\).  For the 50 types other than the elementary abelian type, every
action-invariant exterior-square kernel is recorded: each record is either
nonfaithful, or has a verified clique of size at least seven.  There is no
eligible order-\(32\) candidate.  The remaining type \(C_2^5\) is excluded
without enumerating its exterior-square kernels by Corollary H6.2 in
`notes/exact_h6.md`, which proves that every exact-center commutator map on
that quotient has a nine-clique.  The saved verifier checks the completeness
of the 51-type partition, all kernel serial ranges, radical witnesses, and
clique witnesses.  This proves (T2N.7) by a computer-assisted exhaustive
argument.  The two relevant certificate checks are reproducible with

```bash
python3 -m unittest \
  src.verification.test_exact_computation.ScalarSymplecticLogTests.test_h6_exterior_square_scan_certificates \
  src.verification.test_exact_computation.ScalarSymplecticLogTests.test_h6_c2_5_alternating_form_certificate \
  -v
```

### [PROVED] Closure of the maximal-centralizer branch

Under the hypotheses of (T2N.6), one always has

\[
 [P:Z(P)]\le64
 \qquad\text{and}\qquad
 a(P)\le10.
 \tag{T2N.8}
\]

The implication uses the complete central-extension certificate in
`notes/h8_bounded_cutoff.md`: it checks every exact center quotient of order
at most \(81\) at clique cutoff eight, and the maximum abelian-cover number
in that inventory is ten.

For completeness, the group-theoretic reduction to order at most \(64\)
uses (T2N.7) only in the last row of the preliminary table.  If \(r\le5\),
that table already gives the desired bound.  If \(r=6\), then (T2N.7)
improves \([H:Z(H)]\le32\) to \(16\), while (T2N.1) gives
\([Z(H):Z(P)]=2\).  Hence

\[
 [P:Z(P)]
 =2[H:Z(H)][Z(H):Z(P)]
 \le2\cdot16\cdot2=64.
\]

Consequently, if a finite \(2\)-group \(P\) with \(\nu(P)=8\) satisfies
\(a(P)>10\), then no centralizer belonging to any maximum eight-clique is a
maximal subgroup of \(P\).  This leaves a single structural residual branch;
it does not prove that the branch is empty.

### [PROVED] Every residual maximalization has nontrivial intersection

Fix any maximum eight-clique, enlarge its centralizer images in
\(Q=P/Z(P)\) to arbitrary maximal overgroups, and retain any
inclusion-minimal subcover \(M_1,\ldots,M_k\).  The hyperplane argument in
notes/two_group_nu8.md gives \(k\in\{3,5,7\}\).  Because every maximal
subgroup of a finite \(2\)-group is normal,

\[
 D=\bigcap_{i=1}^k M_i
\]

is already the common core.  The normal vectors of the \(k\) hyperplanes
form a minimal odd circuit, so

\[
 Q/D\cong C_2^{\,k-1}.
\]

If \(D=1\), then \(|Q|\le2^6=64\), and the same exact cutoff-eight
certificate used in (T2N.8) gives \(a(P)\le10\).  Therefore every
hypothetical \(a(P)>10\) case has \(D\ne1\) for every maximum clique and
every choice of maximal overgroups.  The binary residual is thus a
nontrivial-common-core problem, parallel to the solvable nonnilpotent
residual.
