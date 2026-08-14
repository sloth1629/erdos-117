# EVIDENCE LEDGER

**Bundle:** `ERDOS117_GLOBAL_PRO_RESULT`
**Date:** 2026-08-14
**Rule:** each row has exactly one evidence label. “Dependency” identifies the shortest proof chain; “Gap or falsifier” records what remains, if anything.

## A. Audited packet inputs used

| ID | Claim | Label | Scope | Dependency | Gap or falsifier |
|---|---|---|---|---|---|
| P-SS-1 | The triangular-cocycle group \(S(q,m)\) has central quotient a nondegenerate \(2m\)-dimensional symplectic space, with \(\nu(S(q,m))=\pi(q,m)\). | `[PROVED]` | Every prime power \(q\), \(m\ge1\) | Packet `notes/scalar_symplectic_family.md`; independently summarized in Proposition 4.1 | None within scope |
| P-SS-2 | \(a(S(q,m))=q^m+1\). | `[PROVED]` | Every prime power \(q\), \(m\ge1\) | Isotropic-size lower bound plus symplectic spread; packet and Proposition 4.1 | None within scope |
| P-H8-1 | The source packet isolated the all-nonmaximal finite \(2\)-group branch and the solvable nontrivial-core branch; the surrounding repository subsequently closed both and proved \(h(8)=10\). | `[PROVED]` | Exact cutoff-eight theorem in the current repository | Current `STATUS.md`, `notes/two_group_nu8_next.md`, and common-core closure notes | This scalar bundle is not a dependency of the exact cutoff-eight proof |
| P-UP-1 | The audited universal upper bound is \(h(n)\le2^{O(n\log\log n)}\), not a fixed-base bound. | `[PROVED]` | Arbitrary groups after finite reduction; CFSG-dependent | Packet `STATUS.md` and `subfactorial_upper.md` | Fixed-base universal upper remains open |
| P-DP-1 | Fixed powers of one seed group give only a polynomial relation between \(a\) and \(\nu\). | `[PROVED]` | Finite seed group | Packet `notes/graph_products.md` | Does not determine the global rate |
| LIT-T3 | The \(t=3\) tensor point set of size \(q^3+1\) under the tensor-cube alternating form appears explicitly in Pavese, arXiv:2605.22289v1, Section 3. | `[CITED-VERIFIED]` | Every prime power \(q\), rank four scalar symplectic geometry | Primary PDF, displayed definition of \(O_1\) and equation (3.1) | Cross-check only; not load-bearing |
| LIT-W5 | Ceria–De Beule–Pavese–Smaldore, arXiv:2203.04553, Theorem 3.7, proves a partial ovoid of \(W(5,q)\) of size \(q^2+q+1\). | `[CITED-VERIFIED]` | Every prime power \(q\) under the theorem's stated nonzero-parameter hypothesis | Primary PDF, Theorem 3.7 | Cross-check only; not load-bearing |

## B. New load-bearing mathematical claims

