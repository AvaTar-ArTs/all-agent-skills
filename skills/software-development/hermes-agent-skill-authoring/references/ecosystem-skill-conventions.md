# Skill Conventions Across Ecosystems

Observed 2026-05-15 while analyzing `~/.agent-skills/` and `~/.cline/` as reference points for hermes-agent skill authoring.

## .agent-skills (Canonical Authoring Surface)

- **76 SKILL.md files**, 500B–22K chars each
- Frontmatter: `name` + `description` always. Sometimes `version`, `author`, `license`, `metadata.hermes.{tags, related_skills}`
- Description format: "Use when [trigger conditions]" — never summarize workflow
- Structure: `# Title` → `## Overview` → `## When to Use` → body → `## Common Pitfalls` → `## Verification Checklist`
- Rich body: flowcharts, rationalization tables, `<SUBAGENT-STOP>` directives, cross-skill references
- Disabled skills live in `skills/disabled/`

## .cline (Runtime Consumer, 3 days old)

- **3 SKILL.md files**, 500–1700 chars each
- Same YAML frontmatter pattern (`name` + `description`)
- Much more compact — checklist-style, minimal prose
- `chat-history-export` skill has **no YAML frontmatter** — raw markdown
- Structure: `# Title` → `## When to Use` → `## How to Use` → command blocks
- No version/author/license/metadata blocks

## Key Differences vs Hermes-Agent

| Aspect | .agent-skills | .cline | hermes-agent |
|--------|-----------------|--------|-------------|
| Skill count | 76 | 3 | varies |
| Size range | 500B–22K | 500–1700 | 8–14K target |
| Frontmatter | name+description (+optional) | name+description | name+description+version+author+license+metadata |
| Structure | Full 6-section | Sparse 3-section | 5-section minimum |
| Peer cross-refs | `metadata.hermes.related_skills` | None | `metadata.hermes.related_skills` |
| Disabled handling | `skills/disabled/` | N/A | N/A |

## ~/Guides (Cross-Platform Documentation Hub, 1.4GB)

Not a runtime surface — acts as the "librarian" for a multi-agent home directory. Key patterns:

- **Path inventories with taxonomy**: 203 paths classified by 12 buckets (first-party ecosystems, vendor SDK noise, ephemeral caches, false positives) — see `_agent_paths_inventory.txt` + `AGENT_ECOSYSTEM_INDEX_AND_REVIEW.md`
- **Dotfolder catalog**: 302 dotfolders tagged as A (agents/skills/rules), M (MCP/telemetry), I (third-party IDE), D (dev toolchain), O (OS), P (personal projects) — see `AGENT_DOTFILES_AND_DOTFOLDERS.md`
- **Unified ecosystem documents**: `Ecosystem-Unified-Organization-2026-05-15.md` — 3-layer architecture (Hooks Engine → Cognitive Polymath Mesh → Control Plane) with assets tallied across 5+ platforms
- **9-volume Book of Memory**: Mirrors `.agent-skills/book_of_memory/` — Platforms, Agents, Skills, Business, Cognition, Tools, Memory, Patterns, Implementation

### MULTI_AGENT_HYGIENE — The Cross-Contamination Problem

Diagnosed 2026-05-15 in `MULTI_AGENT_HYGIENE.md`. Core discovery:

6 AI agents in one `$HOME` cross-contaminate because every agent makes three wrong assumptions:
1. "I'm the only agent here" — searches `$HOME` recursively, finds everything
2. "Generic filenames are mine" — `SKILL.md`, `CLAUDE.md`, `agents/`, `rules/` used by every agent
3. "Content was written for me" — loads a file and assumes tool names, paths, conventions match

Confirmed case: Cline loaded `using-superpowers` from `~/.gemini/extensions/supremepower/skills/` — a Gemini extension directory. The skill referenced Claude Code tools (`Task`, `WebFetch`, `Bash`) that Cline doesn't have.

The fix has three layers:
1. **Scoping**: Each agent loads only from its own directory
2. **Adaptation pipeline**: `adapt-skill.py` with 31 phrase transformations (Claude Code → Cline, etc.)
3. **Isolation rules**: Never copy a SKILL.md between agent directories without adaptation

### Relevant Architecture Patterns

- **Walkthrough pattern**: Phase template (0-7) for reproducible project how-tos — Prerequisites → Enter project → Env → Install → Secrets → Run → Verify
- **Horizontal vs Vertical taxonomy**: "Horizontal" = persona orchestrators (SupremePower-style); "Vertical" = product pipeline code (DeepTutor `deeptutor/agents/`)
- **Reference ledger convention**: Fenced `+` and `-` blocks for canonical path aliases

## Takeaway for Porting

When adapting a .agent-skills skill to hermes-agent:
1. Add `version`, `author`, `license`, `metadata.hermes.{tags, related_skills}` frontmatter
2. Expand to hermes-agent's expected structure (Overview → When to Use → body → Pitfalls → Verification)
3. Target 8–14K chars; push heavy reference to `references/`
4. Convert `<SUBAGENT-STOP>` directives to platform-appropriate equivalents
5. Replace `superpowers:skill-name` cross-references with hermes-agent skill names
