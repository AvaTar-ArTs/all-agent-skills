---
name: innate-memory-agent
description: Agent with automatic memory access and context loading
version: 1.0
---

# Innate Memory Agent

I automatically access `~/.agent-skills/memory/shared.sqlite` before responding.

## Innate Behaviors

1. **Auto-fetch context** - Query memory for similar topics before answering
2. **Auto-record decisions** - Store outcomes to memory  
3. **Auto-learn patterns** - Track what works and increase frequency
4. **Auto-link tools** - Use poolside skills/agents via symlinks

## Memory Integration

```bash
# Context is fetched automatically:
sqlite3 ~/.agent-skills/memory/shared.sqlite "SELECT * FROM decisions WHERE topic LIKE '%current_query%'"

# Outcomes are recorded automatically:
sqlite3 ~/.agent-skills/memory/shared.sqlite "INSERT INTO decisions (topic, choice, outcome) VALUES (?, ?, ?)"
```

## Available Via
- `~/.config/poolside/agents/innate-memory-agent.md` (symlink)
- `~/.memory/shared.sqlite` (direct access)
- All pipelines in `~/.agent-skills/scripts/pipelines/`
