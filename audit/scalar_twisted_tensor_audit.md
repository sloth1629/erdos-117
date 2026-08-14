# Independent audit of the scalar twisted-tensor barrier

## [PROVED] Audit verdict

The proof in `results/scalar_twisted_tensor/GLOBAL_RESEARCH_REPORT.md` was
reconstructed against the repository's scalar group dictionary.  The
following conclusions are valid:

\[
\pi(q,2^{t-1})\ge q^t+1
\qquad(q\text{ a prime power},\ t\ge1\text{ odd}),
\]

all nonbinary scalar symplectic models are jointly subexponential in their
clique cutoff, and the complete scalar-symplectic envelope has exact
exponential base \(\sqrt2\).  Except for \((q,m)=(2,1)\), the pointwise bound

\[
q^m+1\le2^{\pi(q,m)/2}
\]

also holds.  These results concern scalar-valued nondegenerate alternating
commutator geometries only; they are not a universal upper bound for Erdős
Problem 117.

## [PROVED] Reconstruction of the load-bearing chain

The audit checked the following steps independently.

1. On each cyclic bit-string orbit of length \(d\), the fixed vectors of the
   Frobenius-shift map are parametrized by \(\mathbb F_{q^d}\), contributing
   exactly \(d\) base-field dimensions.  The Moore-matrix root argument shows
   that these fixed vectors span the whole orbit after scalar extension.
2. For odd \(t\), the tensor product of determinant forms restricts to an
   \(\mathbb F_q\)-valued nondegenerate alternating form.  In characteristic
   two the tensor matrix is symmetric with zero diagonal, so alternation is
   checked directly rather than inferred from skew-symmetry.
3. The image of \([a:b]\in\operatorname{PG}(1,q^t)\) is well defined because
   rescaling multiplies its tensor by the field norm.  The pairing of two
   distinct images is exactly \(N(ad-bc)\ne0\), giving \(q^t+1\) pairwise
   nonorthogonal points.
4. The explicit orthogonal-gluing construction proves superadditivity of
   \(\pi(q,m)-1\).  Choosing the largest seed dimension in
   \(1,4,16,\ldots\) below \(m\) gives
   \(\pi(q,m)>1+m^{\log_2q}/q\), which is superlinear for every fixed
   \(q>2\).
5. The elementary plane bound \(\pi(q,m)\ge mq+1\) handles unbounded fields.
   Splitting an arbitrary sequence into bounded- and unbounded-field
   subsequences proves the uniform nonbinary collapse.
6. In characteristic two, the all-off-diagonal Gram matrix has rank \(k\)
   for even \(k\) and \(k-1\) for odd \(k\), while the even-weight model
   attains \(2m+1\).  Hence \(\pi(2,m)=2m+1\), and combining this exact binary
   formula with the nonbinary collapse gives scalar base \(\sqrt2\).
7. The pointwise proof's only delicate arithmetic branch is \(q=3\).  The
   \(t=3\) seed gives \(\pi(3,4)\ge28\); gluing by four dimensions increases
   the certified exponent by \(27/2\), more than the factor \(3^4=81\).
   The four residue classes and the cases \(q=2\), \(q\ge4\) check exactly as
   stated.

No classification theorem, CFSG input, or computation enters this chain.

## [COMPUTED] Certificate reconstruction

The two supplied generators reproduce their JSON certificates byte for byte.
Independent base-field verifiers check the full-rank alternating matrices,
all 28 projective points and 378 pairings in \(W(7,3)\), and all 13 points and
78 pairings in the auxiliary \(W(5,3)\) certificate.  The exact-integer
pointwise audit also passes.  These checks are regression-tested by
`src/verification/test_scalar_twisted_tensor_bundle.py`; they are sanity
certificates, not proof dependencies.

The imported ZIP had SHA-256

```text
920a8f03d55d0eb5fe608dd3e05c363c5c01e0fffe19893507d4af0e4b6fbd9f  ERDOS117_GLOBAL_PRO_RESULT.zip
```

The integrated bundle has a regenerated internal manifest because its
historical statements that \(h(8)\) remained open were normalized to the
current repository theorem \(h(8)=10\).
