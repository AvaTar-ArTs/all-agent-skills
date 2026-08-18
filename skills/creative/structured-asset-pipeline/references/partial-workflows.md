# Partial Workflows (R9)

The pipeline supports four partial modes. Prerequisites are checked before starting; missing prerequisites are surfaced to the user.

## Mode table

| Mode | Natural language cues | Stages run | Prerequisites |
|------|-----------------------|-----------|---------------|
| analyze-only | "just analyze", "give me a plan", "what would this take" | 1–2 | none |
| specs-only | "write the specs, don't generate", "spec it out first" | 1–3 | none |
| generate-only | "specs are ready, generate", "run from existing specs" | 6–8 | specs/ dir + 00-meta.yaml exist |
| regenerate-N | "redo unit 02", "regenerate page 3 and 7" | 4 (mini-confirm), 6–8 for listed units | specs for listed units exist |

## analyze-only

1. Stages 1–2 (intake + analyze).
2. Write `source-{slug}.md` and `analysis.md`.
3. Present analysis summary; stop.
4. Resume: user says "continue" → proceed to Stage 3 (plan).

## specs-only

1. Stages 1–3 (intake + analyze + plan/spec-write).
2. Write all spec files.
3. Present unit table; ask if user wants to review specs (one question).
4. Stop before confirmation gate.
5. Resume: user says "generate" → jump to Stage 4 confirmation gate.

## generate-only

Prerequisites check:
- `assets/{slug}/specs/` exists with at least one unit YAML
- `assets/{slug}/specs/00-meta.yaml` exists

1. Mini-confirmation: present unit table, confirm backend and env vars (`--dry-run` each adapter).
2. Run Stages 6–8.

## regenerate-N

Used to redo specific units (by unit_id or NN prefix).

1. Parse unit list from user input (e.g., "02", "page 3 and 7").
2. Check spec files exist for each named unit.
3. Mini-confirmation: show unit table, estimate cost.
4. For each listed unit:
   - `backup_with_timestamp(out_abs)` (R4)
   - Re-run adapter
   - Verify
5. Update `report.md` with regenerated statuses.

## Resume after interruption

If a run was interrupted mid-generate:
- Check `logs/run.jsonl` for completed units.
- Present status table to user.
- Ask: continue with remaining units, or restart specific ones?
