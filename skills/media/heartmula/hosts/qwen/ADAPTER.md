---
host: qwen
source: ~/.agent-skills/skills/media/heartmula/SKILL.md
---

# Adapter: Qwen

## What changes

- Prefer a Qwen “plan-first” wrapper: installation + environment checks first, then one concrete run command.
- Keep dependency fix steps but avoid pinning to dates; treat them as “if conflict occurs, do X”.

## What to promote (live)

- Qwen skill wrapper (MD) that:
  - links here for full steps
  - provides a short “quickstart” and “troubleshooting” section

