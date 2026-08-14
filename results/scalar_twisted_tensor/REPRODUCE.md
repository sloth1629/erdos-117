# REPRODUCTION AND AUDIT

## Environment used `[COMPUTED]`

- Date: 2026-08-14
- Python: 3.13.5
- Platform: Linux x86_64
- External Python packages: none

## Source packet hashes `[COMPUTED]`

```text
dc7737d7f052d44ed0b8f9024d6a0502a05339afd6fd99927a01171447ba25bd  ERDOS117_GLOBAL_GPT56_SOL_PRO_HANDOFF.zip
1ba4754b42732a266df5d807dfc95de2e90ef7326014871b758e71d696c12408  붙여넣은 텍스트 (1)(20260814-065322).txt
```

`[COMPUTED]` The internal `SHA256SUMS.txt` in the source packet passed completely before the research run.

## Run all included checks

From the bundle root:

```bash
set -euo pipefail

python3 scripts/generate_w73_q3_twisted_tensor_certificate.py \
  certificates/W73_Q3_TWISTED_TENSOR_28.regenerated.json
python3 scripts/verify_w73_q3_twisted_tensor_certificate.py \
  certificates/W73_Q3_TWISTED_TENSOR_28.regenerated.json

python3 scripts/generate_w53_q3_certificate.py \
  certificates/W53_Q3_NORM_ONE_13.regenerated.json
python3 scripts/verify_w53_q3_certificate.py \
  certificates/W53_Q3_NORM_ONE_13.regenerated.json

python3 scripts/verify_scalar_pointwise_audit.py

sha256sum -c MANIFEST.sha256
```

The regenerated JSON files should be byte-for-byte identical to the shipped files:

```bash
cmp certificates/W73_Q3_TWISTED_TENSOR_28.regenerated.json \
    certificates/W73_Q3_TWISTED_TENSOR_28.json
cmp certificates/W53_Q3_NORM_ONE_13.regenerated.json \
    certificates/W53_Q3_NORM_ONE_13.json
```

## What each verifier establishes

### `verify_w73_q3_twisted_tensor_certificate.py`

`[COMPUTED]` Checks, without extension-field arithmetic:

- the exported \(8\times8\) matrix is alternating over \(\mathbb F_3\);
- its rank is eight;
- the 28 vectors represent distinct projective points;
- all 378 unordered pairings are nonzero.

### `verify_w53_q3_certificate.py`

`[COMPUTED]` Checks, without extension-field arithmetic:

- the exported \(6\times6\) matrix is alternating over \(\mathbb F_3\);
- its rank is six;
- the 13 vectors represent distinct projective points;
- all 78 unordered pairings are nonzero.

### `verify_scalar_pointwise_audit.py`

`[COMPUTED]` Checks exact integer versions of the pointwise inequalities over the finite ranges recorded in its transcript. It is an arithmetic audit, not a replacement for the infinite symbolic proof in `GLOBAL_RESEARCH_REPORT.md`.

## Expected saved transcripts

- `certificates/TWISTED_TENSOR_GENERATOR_TRANSCRIPT.txt`
- `certificates/TWISTED_TENSOR_VERIFICATION_TRANSCRIPT.txt`
- `certificates/GENERATOR_TRANSCRIPT.txt`
- `certificates/VERIFICATION_TRANSCRIPT.txt`
- `certificates/SCALAR_POINTWISE_AUDIT_TRANSCRIPT.txt`
- `certificates/SOURCE_PACKET_SHA256_AUDIT.txt`
- `certificates/ENVIRONMENT_AND_INPUT_HASHES.txt`
- `certificates/BUNDLE_VALIDATION_TRANSCRIPT.txt`
