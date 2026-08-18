---
name: ecosystem-layering
description: Use when managing multiple AI coding agents (Codex, Cursor, Codex, Cline, Copilot, Gemini CLI, etc.) that share a home directory — to prevent cross-contamination, skill conflicts, and tool-name mismatches by layering canonical sources, runtime surfaces, and documentation hubs.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ecosystem, governance, multi-agent, adaptation, hygiene, layering]
    related_skills: [hermes-agent, hermes-agent-skill-authoring]
---

# Ecosystem Layering

## Overview

If you run more than one AI coding agent on your machine, they will silently contaminate each other. Every agent recursively searches `$HOME` for files named `SKILL.md`, `AGENTS.md`, `AGENTS.md`, and loads whatever it finds first — regardless of which agent it was written for. This skill teaches a three-layer governance pattern that prevents cross-contamination while keeping all agents functional.

The pattern separates concerns into three planes: **canonical** (source of truth, write here), **runtime** (what each agent loads, scoped to its directory), and **librarian** (cross-platform documentation, maps relationships). Between canonical and runtime sits an **adaptation pipeline** that translates tool names, paths, and conventions so each agent gets content written for its own toolset.

## When to Use

- You have 2+ AI coding agents installed (any combination of Codex, Cursor, Codex, Cline, GitHub Copilot, Gemini CLI, Qwen, Windsurf, Codeium, etc.)
- An agent loaded a skill and referenced tools it doesn't have (Codex skill loaded by Cursor, etc.)
- You're setting up a new agent and don't want it loading skills from other agents
- Skills or agents appear to work but produce wrong results because they're using another platform's tool names
- You're building a skill ecosystem and want it to work across multiple platforms
- You're seeing "unknown tool" errors from skills that work fine in another agent

Don't use for:
- Single-agent setups — the problem doesn't exist
- Purely containerized/isolated agents that don't share `$HOME`
- Teams where each developer uses exactly one platform

## The Three-Plane Model

Every healthy multi-agent ecosystem separates into three planes. Each has a distinct role and a distinct edit rule.

```
┌─────────────────────────────────────────────┐
│  CANONICAL PLANE  (Write here first)         │
│  ~/.agent-skills/, ~/.hermes/skills/      │
│  Source of truth for skills, agents, rules   │
│  EDIT: Always                                 │
└──────────────┬──────────────────────────────┘
               │  adapt-skill.py / manual
               ▼
┌─────────────────────────────────────────────┐
│  RUNTIME PLANES  (Scoped per agent)          │
│  ~/.cline/skills/, ~/.codex/skills/, ...     │
│  Each agent loads ONLY from its own dir      │
│  EDIT: Never directly — adapt from canonical  │
└─────────────────────────────────────────────┘
               │
┌──────────────┴──────────────────────────────┐
│  LIBRARIAN PLANE  (Maps everything)          │
│  ~/Guides/, docs/ECOSYSTEM_MAP.md            │
│  Cross-platform docs, path inventories       │
│  EDIT: Append, don't overwrite               │
└─────────────────────────────────────────────┘
```

### Plane Roles

| Plane | Purpose | Edit Rule | Example Paths |
|-------|---------|-----------|---------------|
| **Canonical** | Single source of truth for behaviors | Always edit here; changes flow downstream | `~/.agent-skills/skills/`, `~/.hermes/skills/` |
| **Runtime** | What each agent actually loads | Never edit directly; adapt from canonical | `~/.cline/skills/`, `~/.codex/skills/`, `~/.cursor/skills/` |
| **Librarian** | Cross-platform maps, inventories, analysis | Append; treat as documentation, not runtime | `~/Guides/`, `docs/ECOSYSTEM_MAP.md` |

### The Golden Rule

**Canonical writes, runtime reads, librarian maps.** If you fix a bug in `~/.cline/skills/brainstorming/SKILL.md` directly, it will be overwritten the next time someone adapts from canonical. Always fix in canonical, then re-adapt.

## The Cross-Contamination Problem

Every AI coding agent makes three assumptions — all wrong in a multi-agent home directory:

1. **"I'm the only agent here"** — Recursively searches `$HOME`, finds every `SKILL.md`, `AGENTS.md`, `agents/` directory
2. **"Generic filenames are mine"** — `SKILL.md` means different things to Codex (expects `Task`/`Bash`/`WebFetch` tools) vs Cline (`spawn_agent`/`run_commands`/`fetch_web_content`)
3. **"Content was written for me"** — Loads a file and assumes tool names, paths, and conventions match its own

### Real Confirmed Case

Cline activated the `using-superpowers` skill and loaded it from `~/.gemini/extensions/supremepower/skills/` — a Gemini extension directory. The skill was written for Codex and referenced tools Cline doesn't have:

