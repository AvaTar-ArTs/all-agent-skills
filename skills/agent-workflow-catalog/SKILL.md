---
name: agent-workflow-catalog
description: Use when routing complex work through ordered skills and agents.
version: 0.1.0
author: Hermes
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [routing, agents, skills, workflows, evidence, approvals]
    related_skills: [using-superpowers, innate-workflow, capability-atlas]
---

# Agent Workflow Catalog

## Overview

Route a complex request before solving it. Select a goal-specific workflow, run its skills in order, add specialist agents as independent thinking lanes, gather evidence, state approval gates, and return a reviewable execution handoff.

This skill is a canonical routing procedure. It does not replace domain skills or specialist agents and does not authorize mutation, publication, credential use, payment, deletion, or external submission.

Detailed routes live in [references/workflows.md](references/workflows.md).

Canonical related capability:

- `ecosystem-layering` — `~/.agent-skills/skills/autonomous-ai-agents/ecosystem-layering/SKILL.md`

The portability route intentionally uses this skill to separate canonical sources, runtime adapters, and librarian documentation.

## When to Use

Use when a request spans multiple skills, agents, tools, artifacts, hosts, or approval boundaries, especially for:

- exported conversations and knowledge systems;
- Seller OS and Automation Offer Workbench work;
- visual assets, HyperFrames, or launch packages;
- cross-host skill and agent portability;
- multi-agent implementation or review;
- ecosystem audits and evidence ledgers.

Do not use this as a substitute for `systematic-debugging`, `test-driven-development`, or another rigid process skill when that skill directly governs the task.

## Prerequisites

- Canonical source: `~/.agent-skills/`.
- Hermes runtime, when applicable: `~/.hermes/`.
- A stated goal or a request that can be converted into one.
- Permission boundaries and destination artifacts identified.

## How to Run

1. Identify the user's real goal, not just the surface artifact.
2. Select the closest route from `references/workflows.md`.
3. Add process skills first, then domain skills.
4. Add specialist agents as independent review or execution lanes.
5. Gather source paths, requirements, current-state checks, and constraints.
6. State stop conditions before mutation.
7. Return the routing contract below.
8. If the user asks to proceed, execute only the approved route and verify outputs.

## Quick Reference

Primary routes:

- exports → `chat-history-export` → `research-source-intake` → `capability-atlas` → `narrative-documentation` → `chroma`
- Automation Offer Workbench → `content-strategy` → `domain-modeling` → `build-mcp-server` → `mcp-integration` → `quality-regression-testing` → `narrative-documentation`
- visual proof library → `structured-asset-pipeline` → `image-to-code` → `design-md` → `hyperframes` → `hyperframes-creative`
- safe automation → `automation-recommender` → `hook-development` → `quality-regression-testing` → `verification-before-completion`
- portability → `capability-atlas` → `ecosystem-layering` → `skill-development`
- implementation validation → `systematic-debugging` → `test-driven-development` → `quality-regression-testing` → `requesting-code-review`

Common agents:

- evidence and context: `filesystem-inventory`, `context-fetcher`, `knowledge-fetcher`
- documentation: `documentation-manager`, `technical-writer`
- ecosystem: `ecosystem-analyzer`, `ecosystem-learning`, `ecosystem-dev`
- delivery: `project-launch-manager`, `project-shipper`, `content-creator`
- review: `code-reviewer`, `testing-specialist`

## Routing Contract

```markdown
## Agent Workflow Route

Intent: <what the user is really trying to accomplish>
Goal: <one-sentence outcome>

Required skills:
1. <skill> — <why it comes first>
2. <skill> — <what it gates>

Specialist agents:
1. <agent> — <decision or inspection lane>
2. <agent> — <independent challenge>

Evidence to gather:
- <path, source, requirement, or check>

Execution order:
1. <step>
2. <step>
3. <step>

Approval gates:
- <mutation, credential, publication, or submission boundary>

Artifacts:
- <expected path or output>

Verification:
- <real command, test, or review>

Uncertainty and next action:
- <unknown or reversible next inquiry>
```

## Procedure

### 1. Identify the route

Choose the narrowest route that covers the goal. If no route fits, create a provisional route with an explicit `unknown` status rather than inventing a capability.

### 2. Separate method from persona

Skills define how work proceeds. Agents provide specialist perspectives. Do not add an agent merely because its name sounds relevant; state the decision or evidence lane it owns.

### 3. Separate historical from current evidence

For exported material, classify claims as historical, reusable principle, or requiring current verification. Do not turn old pricing, API, hosting, marketplace, or platform claims into current advice without fresh research.

### 4. Protect sources and boundaries

Preserve originals. Exclude secrets, auth, runtime databases, sessions, logs, caches, and vendor trees unless separately approved. Keep platform submission, payment, publishing, and credential actions manual by default.

### 5. Verify the handoff

A route is valid when the selected skill and agent names resolve, evidence sources are identifiable, approval gates are explicit, artifacts have destinations, and the verification command is real.

## Common Pitfalls

- Selecting agents before selecting process skills.
- Treating a file's existence as proof that a skill is active.
- Treating a historical export as current market evidence.
- Copying canonical skills into runtime trees without adaptation.
- Calling a summary a replacement for its source.
- Letting multiple agents edit the same files without isolation.
- Automating publication, credential entry, payment, or submission.
- Claiming completion without executing a verification step.

## Verification Checklist

- [ ] Goal and intended artifact are explicit.
- [ ] Ordered skills are real or clearly marked as aliases/pending adapters.
- [ ] Each agent has a named thinking or execution lane.
- [ ] Evidence sources and exclusions are listed.
- [ ] Approval gates are explicit.
- [ ] Artifacts have destinations.
- [ ] A real verification command or review exists.
- [ ] Uncertainty and next action are reported.
- [ ] Canonical/runtime lineage is preserved.
