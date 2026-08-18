# Backend: ElevenLabs

## Env vars
- `ELEVENLABS_API_KEY` (required)

## Allowed spec.params fields
`voice_id` (can also be `spec.voice_id` at top level), `output_format` (e.g. `mp3_44100_128`), `stability`, `similarity_boost`, `style`, `speed`

## voice_id
Required. Must be set in `spec.voice_id` or `spec.params.voice_id`. Find voice IDs in your ElevenLabs account or via the API: `GET https://api.elevenlabs.io/v1/voices`.

Do NOT hardcode a voice ID in the adapter — voices are account-scoped.

## Models (verify current at https://elevenlabs.io/docs)
- `eleven_multilingual_v2` (default, recommended — multilingual, high quality)
- `eleven_monolingual_v1` (English only, legacy)
- `eleven_turbo_v2` (fast, lower cost)
- `eleven_turbo_v2_5` (fast multilingual)

## API
```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128
Headers: xi-api-key: $ELEVENLABS_API_KEY
Body: {"text": "...", "model_id": "eleven_multilingual_v2", "voice_settings": {...}}
Response: binary audio stream (mp3 or wav)
```

## Cost notes
Pricing is per character. Typically ~$0.000024/char on the Starter plan. A 1000-char script ≈ $0.024.
Check https://elevenlabs.io/pricing for current rates.

## Output formats
`mp3_44100_128` (default), `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_44100`, `ulaw_8000`

## v1 scope
This adapter covers TTS. ElevenLabs also has sound-effects and music endpoints — v2 candidates.

## Failure modes
| Code | Meaning |
|------|---------|
| 1 | Missing voice_id or empty prompt |
| 2 | 401/403 invalid API key |
| 3 | 5xx server error; 429 rate limit |
