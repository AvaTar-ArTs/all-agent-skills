---
name: ralph-self-audit
description: Use before consequential actions, broad audits, generated artifacts, installations, or completion claims to challenge assumptions, locate evidence, confirm destinations and authorization, and run a bounded self-correction loop.
---

# Ralph Self-Audit

Run this as a bounded reasoning gate. It is a safety and deductiveness check, not permission to delay indefinitely.

## Trigger

Activate when any of these are true:

- The request is broad, ambiguous, or spans multiple ecosystems.
- A write, install, move, merge, deletion, or external action is contemplated.
- A report or artifact will be created for later use.
- The proposed destination is temporary, hidden, unindexed, or inferred.
- The evidence is incomplete, duplicated, stale, or based only on filenames.
- The response is about to claim completion, readiness, understanding, or “learned” capability.

## Bounded loop

Perform at most two passes. Stop early when the second pass adds no material correction.

### Pass 1 — RALPH

1. **Request** — Restate the concrete outcome and separate explicit instructions from assumptions.
2. **Authority** — Identify what actions are authorized, what is read-only, and what requires user confirmation.
3. **Locate evidence** — Inspect the canonical source, relevant skills/agents, existing indexes, and current state. Do not infer purpose from names alone.
4. **Place outputs** — Choose a durable, discoverable destination. `/tmp` is scratch-only unless explicitly requested.
5. **Hazards** — Check duplication, stale catalogs, scope creep, destructive effects, privacy, and false precision.

### Pass 2 — correction

Ask:

- What did I assume that the evidence does not establish?
- What competing explanation or duplicate source could change the conclusion?
- What important capability, dependency, or downstream use did I fail to inspect?
- Is the chosen output location indexed so another skill or agent can find and use it?
- What is the smallest verification that would falsify my conclusion?

Correct the plan or ask the user only if the unresolved ambiguity materially changes the action. Otherwise proceed with the safest reasonable assumption and state it.

## Durable artifact rule

For reports, inventories, roadmaps, audits, registries, or reusable logs:

1. Do not leave the final artifact only in `/tmp`.
2. Use the ecosystem’s canonical, discoverable area, normally `~/.agent-skills/docs/audits/<audit-name>/`.
3. Include a short `README.md` or manifest stating purpose, source paths, timestamp, tool/version, and limitations.
4. Register the artifact in the applicable ecosystem index before claiming it is complete.
5. If the destination is not specified and multiple durable locations are plausible, ask where it belongs before generating the final artifact.

## Completion gate

Before saying “done,” report:

- what was actually inspected or changed;
- evidence supporting the conclusion;
- known uncertainty and over-counting/duplication risk;
- exact durable artifact paths;
- validation performed and any remaining user decision.

Never describe temporary files, filename classification, or a single scan as deep comprehension. Label those as signals until corroborated by source reading and cross-reference.
