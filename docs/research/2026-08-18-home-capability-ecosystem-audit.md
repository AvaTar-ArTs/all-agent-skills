# Home Capability Ecosystem Audit

Date: 2026-08-18  
Scope: home-level `skills`, `skill`, `agents`, and `agent` roots  
Method: existing home indexes plus fresh read-only filesystem inspection; no
private histories, credentials, or session contents were copied into this
repository

## Executive assessment

`~/.agent-skills` is the intended canonical reusable-capability source. The
home directory also contains host projections, package caches, backups,
project-local systems, generated catalogs, and historical copies. These must
be classified separately rather than treated as one runtime library.

The central problem is lifecycle and provenance management, not lack of
capability coverage.

## Home-wide snapshot

The existing home audit reported approximately:

| Measure | Approximate count |
|---|---:|
| Capability-related roots | 3,459 |
| Skill-like files | 7,789 |
| Agent-like Markdown files | 3,285 |
| Duplicate skill-name groups | 1,806 |
| Duplicate agent-name groups | 445 |
| Exact skill duplicate groups | 2,111 |
| Exact agent duplicate groups | 797 |

These are audit-snapshot figures, not a claim that all matching files are
active or removable. They include canonical files, projections, caches,
backups, project-local copies, examples, generated catalogs, and archives.
Re-run the scanner before making current-state decisions.

## Capability lifecycle model

The same capability can exist as:

```text
canonical source → host projection → plugin cache → backup →
project-local copy → generated catalog entry
```

Classify each discovered record as exactly one primary lifecycle state:

```text
active
projected
project-local
system
compatibility
experimental
archived
cached
```

Deduplicate only after comparing content hash, provenance, owner, source
repository, source commit, and lifecycle state. Filename equality is not
evidence of replacement equivalence.

## Primary source and projections

Canonical source:

```text
~/.agent-skills/
  agents/
  skills/
  catalog/
  docs/
  scripts/
  hooks/
```

Relevant host or compatibility surfaces include:

```text
~/.claude/skills
~/.claude/agents
~/.codex/skills
~/.codex/agents
~/.agents/skills
~/.gemini/skills
~/.cursor/skills
~/.qwen/skills
~/.opencode/skills
```

These should not become independent authoring sources. A projection may be a
symlink, generated copy, or package-managed cache, but its authority and
health must be recorded explicitly.

Backups and historical material, including dated agent-skills backups and
full-canonical snapshots, should remain recoverable but excluded from runtime
discovery.

## Runtime context interpretation

Disk size and model-context size are different measurements. The current
Codex loader uses skill frontmatter metadata for discovery and loads a skill
body after the skill triggers. Therefore, the most relevant context controls
are:

- duplicate or ambiguous discovery metadata;
- long skill descriptions;
- duplicate agent descriptions;
- plugin metadata;
- MCP and app schemas;
- automatically injected host surfaces;
- repeated instructions across `AGENTS.md`, agents, and skills.

Large skill bodies still merit progressive disclosure for triggered-task
context and maintainability, but their byte size alone is not proof of startup
context consumption.

Primary references:

- <https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md>
- <https://github.com/openai/codex/blob/main/codex-rs/core-skills/src/loader.rs>
- <https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md>
- <https://help.openai.com/en/articles/20001256-plugins-in-codex/>

## External app and MCP boundary

Codex Apps and MCP servers are separate from local skill and agent content.
They can expose external reads and writes, account operations, deployments,
secrets, permissions, financial actions, and destructive operations.

The Codex Apps audit recorded 1,416 tool schemas across 82 connector families.
That surface should be governed by connector/profile and action policy rather
than bundled into the default local skill projection.

Recommended action tiers:

```text
read-local
local-write
external-read
external-write
account-sensitive
financial
destructive
```

Default runtime access should be read-local or local-write. External writes,
financial actions, secret/permission changes, deployments, refunds, deletes,
and domain changes should require explicit approval.

## Lock and catalog authority

The authority registry should live at:

```text
~/.agent-skills/catalog/capability-authority.json
```

Each record should include:

```json
{
  "id": "codebase-inspection",
  "kind": "skill",
  "canonical_path": "skills/codebase-inspection/SKILL.md",
  "status": "active",
  "source": "local-authored",
  "sha256": "...",
  "host_projections": ["codex", "claude"],
  "project_local": false,
  "risk_tier": "read-local",
  "aliases": [],
  "replaced_by": null,
  "last_verified": "2026-08-18"
}
```

Generate lock files, catalogs, projection indexes, and health reports from
that registry. Do not maintain several independently authoritative locks.

## Home-wide indexing exclusions

Indexers must exclude content from:

```text
~/.env.d
~/.secrets
~/.ssh
~/.mcp-auth
~/.claude-code-history
~/.codex-history
~/.zsh_sessions
~/.claude/projects
~/.chatgpt
~/.engram
~/.remember
~/.specstory
```

Also exclude environment files, credential and auth files, keychains, session
databases, browser data, cookies, tokens, private keys, credential backups,
SQLite databases, and large caches. Reports should retain only redacted path
metadata and classification.

## GitHub reconciliation boundary

When local and remote repositories diverge, compare these independently:

1. local commits absent remotely;
2. remote commits absent locally;
3. uncommitted local changes;
4. generated catalogs;
5. projection-only changes.

Use a clean temporary worktree for reconciliation. Do not merge remote
catalogs directly into a dirty home source tree.

## Target architecture

```text
~/.agent-skills
  canonical source

~/.codex
~/.claude
~/.gemini
~/.cursor
~/.qwen
~/.opencode
  generated or compatibility projections

~/projects/*/.agents
  project-local capabilities

~/.agent-skills/catalog
  authority, hashes, provenance, lifecycle, projection health

backups and caches
  excluded from runtime discovery
```

## Research-backed implementation order

1. Rotate any credentials found in local MCP configuration before publishing
   configuration-derived material.
2. Establish the capability authority registry.
3. Validate projections and reconcile lock files against canonical sources.
4. Separate active, projected, project-local, archived, cached, system, and
   experimental indexes.
5. Keep default Codex skills and agents compact, with specialized capabilities
   available on demand.
6. Gate Codex Apps connector families and external actions by profile.
7. Classify duplicates by hash and provenance before consolidation.
8. Perform GitHub reconciliation only in a clean worktree.

## Related repository artifacts

- [Capability architecture audit](2026-08-18-capability-architecture-audit.md)
- [Import scope](../IMPORT-SCOPE.md)
- [Codex Apps inventory](../inventories/codex-apps-capability-inventory-2026-08-18.md)
- [Capability authority schema](../../catalog/capability-authority.schema.json)

