---
name: frontend-ux-modernizer
description: Modernize ESO project frontend code with traceability and service-ticket logging. Use when updating UI/UX or modernizing frontend components to maintain code lineage.
---

# Frontend UX Modernizer

This skill guides the modernization of UI/UX components in the ESO ecosystem, ensuring every change is traceable and logged.

## Workflow

1. **Assess**: Analyze the existing component.
2. **Modernize**: Apply changes, using Flutter as the preferred framework.
3. **Trace**: Add `// ETS: <TIMESTAMP>-<TICKET_ID> | MOD | docs/HISTORY_TICKET.md#<TICKET_ID>` tags to modified files.
4. **Log**: Run `~/scripts/log-milestone.sh` to record the change in the project's history ticket.

## Rules of Engagement

- **High-Signal**: Log only architectural or high-impact changes.
- **Lineage**: Always link code changes to the history ticket using ETS tags.
- **Simplicity**: Favor clean, maintainable, and high-performance UI components.
