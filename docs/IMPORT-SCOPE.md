# Import scope

Source reviewed: `/Users/steven/.agent-skills`  
Import date: 2026-08-18

## Included

- `agents/`: reusable agent definitions and public agent guidance
- `skills/`: reusable skills, references, scripts, templates, assets, and
  host-format metadata bundled with those skills
- `docs/inventories/`: the Codex Apps capability inventory
- `catalog/capability-authority.schema.json`: the public registry schema
- repository governance and research documentation

## Excluded

- credentials, environment files, auth material, tokens, and secrets
- histories, sessions, memory stores, databases, and private exports
- backups, caches, dormant archives, ZIP archives, and generated raw indexes
- machine-specific audit JSON and local projection snapshots
- private Deeptutor documentation
- API-key reference material
- external symlinks and symlinked project content
- Python bytecode and other generated build artifacts

## Validation

- 327 `SKILL.md` files imported
- 221 agent Markdown files imported
- 0 skill metadata failures in the imported set
- 0 TOML parse failures
- no detected live bearer-token, AWS access-key, or private-key patterns
- no remaining symlinks in the imported source tree

The imported source retains inherited formatting issues such as trailing
whitespace in some upstream/local files. Those are intentionally not silently
rewritten during the initial publication because formatting changes would make
provenance review harder. They can be addressed in a separate normalization
commit.

