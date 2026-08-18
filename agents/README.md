# Agents — ~/.agent-skills/agents/

**241 agent files · 11 subdirectory packs · ~100 root-level agents · Documented August 6, 2026**

Agent definition files for specialist AI personas. Each `.md` file defines a specialist with a system prompt, tool list, and triggering description. The harness routes tasks to agents based on description match and keyword triggers.

---

## How Agents Work

### Invocation
Via the `Agent` tool. The `description` field in each agent's frontmatter is what the harness uses for routing. Named invocation also works.

### Agent File Format

```markdown
---
name: agent-name
description: When to use this agent. Trigger keywords and use conditions.
tools: [Read, Write, Bash, ...]  # or "All tools"
---

[System prompt — persona, capabilities, behaviors]
```

### Agent vs. Skill

- **Skills** teach Claude HOW to do a specific type of work (process/methodology)
- **Agents** ARE a specific specialist persona (identity/capability set)
- Skills are invoked before responding; agents are spawned for multi-step or parallel work

---

## Root-Level Agents: Quick Index

### Creative & Content
`ai-music-video-creator` · `ai-xeo` · `bots` · `brand-guardian` · `content-creator` · `content-organizer` · `instagram-curator` · `tiktok-strategist` · `twitter-engager` · `reddit-community-builder` · `visual-storyteller` · `whimsy-injector`

### Engineering & Architecture
`api-specialist` · `backend-architect` · `database-specialist` · `devops-automator` · `devops-engineer` · `frontend-architect` · `frontend-developer` · `javascript-expert` · `mobile-app-builder` · `performance-benchmarker` · `performance-engineer` · `python-expert` · `security-engineer` · `system-architect` · `system-analyzer` · `technical-writer` · `testing-specialist`

### AI & Ecosystem
`agent-creation-guidance` · `ai-engineer` · `ai-workflow-manager` · `capability-atlas` · `conversation-analyzer` · `ecosystem-analyzer` · `ecosystem-dev` · `ecosystem-learning` · `ecosystem-synergy` · `innate-memory-agent` · `integrated-evolution` · `self-evolution`

### Product & Business
`analytics-reporter` · `app-store-optimizer` · `experiment-tracker` · `feedback-synthesizer` · `finance-tracker` · `growth-hacker` · `knowledge-automation-strategist` · `legal-compliance-checker` · `project-launch-manager` · `project-shipper` · `rapid-prototyper` · `revenue-optimizer` · `sprint-prioritizer` · `xeo-strategist`

### Research & Knowledge
`knowledge-fetcher` · `notebooklm-enhancement-advisor` · `seo-keyword-analyst` · `tool-evaluator` · `trend-researcher`

### Operations & Support
`context-fetcher` · `context-handoff-compiler` · `context-management` · `date-checker` · `documentation-management` · `documentation-manager` · `file-creator` · `filesystem-inventory` · `git-workflow` · `infrastructure-maintainer` · `path-list-analyzer` · `support-responder` · `task-management` · `tree-explorer` · `workflow-optimizer` · `workflow-orchestrator`

### Steven-Specific
`avatararts-organizer` · `iterm2-ecosystem-dev` · `ice-tracker-assistant` · `sorty`

### Studio Coordination
`studio-coach` · `studio-producer`

### Lightweight / Utility
`ask` · `joker` · `plan` · `review`

---

## Subdirectory Packs

| Pack | Agents | Purpose |
|---|---|---|
| `1-eng-specialist-pack/` | 11 | Curated engineering specialists (api, db, devops, frontend, js, perf, python, security, sys-arch, technical-writer, testing) |
| `2-personal-tooled/` | varies | Personal agents with tool specialization |
| `3-contains-studio/` | varies | Studio and creative coordination agents |
| `5-misc-personal/` | varies | Miscellaneous personal agents |
| `commands/` | 3 | Slash-command agents: `export`, `hooks-create`, `hooks-status` |
| `deep-learning/` | varies | ML/DL specialist agents |
| `documentation/` | varies | Documentation specialist agents |
| `gemini-roles/` | varies | Gemini CLI role definitions |
| `skill-creator/` | full subsystem | Skill creation: agents + assets + references + scripts |
| `skill-installer/` | full subsystem | Skill installation: agents + scripts |
| `skill-porter/` | conversion | Skill format conversion with before/after examples |

---

## Special Files

| File | Purpose |
|---|---|
| `AGENT_PATTERN_GUIDE.md` | Reference guide for agent patterns; use when creating or combining agents |
| `MANIFEST.csv` | Master agent manifest |
| `enriched-agents.csv` | Enriched catalog with AI-generated descriptions |
| `cleanup-manifest.csv` | Agent cleanup operations manifest |
| `openai.yaml` | OpenAI agent configuration |

---

## Full Catalog

See [`../docs/AGENTS-CATALOG.md`](../docs/AGENTS-CATALOG.md) for the complete agent-by-agent reference with roles, pack contents, and subsystem details.
