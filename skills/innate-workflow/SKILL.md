---
name: innate-workflow
description: "Use when starting or ending a session that should follow the local audit, skill-selection, task-work, and memory-update rhythm."
---

# Innate Workflow

Auto-trigger sequence at start/end of every session:

1. **workspace-ecosystem-audit** - Understand environment
2. **using-superpowers** - Find relevant skills (queries memory)
3. **ralph-self-audit** - Challenge assumptions, evidence, authorization, destination, and completion claims
4. **Task Work** - Execute with full context
5. **verification-before-completion** - Verify the result and locate durable artifacts
6. **self-evolving-memory** - Record outcomes, learn

## Session Close — Memory Ritual

Before ending any substantive session, ask:

- **Did a decision get made that ALL AI tools should know?**
  If yes → write it to `shared.sqlite` via `cross-tool-memory` skill.
  Example: naming conventions, architecture choices, preference changes that affect
  how Codex, Gemini, or Qwen should behave — not just Claude Code.

- **Did something worth remembering across Claude Code sessions happen?**
  If yes → write it to Engram MCP (investigation context, session narrative, decisions made).

These are two different destinations for two different scopes. Cross-tool decisions
go to `shared.sqlite`. Session history and rich context go to Engram.

All runtime state in `~/.agent-skills/memory/shared.sqlite`.
