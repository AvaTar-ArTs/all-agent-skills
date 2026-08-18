---
name: automation-offer-workbench
description: Use when productizing automation into reviewable offers.
version: 0.1.0
author: Hermes
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [automation, offers, mcp, seller-os, productization, approvals]
    related_skills: [agent-workflow-catalog, build-mcp-server, quality-regression-testing]
---

# Automation Offer Workbench

## Overview

Create a provider-agnostic workbench that turns a client need into an automation plan, tool or MCP adapter, service package, proof asset, documentation, and buyer-facing handoff.

## When to Use

Use when combining Seller OS, media organizer, Fiverr, MCP, Python automation, evidence, and fulfillment workflows into one buyer-safe system.

## Prerequisites

- Preserve `~/fiverr` as the canonical root.
- Separate historical conversation evidence from current-market validation.
- Use agents: `project-launch-manager`, `project-shipper`, `technical-writer`, and `code-reviewer`.
- Start with read-only or preview-only behavior.

## How to Run

1. Gather the request, buyer scenario, source evidence, and desired deliverable.
2. Model entities: Offer, Buyer Scenario, Evidence Item, Source Asset, Workflow State, Approval Gate, Tool, Package, and Handoff.
3. Define states: clarify → fill → preview → approve → package → validate → handoff → platform hold.
4. Define provider-agnostic tool contracts and least-privilege MCP access.
5. Build the smallest local vertical slice.
6. Add preview and dry-run output before write-capable behavior.
7. Generate service copy and proof assets only from approved evidence.
8. Add regression tests and independent review.
9. Produce a local-ready handoff and explicit manual next actions.

## Quick Reference

```text
Skills: content-strategy → domain-modeling → build-mcp-server → mcp-integration
        → quality-regression-testing → narrative-documentation
Agents: project-launch-manager → project-shipper → technical-writer → code-reviewer
Canonical root: ~/fiverr
Default mode: local, preview-first, provider-agnostic
```

## Approval Gates

Require explicit approval before importing drafts, changing canonical state, enabling write-capable MCP tools, exposing a tunnel, using credentials, automating a marketplace, contacting buyers, publishing, submitting, or claiming current pricing/demand/outcomes.

## Common Pitfalls

- Duplicating or relocating `~/fiverr`.
- Claiming current buyer demand from historical material.
- Adding write-capable MCP tools before preview and regression coverage.
- Publishing offer language without evidence or scope boundaries.

## Verification Checklist

- [ ] Canonical root is preserved.
- [ ] Buyer scenario and scope are explicit.
- [ ] Historical claims are marked separately from current claims.
- [ ] Preview and dry-run output exist before mutation.
- [ ] Secret redaction and hold behavior are tested.
- [ ] MCP permissions and tool boundaries are documented.
- [ ] Generated buyer package links to evidence.
- [ ] Independent code and workflow review completed.
