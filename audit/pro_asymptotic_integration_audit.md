# Audit of the integrated Pro asymptotic pass

Audit date: 2026-08-15.

## Scope

`[PROVED]` This integration is a curated mathematical merge, not a bulk
copy of model output.  Nonstandard labels such as `PROVED RANGE` and
`COMPUTED-CERTIFIED` were translated to the repository protocol, conditional
implications were kept conditional, and duplicate or failed prompts were not
imported.

`[UNVERIFIED]` Erdős Problem 117 remains open.  In particular the Pro pass
does not prove the prime-uniform \(p\)-group half-rate input, the universal
\(\sqrt2\)-base upper bound, existence of the asymptotic rate, or exact
values after cutoff eight.

## Input ledger

The archived inputs audited for `notes/asymptotic_reductions_integrated.md`
had the following SHA-256 values:

| input | SHA-256 |
|---|---|
| `ERDOS117_PRO17_COMPLETED_RESULT.zip` | `99e4d50143230c067ee02b841e419ab9b8d4af750e0db219f2ab463d9f846e43` |
| `ERDOS117_PRO18_LP_ROUNDING_RESULT.zip` | `9a85b77acc18b3b906e50f328ae85a74181e30d4bc7dd4bb7fb9ded6c39127af` |
| `ERDOS117_PRO_19_RESULT.zip` | `519900e7c9eeb6e27731feb33b598ac33aa03c186151130648e3732a826e524e` |
| `ERDOS117_PRO20_PROVED_RANGE_RESULT.zip` | `641ca98e52cb8c42853b84071c692c9dc02f2b375928088e9fa6292ec6b4490d` |
| `ERDOS117_NILPOTENT_TRANSFER_RESULT.zip` | `7e64d07f7d06c06fc5f24ba64775550e3bf2ea41fea567bc9e4157f2efdfe545` |
| `ERDOS117_PRO22_GLOBAL_STITCHING_RESULT.zip` | `e648aeda3b82973365fd79ecb21e138e6b252c5d37215d481d85a87a4a574ac8` |
| `ERDOS117_PRO23_COMPLETED_DELIVERABLE.zip` | `a31578e6f4a24aaff9b2e963799d7edaff73d6415b32f2461d887fe2c58b1b35` |
| higher-codomain inverse package | `65cc255fdf183145067dde097fd01755cbd99787cded2bdf8085059f2f4ea9b2` |
| coupled action--cocycle report | `bcb4f1fb544db19dfe3e26169fce49236f684755a98bfb88a589ebafb7fb8951` |
| action-depth report | `c090fe8acef9d59804b8a2f7cdd48b4cf79ad29ce62a5183fb9473a712a3fcdf` |

`[PROVED]` Every ZIP manifest and bundled dependency-free verifier present
in these packages was checked before integration.  The long proofs were
then re-read against their hypotheses.  The merge retains the following
load-bearing corrections made during that audit:

1. nilpotent transfer requires one error function uniform in the prime;
2. global stitching uses the running envelope
   \(\widehat\eta(n)=\max_{m\le n}\eta(m)\), not a pointwise error term;
3. direct products use only the clique lower bound and cover upper bound,
   never one-shot clique multiplicativity;
4. the global theorem is conditional on the nilpotent input;
5. rate regularization supplies a criterion, not the missing amplifier;
6. scalar-visible estimates do not imply the existence of a favourable
   scalar projection.

## Dynamic-centralizer certificate

The original certificate and verifier hashes were

```text
8cf00aa198d090a464076965185791cfcc0cfe3b0c7a7060ec5a94e43bb7129e  certificates(1).json
8bacb0a4ba853434a61bb2c5e0aa1d71fbe02e43e3387216ce954b4e0c09d48a  verify_certificate.py
```

The verifier was changed only to use the repository certificate path and a
Python-3.9-compatible population-count helper.  The mathematical search and
certificate checks were not changed.

`[COMPUTED]` Direct execution under the repository Python 3.9 verified:

```text
[OK] scalar_symplectic_d2: |G|=32, |Z|=2, nu=5, tau=15/7, kappa=15/14, R=45/7
[OK] mixed_order_64: |G|=64, |Z|=4, nu=6, tau=3, R=a_f=6, P=9, kappa=3/4
[OK] binary chain-ring Heisenberg family: m=1..4, nu=R=a_f=3*2^(m-1), tau=3, P=3^m
[OK] one-pair extension census: 28672 / 28672 cases contain a 10-clique, digest=51350b8afcaae75d302efbf08522c6f9b5a77a29f939d1212d07e1f8ecbc9140
[OK] all exact certificates verified with the Python standard library only
```

The independent regression entry point is
`src/verification/test_dynamic_fractional_centralizer.py`.

## Claims deliberately rejected or left open

`[DISPROVED]` The nodewise dynamic inequalities
\(\eta(H)\le0\) and \(\kappa(H)\le1\) are false.  The order-32 exact model
has \(\kappa=15/14\), while the order-64 model shows that the max-child
majorant can exceed the exact dynamic value.

`[DISPROVED]` A linear class-two local-drop inequality is false, as already
recorded in `notes/class_two_local_drop_counterexample.md`.  None of the
integrated Pro deductions uses it or the false common-centralizer
surjectivity.

`[UNVERIFIED]` The exact dynamic identity reduces its target to a sublinear
expected accumulated entropy charge.  The certificate and chain-ring family
rule out two naive local obstructions but do not prove this global bound.

`[UNVERIFIED]` The p-group residual after all integrated reductions consists
of mixed high-rank operator directions with shared output, nontrivial scalar
kernel lattice, and possibly higher-class commutator layers.  It is not
legitimate to infer the half-rate bound by summing scalar ranks independently.

## Independent reconstruction bar

`[PROVED]` The proofs in `notes/asymptotic_reductions_integrated.md` were
reconstructed from the displayed formulas rather than accepted from the
package verdicts.  The dynamic finite claims additionally have a saved
machine-readable witness and an independent verifier.  No optimizer output
is used as an upper certificate without an explicit coloring, LP dual, or
exhaustive verification step.
