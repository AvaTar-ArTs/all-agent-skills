# Skills — ~/.agent-skills/skills/

**936 files · ~99 skill directories · Documented August 6, 2026**

Skills are the primary capability units of this ecosystem. Each skill is a self-contained directory that teaches an AI agent how to do a specific type of work — with instructions, references, scripts, and optional sub-agents.

---

## How Skills Work

### Invocation
In Claude Code: `Skill` tool with the skill name  
In Codex: `Skill` tool  
In Gemini CLI: `activate_skill` tool  
In Cursor: `/skills:name` or extension UI  

### Structure Contract

```
skill-name/
├── SKILL.md          ← Required: frontmatter + instructions
├── assets/           ← Optional: icons, images
├── references/       ← Optional: supporting docs, API specs, platform translations
├── scripts/          ← Optional: Python, JS, shell scripts
└── agents/           ← Optional: sub-agent definitions
```

### Key Principle: Use Before Responding

Per `using-superpowers`: check for an applicable skill before ANY response or action. Even a 1% chance a skill applies = invoke it.

---

## Quick Index by Category

### Entry Points (Start Here)
- `using-superpowers` — session entry, skill-check contract
- `innate-workflow` — session rhythm: audit → skills → execute → memory
- `brainstorming` — HARD-GATE: no code until design is approved
- `workflow-bootstrap` — mandatory workflow definitions

### Agent & Skill Development
`agent-creation-guidance` · `agent-development` · `automation-recommender` · `brainstorm` · `capability-atlas` · `command-development` · `dispatching-parallel-agents` · `skill-creator` · `skill-development` · `skill-installer`

### MCP & Plugin
`build-mcp-app` · `build-mcp-server` · `build-mcpb` · `hook-development` · `mcp-app-development-principles` · `mcp-integration` · `plugin-settings` · `plugin-structure`

### Code Quality
`code-review` · `devtu-fix-tool` · `devtu-optimize-descriptions` · `devtu-optimize-skills` · `frontend-ux-modernizer` · `git-ai-assistant` · `git-ai-cursor-integration` · `receiving-code-review` · `verification-before-completion`

### Implementation Pipeline
`executing-plans` → `verification-before-completion` → `finishing-a-development-branch`

### Frontend & Design
`design-taste-frontend` · `dogfood` · `frontend-design` · `taste-skill`

### Documentation & Narrative
`claude-md-improver` · `narrative-blueprints` · `narrative-documentation`

### Ecosystem & Memory
`agmsg` · `cross-tool-memory` · `ecosystem-clarity` · `ecosystem-intelligence` · `ecosystem-navigation` · `managing-ecosystem-cleanup` · `self-evolving-memory` · `self-improvement` · `workspace-ecosystem-audit`

### Research & Knowledge
`deep-research` · `find-docs` · `research/*` · `setup-tooluniverse` · `tooluniverse`

### Communication & Access Control
`discord-access` · `discord-configure` · `imessage-access` · `imessage-configure` · `telegram-access` · `telegram-configure`

### Apple & macOS
`apple` · `cua-driver` · `eza-nav`

### Session & Export
`agmsg` · `chat-history-export` · `session-export` · `session-report`

### Sub-Libraries (Click Into Subdirectory for README)
- `creative/` — 20 sub-skills (comfyui, baoyu-comic, songwriting-and-ai-music, p5js, ...)
- `deep-learning/` — 9 sub-skills (model-training-workflow, pytorch-debugging, ...)
- `mlops/` — 10 sub-skills (vllm, audiocraft, dspy, vector-databases, ...)
- `productivity/` — 9 sub-skills (notion, airtable, google-workspace, ...)
- `software-development/` — 11 sub-skills (TDD, systematic-debugging, writing-plans, ...)
- `github/` — 6 sub-skills (github-pr-workflow, github-issues, ...)
- `autonomous-ai-agents/` — 5 sub-skills
- `research/` — 5 sub-skills (arxiv, blogwatcher, polymarket, ...)
- `gaming/` · `red-teaming/` · `smart-home/` · `social-media/` · `email/` · `media/` · `devops/`

---

## Full Catalog

See [`../docs/SKILLS-CATALOG.md`](../docs/SKILLS-CATALOG.md) for the complete skill-by-skill reference with purposes, structures, and notes.

---

## Dormant Archives

`dormant_archives/` contains 7 ZIP files of retired skills. They are preserved but not active. To restore: unzip into `skills/`, verify SKILL.md, test invocation.

---

## Special Files

| File | Purpose |
|---|---|
| `.system/` | Platform-managed system skills — do not edit |
| `checkpoint.skill` | Ecosystem checkpoint marker |
| `VERSIONING_NOTES.md` | Skill versioning conventions |
| `enriched-skills.csv` | Full enriched skills catalog (AI-generated descriptions) |
| `docs-06-21-12:37.csv` | Catalog snapshot June 21 |
