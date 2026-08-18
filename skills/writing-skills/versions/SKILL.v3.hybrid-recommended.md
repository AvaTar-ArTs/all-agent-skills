---
name: writing-skills
description: Use when creating, revising, or validating skills so they are test-backed, discoverable, and reliable before deployment.
---

# Writing Skills (TDD for Documentation)

## Core Principle
Treat skill authoring as RED-GREEN-REFACTOR:
1. RED: run baseline scenario without the skill and capture failures.
2. GREEN: write minimal skill content that fixes observed failures.
3. REFACTOR: pressure-test for loopholes and tighten wording.

## Hard Rule
No new skill or major skill edit ships without evidence from at least one failing baseline and one passing verification run.

## When To Create Skills
Create when:
- Pattern is reusable across tasks.
- Behavior is non-obvious without guidance.
- Future agents or teammates will benefit.

Avoid when:
- It is one-off project context.
- It is better enforced by automation/linting/hook rules.

## SKILL.md Contract
- Frontmatter requires `name` and `description`.
- Description should focus on trigger conditions ("Use when...").
- Include: overview, when to use, core pattern, common mistakes, validation notes.
- Keep long references in supporting files.

## Validation Checklist
- Baseline failure documented.
- Updated skill added.
- Post-change validation passes.
- Common misinterpretations addressed.
- Token-heavy material moved to references where possible.

## Deployment Notes
- Keep naming searchable and explicit.
- Keep instructions concrete, testable, and tool-agnostic.
- Update related docs/changelogs when behavior changes.
