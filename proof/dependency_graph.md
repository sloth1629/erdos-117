# Proof Dependency Graph

No complete solution of Erdos Problem 117 is claimed.

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
      |
      +-- maximum-clique centralizer arguments
      |     +-- C_G(maximum clique)=Z(G)
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

      +-- Bryce--Fedri--Serena irredundant-cover theorem f(5)=16 [external]
            +-- nu(G)=5 implies [G:Z(G)] <= 16
            +-- central-extension commutators factor through Q wedge Q
                  +-- Schur-cover normal-kernel enumeration [computer]
                        +-- omega <= 5 implies chi <= 5 for |Q| <= 16
                              +-- h(5)=5

      +-- six-cover theorem f(6)=36
            |-- maximal/nonmaximal structural reduction [proved/audited]
            |-- finite maximal-cover leaves [computer + independent verifier]
            `-- nu(G)=6 implies [G:Z(G)] <= 36
                  +-- C2^5 zero-radical obstruction [proved]
                  +-- Schur-cover normal-kernel enumeration [computer]
                        +-- omega <= 6 implies chi <= 6 for |Q| <= 36
                              +-- h(6)=6

The \(h(5)\) and \(h(6)\) branches are explicitly computer-assisted.  Their
load-bearing external dependencies are the audited subgroup-cover theorems
and the standard nonabelian-exterior-square/Schur-cover construction; the
repository contains repaired structural reductions and independent finite
certificates for the six-cover leaves.  All other branches displayed above
are computation-independent. Neumann (1976) is
primary-verified historical corroboration. Pyber's fixed-base exponential
upper bound remains inaccessible at proof level and therefore lies outside
the proved dependency graph.
