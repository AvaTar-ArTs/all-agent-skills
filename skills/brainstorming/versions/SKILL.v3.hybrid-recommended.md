---
name: brainstorming
description: Use when starting any feature, component, or behavior change that needs requirement clarity and design validation before implementation.
---

# Brainstorming Ideas Into Designs

## Overview
This skill turns ideas into approved designs before implementation starts.

<HARD-GATE>
Do NOT implement, scaffold, or invoke implementation skills until a design is presented and explicitly approved.
</HARD-GATE>

## Required Sequence
1. Explore context (code/docs/recent changes).
2. Ask clarifying questions one at a time.
3. Propose 2-3 approaches with trade-offs and a recommendation.
4. Present design sections and confirm approval.
5. Write design doc to `docs/plans/YYYY-MM-DD-<topic>-design.md`.
6. Hand off to planning skill for implementation plan.

## Process Rules
- One question per message.
- Prefer multiple-choice when practical.
- Include constraints, success criteria, and non-goals.
- Keep designs concise for simple work; deeper for complex work.
- Cover architecture, components, data flow, error handling, and tests.
- Revisit assumptions when user feedback indicates mismatch.

## Anti-Pattern
"Too simple for design" is not valid. Simple tasks still need a brief explicit design and approval.

## Transition
After approval, proceed to a planning skill. Do not skip the planning step.
