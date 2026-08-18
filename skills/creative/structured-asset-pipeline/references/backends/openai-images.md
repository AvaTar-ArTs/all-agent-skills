# Backend: OpenAI Images

## Env vars
- `OPENAI_API_KEY` (required)
- `OPENAI_BASE_URL` (optional; default: `https://api.openai.com`)

## Top-level spec fields
`model` (default: `gpt-image-1`), `size` (explicit size string, overrides aspect_ratio mapping), `aspect_ratio` (maps to size automatically)

## Allowed spec.params fields
`quality`, `background`, `output_format`, `style`

## Models
- `gpt-image-1` (default, recommended for quality)
- `dall-e-3`
- `dall-e-2`

## Size mapping

| aspect_ratio | gpt-image-1 size | dall-e-3 size |
|-------------|------------------|---------------|
| 1:1 | 1024x1024 | 1024x1024 |
| 3:4 / 2:3 / 9:16 | 1024x1536 | 1024x1792 |
| 4:3 / 3:2 / 16:9 | 1536x1024 | 1792x1024 |

## Response format
`gpt-image-1` returns `b64_json` by default. The adapter decodes and writes directly.
`dall-e-3` may return a `url` — adapter downloads to `--out`.

## Cost notes (verify at build time — pricing changes)
- `gpt-image-1` high quality: ~$0.17–$0.25/image
- `dall-e-3` standard: ~$0.04/image

## Failure modes
| Code | HTTP status | Meaning |
|------|-------------|---------|
| 2 | 401/403 | Missing or invalid `OPENAI_API_KEY` |
| 3 | 429 | Rate limited; adapter retries once after 3s |
| 3 | 400 with content_policy | Policy block; do not retry; edit prompt |
| 3 | 5xx | Server error; adapter retries once |

## Prompt tips
- gpt-image-1 follows detailed art direction well; be specific about style, lighting, and composition
- Negative prompt not supported natively; use "avoid X" phrasing in the positive prompt
