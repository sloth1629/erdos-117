# Inclusion-maximal element centralizers at binary cutoff eight

This note sharpens the finite \(2\)-group reduction in
`notes/two_group_nu8.md`.  It deliberately does **not** enlarge a
centralizer to an arbitrary maximal subgroup.  In particular, it makes no
claim that such an enlargement preserves irredundancy, private cells, or the
core of the original cover.

Throughout this note, an *inclusion-maximal element centralizer* means a
maximal member of the finite poset

\[
 \mathcal C(P)=\{C_P(y):y\in P\setminus Z(P)\}.
\tag{IMC.1}
\]

Every member of this poset is a proper subgroup.  Maximality in
\(\mathcal C(P)\) must not be confused with being a maximal subgroup of
\(P\).

## The local bound

### [PROVED] An inclusion-maximal element centralizer has a small center image

Let \(P\) be a finite \(2\)-group with \(\nu(P)=8\), and let

\[
 C=C_P(y),\qquad y\notin Z(P),
\]

be inclusion-maximal in \(\mathcal C(P)\).  Then one of the following holds:

1. \(C\) is a maximal subgroup of \(P\), and
   \([P:Z(P)]\leq64\);
2. \(C\) is not a maximal subgroup of \(P\), and
   \([C:Z(P)]\leq32\).

**Proof.**  Put \(r=\nu(C)\).  Lemma CB.2 of
`notes/candidate_bound.md` applies to every noncentral element, not merely
to a member of a chosen maximum clique.  It therefore gives

\[
 r=\nu(C_P(y))\leq \nu(P)-2=6.
\tag{IMC.2}
\]

There is no group of noncommuting clique number two: two noncommuting
elements \(u,v\) would make \(u,v,uv\) a three-clique.  Thus

\[
 r\in\{1,3,4,5,6\}.
\tag{IMC.3}
\]

If \(C\) is a maximal subgroup, set \(K=P\).  Otherwise the normalizer
condition for finite \(p\)-groups gives \(N_P(C)>C\).  Choose a subgroup
\(K/C\) of order two in \(N_P(C)/C\).  Then

\[
 C\mathrel{\triangleleft}K,\qquad [K:C]=2,
 \qquad K<P.
\tag{IMC.4}
\]

The last strict inclusion follows because \(K=P\) would make \(C\) a
maximal subgroup.  In both cases \(C=C_K(y)\) and \([K:C]=2\).

We next identify the center of this intermediate group.  Certainly
\(Z(P)\leq Z(K)\).  If \(z\in Z(K)\setminus Z(P)\), then \(z\) is
noncentral in \(P\) and

\[
 C<K\leq C_P(z)<P.
\]

This contradicts the inclusion-maximality of \(C\) in \(\mathcal C(P)\).
Consequently

\[
 Z(K)=Z(P).
\tag{IMC.5}
\]

Now repeat inside \(K\) the center-layer twist proof underlying Theorem
(T2N.1) of `notes/two_group_nu8_next.md`, for the pair
\(C=C_K(y)<K\).  The construction applies because \(C\) is an index-two
centralizer in \(K\), and (IMC.5) identifies the fixed center layer with
\(Z(P)\).  Its precise conclusion is

\[
 q:=[Z(C):Z(K)]\geq2,
 \qquad r+q\leq\nu(K)\leq8.
\tag{IMC.6}
\]

For clarity, the twist argument is not being used as a black box with the
wrong ambient group.  If \(g\in K\setminus C\), conjugation by \(g\) on
\(A=Z(C)\) has fixed subgroup \(Z(K)\).  The map
\(a\mapsto[a,g]\) therefore has image of order \(q\), and a transversal
for its kernel gives a \(q\)-clique in \(gA\).  Twisting a maximum
\(r\)-clique of \(C\) by suitable elements of \(A\) joins it to that
\(q\)-clique.  This proves (IMC.6).  Moreover \(q>1\), because
\(y\in Z(C)\setminus Z(K)\), as \(C_K(y)=C<K\).

The exact center-quotient bounds through cutoff six, together with the fact
that all displayed indices are powers of two, now give the following table.

| \(r\) | bound for \([C:Z(C)]\) | bound for \(q\) | bound for \([C:Z(P)]\) | bound for \([K:Z(P)]\) |
|:---:|---:|---:|---:|---:|
| \(1\) | \(1\)  | \(4\) | \(4\)  | \(8\)  |
| \(3\) | \(4\)  | \(4\) | \(16\) | \(32\) |
| \(4\) | \(8\)  | \(4\) | \(32\) | \(64\) |
| \(5\) | \(16\) | \(2\) | \(32\) | \(64\) |
| \(6\) | \(16\) | \(2\) | \(32\) | \(64\) |

