---
name: capability-atlas
description: This skill should be used when the user asks to "map a capability across hosts", "translate a skill to Gemini, Qwen, Codex, or Cursor", "build a universal capability matrix", "mirror an agent or skill into ~/.gemini", "preserve behavior while renaming or repackaging", or wants a self-evolution loop that keeps capability parity across renderings.
---

# Capability Atlas

## Purpose

Use this skill to preserve a capability while translating it across hosts, packaging formats, and runtime surfaces. The capability stays stable; the renderings can change.

## Core Idea

A capability is the stable unit. A host-specific form is just one rendering of that capability.

Keep these parts stable:

- function
- trigger
- input/output contract
- parity tests
- translation notes

Allow these parts to vary:

- name
- file shape
- host packaging
- wrapper scripts
- installation path

## When To Use

Use this skill when a task needs one of these outcomes:

- turn a capability into a skill, agent, hook, command, script, plugin, extension, doc, plan, or test
- move a capability from one host to another without losing behavior
- normalize a capability that exists in multiple ecosystems
- define what is canonical and what is a host rendering
- prove that two renderings still behave the same

## Workflow

### 1. Identify the canonical function

State what the capability actually does in one sentence. If the name is confusing, ignore the name and describe the function.

### 2. Build the capability matrix

Capture the capability in a matrix with these fields:

- function
- trigger
- inputs
- outputs
- host renderings
- canonical location
- parity tests
- drift risks
- notes

Use the reference template in `references/capability-matrix-template.md`.

### 3. Choose host renderings

Map the same function into the appropriate forms:

- skill for procedural and interactive behavior
- agent for autonomous or role-based behavior
- hook for event-driven behavior
- command for explicit user invocation
- script for deterministic automation
- plugin or extension for bundled delivery
- doc, plan, or test for reasoning, governance, and proof

### 4. Translate without losing the contract

Rename or repackage as needed, but keep the behavior contract intact.

- Keep the trigger meaning equivalent.
- Keep the input/output semantics equivalent.
- Keep the verification story equivalent.
- Record any host-specific differences explicitly.

### 5. Add parity tests

Write tests or test prompts that prove the capability still behaves correctly after translation.

Use the checklist in `references/parity-tests.md`.

### 6. Preserve the reasoning

If a capability already has good analysis, do not flatten it into a short summary. Preserve the useful depth and layer the canonical translation on top of it.

## Self-Evolution Loop

Apply this loop when refining the capability or adapting it to a new host:

1. observe the current behavior
2. abstract the stable function
3. render it in the target host
4. verify parity
5. refine the translation

## Output Format

When documenting or implementing a translation, produce:

1. a capability matrix
2. a host translation summary
3. a parity test list
4. a drift note if any host differs from the canonical behavior

## Additional Resources

- `docs/CAPABILITY_ATLAS_WALKTHROUGH.md`
- `references/capability-matrix-template.md`
- `references/host-translation-rules.md`
- `references/parity-tests.md`
