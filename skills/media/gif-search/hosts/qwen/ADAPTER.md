---
host: qwen
source: ~/.agent-skills/skills/media/gif-search/SKILL.md
---

# Adapter: Qwen

## What changes

- Ensure environment variables are loaded from `~/.env.d/` (not `~/.hermes/.env`).
- If Qwen uses command wrappers, create a Qwen command that shells out to `curl` + `jq` as described in the Tier‑0 skill.

## What to promote (live)

- A Qwen-local command wrapper (TOML/MD depending on your Qwen runtime) that points to this Tier‑0 skill.

## Secrets

- `TENOR_API_KEY` is required; never inline it in docs or command definitions.

