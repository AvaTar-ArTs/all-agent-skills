# PORT_NOTES — structured-asset-pipeline

## Inheritance from baoyu-comic

This skill's operational rules are distilled from **baoyu-comic** (JimLiu / 宝玉, MIT license) and its Hermes-agent port. We did not copy art styles, presets, or comic-specific schemas; only the pipeline discipline.

### Rules inherited (by theme)

| baoyu pattern | Generalized rule |
|---------------|-----------------|
| Prompt files written before `image_generate` | R1: spec to disk before adapter call |
| `curl -o /absolute/path` in every download | R2: absolute paths only |
| `test -s file` after every download | R3: verify non-empty |
| Backup with timestamp before regenerate | R4: backup_with_timestamp |
| Step 2 confirmation before images | R5: confirmation gate |
| Visible defaults on clarify timeout | R6: visible defaults |
| Strip secrets from source content | R7: secret stripping on intake |
| Character text descriptions embedded in every prompt | R8: consistency via text |
| Partial workflows (storyboard-only, prompts-only, images-only, regen-N) | R9: partial workflows first-class |
| Art / tone adapters as separate reference files | R10: one adapter per backend |

### Apr 2026 CWD incident (baoyu R2 origin)

Pages 06–09 of a 10-page comic run landed at the repo root instead of `comic/<slug>/` because:
- Batch 3 of image downloads inherited a stale CWD from batch 2
- `curl -o 06-page-skills.png` (relative path) wrote to the wrong directory silently
- The agent then spent several turns claiming files existed where they did not

This incident is the origin of **R2** and the absolute-path requirement enforced in `scripts/common/paths.require_abs()` and every adapter's `--out` validation.

## What is NOT inherited from baoyu

- Art-style / tone / layout catalogs (ligne-claire, manga, etc.) — those belong in derivative skills
- Comic-specific storyboard schema — generalized to unit-spec YAML
- `image_generate` Hermes tool — replaced by contract-first adapter scripts
- `clarify` Hermes tool — replaced by runtime-neutral "ask the user" guidance
- Ohmsha / wuxia / preset system — excluded (YAGNI §11)

## Future derivatives

1. **TrashCat comics skill** — loads character text anchors from Chozen/TrashCats YAML; calls this pipeline with `modality: image` + grunge style presets baked into consistency blocks.
2. **Music batch skill** — intake: CSV/YAML track list → N audio units; backends: ElevenLabs + Suno.
