# Cline Tool Mapping

Every Claude Code tool reference in a skill can be mapped to Cline's equivalent.
Use this when adapting skills from `obra/superpowers` or any Claude Code-native skill.

## Claude Code → Cline

| Claude Code | Cline | Notes |
|-------------|-------|-------|
| `Read` | `read_files` | Path-based, supports line ranges |
| `Write` | `editor` with `new_text` | Creates file if missing |
| `Edit` | `editor` with `old_text`→`new_text` | Exact-match replacement |
| `Bash` | `run_commands` | Array of shell commands |
| `Grep` | `search_codebase` | Regex pattern search |
| `Glob` | `search_codebase` or `run_commands` with `find` | File pattern matching |
| `Task` (subagent) | `spawn_agent` or `team_spawn_teammate` | Cline has richer team system |
| `Skill` | `skills` | Same concept, native |
| `WebFetch` | `fetch_web_content` | URL + analysis prompt |
| `WebSearch` | `fetch_web_content` | Same approach |
| `TodoWrite` | Structured markdown checklists | `- [ ]` format inline |
| `LS` | `run_commands` with `eza -la` | Directory listing |
| `mcp__*` | MCP tools via Cline MCP | Same protocol |

## Gemini → Cline

| Gemini | Cline |
|--------|-------|
| `read_file` | `read_files` |
| `write_file` | `editor` |
| `search_codebase` | `search_codebase` |
| `run_command` | `run_commands` |

## Codex → Cline

| Codex | Cline |
|-------|-------|
| `read` / `write` / `edit` | `read_files` / `editor` |
| `glob` / `grep` | `search_codebase` |
| `bash` | `run_commands` |
| `web_fetch` / `web_search` | `fetch_web_content` |
| `superpowers-codex` | `skills` tool |

## Path conventions

| Claude/Generic | Cline |
|---------------|-------|
| `~/.claude/` | `~/.cline/` |
| `.claude-plugin/` | `~/.cline/skills/` |
| `CLAUDE.md` | `CLINE.md` |
| `/skills:name` | `skills` tool with `skill: name` |
| `docs/plans/` | `docs/plans/` (same) |
| `git worktree` | `git worktree` (same) |

## Adaptation rules

When adapting a skill for Cline:

1. **Tool names** — Swap Claude names for Cline equivalents using this table
2. **Paths** — `~/.claude` → `~/.cline`, `CLAUDE.md` → `CLINE.md`
3. **Subagents** — `Task` tool → `spawn_agent` with `systemPrompt` + `task`
4. **Teams** — Cline has `team_*` tools for multi-agent orchestration (use where Claude would spawn multiple Tasks)
5. **Methodology** — The skill's process is the valuable part. Tool names are just plumbing.
