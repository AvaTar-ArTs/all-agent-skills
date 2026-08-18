---
name: sage
description: Route any problem through the best skills, agents, and evidence before acting.
---

# /sage

Sage is the master routing command for Steven's AI ecosystem. Use it when the user wants the system to decide who should think about a problem before solving it.

## Behavior

When invoked as `/sage <request>`:

1. Treat the text after `/sage` as the problem to route.
2. Start with `using-superpowers` discipline: if any skill might apply, it must be used.
3. Apply `innate-workflow` as the surrounding loop when session-level audit, task work, verification, or memory update may matter.
4. Use `brainstorming` before any new feature, creative direction, implementation, or workflow design.
5. Use `workflow-orchestrator` for ambiguous or multi-surface requests.
6. Select the best specialist agents from `~/.agent-skills/agents`.
7. Return a concise routing plan before implementation.

## Output Format

```markdown
## Sage Routing

Intent: <interpreted goal>

Required skill gates:
- <skill>: <why>

Best thinkers:
- <agent>: <what they should decide or inspect>

Evidence to gather first:
- <path/source/check>

Recommended path:
1. <next step>
2. <next step>
3. <next step>

Stop conditions / permissions:
- <approval gates>
```

## Default Thinker Pools

- Cross-tool workflow: `workflow-orchestrator`, `local-ecosystem-auditor`
- Creative/music production: `studio-producer`, `visual-storyteller`, `ai-music-video-creator`
- Code implementation: `system-architect`, `python-expert`, `javascript-expert`, `testing-specialist`
- Debugging: `system-analyzer`, `test-results-analyzer`, `code-reviewer`
- Organization: `sorty`, `content-organizer`, `content-consolidator`
- Repository safety: `repo-forensics`, `git-workflow`, `code-reviewer`
- Business/revenue: `revenue-optimizer`, `xeo-strategist`, `avatararts-organizer`

## Special Route: nocturneMelodies / HeartMuLa

If the request mentions nocturneMelodies, HeartMuLa, Suno, lyrics, tags, albums, or generated music, route through:

```text
using-superpowers
→ heartmula
→ nocturne-heartmula-bridge
→ structured-asset-pipeline
→ repo-forensics
Thinkers: workflow-orchestrator, studio-producer, python-expert, visual-storyteller, ai-music-video-creator
```

Do not assume `DISCO/` exists. Inspect current paths and CSV headers first. Keep generation outputs staged under `HeartmuLa/runs/<run-slug>/` until verified and explicitly promoted.
