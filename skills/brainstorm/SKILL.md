---
name: brainstorm
description: "Use when the user explicitly invokes `brainstorm` or asks for brainstorm mode. Route to the canonical `brainstorming` skill before creative work, feature work, component changes, behavior changes, or implementation."
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
  - "2026-08-15: Reduced to an explicit-only compatibility alias for the canonical brainstorming workflow."
---

# Brainstorm Compatibility Alias

Load `brainstorming` and follow its complete canonical workflow. Keep this alias
explicit-only so it does not compete with automatic triggering by the canonical
skill.
