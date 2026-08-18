# Backend: fal.ai

## Env vars
- `FAL_KEY` (required; fallback `FAL_API_KEY`)

## Allowed spec.params fields
`input_overrides` (dict, model-specific), `image_size` (convenience)

## Model selection
`spec.model` is **required** — it is the fal model endpoint path (e.g. `fal-ai/flux/schnell`, `fal-ai/flux/dev`).

## Recommended models (verify current catalog at https://fal.ai/models)
- `fal-ai/flux/schnell` — fast drafts (~2–4s)
- `fal-ai/flux/dev` — quality (~5–10s)
- `fal-ai/flux-pro` — highest quality

## API flow (queue-based)
1. `POST https://queue.fal.run/{model}` — submit job
2. Receive `request_id` + status/response URLs
3. Poll status URL until `status == "COMPLETED"`
4. GET response URL; find first image URL under `images[0].url`
5. Download to `--out`

## Auth header
`Authorization: Key <FAL_KEY>` (note: `Key`, not `Bearer`)

## Cost notes
Schnell: ~$0.003/image. Dev: ~$0.025/image. Check https://fal.ai/pricing.

## Failure modes
| Code | Meaning |
|------|---------|
| 1 | Missing spec.model |
| 2 | 401 invalid key |
| 3 | Queue failure; poll timeout (default 300s) |