For \(r=1\), the group \(C\) is abelian.  For \(r=3,4,5\), the exact
bounds \(4,9,16\) round to \(4,8,16\).  For \(r=6\), the
computer-assisted exact binary cutoff-six theorem (T2N.7) gives
\([C:Z(C)]\leq16\).  Equation (IMC.6) gives the third column, and

\[
 [C:Z(P)]=[C:Z(C)]q,
 \qquad [K:Z(P)]=2[C:Z(P)]
\]

gives the last two.  If \(K=P\), the last column proves alternative 1.
If \(K<P\), the penultimate column proves alternative 2. \(\square\)

## The global consequence

### [PROVED] Every finite binary cutoff-eight center quotient has order at most \(128\)

If \(P\) is a finite \(2\)-group with \(\nu(P)=8\), then

\[
 [P:Z(P)]\leq128.
\tag{IMC.7}
\]

**Proof.**  Choose a maximum noncommuting set
\(x_1,\ldots,x_8\), and put \(H_i=C_P(x_i)\).  Maximality of the set
implies

\[
 P=H_1\cup\cdots\cup H_8.
\tag{IMC.8}
\]

For each \(i\), ascend from \(H_i\) in the finite poset
\(\mathcal C(P)\) and choose an inclusion-maximal element centralizer
\(C_i\) containing it.  Then the eight \(C_i\) still cover \(P\).  They
need not be distinct or irredundant, and no assertion about their common
core is used.

If some \(C_i\) is a maximal subgroup of \(P\), the local theorem gives
\([P:Z(P)]\leq64\).  Otherwise every \(C_i\) satisfies

\[
 |C_i/Z(P)|\leq32.
\]

The eight images cover \(Q=P/Z(P)\), so counting the identity only once
gives

\[
 |Q|
 \leq 1+\sum_{i=1}^8\bigl(|C_i/Z(P)|-1\bigr)
 \leq 1+8(32-1)=249.
\tag{IMC.9}
\]

Since \(|Q|\) is a power of two, (IMC.9) implies \(|Q|\leq128\), proving
(IMC.7). \(\square\)

### [PROVED] Certified boundary consequence

The complete exact-center certificate in `notes/h8_bounded_cutoff.md`
contains no binary quotient of order at most \(64\) whose extension graph
has clique number eight.  Therefore every hypothetical finite \(2\)-group
with \(\nu(P)=8\) must in fact satisfy

\[
 [P:Z(P)]=128.
\tag{IMC.10}
\]

This last sharpening is computer-assisted and is logically separate from
the union count: (IMC.7) uses the exact binary cutoff-six certificate but
does not use the cutoff-eight certificate.  The cutoff-eight certificate is
used only to exclude the powers of two at most \(64\).

## Computational dependencies and audit status

The load-bearing finite computation in (IMC.7) is precisely the order-\(32\)
binary cutoff-six certificate used in Theorem (T2N.7) of
`notes/two_group_nu8_next.md`.  Its two focused checks are

```bash
python3 -m unittest \
  src.verification.test_exact_computation.ScalarSymplecticLogTests.test_h6_exterior_square_scan_certificates \
  src.verification.test_exact_computation.ScalarSymplecticLogTests.test_h6_c2_5_alternating_form_certificate \
  -v
```

The additional boundary statement (IMC.10) depends on the saved
order-at-most-\(81\) cutoff-eight certificate checked by

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-test-pycache \
python3 -m unittest \
  src.verification.test_h8_bounded_cutoff.H8BoundedCertificateTests.test_h8_bounded_cutoff_saved_certificate \
  -v
```

[PROVED] An independent line-by-line reconstruction checked the scope of
CB.2, the normalizer and intermediate group, both inclusions in
\(Z(K)=Z(P)\), the twist construction in ambient group \(K\), every row of
the table, the union count, and the universal boundary-certificate
quantifier.  The focused cutoff-six tests and the saved cutoff-eight
certificate test were also rerun successfully.  The audit was performed on
the frozen pre-clarification payload; the only subsequent change is the
wording clarification above that the proof of (T2N.1), rather than its
more narrowly stated theorem, is repeated inside \(K\).
