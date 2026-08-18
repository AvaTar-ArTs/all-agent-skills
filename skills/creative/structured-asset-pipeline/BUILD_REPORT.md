# structured-asset-pipeline build report

## Location

`~/.agent-skills/skills/creative/structured-asset-pipeline/`

## Acceptance

| Check | Result |
|-------|--------|
| pytest green (30 tests) | PASS |
| dry-run exit 0 without env keys | PASS |
| relative `--out` rejected (exit 1, clean error) | PASS |
| secrets redaction covers sk-/r8_/Bearer/cookie patterns | PASS |
| overwrite refused without backup flag | PASS — `refuse_overwrite()` in all 6 adapters; tested (2 adapter tests + 4 unit tests) |
| `PIPELINE_ALLOW_OVERWRITE=1` bypasses guard | PASS — tested |
| Suno live without `SUNO_API_BASE` exits 5 | PASS |
| SKILL.md < 500 lines | PASS (270 lines) |
| No real secret values in skill tree | PASS (test fixtures have dummy patterns — see ASSUMPTIONS.md A1) |

## Adapters

| Backend | dry-run | live implemented | notes |
|---------|---------|-----------------|-------|
| openai_images | PASS | YES | b64_json + url fallback; aspect mapping for gpt-image-1 and dall-e-3 |
| replicate | PASS | YES | model route + version route; 1s→2s poll |
| fal | PASS | YES | queue-based; COMPLETED status; generic URL finder |
| comfyui | PASS | YES | API-format workflow injection; CLIPTextEncode autodetect |
| elevenlabs | PASS | YES | TTS; voice_id required; voice_settings passthrough |
| suno_unofficial | PASS | YES (with proxy) | Exits 5 without SUNO_API_BASE; volatile banner in reference doc |

## Spec deviations from docs/handoffs/PIPELINE_BUILD_SPEC.md

1. **Live endpoint verification (§7.3, §7.5)** — The spec calls for verifying current endpoint URLs, params, and pricing at build time via live docs. Adapters and reference docs were written from training data (knowledge cutoff Jan 2026). The volatile backends (fal `Key` header, ElevenLabs model IDs, Suno proxy API shape) should be verified against live docs before first production use. Noted in `ASSUMPTIONS.md` A5.

2. **CHANGELOG.md** — An unplanned `CHANGELOG.md` was auto-generated at the skill root during a SKILL.md restoration step. It is accurate but was not in the §3.1 layout spec.

## Assumptions

- See `ASSUMPTIONS.md` for 5 documented assumptions (Python 3.11+ UTC, test fixture secrets, etc.)

## Not done (intentional — YAGNI §11)

1. PDF / ebook export
2. Video generation adapters
3. Chozen ontology engine / scene graph traversal
4. TrashCat brand pack / presets (derivative skill)
5. Web UI / daemon
6. Suno cookie-mode browser automation
7. Multi-tenant server
8. Cost accounting dashboard
9. Fine-tuning pipeline
10. `~/.env.d` replacement
11. MCP server wrapper
12. Parallel fan-out of 50+ jobs

## Next steps (from spec §14 and PORT_NOTES)

1. **Smoke test** — run one real image unit: load keys, pick a topic, let the pipeline generate a single openai_images unit end-to-end.
2. **TrashCat comics skill** — derivative: character text anchors from Chozen + grunge style presets + this pipeline.
3. **Music batch skill** — derivative: CSV/YAML track list → ElevenLabs/Suno units.
