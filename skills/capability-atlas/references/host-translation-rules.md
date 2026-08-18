# Host Translation Rules

## Keep Stable

- behavior contract
- trigger meaning
- input and output semantics
- verification method
- canonical mapping notes

## Allow To Change

- file names
- directory layout
- wrapper scripts
- packaging format
- host-specific terminology

## Preferred Renderings

| Need | Preferred form |
|---|---|
| Procedural workflow | Skill |
| Autonomous role | Agent |
| Event-bound action | Hook |
| Explicit action | Command |
| Deterministic automation | Script |
| Bundled delivery | Plugin or extension |
| Governance and proof | Doc, plan, or test |

## Translation Check

Before promoting a translation, confirm:

1. The same user intent triggers the capability.
2. The same behavior is produced or an intentional delta is documented.
3. Tests or prompts prove parity.
4. The host-specific wrapper does not silently change the meaning.

