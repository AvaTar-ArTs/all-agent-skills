---
name: math-olympiad
description: Solves competition math problems using a rigorous, multi-stage process involving interpretation, internal refinement, adversarial verification, and calibrated abstention. Use for IMO, Putnam, USAMO, AIME, and similar competition math problems.
version: 0.1.0
---

# Competition Math Problem Solver

## Overview

This skill addresses competition mathematics problems (e.g., IMO, Putnam, USAMO, AIME) by employing a sophisticated, multi-stage process. It prioritizes rigorous reasoning, adversarial verification to catch subtle errors, and calibrated abstention when a confident solution cannot be reached. The goal is to provide accurate, verifiable, and elegantly presented solutions.

## Core Methodology

The solver operates through a structured workflow designed to maximize accuracy and minimize common errors in mathematical problem-solving:

1.  **Interpretation Check:** The first step involves a quick analysis of the problem statement to identify potential ambiguities and confirm the most likely intended interpretation, especially for problems with both easy and hard readings.
2.  **Candidate Generation & Refinement:** Multiple "solver" agents are launched in parallel, each attempting to solve the problem from different starting angles. Each solver internally refines its approach through cycles of solving, self-improvement, and self-verification before outputting its final state.
3.  **Solution Cleaning:** Before verification, the solver's intermediate thinking traces and false starts are stripped away, leaving only the core argument, method, and answer. This ensures the verifier works with a clean, isolated proof.
4.  **Adversarial Verification:** Multiple "verifier" agents, operating in fresh context without knowledge of the solver's thought process or other verifiers' verdicts, attack the cleaned solution. They use specific, pattern-based checks (e.g., checking for domain specialization, hypothesis validity, handling of edge cases) to find flaws.
5.  **Ranking and Voting:** Solutions are ranked based on verification outcomes. An asymmetric voting system (e.g., 4 "Holds" to confirm, 2 "Hole Found" to refute) is used with early exit strategies to efficiently determine if a solution is valid.
6.  **Revision:** If verification finds a hole: a "reviser" agent attempts to fix the proof based on the verifier's feedback, again working from a clean context and without access to the original solver's detailed thought process. This cycle may repeat up to three times.
7.  **Calibrated Abstention:** If verification consistently fails after multiple cycles, the agent will confidently state "no confident solution" and provide details on what was attempted and where the proof breaks. It avoids guessing or providing incorrect answers.
8.  **Presentation:** Once a solution is verified as correct, a "presentation" agent refines the proof for clarity, elegance, and conciseness, potentially inlining lemmas or finding shorter arguments. If LaTeX is available, it can compile the final proof into a PDF.

## Key Principles

-   **Context Isolation:** Crucial at multiple stages (solver refinement, verifier, reviser) to prevent bias.
-   **Pattern-Based Verification:** Adversarial checks are guided by known failure patterns in mathematical proofs.
-   **Asymmetric Trust:** Solutions are confirmed with strong consensus but refuted with minimal dissent.
-   **Honest Abstention:** Prioritizing correctness over claiming solutions.
-   **Separation of Concerns:** Distinct agents for solving, verifying, revising, and presenting.

## Usage Guidance

This skill is activated when dealing with competition math problems requiring rigorous proof or numeric answers. For numeric-answer problems (like AIME), a simplified approach focuses on answer verification. For proof-based problems, the full workflow is engaged.

## Limitations

-   Does not perform unbounded computation; relies on pure reasoning and bounded local computation (e.g., modular arithmetic, small-case enumeration).
-   Does not perform web searches or literature reviews; all reasoning is internal.
-   Abstains on problems that require deep domain knowledge beyond general mathematical principles or computational limits.

---

## Generalization Notes

While the problem domain is specific (competition math), the methodology employed—adversarial verification, layered refinement, context isolation, and calibrated abstention—is generalizable to complex reasoning and verification tasks in other domains. The core principles of breaking down problems, cross-checking work, and admitting uncertainty are universally valuable.
