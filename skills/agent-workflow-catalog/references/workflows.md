# Agent Workflow Catalog — Reference Routes

Use these routes with `agent-workflow-catalog/SKILL.md`. They are routing templates, not permission to execute side effects.

## Export to knowledge system

Skills: `chat-history-export` → `research-source-intake` → `capability-atlas` → `narrative-documentation` → `chroma`

Agents: `filesystem-inventory` → `content-organizer` → `documentation-manager` → `technical-writer`

Result: source-linked briefs, decisions, timelines, evidence ledger, and searchable knowledge base.

## Automation Offer Workbench

Skills: `content-strategy` → `domain-modeling` → `build-mcp-server` → `mcp-integration` → `quality-regression-testing` → `narrative-documentation`

Agents: `project-launch-manager` → `project-shipper` → `technical-writer` → `code-reviewer`

Result: provider-agnostic offer model, workflow states, approval gates, reusable tool, buyer deliverables, proof assets, and fulfillment handoff.

Boundary: preserve `~/fiverr` as the canonical root. Do not infer buyer demand or client outcomes from local files.

## Current-market validation

Skills: `research-source-intake` → `research` → trend-researcher-compatible workflow → `content-strategy`

Agents: `trend-researcher` → `technical-writer`

Result: historical/current classification, claim queue, date sensitivity, confidence, and validation method.

## Visual proof library

Skills: `structured-asset-pipeline` → `image-to-code` → `design-md` → `hyperframes` → `hyperframes-creative` → `product-launch-video`

Agents: `content-organizer` → `content-consolidator` → `technical-writer`

Result: visual tokens, reusable proof components, asset taxonomy, and source-preserving ledger.

Note: the canonical `image-to-code` skill is nested at `~/.agent-skills/skills/taste-skill/skills/image-to-code-skill/SKILL.md`.

## Seller OS interface

Skills: `build-mcp-app` → `build-mcp-server` → `frontend-design` → `design-md` → `mcp-integration`

Agents: `project-launch-manager` → `code-reviewer` → `technical-writer`

Result: local-first read-only dashboards, artifact previews, explicit approvals, buyer-package generation, and audit history.

## Preview-first automation

Skills: `automation-recommender` → `hook-development` → `quality-regression-testing` → `verification-before-completion`

Agents: `ecosystem-analyzer` → `code-reviewer`

Result: inventory, dry run, proposed change set, approval, separate output, validation, append-only changelog, and rollback reference.

## Semantic personal knowledge

Skills: `self-evolving-memory` → `chroma` → `local-knowledge-engineering` → `session-export` → `session-report`

Agents: `context-fetcher` → `knowledge-fetcher` → `ecosystem-learning`

Result: semantic retrieval by project, workflow, claim, asset, and implementation status.

Note: `local-knowledge-engineering` is a referenced route name and should be resolved to its owning source or adapter before activation if no standalone skill is available.

## Duplicate detection without deletion

Skills: `workspace-ecosystem-audit` → `codebase-inspection` → `quality-regression-testing`

Agents: `filesystem-inventory` → `ecosystem-analyzer` → `content-consolidator`

Result: hashes, paths, sizes, near-duplicate analysis, mirror/version classification, and review-only recommendation.

## Launch portfolio

Skills: `content-strategy` → `narrative-blueprints` → `narrative-documentation` → `product-launch-video` → `faceless-explainer`

Agents: `project-launch-manager` → `trend-researcher` → `technical-writer`

Result: flagship offer, supporting offers, buyer, scope, evidence, proof, risks, and next validation step.

## Cross-host portability

Skills: `capability-atlas` → `ecosystem-layering` → `hermes-integration` → `skill-development` → `openai-docs`

Agents: `ecosystem-synergy` → `ecosystem-learning` → `technical-writer`

Result: host-agnostic workflow specification and deliberate adapters for Hermes, Codex, Claude Code, OpenCode, MCP, and local Python.

## Multi-agent review

Skills: `subagent-driven-development` → `requesting-code-review` → `receiving-code-review` → `quality-regression-testing` → `systematic-debugging`

Agents: `project-launch-manager` → `code-reviewer` → `technical-writer` → `ecosystem-analyzer`

Result: requirements, architecture, safety, documentation, and regression reviews with disagreements preserved.

## Explainable systems

Skills: `narrative-blueprints` → `narrative-documentation` → `pretext` → `humanizer` → `design-md`

Agents: `technical-writer` → `content-creator`

Result: source-linked case study or explainer covering before state, preview, controlled transformation, validation, and handoff.

## Priority synthesis: Automation Offer Workbench

Skills: `workspace-ecosystem-audit` → `research-source-intake` → `capability-atlas` → `automation-recommender` → Automation Offer Workbench design → `quality-regression-testing` → `requesting-code-review`

Agents: `filesystem-inventory` → `ecosystem-analyzer` → `project-launch-manager` → `ecosystem-dev` → `technical-writer` → `code-reviewer` → `project-shipper`

Result: evidence-backed implementation map that preserves all source material and introduces mutation only behind preview and approval gates.
