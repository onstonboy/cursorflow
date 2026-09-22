# Project agent instructions

Shared entry point for agents that read root `AGENTS.md` (Codex, Antigravity, Devin, Trae, Grok, OpenCode, Kimi, OMP, Pi, and others).

Canonical packages are authored under `.cursor/` and mirrored by `./scripts/sync-packages.sh`.

## Package roots by agent

| Agent | Root | Rules | Commands / workflows | Skills |
|-------|------|-------|----------------------|--------|
| Codex / Antigravity | `.agents/` | `.agents/rules/` | `.agents/workflows/` | `.agents/skills/` |
| Devin | `.devin/` | `.devin/rules/` | (imports `.claude/commands/`) | `.devin/skills/` |
| Trae | `.trae/` | `.trae/rules/` | `.trae/commands/` | `.trae/skills/` |
| Grok | `.grok/` | `.grok/rules/` | — | `.grok/skills/` |
| OpenCode | `.opencode/` | `.opencode/rules/` (+ `opencode.json` instructions) | `.opencode/commands/` | `.opencode/skills/` |
| Kimi | `.kimi-code/` | `.kimi-code/rules/` | `.kimi-code/commands/` | `.kimi-code/skills/` |
| OMP | `.omp/` | `.omp/rules/` | `.omp/commands/` | `.omp/skills/` |
| Pi | `.pi/` | `.pi/rules/` | — | `.pi/skills/` |

Claude Code uses `CLAUDE.md` + `.claude/`. Qwen Code uses `QWEN.md` + `.qwen/`.

## Rules

Follow the rules tree for your agent (especially `common/project_rule_common.mdc` and any `project-rule_*` files). Prefer shared building blocks already in the repo over one-offs.

## Workflows / commands

Cook / review and related long prompts live under that agent’s commands (or `.agents/workflows/`) directory, including `common/` and generated `specify/` files when present.

## Skills

When a task matches a skill `description`, read that skill’s `SKILL.md` and follow it before inventing a new approach.

## UI/UX

When UI/UX is in scope, consult that agent’s `uiux_reference/` tree.

## Source of truth

Edit only under `.cursor/`, then run `./scripts/sync-packages.sh`.

See `.cursor/docs/MULTI_AGENT_SKILLS.md` and `.cursor/docs/AGENTS_SETUP.md`.
