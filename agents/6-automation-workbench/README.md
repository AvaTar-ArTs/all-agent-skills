# Automation Workbench Agents

This is an additive agent pack for turning exported conversations, Seller OS material, MCP designs, automation workflows, and visual proof assets into traceable deliverables.

## How discovery works

The agent harness scans Markdown agent definitions beneath `~/.agent-skills/agents/`. The directory name is organizational; routing is based on each file's YAML `description`. Named invocation is also supported.

These agents do not run merely because the folder exists. Use an explicit name when precision matters, or describe the task using the trigger language below.

## Agent routing map

| Agent | Use when | Primary output |
|---|---|---|
| `export-knowledge-curator` | HTML, JSON, ZIP, Markdown, or image exports need structured, source-traceable analysis | Source register, capability map, evidence ledger |
| `automation-offer-architect` | Technical notes need to become a bounded service or product offer | Offer scope, delivery workflow, acceptance criteria |
| `preview-first-operator` | A workflow may change files, plugins, skills, hooks, or other state | Backup, dry run, approval gate, validation, changelog |
| `host-portability-architect` | One workflow must work across agent hosts or packaging formats | Capability matrix, host adapters, parity tests |
| `proof-asset-strategist` | Screenshots, diagrams, videos, or outputs need to support a credible offer | Asset-to-claim matrix, demo sequence, proof checklist |

## Suggested sequences

### Export to knowledge

`export-knowledge-curator → capability-atlas skill → narrative-documentation skill`

### Technical capability to service offer

`export-knowledge-curator → automation-offer-architect → project-launch-manager`

### Any state-changing maintenance

`preview-first-operator → specialist agent → quality-regression-testing skill`

### Cross-host translation

`host-portability-architect → capability-atlas skill → skill-development skill`

### Buyer-facing proof

`proof-asset-strategist → design-md skill → product-launch-video skill`

## Safety contract

- Existing sources remain authoritative and are not deleted by default.
- Proposed changes should be previewed before execution.
- Historical claims are separated from current claims requiring verification.
- Prototype, planned, and production-ready capabilities must remain distinct.
- Every approved modification should have an append-only changelog.

## Change log

- 2026-08-15: Added the automation-workbench agent pack and this routing guide.
