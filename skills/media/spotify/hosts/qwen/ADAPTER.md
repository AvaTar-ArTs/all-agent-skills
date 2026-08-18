---
host: qwen
source: ~/.agent-skills/skills/media/spotify/SKILL.md
---

# Adapter: Qwen

## What changes

- If Qwen uses tool-call schemas, mirror the Spotify “tool function names” and failure-mode guidance into Qwen’s preferred invocation format.
- Keep the “critical failure modes” section verbatim-ish (no secrets), because it’s the highest value operator guidance.

## Secrets/state

- Treat Spotify OAuth refresh/access tokens as secrets; keep them out of sync/backup.

