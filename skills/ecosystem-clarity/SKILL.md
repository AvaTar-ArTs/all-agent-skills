---
name: ecosystem-clarity
description: Single reference for how Supremepower/Cursor skills, agents, and the multi-ecosystem map fit together. Use when coordinating across Qwen/Gemini/Codex/Cursor, when creating skills or agents, when cleaning ecosystem bloat, or when the user asks how everything connects.
---

> **Supremepower:** Enhanced from Cursor ecosystem-clarity. Same map and workflow; paths below include Cursor for cross-ecosystem coordination.

# Ecosystem Clarity

One place to see how Supremepower and Cursor tie to other ecosystems (Qwen, Codex, Gemini) and when to use which workflow or skill.

## The map (cross-ecosystem)

**Canonical reference (Cursor):** `~/.cursor/qwen-ecosystem-map.md` — consult when porting or when referring to .qwen / .gemini / iterm2/Codex paths. From Gemini you may not have direct file access; the map documents Qwen Superpowers → Cursor ports, Gemini/Codex agents, plugin-like equivalents.

**This environment (Supremepower):** Custom skills in `~/.supremepower/skills/` (generated from Cursor-enhanced superpowers); custom agents in `~/.supremepower/agents/`. Load skills via the extension.

## Superpowers-style workflow (same everywhere)

**Flow:** brainstorm → writing-plans → executing-plans or subagent-driven-development → finishing-a-development-branch; code review (requesting/receiving-code-review); systematic-debugging before fixes; verification-before-completion before done; dispatching-parallel-agents for 2+ independent tasks; writing-skills for authoring skills.

**Cursor:** Skills under `~/.cursor/skills/` (including superpowers subtree). **Supremepower:** Skills under `~/.supremepower/skills/` (generated from that enhanced set). Same methodology; different load mechanism (Cursor reads files, Gemini uses extension).

## When to use which (Cursor; reference from Gemini)

| Need | In Cursor | In Supremepower |
|------|-----------|-----------------|
| Create a skill | create-skill, cursor-config-content-workflow | writing-skills (TDD for skills); new skills can be added to ~/.supremepower/skills and regenerated from Cursor source |
| Workflow / where things live | cursor-workflow-bootstrap, ecosystem-clarity | workflow-bootstrap, this skill |
| Narrative/persuasive docs | narrative-blueprints | Same concept (concept + monetization + workflow) |
| Cleanup duplicates/backups | managing-ecosystem-cleanup | Same principle (audit → propose → execute with manifest) |

## Cleanup

When context or disk is bloated by duplicate plugins, backup skills, or multiple versions: audit first, propose removals with impact, execute only with a manifest for restore. Never delete without a restore path. Cursor skill: **managing-ecosystem-cleanup**.

When in doubt, open the map (if available) and the skill or agent that best matches the task.
