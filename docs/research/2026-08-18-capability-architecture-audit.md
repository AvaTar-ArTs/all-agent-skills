# Capability Architecture Audit

Date: 2026-08-18  
Scope: local `~` capability roots, `~/.agent-skills`, `~/.codex`, host
projections, and Codex Apps/MCP exposure  
Method: primary-documentation research plus read-only local inspection

## Executive conclusion

The recommended architecture is a canonical source plus generated host
projections. The full local library should not be treated as one runtime
context, and home-wide discovery should not be treated as an active registry.

The local evidence supports four separate controls:

1. capability identity and provenance;
2. lifecycle classification;
3. projection and lock-file health;
4. runtime and external-action policy.

## Primary-source findings

OpenAI's current Codex skill guidance defines a skill as a directory with a
required `SKILL.md`, YAML `name` and `description`, and optional `agents/`,
`scripts/`, `references/`, and `assets/` directories. The loader uses the
frontmatter for discovery and loads the body after triggering. It also defines
limits for names, descriptions, scan depth, and skill directories.

Sources:

- <https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md>
- <https://github.com/openai/codex/blob/main/codex-rs/core-skills/src/loader.rs>
- <https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md>
- <https://github.com/openai/codex/blob/main/docs/agents_md.md>

OpenAI's plugin guidance distinguishes skills from apps and MCP-backed actions.
It recommends reviewing authentication, exposed tools, write behavior,
permissions, and keeping initial app access read-only where possible.

- <https://help.openai.com/en/articles/20001256-plugins-in-codex/>

Anthropic documents MCP as an external tool/data integration surface and
documents explicit tool allow/deny controls for Claude Code.

- <https://docs.anthropic.com/en/docs/mcp>
- <https://docs.anthropic.com/en/docs/claude-code/cli-usage>

## Local evidence

The canonical local source is:

```text
/Users/steven/.agent-skills
```

The local skills scan found approximately 330 parsed `SKILL.md` files. They
currently pass the observed Codex loader constraints:

- no missing frontmatter;
- no missing `name` or `description`;
- no names over 64 characters;
- no descriptions over 1,024 characters;
- no skills beyond the tested scan depth.

The local skills tree does contain 22 duplicate declared names, including
system/local or category-specific variants of `skill-creator`, `skill-installer`,
`codex`, `claude-code`, `codebase-inspection`, `notion`,
`test-driven-development`, and `writing-plans`.

The local lock file contains 25 entries, including six unresolved paths and
multiple content-hash mismatches. It should not be treated as authoritative
until provenance and path reconciliation are complete.

The active Codex projection is substantially smaller than the canonical
library. It contains system skills, a small local set, and curated symlinks
back to the canonical source. That projection model is appropriate for a lean
runtime.

The Codex Apps surface exposes 1,416 tool schemas across 82 connector
families. This is a separate authority plane from local skills and agents. It
includes read, write, account, financial, deployment, secret, permission, and
destructive capabilities.

## Correct context interpretation

The number of local skill bodies is not itself equal to startup context cost.
The documented loader uses metadata for discovery and loads bodies after
triggering. Context reduction should therefore focus first on:

- duplicate or ambiguous discovery names;
- unnecessarily long descriptions;
- duplicate projections and plugin metadata;
- broad MCP/app schemas;
- automatically injected agents or skills;
- repeated policy text across `AGENTS.md`, agents, and skills.

Progressive disclosure remains useful for triggered-task context, maintenance,
and reliability, but large bodies should not be classified as startup defects
without runtime measurement.

## Governance model

Every capability should have one canonical record with:

- stable ID;
- kind: skill, agent, command, hook, plugin, or app;
- canonical path;
- content hash;
- provenance and source repository;
- lifecycle status;
- host projections;
- risk tier;
- aliases and replacement relationships;
- last verification timestamp.

Suggested lifecycle values:

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

Suggested action tiers:

```text
read-local
local-write
external-read
external-write
account-sensitive
financial
destructive
```

## Security boundary

The home audit found credential-bearing and history-bearing locations that
must not enter public indexes. MCP configuration also requires separate
credential review. Authorization values must never be committed to this
repository; rotate exposed credentials before publishing configuration-derived
reports.

The repository excludes environment files, credentials, tokens, auth files,
histories, sessions, memory stores, databases, backups, caches, and archives
by default. These exclusions are defense-in-depth, not a substitute for
reviewing staged files.

## Import policy

Do not bulk-copy the entire home capability tree. Import in separate reviewed
sets:

1. public upstream skills with source and license metadata;
2. user-authored reusable skills explicitly approved for publication;
3. agents after host portability and tool-policy review;
4. generated catalogs only after deterministic generation is implemented.

Every import should pass frontmatter validation, duplicate-ID detection,
secret-path exclusion, license/provenance recording, and a staged-file review.

## Research-backed next step

The next implementation should be a deterministic authority/index generator,
not a broad content migration. It should produce active, projected,
project-local, archived, cached, and system indexes from one registry and
validate lock files and projections against the same source.

