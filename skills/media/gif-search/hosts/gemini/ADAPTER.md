---
host: gemini
source: ~/.agent-skills/skills/media/gif-search/SKILL.md
---

# Adapter: Gemini

## Notes

- Keep as a documentation-first skill; Gemini runtime wrappers should call out `curl` + `jq` requirements.
- Load `TENOR_API_KEY` from `~/.env.d/` (preferred) or Gemini’s secrets store if configured.