| Codex Tool (in skill) | Cline Tool (actual) |
|---|---|
| `Task` | `spawn_agent` |
| `WebFetch` | `fetch_web_content` |
| `Bash` | `run_commands` |
| `Read` / `Write` / `Edit` | `read_files` / `editor` |
| `Grep` / `Glob` | `search_codebase` |

Cline tried to use Codex tools it didn't have. This wasn't a crash — it was silent wrong behavior. The skill's instructions were followed with the wrong tools.

### Risk Surface by File Type

| File Pattern | Found In | Risk |
|---|---|---|
| `SKILL.md` | Every agent's `skills/` dir, extensions, caches | **Highest** — every agent loads skills |
| `AGENTS.md` / `CLINE.md` / `GEMINI.md` / `AGENTS.md` | Project roots, dotfolders | Auto-loaded as context on session start |
| `agents/` directory | Every dotfolder | Subagent definitions with platform-specific tool references |
| `rules/` directory | `.cursor/rules/`, `.codex/rules/`, `.qwen/rules/` | Behavioral constraints with platform syntax |
| `settings.json` / `config.toml` | Each dotfolder | MCP allow-lists, provider configs, permission models |

## The Adaptation Pipeline

When a skill must be shared across agents, run it through an adaptation pipeline instead of copying raw.

### The Pattern

```
canonical SKILL.md (written for Codex)
        │
        ▼
  adaptation script + tool-mapping tables
        │
        ▼
  platform-native SKILL.md in agent's scoped directory
```

### What Gets Transformed

A complete adaptation needs at minimum:

| Category | Codex (canonical) | Cline | Codex | Cursor | Copilot |
|---|---|---|---|---|---|
| File read | `Read` tool | `read_files` | `read_file` | `read_file` | `read_file` |
| File write | `Write` / `Edit` | `editor` | `write_file` / `patch` | `edit_file` | `edit_file` |
| Search | `Grep` / `Glob` | `search_codebase` | `search_files` | `grep_search` | `search` |
| Shell | `Bash` | `run_commands` | `terminal` | `run_in_terminal` | `execute_command` |
| Subagent | `Task` | `spawn_agent` | `delegate_task` | `spawn_task` | `task` |
| Web | `WebFetch` / `WebSearch` | `fetch_web_content` | `web_search` | `web_fetch` | `web_search` |
| Skill | `Skill` tool | `use_skill` | `skill` | `activate_skill` | `skill` |
| Context file | `AGENTS.md` | `CLINE.md` | `AGENTS.md` | `RULES.md` | `.github/copilot-instructions.md` |
| Settings dir | `~/.Codex/` | `~/.cline/` | `~/.codex/` | `~/.cursor/` | `~/.copilot/` |
| Memory file | `AGENTS.md` | `memory/MEMORY.md` | `memories/MEMORY.md` | `MEMORY.md` | — |

### Minimal Adaptation Script Template

```python
#!/usr/bin/env python3
"""Adapt a canonical SKILL.md to a target platform."""
import sys, re, pathlib

TOOL_MAP = {
    "Task": "delegate_task",
    "Bash": "terminal",
    "Read": "read_file",
    "Write": "write_file",
    "Edit": "patch",
    "Grep": "search_files",
    "Glob": "search_files",
    "WebFetch": "web_search",
    "WebSearch": "web_search",
    "Skill": "skill_view",
    "AGENTS.md": "AGENTS.md",
    "~/.Codex/": "~/.hermes/",
}

PATH_MAP = {
    "~/.Codex/skills/": "~/.hermes/skills/",
    "Codex": "Hermes Agent",
}

def adapt(content, tool_map, path_map):
    for old, new in tool_map.items():
        content = re.sub(rf'\b{re.escape(old)}\b', new, content)
    for old, new in path_map.items():
        content = content.replace(old, new)
    return content

if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2])
    content = src.read_text()
    adapted = adapt(content, TOOL_MAP, PATH_MAP)
    # Add adaptation banner
    adapted = f"<!-- Adapted from {src} for Hermes Agent -->\n{adapted}"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(adapted)
    print(f"Adapted {src} → {dst}")
```

## Practical Setup

### Step 1: Choose Your Canonical Surface

Pick ONE directory as source of truth. Options:

```bash
# Option A: Dedicated repo (recommended for shared ecosystems)
~/.agent-skills/skills/

# Option B: Hermes Agent's own skill tree (for hermes-centric setups)
~/.hermes/skills/

# Option C: Platform-native canonical (for single-platform users)
~/.Codex/skills/  # if Codex is your primary
```

Write ALL new skills here first. Never write directly into runtime directories.

### Step 2: Inventory What You Have

Before scoping agents, know what's on disk:

