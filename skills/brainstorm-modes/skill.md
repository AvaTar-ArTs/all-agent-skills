---
name: brainstorm-modes
description: "Use when the user explicitly asks for brainstorm modes, brainstorming mode, or a brainstorm-mode workflow. Route to the canonical `brainstorming` skill, which handles requirements discovery, alternative comparison, design approval, and transition to planning before implementation."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [brainstorming, compatibility, design, workflow-gate]
    related_skills: [brainstorming, writing-plans]
disable-model-invocation: true
changelog:
  - "2026-08-15: Added as an explicit-only compatibility alias routed to canonical brainstorming."
---

# Brainstorm Modes Compatibility Alias

Load `brainstorming` and follow its canonical workflow. This alias exists so
existing prompts that say “brainstorm modes” continue to resolve without creating
a second design process or competing automatic trigger.
