# Workflow — stage-by-stage detail

## Stage 1: Intake & secret strip

**Input:** User-provided content (topic, pasted text, file path, URL)
**Output:** `assets/{slug}/source-{slug}.md`

1. Derive slug: 2–4 words kebab-case from topic (e.g. `trashcat-first-fire`).
2. If `assets/{slug}/` already exists: stop and ask — options: reuse/resume, backup-and-fresh, or abort (R11 conflict rule).
3. Scan content for secrets using `secrets.redact()` (R7). Warn user of any redactions.
4. Write cleaned content to `source-{slug}.md`.

**Jump point for partial mode:** `analyze-only` starts here.

## Stage 2: Analyze

**Input:** source-{slug}.md
**Output:** `assets/{slug}/analysis.md`

Use the template at `references/templates/analysis.md`. Answer:
- Target audience
- Core message
- Entities / characters needing text anchors
- Recommended unit count and kinds (image / audio)
- Recommended backend per unit type
- Risks / content notes

## Stage 3: Plan units + write specs

**Input:** analysis.md
**Output:** `plan.md`, `assets/{slug}/specs/00-meta.yaml`, `assets/{slug}/specs/NN-*.yaml`

1. Write `00-meta.yaml` (run-level metadata).
2. For each unit: write a spec YAML per the schema in `references/unit-spec-schema.md`.
   - Prompt is **final** at write time — embed all character text anchors now (R1, R8).
   - `out_relpath` must be set; the agent will compute the absolute path at generation time (R2).
3. Write `plan.md` with unit inventory table: NN | kind | backend | intent | out_relpath.

**Jump point for partial mode:** `specs-only` stops here.

## Stage 4: Confirmation gate ⚠️ REQUIRED

**Never skip.** Present:
- Table of units: NN, kind, backend, one-line intent
- Total unit count
- Env vars required and their presence (`--dry-run` each adapter to check)
- Output directory
- Estimated cost (rough: see backend references)

Ask user to confirm. Also ask (one question at a time, R6):
1. "Confirm backend(s) and scope?"
2. "Review specs before generation? (yes/no)"
Set `confirmed_at` timestamp in 00-meta.yaml before proceeding.

## Stage 5: (Optional) User reviews specs

Only if user requested in Stage 4. Present each spec's prompt for approval. User can edit spec files; agent re-validates after edits.

## Stage 6: Generate via adapters

**For each unit in order:**

```text
1. backup_with_timestamp(out_abs) if out file exists (R4)
2. Compute out_abs = os.path.join(run_dir, spec.out_relpath)  — absolute (R2)
3. run adapter --spec SPEC_ABS --out OUT_ABS
4. Parse stdout JSON result
5. verify_nonempty(out_abs) (R3)
6. Append to logs/run.jsonl
7. On failure: one auto-retry; on second failure: mark failed, continue
```

Default: sequential. Optional: 2 concurrent if user requests speed.

**Jump point for partial mode:** `generate-only` starts here (requires specs/ to exist).
**Jump point for partial mode:** `regenerate-N` applies to listed unit ids only.

## Stage 7: Verify

Independent verification pass: for each unit marked done, re-run `verify_nonempty(out_abs)`. Report any that fail post-hoc.

## Stage 8: Report

Write `report.md` using template at `references/templates/report.md`. In chat: short prose summary, list file paths, surface any failures with exact regenerate instruction.

## Failure handling

- Per-unit: one auto-retry; if still failed, mark in logs, continue, surface in report.
- Systemic (missing API key): fail fast before loop; surface at Stage 4 gate.
- Content policy reject (HTTP 400 policy): do not retry; surface and propose a prompt edit (R9 spec-edit-first rule).