```bash
# Find every SKILL.md in home directory (excluding node_modules and caches)
find ~/ -name "SKILL.md" \
  -not -path "*/node_modules/*" \
  -not -path "*/.git/*" \
  -not -path "*/cache/*" \
  -not -path "*/__pycache__/*" \
  | sort > ~/skill-inventory.txt

# Count per source directory
cat ~/skill-inventory.txt | sed 's|/[^/]*$||' | sort | uniq -c | sort -rn

# Find every AGENTS.md / CLINE.md / AGENTS.md
find ~/ -maxdepth 3 \( -name "AGENTS.md" -o -name "CLINE.md" -o -name "AGENTS.md" -o -name "GEMINI.md" \) \
  -not -path "*/node_modules/*" \
  -not -path "*/.git/*" \
  | sort
```

### Step 3: Scope Each Runtime Agent

For each agent, ensure it loads ONLY from its own directory:

| Agent | Must load from | Must NOT load from |
|-------|---------------|-------------------|
| Hermes Agent | `~/.hermes/skills/` | `~/.Codex/skills/`, `~/.codex/skills/`, etc. |
| Codex | `~/.Codex/skills/` | `~/.gemini/extensions/`, `~/.hermes/skills/` |
| Codex | `~/.codex/skills/` | `~/.qwen/skills/`, `~/.cursor/skills/` |
| Cursor | `~/.cursor/skills/` | `~/.Codex/skills/`, `~/.cline/skills/` |
| Cline | `~/.cline/skills/` | `~/.gemini/extensions/`, `~/.qwen/skills/` |

### Step 4: Populate Runtime from Canonical via Adaptation

After writing a skill in canonical, adapt it to each runtime:

```bash
# Adapt canonical skill to Hermes Agent runtime
python scripts/adapt-skill.py \
  ~/.agent-skills/skills/brainstorming/SKILL.md \
  ~/.hermes/skills/software-development/brainstorming/SKILL.md

# Batch-adapt all skills
for skill in ~/.agent-skills/skills/*/SKILL.md; do
  name=$(basename $(dirname "$skill"))
  python scripts/adapt-skill.py "$skill" "~/.hermes/skills/$category/$name/SKILL.md"
done
```

### Step 5: Build the Librarian

Create a cross-platform documentation surface:

```bash
mkdir -p ~/Guides

# Inventory all platforms
cat > ~/Guides/ECOSYSTEM_MAP.md << 'EOF'
# Ecosystem Map

## Platforms
| Platform | Path | Size | Skills | Agents |
|----------|------|------|--------|--------|

## Adaptation Map
| Canonical Skill | Hermes Agent | Codex | Codex |
|-----------------|-------------|-------------|-------|

## Drift Log
| Date | File | Change | Platforms Updated |
|------|------|--------|-----------------|
EOF
```

## Isolation Rules (Cut Here and Post)

1. **Never copy a SKILL.md between agent directories without adaptation** — raw copies carry wrong tool names
2. **Each agent's context file stays in its own dotfolder** — `AGENTS.md` ≠ `CLINE.md` ≠ `GEMINI.md`
3. **Canonical is the only place you edit** — runtime directories are generated
4. **Before activating any skill, note which directory it loaded from** — if it's not your agent's directory, it's contamination
5. **If an agent loads from another agent's directory, stop and scope** — add the foreign directory to that agent's ignore list

## Common Pitfalls

1. **"This skill is simple, it doesn't need adaptation."** Every skill references tools. Even if it only has one reference, a wrong tool name causes silent failures. Always adapt.

2. **"I'll just fix it in the runtime copy."** The fix will be overwritten on next adaptation from canonical. Fix once in canonical; re-adapt everywhere.

3. **"My agents only load from their own directories — I'm safe."** Many agents' auto-discovery is not configurable. They search `$HOME` recursively by default. Verify with the inventory in Step 2.

4. **"I don't need a librarian — the skills are self-documenting."** Six months later, you won't remember which copy was canonical and which was a stale runtime mirror. The librarian is your map back.

5. **"I only have one agent now, so this is premature."** Agents accumulate. Set up the pattern before you need it. Retrofitting is 10x harder.

6. **"The tool names are close enough — the agent will figure it out."** Agents can't infer tool mappings. A skill referencing `Task` will fail in Hermes Agent because `Task` doesn't exist. The error won't be "unknown tool" — it will be wrong behavior from a skipped tool call.

7. **"I'll use symlinks to share skills between agents."** Symlinks share raw content without adaptation. A symlinked `SKILL.md` from `~/.Codex/skills/` into `~/.hermes/skills/` will deliver Codex tool names to Hermes Agent. This is worse than a copy because it looks clever.

## Verification Checklist

### After Setting Up a New Agent
- [ ] Agent loads skills ONLY from its own directory (check with Step 2 inventory)
- [ ] For each loaded skill: tool names match the agent's toolset (spot-check 3 skills)
- [ ] Context file is the right name for this agent (`CLINE.md` for Cline, `AGENTS.md` for Codex, etc.)
- [ ] No symlinks into other agents' directories

