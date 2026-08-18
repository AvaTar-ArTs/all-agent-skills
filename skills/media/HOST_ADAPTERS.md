# Host Adapters (media skills)

`~/.agent-skills` is the agnostic Tier-0 hub. Skills in this tree may need host-specific renderings (Qwen/Gemini/Cursor/Codex) to match each runtime’s expected formats (YAML frontmatter, TOML agent profiles, command wrappers, plugin/extension packaging).

## Standard layout (per skill)

Each skill may optionally include:

```
hosts/
  qwen/
    ADAPTER.md
  gemini/
    ADAPTER.md
  cursor/
    ADAPTER.md
  codex/
    ADAPTER.md
```

### Rules

- Keep `SKILL.md` as the Tier‑0 source-of-truth.
- `hosts/*/ADAPTER.md` describes:
  - what needs to change for that host (format, env var location, tool naming)
  - what *must not* be imported (runtime/state/secrets)
  - what files would be generated/promoted into the live host runtime (e.g., `~/.qwen`, `~/.codex`)
- If a host needs an actual machine-readable artifact (e.g., TOML), store it under the host folder (e.g., `hosts/qwen/command.toml`) and keep it minimal.

