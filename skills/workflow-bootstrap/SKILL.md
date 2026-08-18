---
name: workflow-bootstrap
description: Defines mandatory workflows and where Supremepower/Gemini capabilities live. Use when starting creative work, multi-step implementation, or when the user asks how skills and agents are organized. Ensures brainstorm before coding and plan-before-implement discipline.
---

> **Supremepower:** Enhanced from Cursor workflow bootstrap. Same methodology; skills loaded via the extension.

# Supremepower Workflow Bootstrap

## Where things live (this environment)

| Type | Path | Scope |
|------|------|--------|
| Custom skills | ~/.supremepower/skills/<name>/SKILL.md | Generated from Cursor-enhanced superpowers; load via extension |
| Custom agents | ~/.supremepower/agents/ | Per config.json; extension may use bundled agents if empty |
| Bundled skills/commands | Extension (e.g. /plan, /brainstorm, /implement, /tdd, /debug, /sp:*) | Use extension UI or commands to invoke |

Config: ~/.supremepower/config.json (customSkillsPath, customAgentsPath).

## Mandatory workflows

**Before creative work (features, components, behavior changes):**
1. Use the **brainstorming** skill to explore intent, requirements, and design.
2. Document the design (e.g. docs/plans/YYYY-MM-DD-<topic>-design.md).
3. Only then move to implementation.

**Before multi-step implementation:**
1. Use the **writing-plans** skill to produce a bite-sized implementation plan.
2. Save to docs/plans/YYYY-MM-DD-<feature>.md.
3. Optionally use **using-git-worktrees** for an isolated branch before executing.
4. Use **executing-plans** (or **subagent-driven-development** if tasks are independent and in-session) to run the plan with review checkpoints.

**After a major project step:**
- Use code review (e.g. **requesting-code-review** / **receiving-code-review**) against the plan and standards.

## Skill chain

- **brainstorming** -> design doc -> **writing-plans** -> plan doc -> **executing-plans** (or **subagent-driven-development**) -> **finishing-a-development-branch**.
- **requesting-code-review** / **receiving-code-review** when a chunk is done.
- **test-driven-development**: during implementation (red-green-refactor); **using-git-worktrees**: when starting isolated branch work.
- **systematic-debugging**: before any fix; **verification-before-completion**: before any completion claim.
- **dispatching-parallel-agents**: when 2+ independent problems; **writing-skills**: TDD for authoring skills.

## When a skill applies

If a task matches a skill description, use that skill. Do not skip mandatory workflows (brainstorm before coding; plan before multi-step implementation).

## Cross-ecosystem

This set is generated from canonical superpowers at `~/iterm2/superpowers/skills/` and propagated for local use. For how Supremepower ties to Cursor, Qwen, and Codex, use the **ecosystem-clarity** skill when available.
