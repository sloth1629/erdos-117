# Proof Dependency Graph

No complete solution of Erdos Problem 117 is claimed; the exact range proved
here is now \(1\le n\le7\).

    elementary group and graph definitions
      +-- graph/group dictionary: omega(Gamma_G)=nu(G), chi(Gamma_G)=a(G)
      |     +-- exact central-coset compression Delta_G
      |     |     +-- isoclinism invariance
      |     |     +-- finite commutation-model theorem
      |     |     |     +-- finite-group supremum and attainment of h(n)
      |     |     |     +-- transfer of finite conjugacy-class bounds
      |     |     +-- exact finite computation
      |     +-- chromatic-versus-clique formulation of h(n)
      |
      +-- finite Ramsey theorem
      |     +-- uniform centralizer-index bound
      |     +-- finite-index center for arbitrary G
      |     +-- self-contained 4^(n^2) center-index bound
      |     +-- 4 nu(G)^2 BFC bound
      |           +-- Guralnick--Maroti derived-subgroup bound [CITED-VERIFIED] (CFSG)
      |           +-- C=C_G(G'), with C/Z(C) abelian
      |                 +-- Nagy--Pach--Tomon abelian coset-cover bound [CITED-VERIFIED]
      |                 +-- elementary automorphism and commutator indices
      |                       +-- [G:Z(G)] and h(n) <= 2^O(n log log n)
      |
      +-- maximum-clique centralizer arguments
      |     +-- C_G(maximum clique)=Z(G)
      |     +-- factorial coset-cover lemma
      |     |     +-- [G:Z(G)] <= nu(G)!
      |     |     +-- nu(G) <= 8 implies |G/Z(G)| <= 40,320
      |     +-- nu(C_G(x)) <= nu(G)-2 for x noncentral
      |     |     +-- h(n) <= n h(n-2)
      |     |     +-- h(1)=h(2)=1, h(3)=3, h(4)=4
      |     +-- finite conjugacy classes have size at most 4 nu(G)^2
      |           +-- [G:Z(G)] <= (4 n^2)^n
      |
      +-- direct-product commutator identity
      |     +-- noncommuting graph is the OR product
      |     +-- direct-power chromatic rate is fractional chromatic number
      |     +-- direct-power clique rate is complementary Shannon capacity
      |
      +-- scalar symplectic groups S(q,m)
            +-- a(S(q,m)) = q^m+1 via a symplectic spread
            +-- nu(S(q,m)) = maximum partial-ovoid size pi(q,m)
            |     +-- pi(2,m)=2m+1
            |     |     +-- liminf h(n)^(1/n) >= sqrt(2)
            |     +-- pi(3,2)=7
            |           +-- (nu,a)(S(3,2))=(7,10)
            |                 +-- binary exact candidate is false
            +-- pi(q,m) >= mq+1

      +-- Bryce--Fedri--Serena irredundant-cover theorem f(5)=16 [CITED-VERIFIED]
            +-- nu(G)=5 implies [G:Z(G)] <= 16
            +-- central-extension commutators factor through Q wedge Q
                  +-- Schur-cover normal-kernel enumeration [COMPUTED]
                        +-- omega <= 5 implies chi <= 5 for |Q| <= 16
                              +-- h(5)=5

      +-- six-cover theorem f(6)=36
            |-- maximal/nonmaximal structural reduction [PROVED]
            |-- finite maximal-cover leaves [COMPUTED]
            `-- nu(G)=6 implies [G:Z(G)] <= 36
                  +-- C2^5 zero-radical obstruction [PROVED]
                  +-- Schur-cover normal-kernel enumeration [COMPUTED]
                        +-- omega <= 6 implies chi <= 6 for |Q| <= 36
                              +-- h(6)=6

      +-- Abdollahi--Jafarian Amiri seven-cover theorem f(7)=81 [CITED-VERIFIED]
            +-- self-contained finite center-index bound for arbitrary G
            +-- maximum-clique centralizers descend to a finite irredundant
            |   seven-cover with trivial intersection
            +-- nu(G)=7 implies |G:Z(G)| <= 81
                  +-- complete 738-type SmallGroups inventory [COMPUTED]
                  |     +-- 660 ordinary types / 55,970 normal kernels
                  |     +-- C2^5 nine-clique obstruction [PROVED]
                  |     +-- C3^4 exact GL(4,3)-orbit certificate [COMPUTED]
                  |     +-- 62 explicit nonidentity zero exterior rows
                  |     +-- 11 complete character-annihilator BFS scans
                  |     +-- C4^2 x C2^2 subgroup certificate [COMPUTED]
                  |     +-- C2^3 x D8 affine-dual certificate [COMPUTED]
                  |     +-- C2^6 alternating-pencil classification
                  |           +-- every cutoff-seven graph is 9-colorable
                  +-- S(3,2) has (nu,a)=(7,10) [PROVED]
                        +-- h(7)=10

      +-- [PROVED] finite 5-group branch at cutoff eight
            +-- [CITED-VERIFIED] Berkovich finite p-group cover and
            |   structure theorems
            +-- [PROVED] at most eight F5-hyperplanes imply a six-pencil
            |     +-- [PROVED] torus count excludes normal-span dimension
            |     |   at least five
            |     +-- [COMPUTED] dimensions two through four
            +-- [PROVED] an eight-centralizer cover would cover a pencil member by
            |   at most four proper subgroups, an impossibility
            +-- [PROVED] nu(P) <= 8 implies
                (nu(P),a(P))=(1,1) or (6,6)

      +-- [PROVED] finite 3-group branch at cutoff eight
            +-- [CITED-VERIFIED] Berkovich lower bound, equality structure,
            |   and exclusion of clique number five
            +-- [PROVED] maximal-centralizer amplification
            |     +-- a nonabelian maximal centralizer has clique number four
            +-- [PROVED] a nonabelian outer intersection forces
            |     J=[Z(H),y] of order three
            |     +-- J != H' gives a twelve-clique
            |     +-- J = H' gives a scalar symplectic central quotient
            |           +-- pi(3,2)=7 and pi(3,m)>=3m+1 for m>=3
            |                 +-- contradiction to nu(P)=8
            +-- [PROVED] all outer intersections are abelian
            |     +-- private-cell subgroup plus seven centralizers
            |           +-- nu(P)=8 implies a(P)=8
            +-- [PROVED] max a(P) for finite 3-groups with nu(P)<=8 is 10

      +-- [PROVED] finite 2-group reduction at cutoff eight
            +-- [PROVED] factorial t-fold intersection bounds rounded to
            |   powers of two
            |     +-- two cover members have index at most four
            |     +-- order 8192 excluded by complement counting
            |     +-- order 4096 excluded by exact intersections and
            |           three-term Bonferroni bounds
            |           +-- [P:Z(P)] <= 2048 when nu(P)=8
            +-- [PROVED] maximalized Frattini hyperplanes contain a minimal
                  odd circuit of size 3, 5, or 7
                  +-- the eight clique-centralizers cannot all be maximal

The \(h(5)\), \(h(6)\), and \(h(7)\) branches are explicitly
computer-assisted.  Their
load-bearing external dependencies are the audited subgroup-cover theorems
and the standard nonabelian-exterior-square/Schur-cover construction; the
repository contains repaired structural reductions and independent finite
certificates for the six-cover leaves.  At seven, the external dependency is
Theorem B (p. 292, proof pp. 299--300) of Abdollahi--Jafarian Amiri; the
repository independently certifies every post-reduction finite case. All
other branches displayed above are computation-independent except for the
explicitly marked small-dimensional hyperplane-cover check in the finite
\(5\)-group cutoff-eight branch.  The finite \(3\)- and \(5\)-group
branches are closed and the finite \(2\)-group branch is reduced, but these
results do not determine \(h(8)\).
Neumann (1976) is primary-verified historical corroboration. The displayed
subfactorial
branch uses the proof-audited Guralnick--Maróti and Nagy--Pach--Tomon
theorems and retains the former's CFSG dependence.  Pyber's stronger
fixed-base exponential upper bound remains inaccessible at proof level and
therefore lies outside the proved dependency graph.
