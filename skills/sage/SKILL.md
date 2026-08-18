---
name: sage
description: Use when routing problems through skills and agents first.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [routing, agents, skills, orchestration, superpowers]
    related_skills: []
user-invocable: true
---

# Sage

## Overview

Sage is Steven's master routing skill: it decides which skills, agents, evidence sources, and approval gates should be used before a problem is solved. It exists to prevent premature implementation and to make the local `~/.agent-skills` ecosystem act like an intentional council instead of a pile of prompts.

Sage answers one question first: who should think about this problem, in what order, with what evidence? It should produce a routing plan before implementation, cleanup, generation, commits, or promotion into live systems.

## When to Use

Use Sage when the user says or implies:

- `/sage ...`
- `who should think about this?`
- `source this through the right agents`
- `use the ultimate pathway`
- `route this through ~/.agent-skills`
- `start with using-superpowers and brainstorming`
- `I need the right agents/skills for this problem`

Do not use Sage as a substitute for the actual specialist skill. Sage chooses the path; the selected skills and agents still do the work.

## Quick Start

When invoked directly or by `/sage`, do not solve first. Produce the routing plan first.

Default opening stack:

```text
using-superpowers
→ innate-workflow
→ brainstorming, if new design/feature/workflow/creative direction is involved
→ workflow-orchestrator, if the task spans multiple files, tools, repos, or concepts
→ specialist skills/agents
→ verification-before-completion before final claims
```

For implementation-heavy work:

```text
brainstorming
→ writing-plans
→ test-driven-development
→ requesting-code-review
→ verification-before-completion
→ finishing-a-development-branch
```

For debugging:

```text
systematic-debugging
→ domain expert
→ targeted regression test
→ verification-before-completion
```

## Style Variations

Choose a style explicitly when the user asks, or select it from the task:

- `concise-router`: smallest actionable route.
- `deliberative-council`: multiple specialist perspectives and trade-offs.
- `technical-architect`: architecture, implementation, tests, constraints, and risks.
- `creative-studio`: producer-led music, story, visual design, and production.
- `research-source-first`: provenance, competing evidence, citations, and uncertainty.

Load detailed profiles from `references/styles/`. Style changes emphasis and output shape; it does not bypass evidence gathering, approval gates, or verification.

## Procedure

1. Identify the user's real intent.
2. Check for required skill gates, starting with `using-superpowers`.
3. Add `brainstorming` before creating, modifying, implementing, or designing anything.
4. Add `workflow-orchestrator` for cross-surface tasks.
5. Choose the best specialist agents from `~/.agent-skills/agents`.
6. Name the first evidence to inspect.
7. State stop conditions: approvals, secrets, destructive actions, commits, pushes, external spending, or live promotion.
8. Only after routing, proceed into the selected workflow if allowed.

## Routing Matrix

| Request type | Skill gates | Best thinkers |
|---|---|---|
| New feature/workflow | using-superpowers, brainstorming, writing-plans | workflow-orchestrator, system-architect |
| Code implementation | writing-plans, test-driven-development | python-expert, javascript-expert, testing-specialist |
| Bug/failure | systematic-debugging, verification-before-completion | system-analyzer, test-results-analyzer |
| Repository audit | repo-forensics | code-reviewer, local-ecosystem-auditor |
| Cleanup/consolidation | workspace-ecosystem-audit, repo-forensics | content-consolidator, sorty |
| Creative production | brainstorming, structured-asset-pipeline | studio-producer, visual-storyteller, content-creator |
| Music / nocturneMelodies | heartmula, nocturne-heartmula-bridge, structured-asset-pipeline | studio-producer, ai-music-video-creator, python-expert |
| Business/revenue | brainstorming, writing-plans | revenue-optimizer, xeo-strategist, avatararts-organizer |
| Docs/handoff | verification-before-completion, session-export | technical-writer, documentation-management |

## Output Template

```markdown
## Sage Routing

Intent: <the real task>

Required skill gates:
- <skill>: <why it applies>

Best thinkers:
- <agent>: <what they should inspect or decide>

Evidence to gather first:
- <file/path/source/check>

Recommended path:
1. <step>
2. <step>
3. <step>

Stop conditions / permissions:
- <approval gate>
```

## Hard Rules

- Skills first, especially `using-superpowers`.
- Brainstorm before implementation.
- Plans before multi-step execution.
- Debugging discipline before fixes.
- Verification before completion claims.
- No destructive cleanup, commits, pushes, remote writes, paid generation, or live promotion without explicit approval.
- Use `~/.agent-skills` as canonical; treat `~/.agents` as compatibility only.

## Common Pitfalls

1. **Solving immediately instead of routing.** Sage exists to prevent premature execution.
2. **Asking broad clarifying questions before skill gates.** Select likely skills first; they often define what to ask.
3. **Treating agent names as magic.** Assign each thinker a specific evidence source or decision.
4. **Skipping `brainstorming` because the change seems simple.** Simple changes still hide assumptions.
5. **Cleaning or reorganizing before approval.** Cleanup and moves require explicit permission.
6. **Assuming old paths are current.** Inspect live state first.

## Verification Checklist

- [ ] The Sage response names required skill gates.
- [ ] The Sage response names best thinker agents and what each should inspect or decide.
- [ ] The Sage response lists first evidence to gather.
- [ ] The Sage response states a recommended path before execution.
- [ ] The Sage response names stop conditions and approval gates.
- [ ] Any implementation work follows the selected process skill rather than bypassing it.
