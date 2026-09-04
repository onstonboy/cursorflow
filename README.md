## CursorFlow

Minimal AI-agent presets for faster project setup (Cursor, Codex, Claude Code, Antigravity).

---

## What this repo is

Pre-configured folders you can reuse in your own projects:

| Folder | Used by | Contents |
|--------|---------|----------|
| `.cursor/` | Cursor | rules, commands, skills, uiux, docs (**source of truth**) |
| `.agents/` | Codex + Antigravity | rules, workflows, skills, uiux, docs |
| `.claude/` | Claude Code | rules, commands, skills, uiux, docs |

Optional root helpers: `AGENTS.md` (Codex / Antigravity), `CLAUDE.md` (Claude Code).

Edit under `.cursor/`, then mirror everything with:

```bash
./scripts/sync-packages.sh
```

Details: [`.cursor/docs/MULTI_AGENT_SKILLS.md`](.cursor/docs/MULTI_AGENT_SKILLS.md) and [`.cursor/docs/AGENTS_SETUP.md`](.cursor/docs/AGENTS_SETUP.md).

---

## How to use

1. Clone or download this repository.
2. Copy `.cursor/`, `.agents/`, and `.claude/` into the **root** of your project (same level as your source code). Optionally copy `AGENTS.md`, `CLAUDE.md`, and `scripts/sync-packages.sh`.
3. Open the project in your agent of choice — rules, workflows/commands, skills, and UI/UX refs load from that agent’s native paths.

That’s it.

---

This repository contains documentation extracted from ui-ux-pro-max projects (`https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`).

Purpose is to provide more context for AI in this flow.
