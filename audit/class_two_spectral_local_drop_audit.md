# Audit record for the spectral local-drop partial theorem

## [PROVED] Verdict

The hostile reconstruction in `notes/class_two_spectral_local_drop.md`
confirms the weighted spectral-shift inequality for arbitrary-exponent finite
class-two \(p\)-groups.  The proof does not assume a group-homomorphic section
of \(P/C_P(x)\), does not infer actual commutation from projected commutation,
and permits independent \(x\)-shifts of the old centralizer clique without
destroying its edges.

In the faithful binary slice \(D\cap(P')^2=1\), the reconstruction and its
oriented refinement prove:

1. QLD holds for \(|D|\le32\);
2. when \(|D|=64\), QLD holds if \(\nu(C_P(x))\le40\);
3. any remaining \(|D|=64\) counterexample must have
   \(\delta=2\), at least 41 saturated commutator operators, and an
   opposite-eigenvalue separation of every pair of the 63 nonzero directions.

The pair-capacity calculation, threshold table, and order-32768 stress example
have a new dependency-free verifier and regression test.  The original
packet's embedded 66-subspace stress computation is deliberately left
`[UNVERIFIED]` because its recorded source hash did not match the supplied
code block.

## [UNVERIFIED] Remaining scope

The full inequality

\[
[P:C_P(x)]\le4\bigl(\nu(P)-\nu(C_P(x))+1\bigr)^2
\]

is not proved.  Higher-rank faithful binary systems, especially the exact
\(|D|=64\) residue above, and commutator layers hidden in every elementary
quotient for arbitrary-exponent groups remain open.  No Erdős 117 solution or
fixed-base class-two theorem follows yet.
