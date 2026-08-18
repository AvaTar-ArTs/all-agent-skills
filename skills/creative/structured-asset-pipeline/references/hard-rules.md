# Hard Rules (R1–R12) — structured-asset-pipeline

These rules are non-negotiable. Each exists because of a real production failure or battle-tested lesson.

## R1 — Spec before generation
Write the full unit spec (including the final prompt body) to disk **before** calling any adapter or API.
**Why:** Reproducibility. If generation fails or context is lost, the spec is the authoritative record to retry from. Agents that keep prompts "in head" regenerate inconsistently and cannot explain what was sent.

## R2 — Absolute paths only
Never pass relative paths to download/write operations. Always use fully-qualified absolute paths.
```bash
curl -fsSL "<url>" -o /absolute/path/to/out/01-cover.png  # ✅
curl -fsSL "<url>" -o out/01-cover.png                     # ❌ FOOTGUN
```
**War story (Apr 2026):** Pages 06–09 of a 10-page comic landed at the **repo root** instead of `comic/<slug>/` because batch 3 inherited a stale CWD from batch 2. `curl -o 06-page-skills.png` wrote to the wrong directory silently. The agent then spent many turns claiming files existed where they did not.

## R3 — Verify non-empty after every write
After every adapter call or download: `test -f /abs/path && test -s /abs/path`. Do not proceed to the next unit until current unit verifies.

## R4 — Backup before regenerate
If asset or spec files already exist and you are regenerating, rename first:
```
01-page-foo.png → 01-page-foo-backup-20260708-143052.png
```
Never silent overwrite. Use `scripts/common/paths.backup_with_timestamp()`.

## R5 — Confirmation gate before generation
Do not call any adapter until the user has confirmed: backend, scope, and review preferences. Minimum confirmations: (1) backend selection, (2) unit count/scope, (3) whether to review specs before generate.

## R6 — Visible defaults on timeout
If a question times out ("use your best judgement"):
- That is a default **for that one question only**.
- Continue asking remaining questions.
- **Surface the default visibly** in the next message: `"Backend: defaulted to openai_images — say the word to switch."`
- Never collapse remaining questions into silent "use all defaults."
**Why:** An unreported default is indistinguishable from never having asked.

## R7 — Secret stripping on intake
Before writing source-*.md or analysis files, scan for and redact:
- `sk-…`, `sk-proj-…`, `sk-ant-…`
- `r8_…` (Replicate keys)
- `Bearer <token>`, `api_key=…`, `Authorization:` headers
- Session cookies (`__client=`, `session=`)
- Private key blocks (`BEGIN PRIVATE KEY`)
Use `scripts/common/secrets.redact()`. Never copy secrets into unit specs.

## R8 — Consistency via embedded text
For recurring characters or shared style, embed stable text descriptions into every unit's prompt at spec-write time. Optional character-sheet PNGs are human review artifacts, not API inputs (backends are prompt-only by default).

## R9 — Partial workflows are first-class
Support: analyze-only, specs-only, generate-from-existing-specs, regenerate-N. Check prerequisites before each partial mode (e.g., generate-only needs specs/ to exist).

## R10 — One adapter per backend
Each backend is an independently invocable script. Shared logic lives in `scripts/common/`. Never put multi-backend logic in one file.

## R11 — Exit codes are the contract
| Code | Meaning |
|------|---------|
| 0 | Success; asset written; JSON result on stdout |
| 1 | Invalid / validation error (bad spec, missing required field) |
| 2 | Auth / missing credentials |
| 3 | Backend API / network / polling failure |
| 4 | Post-write verification failed |
| 5 | Unsupported operation for this backend |

## R12 — Never claim success without filesystem proof
Do not tell the user "generated page 3" until `verify_nonempty()` confirms the absolute path is a non-empty file. Ephemeral URLs are not success.
