# Backend: Replicate

## Env vars
- `REPLICATE_API_TOKEN` (required; fallback `REPLICATE_API_KEY`)

## Allowed spec.params fields
`version` (model version hash), `input_overrides` (dict, model-specific)

## Model selection
Set `spec.model` to a model reference like `black-forest-labs/flux-1.1-pro` (no version hash needed for models route).
Or set `spec.params.version` to a specific version hash for the predictions route.
Default placeholder: `black-forest-labs/flux-1.1-pro` — operator should verify the current recommended version at https://replicate.com/explore.

## API flow
1. `POST /v1/models/{owner}/{name}/predictions` (or `/v1/predictions` with `version`)
2. Poll `GET /v1/predictions/{id}` until `status == "succeeded"` or `"failed"`
3. Download first URL from `output` field

## Poll schedule
Exponential backoff starting at 1s, multiplying by 1.5 each cycle, capped at 5s (1s → 1.5s → 2.25s → 3.4s → 5s). Default timeout 300s.

## Cost notes
Pricing varies per model. FLUX.1 Pro: ~$0.055/run. Check https://replicate.com/pricing.

## Failure modes
| Code | Meaning |
|------|---------|
| 1 | Missing/invalid spec.model or spec.params.version |
| 2 | 401 invalid token |
| 3 | Prediction failed or canceled; poll timeout |
