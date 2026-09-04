# Claude Code — project notes

## Rules

Follow `.claude/rules/` (especially `common/project_rule_common.mdc` and any `project-rule_*` files). Prefer shared building blocks already in the repo over one-offs.

## Commands

Cook / review and related prompts: `.claude/commands/` (including `common/` and generated `specify/` files when present).

## Skills

Project skills live in `.claude/skills/`. Prefer a matching skill over ad-hoc procedures. List with `/skills`.

## UI/UX

When UI/UX is in scope, consult `.claude/uiux_reference/`.

## Source of truth

Canonical authoring path: `.cursor/`. Keep mirrors in sync with `./scripts/sync-packages.sh`.

See `.cursor/docs/MULTI_AGENT_SKILLS.md` and `.cursor/docs/AGENTS_SETUP.md`.
