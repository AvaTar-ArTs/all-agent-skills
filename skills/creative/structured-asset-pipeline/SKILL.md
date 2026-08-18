---
name: structured-asset-pipeline
description: "Generic structured asset pipeline for multi-unit image and audio generation via contract-first adapters. Use whenever the user wants batch generation, comic pages, album art, voiceovers, music tracks, storyboard-to-assets, regenerate page N, or a reproducible generate-from-spec workflow, even if they only say make the assets or run the pipeline."
version: 1.0.0
license: MIT
metadata:
  tags: [pipeline, image-generation, audio-generation, adapters, creative]
---

# structured-asset-pipeline

Generic, reproducible multi-asset generation: content in → analysis → unit specs → user confirmation → adapters → verified files on disk → report.

**The pipeline is not complete until every requested asset exists on disk at its declared absolute path, is non-empty, and is listed in a completion report — spec files alone never count as "done."**

## When to use

Use this skill when the user wants to:
- Generate a **batch or series** of images (comic pages, storyboard stills, album covers, product mockups)
- Generate **audio** (voiceovers, TTS narration, music tracks)
- Run a **reproducible** generation pipeline they can partially redo
- **Regenerate** specific units from existing specs
- Start from a topic or brief and get **final files on disk**

**When not to use:** A single one-off image with no reproducibility need. A lone asset does not justify a manifest.

## Options

| Option | Values | Default |
|--------|--------|---------|
| Modality | image, audio, mixed | inferred from content |
| Backend | openai_images, replicate, fal, comfyui, elevenlabs, suno_unofficial | openai_images (image), elevenlabs (audio) |
| Partial mode | analyze-only, specs-only, generate-only, regenerate-N | full pipeline |
| Language | any | user's conversation language |

See [references/partial-workflows.md](references/partial-workflows.md).

## Run directory layout

```
assets/{slug}/
├── source-{slug}.md       # secrets-stripped input
├── analysis.md
├── plan.md                # unit inventory
├── characters/            # optional text descriptions for visual consistency (R8)
├── refs/                  # optional user reference copies (provenance only)
├── specs/
│   ├── 00-meta.yaml
│   └── NN-{kind}-{slug}.yaml
├── prompts/               # optional human-readable prompt dumps
├── out/                   # final binary assets
├── logs/run.jsonl
└── report.md
```

## Progress checklist

```
Pipeline Progress:
- [ ] Step 1: Intake & secret strip → source-{slug}.md
- [ ] Step 2: Analyze → analysis.md
- [ ] Step 3: Plan units → plan.md + specs/*.yaml
- [ ] Step 4: Confirm backend / scope / review gates  ⚠️ REQUIRED
- [ ] Step 5: (Optional) User reviews specs
- [ ] Step 6: Generate via adapters (absolute --out)
- [ ] Step 7: Verify each out/* file
- [ ] Step 8: Report → report.md
```

## Hard rules summary (R1–R12)

All rules are in [references/hard-rules.md](references/hard-rules.md). Brief form:

| Rule | Summary |
|------|---------|
| R1 | Spec to disk before any adapter call |
| R2 | Always absolute paths — never rely on CWD (Apr 2026 incident) |
| R3 | Verify file exists and non-empty after every write |
| R4 | Backup before regenerate (rename with `-backup-YYYYMMDD-HHMMSS`) |
| R5 | Confirmation gate before any generation |
| R6 | Visible defaults on timeout; one question at a time |
| R7 | Strip secrets on intake (sk-, r8_, Bearer, cookies) |
| R8 | Character consistency via embedded text, not reference images |
| R9 | Partial workflows are first-class (analyze-only, specs-only, regen-N) |
| R10 | One adapter per backend; shared logic in scripts/common/ |
| R11 | Exit codes: 0=ok 1=invalid 2=auth 3=api/network 4=verify-fail 5=unsupported |
| R12 | Never claim success without filesystem proof |

## Step summary

| Step | Action | Output |
|------|--------|--------|
| 1 | Intake + secret strip | source-{slug}.md |
| 2 | Analyze content | analysis.md |
| 3 | Plan units + write specs | plan.md, specs/*.yaml |
| 4 | Confirm: backend, scope, review gates ⚠️ | user approval |
| 5 | (opt) User reviews specs | approved specs |
| 6 | Generate per unit via adapter | out/*.png/*.mp3 |
| 7 | Verify each file (R3, R12) | verified assets |
| 8 | Report | report.md |

## Calling adapters (generate step)

```bash
# ALWAYS absolute paths (R2)
python /path/to/skill/scripts/adapters/openai_images.py \
  --spec /abs/run/specs/01-cover.yaml \
  --out  /abs/run/out/01-cover.png

# On exit 0: parse stdout JSON; update logs/run.jsonl; verify out file (R3)
# On exit != 0: mark unit failed; one auto-retry; then continue to next unit
```

Use `--dry-run` at the confirmation gate to check env vars before spending money.

## Adapters

| Backend | Kind | Env vars | Cost/latency | Ref |
|---------|------|----------|--------------|-----|
| openai_images | image | `OPENAI_API_KEY` | ~$0.01–$0.25/image | [→](references/backends/openai-images.md) |
| replicate | image | `REPLICATE_API_TOKEN` | per-model | [→](references/backends/replicate.md) |
| fal | image | `FAL_KEY` | per-model, fast | [→](references/backends/fal.md) |
| comfyui | image | `COMFYUI_BASE_URL` | $0 local GPU | [→](references/backends/comfyui.md) |
| elevenlabs | audio | `ELEVENLABS_API_KEY` | per-char | [→](references/backends/elevenlabs.md) |
| suno_unofficial | audio | `SUNO_API_BASE` | **VOLATILE** — unofficial | [→](references/backends/suno-unofficial.md) |

## References

- [Workflow detail](references/workflow.md) — full stage-by-stage
- [Unit spec schema](references/unit-spec-schema.md)
- [Adapter contract](references/adapter-contract.md)
- [Partial workflows](references/partial-workflows.md)
- [Secrets & env](references/secrets-and-env.md)
- [Hard rules](references/hard-rules.md)

## Pitfalls

1. **CWD is a footgun** — Apr 2026: pages 06–09 wrote to repo root instead of output dir because CWD drifted between batches. Always absolute `--out` (R2).
2. **Verify before reporting success** — ephemeral URLs ≠ local files (R12).
3. **Backup before regen** — silently overwriting destroys prior work (R4).
4. **Strip secrets on intake** — source content often contains pasted API keys (R7).
5. **Suno is VOLATILE** — no official API; unofficial proxies break; check status before relying on it.
6. **ComfyUI needs API-format export** — not the full UI JSON. See [backends/comfyui.md](references/backends/comfyui.md).
7. **Confirmation gate is mandatory** — do not skip even for "quick" runs (R5).

## Future skills (not in v1)

| Skill | Builds on |
|-------|-----------|
| TrashCat comics | This pipeline + Chozen character text anchors + grunge style presets |
| Music batch | This pipeline + Suno/ElevenLabs units from a track list CSV/YAML |