| ID | Claim | Label | Scope | Dependency | Gap or falsifier |
|---|---|---|---|---|---|
| N-DESC-1 | For the cyclic Frobenius tensor map \(\tau\) on \((\mathbb F_{q^t}^2)^{\otimes t}\), the fixed space has \(\mathbb F_q\)-dimension \(2^t\) and spans the full tensor space after scalar extension. | `[PROVED]` | Every prime power \(q\), every \(t\ge1\) | Bit-string cyclic orbits; Moore-matrix root bound | A counterexample would have to violate the explicit orbit calculation or Moore nonsingularity |
| N-FORM-1 | For odd \(t\), the tensor determinant form restricts to an \(\mathbb F_q\)-valued nondegenerate alternating form on the fixed space. | `[PROVED]` | Every prime power \(q\), odd \(t\ge1\) | N-DESC-1; tensor nondegeneracy; zero-diagonal characteristic-two audit | Even \(t\) in odd characteristic is intentionally outside scope |
| N-TT-1 | \(\pi(q,2^{t-1})\ge q^t+1\) for every prime power \(q\) and odd \(t\ge1\). | `[PROVED]` | Scalar symplectic geometry | N-DESC-1, N-FORM-1; determinant-norm pairing | Falsified by one distinct pair with zero norm pairing; formula (4.5) excludes this |
| N-GLUE-1 | \(\pi(q,r+s)\ge\pi(q,r)+\pi(q,s)-1\). | `[PROVED]` | Every prime power \(q\), \(r,s\ge1\) | Explicit set in an orthogonal direct sum | Falsified by a zero cross-pair; cross-pair is exactly \(B(c_0,c)\ne0\) |
| N-GEN-1 | \(\pi(q,m)\ge mq+1\). | `[PROVED]` | Every prime power \(q\), \(m\ge1\) | N-GLUE-1 plus \(q+1\) points in a symplectic plane | None |
| N-FIX-1 | For each fixed prime power \(q>2\), \(\log(q^m+1)/\pi(q,m)\to0\). | `[PROVED]` | Fixed nonbinary scalar field | N-TT-1, N-GLUE-1; largest block \(M\in\{1,4,16,\ldots\}\) | Would fail only if the block lower bound or exponent \(\log_2q>1\) failed |
| N-FIX-2 | Quantitatively, the ratio is \(O_q(m^{1-\log_2q})\). | `[PROVED]` | Fixed prime power \(q>2\) | N-FIX-1, inequality (4.15) | Constant depends on \(q\) |
| N-UNI-1 | Uniformly over prime powers \(q\ge3\), the ratio \(\log(q^m+1)/\pi(q,m)\) tends to zero whenever \(\pi(q,m)\to\infty\). | `[PROVED]` | All nonbinary scalar fields jointly | N-GEN-1 for unbounded \(q\); N-FIX-1 for bounded \(q\) | None within scalar class |
| N-ENV-1 | \(\log h_{\mathrm{sc},\ne2}(n)=o(n)\), so \(h_{\mathrm{sc},\ne2}(n)^{1/n}\to1\). | `[PROVED]` | Envelope over all prime powers \(q\ge3\) | N-UNI-1; finiteness from N-GEN-1 | None within scalar class |
| N-BIN-1 | \(\pi(2,m)=2m+1\). | `[PROVED]` | Binary scalar fields | Gram-rank upper bound plus explicit even-weight-space construction | None |
| N-RATE-1 | \(h_{\mathrm{sc}}(n)^{1/n}\to\sqrt2\). | `[PROVED]` | Entire scalar-symplectic class | N-ENV-1, N-BIN-1, P-SS-2 | Does not extend to higher-codomain or arbitrary groups |
| N-POINT-1 | Except at \((q,m)=(2,1)\), \(q^m+1\le2^{\pi(q,m)/2}\). | `[PROVED]` | Every scalar model | N-BIN-1; N-TT-1 at \(q=3,t=3\); N-GEN-1 for \(q\ge4\) | Exact exception explicitly listed |
| N-POINT-2 | Equality in N-POINT-1 occurs at \((q,m)=(3,1)\), and all other nonexceptional proof cases are strict. | `[PROVED]` | Every scalar model | Case audit in Theorem 4.13 | None |
| N-HSC-1 | \(h_{\mathrm{sc}}(n)\le2^{n/2}\) for every \(n\ge4\). | `[PROVED]` | Scalar envelope | N-POINT-1; exceptional model has \(a=3\) | The inequality is false at \(n=3\) because \(3>2^{3/2}\) |
| N-EXCL-1 | Any sequence \(S(q_i,m_i)\) with \(\nu\to\infty\) and efficiency above \(\log2/2\) is impossible. | `[PROVED]` | Scalar-symplectic group sequences | N-RATE-1 and N-UNI-1 | Higher-codomain and non-class-two sequences remain possible |
| N-GRAPH-1 | The scalar conclusions extend to any finite group with the same exact central-coset commutation graph as an \(S(q,m)\) model. | `[PROVED]` | Commutation-equivalent/isoclinic scalar models | \(\nu\) and \(a\) are clique and chromatic invariants of the compressed graph | Does not cover higher-codomain commutator graphs |

## C. Screening results

