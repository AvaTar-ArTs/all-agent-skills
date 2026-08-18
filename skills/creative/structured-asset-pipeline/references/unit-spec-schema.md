# Unit Spec Schema — `structured-asset-pipeline` v1.0

All unit spec files live in `assets/{slug}/specs/NN-{kind}-{slug}.yaml`.

## Run meta (`00-meta.yaml`)

```yaml
schema_version: "1.0"
run_id: "my-project-slug"
slug: "my-project-slug"
created_at: "2026-07-08T14:30:00-05:00"
language: "en"
modality: "mixed"          # image | audio | mixed
default_backend: "openai_images"
universe_ref: null         # optional Chozen universe id (future)
scene_refs: []             # optional list of scene_id strings (future)
notes: ""
```

## Image unit

```yaml
schema_version: "1.0"
unit_id: "01-cover"
kind: "image"
modality: "image"
backend: "openai_images"   # openai_images | replicate | fal | comfyui
status: "pending"          # pending | generating | done | failed | skipped

# Chozen-compatible narrative hooks (optional)
scene_id: null
shot_id: null
character_ids: []

# Generation payload
prompt: |
  Full final prompt text. Include character text anchors if needed (R8).
negative_prompt: ""
aspect_ratio: "3:4"        # free-form; adapter maps to backend enums
size: null                 # e.g. "1024x1536" if backend requires pixels
model: null                # backend-specific; adapter uses defaults
seed: null
params: {}                 # backend-specific extras (no secrets)

# Output contract
out_relpath: "out/01-cover.png"
out_format: "png"

# Provenance
references:
  - ref_id: "01"
    filename: "refs/01-ref-style.png"
    usage: "style"         # style | palette | scene
    traits: "grunge ink, neon rim light, distressed textures"

# Retry / audit
attempts: 0
last_error: null
```

## Audio unit

```yaml
schema_version: "1.0"
unit_id: "01-theme"
kind: "audio"
modality: "audio"
backend: "elevenlabs"      # elevenlabs | suno_unofficial
status: "pending"

scene_id: null
character_ids: []

prompt: |
  For TTS: the spoken script.
  For music (Suno): lyrics / style description.
voice_id: null             # ElevenLabs: required
model: null
duration_hint_sec: null
params:
  # elevenlabs: stability, similarity_boost, style, speed
  # suno: tags, title, make_instrumental

out_relpath: "out/01-theme.mp3"
out_format: "mp3"

attempts: 0
last_error: null
```

## Rules

- `out_relpath` is relative to the run directory root; adapters receive the absolute `--out` path computed by the agent.
- `status` is informational; the agent drives state transitions, not the adapters.
- `params` must never contain API keys or secrets (D12 / R7).
- Prompt is final at spec-write time (R1). Edit spec first, then regenerate (not the other way).
