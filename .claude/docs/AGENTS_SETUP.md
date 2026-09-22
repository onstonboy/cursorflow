# Setup notes: multi-agent mirrors

Companion to [MULTI_AGENT_SKILLS.md](MULTI_AGENT_SKILLS.md) (covers **all** packages, not only skills).

After copying CursorFlow into a project, run `./scripts/sync-packages.sh` whenever you change `.cursor/`.

---

## Package map

| Concern | Cursor | Codex / Anti | Claude | Devin | Trae | Grok | OpenCode | Qwen | Kimi | OMP | Pi |
|---------|--------|--------------|--------|-------|------|------|----------|------|------|-----|----|
| Rules | `.cursor/rules/` | `.agents/rules/` | `.claude/rules/` | `.devin/rules/` | `.trae/rules/` | `.grok/rules/` | `.opencode/rules/` | `.qwen/rules/` | `.kimi-code/rules/` | `.omp/rules/` | `.pi/rules/` |
| Commands | `.cursor/commands/` | `.agents/workflows/` | `.claude/commands/` | via `.claude/` | `.trae/commands/` | — | `.opencode/commands/` | `.qwen/commands/` | `.kimi-code/commands/` | `.omp/commands/` | — |
| Skills | `.cursor/skills/` | `.agents/skills/` | `.claude/skills/` | `.devin/skills/` | `.trae/skills/` | `.grok/skills/` | `.opencode/skills/` | `.qwen/skills/` | `.kimi-code/skills/` | `.omp/skills/` | `.pi/skills/` |
| UI/UX | `.cursor/uiux_reference/` | `.agents/uiux_reference/` | `.claude/uiux_reference/` | `.devin/uiux_reference/` | `.trae/uiux_reference/` | `.grok/uiux_reference/` | `.opencode/uiux_reference/` | `.qwen/uiux_reference/` | `.kimi-code/uiux_reference/` | `.omp/uiux_reference/` | `.pi/uiux_reference/` |
| Docs | `.cursor/docs/` | `.agents/docs/` | `.claude/docs/` | `.devin/docs/` | `.trae/docs/` | `.grok/docs/` | `.opencode/docs/` | `.qwen/docs/` | `.kimi-code/docs/` | `.omp/docs/` | `.pi/docs/` |

Root helpers:

| File | Used by |
|------|---------|
| `AGENTS.md` | Codex, Antigravity, Devin, Trae, Grok, OpenCode, Kimi, OMP, Pi |
| `CLAUDE.md` | Claude Code |
| `QWEN.md` | Qwen Code |
| `.kimi/AGENTS.md` | Kimi (project-local overlay) |
| `.omp/AGENTS.md` | Oh My Pi native context |
| `.opencode/opencode.json` | OpenCode `instructions` → rules |

---

## Codex (OpenAI)

Optional root file `AGENTS.md` — see repo root template.

---

## Claude Code

Optional root file `CLAUDE.md` — see repo root template.

---

## Antigravity (Google; “anti”)

Uses the same `.agents/` layout as Codex. Reuse `AGENTS.md`. Confirm skills with `/skills` when using the CLI.

---

## Devin

Uses `.devin/rules/` and `.devin/skills/`, plus root `AGENTS.md`. Devin CLI can also import `.cursor/` rules and `.claude/` commands.

---

## Trae

Uses `.trae/rules/`, `.trae/commands/`, `.trae/skills/`. Root `AGENTS.md` is supported.

---

## Grok

Uses `.grok/rules/` and `.grok/skills/`. Root `AGENTS.md` is the primary instruction file; Grok also reads `.claude/` and `.cursor/rules/` for compatibility.

---

## OpenCode

Uses `.opencode/commands/` and `.opencode/skills/`. Root `AGENTS.md` plus `.opencode/opencode.json` `instructions` for mirrored rules. Also discovers `.agents/skills/` and `.claude/skills/`.

---

## Qwen Code

Uses `.qwen/` packages and root `QWEN.md` (also accepts `AGENTS.md`).

---

## Kimi Code

Skills: `.kimi-code/skills/` (and `.agents/skills/`). Instructions: root `AGENTS.md` and `.kimi/AGENTS.md`.

---

## Oh My Pi (omp)

Uses `.omp/rules/`, `.omp/commands/`, `.omp/skills/`, plus `.omp/AGENTS.md`. Also auto-discovers other tool layouts.

---

## Pi

Uses `.pi/skills/` and optional `.pi/rules/`. Root `AGENTS.md` / `CLAUDE.md` for always-on context.

---

## Install into another project

1. Copy `.cursor/` and any agent mirrors you need (`.agents/`, `.claude/`, `.devin/`, `.trae/`, `.grok/`, `.opencode/`, `.qwen/`, `.kimi-code/`, `.omp/`, `.pi/`) plus `scripts/sync-packages.sh` into the target repo root.
2. Optionally copy root helpers: `AGENTS.md`, `CLAUDE.md`, `QWEN.md`, `.kimi/AGENTS.md`.
3. After editing anything under `.cursor/`, run `./scripts/sync-packages.sh`.
