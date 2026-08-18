---
name: writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment.
---

# Writing Skills: TDD for Documentation

## Overview
This skill guides the process of creating, editing, and verifying reusable skills (reference guides for techniques, patterns, or tools) using a Test-Driven Development (TDD) approach adapted for documentation. The core principle is to validate skills through rigorous testing before deployment.

## Core Principle: TDD for Skills
Skills must follow a RED-GREEN-REFACTOR cycle:
1.  **RED (Test Case First):** Define pressure scenarios with an AI agent *without* the skill present to document baseline behavior and identify violations.
2.  **GREEN (Minimal Skill):** Write the skill documentation to address the specific rationalizations and failures observed in the RED phase.
3.  **REFACTOR (Close Loopholes):** Test the skill with the agent to ensure compliance. Identify and close any loopholes or new rationalizations agents might use, re-testing until the skill is bulletproof.

## When to Create a Skill
*   Create when a technique, pattern, or tool is not intuitively obvious, would be referenced across projects, applies broadly, or others would benefit.
*   Do not create for one-off solutions, standard practices, or purely project-specific conventions (document those in project-specific docs).

## Skill Types
*   **Technique:** Concrete methods with steps (e.g., condition-based-waiting).
*   **Pattern:** Ways of thinking about problems (e.g., reducing-complexity).
*   **Reference:** API docs, syntax guides, tool documentation.

## SKILL.md Structure Guidelines
*   **Frontmatter:** `name` (alphanumeric, hyphens) and `description` (third-person, "Use when..." triggers, max 1024 chars).
*   **Content:** Clear overview, 'When to Use' section with symptoms/use cases, core patterns, quick reference, implementation examples, common mistakes, and impact.
*   **CSO (Claude Search Optimization):** Use searchable keywords, descriptive naming (gerunds, verb-first), and token-efficient writing. Avoid workflow summaries in the description.
*   **Token Efficiency:** Keep descriptions concise (<500 words). Move extensive details to separate files or external references.
*   **Cross-Referencing:** Use explicit markers like `**REQUIRED SUB-SKILL:** Use skill-name` for dependencies. Avoid force-loading syntax.

## The Iron Law (Same as TDD)

**NO SKILL WITHOUT A FAILING TEST FIRST.** This applies to new skills and edits. Untested changes are not allowed.

## Common Rationalizations for Skipping Testing

| Excuse                      | Reality                                                       |
| :-------------------------- | :------------------------------------------------------------ |
| "Skill is obviously clear"  | Clear to you ≠ clear to other agents. Test it.                |
| "It's just a reference"     | References can have gaps, unclear sections. Test retrieval.   |
| "Testing is overkill"       | Untested skills have issues. Always. 15 min testing saves hours. |
| "I'll test if problems emerge" | Problems = agents can't use skill. Test BEFORE deploying.     |
| "Too tedious to test"       | Testing is less tedious than debugging bad skill in production. |

**All of these mean: Test before deploying. No exceptions.**
