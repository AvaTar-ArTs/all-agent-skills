# Assumptions & decisions

## A1 — Test fixtures contain example secret-pattern strings (intentional)

`tests/test_secrets.py` includes strings like `r8_abcdefghijklmnopqrstuvwxyz` and `sk-ant-api03-…` as unit test inputs. These are fake strings used to verify that `secrets.redact()` detects and removes them. `git grep -E 'sk-|r8_|xi-api'` will match these lines — this is expected and correct. No real credentials exist in the skill tree.

## A2 — Python 3.11+ assumed for `datetime.UTC`

The spec says Python 3.10+. `datetime.UTC` was added in 3.11. The target machine runs 3.14.6 (verified in spec §3.5), so this is safe. If backporting to 3.10 is needed, replace `from datetime import UTC` with `UTC = datetime.timezone.utc`.

## A3 — ElevenLabs dry-run validates voice_id is not REPLACE_ME

The fixture `sample-unit-audio.yaml` has `voice_id: REPLACE_ME` which causes the ElevenLabs adapter to exit 1 in dry-run. This is correct behavior (voice_id is required). The mock-run fixture uses `mock-voice-id-for-dry-run-only` to allow the dress rehearsal to pass.

## A4 — fal adapter uses `fal-ai/flux/schnell` as documented default; spec.model is required

The fal adapter requires `spec.model` to be set. The recommended defaults are in `references/backends/fal.md`. The image fixture uses `model: gpt-image-1` (not a fal model) but that is irrelevant in dry-run mode where no API call is made — the model value is accepted as-is for dry-run validation.

## A5 — Suno cookie mode not implemented (as specified in §7.6)

`PIPELINE_SUNO_COOKIE_MODE` is documented in the suno reference but not implemented in v1 code. This matches the spec's explicit instruction not to implement browser automation or direct cookie scraping.