### After Adding a New Skill to Canonical
- [ ] Skill written to canonical (not directly into any runtime directory)
- [ ] Adapted to each target runtime with tool-name translation
- [ ] Each adaptation verified: a quick "use this skill" test on each platform
- [ ] Librarian updated: skill added to ecosystem map

### Monthly Maintenance
- [ ] Re-run the `find ~/ -name "SKILL.md"` inventory — new stray copies?
- [ ] Check for new `AGENTS.md` / `AGENTS.md` files outside their agent's directory
- [ ] Re-adapt all canonical skills to each runtime (catches canonical changes you forgot to propagate)
- [ ] Audit runtime directories for direct edits (compare with canonical via `diff -r`)

## One-Shot Recipes

### "I just got a new agent. How do I onboard it?"

```bash
# 1. Inventory what it can see
find ~/ -maxdepth 3 -name "SKILL.md" | head -30

# 2. Give it its own scoped skills directory
mkdir -p ~/.newagent/skills/

# 3. Adapt your top 3 most-used skills from canonical
python scripts/adapt-skill.py ~/canonical/skills/brainstorming/SKILL.md ~/.newagent/skills/brainstorming/SKILL.md
python scripts/adapt-skill.py ~/canonical/skills/debugging/SKILL.md ~/.newagent/skills/debugging/SKILL.md
python scripts/adapt-skill.py ~/canonical/skills/verification/SKILL.md ~/.newagent/skills/verification/SKILL.md

# 4. Verify tool names are correct
grep -E 'Task|Bash|Read|Write|WebFetch' ~/.newagent/skills/*/SKILL.md
# Should find NO matches — these are Codex tools
```

### "I found an agent loading from the wrong directory. What do I do?"

```bash
# 1. Identify which skill was loaded and from where
#    (Agent logs usually show the path)

# 2. Check if that directory has a scoped version
ls ~/.myagent/skills/

# 3. If no scoped version exists, adapt it now
python scripts/adapt-skill.py \
  /path/to/foreign/skill/SKILL.md \
  ~/.myagent/skills/adapted-skill/SKILL.md

# 4. Add foreign directory to agent's ignore/exclude list
#    (Platform-specific — check agent docs for exclude patterns)

# 5. Verify the agent now loads from its own directory
#    (Activate the skill again; check the load path in logs)
```

### "I need to audit my ecosystem for contamination risk."

```bash
# Full inventory
find ~/ -name "SKILL.md" \
  -not -path "*/node_modules/*" -not -path "*/.git/*" \
  -not -path "*/cache/*" -not -path "*/__pycache__/*" \
  -exec echo {} \; > /tmp/all-skills.txt

# Group by parent directory
while IFS= read -r path; do
  dir=$(dirname "$path")
  # What agent owns this directory?
  case "$dir" in
    */\.cline/*) echo "CLINE: $path" ;;
    */\.codex/*) echo "CODEX: $path" ;;
    */\.Codex/*) echo "Codex: $path" ;;
    */\.cursor/*) echo "CURSOR: $path" ;;
    */\.gemini/*) echo "GEMINI: $path" ;;
    */\.qwen/*) echo "QWEN: $path" ;;
    */\.hermes/*) echo "HERMES: $path" ;;
    */.agent-skills/*) echo "CANONICAL: $path" ;;
    *) echo "UNKNOWN: $path" ;;
  esac
done < /tmp/all-skills.txt | sort

# Red flag: any UNKNOWN paths, or any agent loading from another agent's directory
```

### "I want to set up the three-plane model from scratch."

```bash
# Plane 1: Canonical
mkdir -p ~/canonical/skills/
# Write all skills here

# Plane 2: Runtime (one per agent)
mkdir -p ~/.hermes/skills/
mkdir -p ~/.Codex/skills/     # if you use Codex
mkdir -p ~/.codex/skills/      # if you use Codex
# Populate via adaptation, never by hand

# Plane 3: Librarian
mkdir -p ~/Guides/
cat > ~/Guides/ECOSYSTEM_MAP.md << 'EOF'
# Ecosystem Map
## Platforms
## Adaptation Map
## Drift Log
EOF

# Create the adaptation script
cat > ~/scripts/adapt-skill.py << 'PYEOF'
# (Use the template from "The Adaptation Pipeline" section above)
PYEOF
chmod +x ~/scripts/adapt-skill.py

echo "Three-plane model initialized."
echo "1. Write skills in ~/canonical/skills/"
echo "2. Adapt to runtimes with ~/scripts/adapt-skill.py"
echo "3. Map everything in ~/Guides/ECOSYSTEM_MAP.md"
```
