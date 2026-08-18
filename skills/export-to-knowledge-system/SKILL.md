---
name: export-to-knowledge-system
description: Use when turning approved exports into traceable knowledge.
version: 0.1.0
author: Hermes
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [exports, knowledge, provenance, evidence, documentation]
    related_skills: [agent-workflow-catalog, research-source-intake, chroma]
---

# Export to Knowledge System

## Overview

Turn approved HTML, JSON, ZIP, Markdown, and supporting-note exports into a traceable knowledge system without deleting or rewriting the originals.

## When to Use

Use when exported conversations or documents contain reusable workflows, claims, decisions, products, agents, implementation patterns, or project history that must become searchable and source-linked.

## Prerequisites

- Approved source roots and an explicit exclusion list.
- A destination for derived Markdown, CSV, and index artifacts.
- `chat-history-export`, `research-source-intake`, `capability-atlas`, `narrative-documentation`, and `chroma` available directly or as deliberate adapters.
- Agents: `filesystem-inventory`, `content-organizer`, `documentation-manager`, and `technical-writer`.

## How to Run

1. Inventory formats, paths, sizes, dates, and provenance.
2. Preserve originals and record a source manifest.
3. Extract text and metadata without treating summaries as originals.
4. Classify material as observed, inherited, inferred, possible, or unknown.
5. Extract workflows, claims, decisions, products, agents, and implementation patterns.
6. Build a capability map and evidence ledger.
7. Create canonical briefs, decision records, timelines, and handoffs.
8. Index only approved derived content for semantic retrieval.
9. Test retrieval with known questions and source evidence.

## Quick Reference

```text
Skills: chat-history-export → research-source-intake → capability-atlas
        → narrative-documentation → chroma
Agents: filesystem-inventory → content-organizer → documentation-manager
        → technical-writer
Outputs: source-manifest.csv, capability-map.md, evidence-ledger.csv,
         briefs/, decisions/, timelines/, retrieval-tests.md
```

## Safety Boundaries

Exclude secrets, auth stores, runtime databases, session stores, memories, logs, caches, vendor trees, and unrelated conversations unless separately approved. A derived summary is a new interpretation; it does not replace or authorize deletion of its source.

## Common Pitfalls

- Treating extracted summaries as original evidence.
- Indexing private runtime data because it is convenient.
- Losing source filenames or conversation dates.
- Calling a derived brief a replacement for the export.

## Verification Checklist

- [ ] Originals remain unchanged.
- [ ] Every derived claim links to a source path and location.
- [ ] Conversation dates and export filenames are preserved.
- [ ] Historical and current-verification-required claims are separated.
- [ ] The evidence ledger parses and has nonempty rows.
- [ ] Retrieval tests return source-backed results.
- [ ] Exclusions and unresolved questions are documented.
