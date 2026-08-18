---
name: self-evolving-memory
description: Use when maintaining persistent, evolving knowledge across sessions. Tracks decisions, learns from outcomes, and adapts memory structure based on usage patterns. Uses SQLite for storage and cross-agent messaging for coordination.
---

# Self-Evolving Memory

## Overview

A persistent memory system that evolves and organizes itself based on usage patterns. Unlike static knowledge bases, this memory:
- Tracks what you remember and why
- Learns from access patterns to optimize retrieval
- Adapts structure based on what proves useful
- Coordinates across agents via agmsg

## When to Use

- Before starting any task to check past decisions
- After completing work to record outcomes and learnings
- When similar patterns emerge to consolidate memory
- For cross-session context preservation

## Memory Structure

```
memory/
├── decisions/        # What was decided, when, why, outcome
├── patterns/         # Repeated observations that matter
├── preferences/      # User/system preferences discovered
├── evolving-index/   # Self-organizing knowledge graph
└── scripts/          # Memory management scripts
```

## Core Workflows

### 1. Record Decision
When making a significant choice:
```sql
INSERT INTO decisions (topic, choice, context, outcome, timestamp)
VALUES (?, ?, ?, ?, datetime('now'))
```

### 2. Check Memory Before Acting
Query similar past situations before starting work.

### 3. Evolve Structure
Monthly: Analyze access patterns, consolidate, prune obsolete entries.

## Cross-Agent Coordination

Uses `agmsg` for memory sharing across sessions and agents.
Run `~/.agent-skills/skills/agmsg/scripts/whoami.sh "$(pwd)" poolside` first.
