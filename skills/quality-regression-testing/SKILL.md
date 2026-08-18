---
name: quality-regression-testing
description: Use when the user asks to "add regression tests", "verify a fix", "prevent regressions", "run quality checks", "test edge cases", or validate that a code, configuration, documentation, or workflow change preserves existing behavior.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, regression, quality, verification]
    related_skills: [test-driven-development, systematic-debugging, subagent-driven-development, verification-before-completion, code-review]
changelog:
  - "2026-08-15: Added to the core workflow chain as the post-fix regression gate."
---

# Quality Regression Testing

## Overview

Use this skill to turn a change or suspected defect into a reproducible quality
check. Preserve existing behavior unless the requested change explicitly changes
the contract. Prefer a small, deterministic regression test that fails for the
old behavior and passes for the corrected behavior.

## When to Use

Apply this workflow to bug fixes, feature work, configuration changes, CLI
changes, documentation examples, integrations, and any change where preserving
existing behavior matters.

## Operating Workflow

### 1. Establish the contract

Identify:

- the requested behavior and any deliberate behavior change;
- the affected entry points, interfaces, files, and dependencies;
- existing tests, fixtures, snapshots, linters, type checks, and CI commands;
- supported platforms, versions, permissions, and environment assumptions.

Read project instructions and existing tests before writing new ones. Treat the
current test suite as evidence, not as a complete specification.

### 2. Reproduce before changing

For a bug, capture the smallest failing input, command, fixture, or interaction.
Run it at least twice when flakiness is possible. Record the observed result and
the expected result. Do not write a test that merely encodes an unverified guess
about the cause.

For a feature, identify the nearest existing behavior and define both the new
case and the compatibility cases that must remain unchanged.

### 3. Build a regression matrix

Cover the smallest useful set of dimensions:

| Dimension | Examples |
|---|---|
| Normal path | valid input, expected permissions, standard configuration |
| Boundary | empty, one item, maximum, missing optional value |
| Invalid input | malformed, unknown, conflicting, or unsupported value |
| Failure | timeout, unavailable dependency, partial result, retry |
| Compatibility | old format, existing caller, previous default |
| Safety | authorization, secret redaction, path containment, destructive action |

Do not multiply combinations without evidence. Select pairwise or representative
cases when the full Cartesian product is unnecessary.

### 4. Write the smallest useful check

Prefer the narrowest layer that catches the behavior:

1. pure unit test for deterministic logic;
2. component or integration test for boundaries between modules;
3. end-to-end test only when the behavior depends on the complete runtime;
4. manual or visual verification for GUI, media, and subjective presentation.

Name the test after the behavior, not the implementation detail. Make fixtures
local, explicit, and stable. Avoid sleeps, wall-clock dependence, network calls,
randomness, global state, and snapshots that obscure the actual assertion unless
the behavior specifically requires them.

### 5. Run in layers

Run the focused regression test first. Then run the relevant package or subsystem
suite, followed by the repository's full validation command when practical. Use
the project's existing package manager and test conventions. If a check cannot be
run, report why instead of presenting it as passed.

For flaky or environment-sensitive tests, repeat enough times to establish a
pattern and report the exact command, environment, and observed frequency.

### 6. Review the change

Confirm that:

- the new test fails against the old behavior or a controlled failing fixture;
- the implementation change is no broader than necessary;
- unrelated tests remain unchanged and passing;
- error messages and failure artifacts are actionable;
- the test does not expose credentials, personal data, or private endpoints;
- documentation and examples remain consistent with the verified behavior.

Use `systematic-debugging` when the failure mechanism is unclear and
`test-driven-development` when implementing the correction through RED-GREEN-
REFACTOR. Use `code-review` or a testing specialist for an independent pass on
high-risk changes.

## Common Pitfalls

- Writing a test for an unverified theory instead of the observed failure.
- Testing only the happy path and missing empty, invalid, boundary, or retry cases.
- Using sleeps, network calls, randomness, or global state that makes the test flaky.
- Claiming the full suite passed after running only a focused test.
- Including credentials, private data, or real destructive operations in fixtures.

## Verification Checklist

- [ ] Confirm the contract and affected behavior.
- [ ] Reproduce the old failure or define the new acceptance case.
- [ ] Cover normal, boundary, invalid, failure, and compatibility cases as applicable.
- [ ] Run the focused test and the relevant subsystem suite.
- [ ] Record skipped or unavailable checks.
- [ ] Review changed paths, assertions, fixtures, and secret handling.

## Required Handoff

Return:

- changed test and implementation paths;
- the regression scenario and expected contract;
- commands run and their real results;
- coverage of boundaries, failures, and compatibility cases;
- skipped checks with reasons;
- remaining risks or recommended follow-up tests.

Never claim “all tests pass” when only a focused test was run. Distinguish
`passed`, `failed`, `skipped`, and `not run` explicitly.

## Prompt examples

```text
Add a regression test for the reported duplicate-submit bug. Reproduce it first,
identify the smallest failing case, write the test before changing production
code, implement the minimal fix, then run the focused test and the full relevant
suite. Report exact commands, results, changed files, and any untested race or
environment assumptions.
```

```text
Quality-check this configuration change. Build a matrix covering the default,
missing optional fields, malformed input, backward compatibility, and secret
redaction. Prefer deterministic automated checks, use a manual checklist only
where automation cannot observe the behavior, and stop before any destructive
operation.
```
