---
name: agent-pattern-guide
description: Reference guide for agent patterns discovered within pack structure. Use when creating or combining agents.
---

# Agent Pattern Guide

## Discovered Patterns from Pack Analysis

### Pattern 1: Specialist Template (1-eng-specialist-pack)
**Structure**: frontmatter (name, expertise, activation_keywords) + persona + principles + integration
**Use for**: Creating domain-specific expert agents
**Examples**: api-specialist, python-expert, security-engineer

### Pattern 2: Workflow Orchestrator (2-personal-tooled)  
**Structure**: coordination logic + multi-tool integration + sequencing
**Use for**: Agents that manage other tools/agents
**Examples**: workflow-orchestrator, bots, context-handoff-compiler

### Pattern 3: Creative Generator (3-contains-studio)
**Structure**: creative focus + business context + multi-modal output
**Use for**: Content creation, marketing, design agents
**Examples**: content-creator, brand-guardian, ai-music-video-creator

### Pattern 4: Ecosystem Aware (5-misc-personal)
**Structure**: environment awareness + cross-tool knowledge + personal optimization
**Use for**: Agents that understand YOUR specific setup
**Examples**: ai-workflow-manager, ecosystem-analyzer, documentation-manager

## Pattern Combinations

| Primary + Secondary | Result Agent Type | Purpose |
|---------------------|-------------------|---------|
| Specialist + Orchestrator | Implementation agent | Uses specialists in sequence |
| Creative + Specialist | Technical content agent | Creative docs and examples |
| Workflow + Ecosystem | Adaptive agent | Learns from your patterns |
| All packs combined | Meta-agent | Full capability routing |