| ID | Claim | Label | Scope | Dependency | Gap or falsifier |
|---|---|---|---|---|---|
| S-POT-1 | No fixed constant \(C\) can satisfy the proposed one-step potential \(\sum_{x\in S}C^{-(\nu(G)-\nu(C_G(x)))}\le1\) for every maximum clique. | `[DISPROVED]` | All groups; counterfamily binary scalar | N-BIN-1 and the exact drop-two centralizer geometry | Explicit counterfamily for every fixed \(C\) |
| S-EXT-1 | The size of a maximal isotropic subspace alone cannot bound ambient dimension in higher-codomain alternating maps. | `[DISPROVED]` | Alternating maps \(V\times V\to\Lambda^2V\) | \(v\wedge w=0\) iff \(v,w\) are dependent | Does not disprove bounds using \(\nu\) or other invariants |
| S-DP-1 | Fixed powers of one seed cannot produce an exponential-in-\(\nu\) lower construction. | `[DISPROVED]` | Fixed finite seed | P-DP-1 | Varying geometry remains possible |
| S-FROB-1 | Frobenius groups with abelian complement and growing abelian kernel have \(\log a/\nu\to0\). | `[DISPROVED]` | Fixed-point-free affine/Frobenius family | Explicit \(\lvert V\rvert+1\)-clique and \(\lvert V\rvert+1\)-cover | Nonabelian complements or non-Frobenius semidirect products not covered |
| S-TT3-1 | The exported \(W(7,3)\) twisted-tensor certificate has 28 distinct projective points, a full-rank alternating form, and 378 nonzero mutual pairings. | `[COMPUTED]` | The \(q=3,t=3\) instance of N-TT-1 | Extension-field generator plus independent base-field verifier | Non-load-bearing; rerun scripts to falsify |
| S-Q3-1 | The exported \(W(5,3)\) norm-one certificate has 13 distinct projective points, a full-rank alternating form, and 78 nonzero mutual pairings. | `[COMPUTED]` | One auxiliary finite geometry over \(\mathbb F_3\) | JSON certificate plus independent standard-library verifier | Non-load-bearing; rerun scripts to falsify |
| S-ARITH-1 | The exact integer boundary audit passes for the stated finite ranges and confirms the unique exception and equality cases used in Theorem 4.13. | `[COMPUTED]` | Finite arithmetic audit only | `scripts/verify_scalar_pointwise_audit.py` and saved transcript | Not a proof of the infinite theorem |
| S-SRC-1 | Every checksum listed in the source packet's `SHA256SUMS.txt` passed before the research run. | `[COMPUTED]` | Supplied context packet | `certificates/SOURCE_PACKET_SHA256_AUDIT.txt` | Detects packet corruption only; not a mathematical proof |

## D. Open candidate lemmas retained

| ID | Claim | Label | Scope | Dependency | Gap or falsifier |
|---|---|---|---|---|---|
| O-ABL-1 | There is an absolute \(C\) such that each finite class-two \(p\)-group \(P\), with \(m=\nu(P)\), has a maximal abelian \(A\ge Z(P)\) with \([P:A]\le C^m\). | `[CONJECTURE]` | Finite class-two \(p\)-groups | Would complement packet abelian-layer theorem | Find a family with \(\log[P:A]/\nu(P)\to\infty\), or prove the bound |
| O-HCOD-1 | A higher-codomain alternating-map family can beat efficiency \(\log2/2\). | `[CONJECTURE]` | Finite class-two groups | Requires exact clique and isotropic-cover analysis | Produce one certified family or prove a universal contrary inequality |
| O-AMAL-1 | A central amalgamation operation exists with nearly additive \(\nu\) and nearly multiplicative \(a\). | `[CONJECTURE]` | Selected group or alternating-map class | Must prevent commutator cancellation | One explicit cancellation-resistant operation with invariant proofs decides viability |
| O-H8-2 | The historical odd-circuit-rigidity route by itself closes the all-nonmaximal finite \(2\)-group branch at \(\nu=8\). | `[UNVERIFIED]` | Superseded attack route only | Packet's odd-circuit reduction | The branch was later closed by a different exact argument |
| O-H8-S | The historical fixed-subgroup/core inequality by itself closes the solvable nontrivial-core branch at \(\nu=8\). | `[UNVERIFIED]` | Superseded attack route only | Packet's quotient skeleton | The branch was later closed by a different common-core argument |
| O-BFC-1 | Centralizer-origin irredundant coset covers satisfy a fixed-base intersection-index theorem. | `[CONJECTURE]` | Abelian sections arising in BFC reduction | Must strengthen the valid \(\exp(O(k\log\log k))\) theorem | Prove a structural property absent from arbitrary covers |

## E. Final status claims

| ID | Claim | Label | Scope | Dependency | Gap or falsifier |
|---|---|---|---|---|---|
| F-117 | Erdős Problem 117 is resolved by this bundle. | `[UNVERIFIED]` | Arbitrary groups | No universal matching upper bound or better/lower exclusion beyond scalar class | Full resolution requires matching construction and universal bound |
| F-H8 | The current repository determines \(h(8)=10\), independently of this scalar bundle. | `[PROVED]` | Exact cutoff eight | Current exact cutoff-eight proof and audits | This bundle alone proves no exact cutoff-eight theorem |
| F-SCALAR | The asymptotic optimization problem for the scalar-symplectic class is determined. | `[PROVED]` | All \(S(q,m)\) | N-RATE-1 and N-ENV-1 | None within the stated class |
