## CursorFlow

Minimal AI-agent presets for faster project setup across Cursor and other coding agents.

---

## What this repo is

Pre-configured folders you can reuse in your own projects:

| Folder | Used by | Contents |
|--------|---------|----------|
| `.cursor/` | Cursor | rules, commands, skills, uiux, docs (**source of truth**) |
| `.agents/` | Codex + Antigravity | rules, workflows, skills, uiux, docs |
| `.claude/` | Claude Code | rules, commands, skills, uiux, docs |
| `.devin/` | Devin | rules, skills, uiux, docs |
| `.trae/` | Trae | rules, commands, skills, uiux, docs |
| `.grok/` | Grok | rules, skills, uiux, docs |
| `.opencode/` | OpenCode | rules, commands, skills, uiux, docs |
| `.qwen/` | Qwen Code | rules, commands, skills, uiux, docs |
| `.kimi-code/` | Kimi Code | rules, commands, skills, uiux, docs |
| `.omp/` | Oh My Pi (omp) | rules, commands, skills, uiux, docs |
| `.pi/` | Pi | rules, skills, uiux, docs |

Optional root helpers: `AGENTS.md`, `CLAUDE.md`, `QWEN.md`, `.kimi/AGENTS.md`, `.omp/AGENTS.md`.

Edit under `.cursor/`, then mirror everything with:

```bash
./scripts/sync-packages.sh
```

Details: [`.cursor/docs/MULTI_AGENT_SKILLS.md`](.cursor/docs/MULTI_AGENT_SKILLS.md) and [`.cursor/docs/AGENTS_SETUP.md`](.cursor/docs/AGENTS_SETUP.md).

---

## How to use

1. Clone or download this repository.
2. Copy `.cursor/` and the agent folders you need into the **root** of your project. Optionally copy root helpers and `scripts/sync-packages.sh`.
3. Open the project in your agent of choice — rules, workflows/commands, skills, and UI/UX refs load from that agent’s native paths.

That’s it.

---

This repository contains documentation extracted from ui-ux-pro-max projects (`https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`).

Purpose is to provide more context for AI in this flow.
