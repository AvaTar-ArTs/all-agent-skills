---
name: export
description: Export current session handoff OR memory database decisions (AvatarArts Terminal Exporter)
---

# /export

AvatarArts Terminal Session Exporter — creates durable project handoffs for continuation.

## Session Export (default)

Creates `.agent-exports/YYYY-MM-DD_HHMMSS-<slug>.md` with:

- YAML frontmatter with session metadata
- Executive snapshot
- Original goal and acceptance criteria
- Work completed with evidence
- Workspace changes (git status)
- Commands and verification results
- Errors and diagnostics
- Remaining work and next steps
- Continuation prompt for next agent
- Provenance and privacy notes

```bash
# Default session export
python3 ~/.config/poolside/skills/session-export/scripts/export_session.py

# With focus
python3 ~/.config/poolside/skills/session-export/scripts/export_session.py --focus "memory integration"

# Deep export with snippets
python3 ~/.config/poolside/skills/session-export/scripts/export_session.py --depth deep --format md
```

## Memory Database Export

Export decisions from `~/.agent-skills/memory/shared.sqlite`:

```bash
python3 ~/.config/poolside/skills/cross-tool-memory/scripts/export_decisions.py decisions json --limit 50
python3 ~/.config/poolside/skills/cross-tool-memory/scripts/export_decisions.py decisions md --topic agent
python3 ~/.config/poolside/skills/cross-tool-memory/scripts/export_decisions.py preferences csv
```

## Options

| Option | Values | Default |
|--------|--------|---------|
| `--focus` | Emphasize task/feature | session goal |
| `--format` | md, json | md |
| `--depth` | compact, standard, deep | standard |
| `--path` | Custom output path | .agent-exports/ |

## Arguments Recognition

- `format=md|json`
- `depth=compact|standard|deep`
- `focus=<text>`
- `path=<path>`
- Free text treated as focus

## Safety Rules

- No network requests or package installs
- No source file mutation
- Secrets redacted as `[REDACTED]`
- Workspace-only writes unless explicit path