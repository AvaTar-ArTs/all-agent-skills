# Backend: Suno (unofficial) — ⚠️ VOLATILE

> **VOLATILE:** This adapter relies on unofficial third-party proxy APIs. Endpoints churn without notice. Verify your provider's current docs before relying on this adapter. Suno's official developer API program is being developed (public signals ~2026-07-03); when it launches, this adapter's internals will be updated while the CLI contract remains stable.

## Verify before use checklist
- [ ] Confirm your proxy is running and accepting requests at `SUNO_API_BASE`
- [ ] Confirm `SUNO_API_KEY` is set if your proxy requires it
- [ ] Run `--dry-run` to validate spec fields before a live call
- [ ] Check your proxy provider's ToS and uptime status

## Env vars
- `SUNO_API_BASE` (required for live mode; set to your local proxy URL, e.g. `http://localhost:3000`)
- `SUNO_API_KEY` (optional; depends on your proxy)
- `SUNO_MODEL_VERSION` (optional; proxy/provider default used if absent)

Without `SUNO_API_BASE`, live mode exits 5 immediately. Dry-run always works.

## Cookie mode (advanced / not default)
`SUNO_COOKIE` exists in the operator's env.d. To use it with a local cookie-based proxy:
1. Set `SUNO_API_BASE=http://localhost:3000` (the local proxy)
2. Set `PIPELINE_SUNO_COOKIE_MODE=1`
3. The proxy handles cookie auth; the adapter never sends cookies to remote third parties directly.
Do NOT set `SUNO_API_BASE` to a remote third-party service and pass `SUNO_COOKIE` to it — that hands your personal Suno account credential to a third party.

## Allowed spec.params fields
`tags` (style tags, e.g. "grunge punk, alley anthem"), `title`, `make_instrumental` (bool), `model_version` (override), `endpoints` (dict — override generate_path / status_path / audio_url_jsonpath for your proxy)

## Music spec fields
```yaml
prompt: "lyrics or style description"
params:
  tags: "punk grunge, downtown alleys"
  title: "Royalty of Refuse"
  make_instrumental: false
```

## API flow (generic proxy shape)
1. `POST {SUNO_API_BASE}/api/generate` — submit job
2. Receive task id
3. Poll `{SUNO_API_BASE}/api/get?ids={task_id}` until `audio_url` appears
4. Download audio to `--out`

If your proxy uses different paths, override via `spec.params.endpoints`.

## Timeouts
Default 600s. Music generation typically 20–60s on current V5-class models.

## ToS / risk notice
Third-party wrappers typically access Suno's platform via shared account pools or managed auth, which may violate Suno's Terms of Service. Use at your own risk. Prefer providers that issue their own API keys (not requiring your personal Suno credentials). Monitor provider status; downtime without notice is common.

## Migration path
When Suno's official partner API ships, update this adapter's HTTP logic. The `--spec`/`--out` CLI and exit codes remain stable; only the request body and URL change.
