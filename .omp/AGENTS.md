# Oh My Pi (omp) — project notes

## Rules

Follow `.omp/rules/` (especially `common/project_rule_common.mdc` and any `project-rule_*` files). Prefer shared building blocks already in the repo over one-offs.

Root `AGENTS.md` also applies. Sticky hard requirements may live in `.omp/RULES.md` when needed.

## Commands

Cook / review and related prompts: `.omp/commands/` (Markdown). OMP also discovers `.claude/commands/` when present.

## Skills

Project skills live in `.omp/skills/`. Prefer a matching skill over ad-hoc procedures.

## UI/UX

When UI/UX is in scope, consult `.omp/uiux_reference/`.

## Source of truth

Canonical authoring path: `.cursor/`. Keep mirrors in sync with `./scripts/sync-packages.sh`.

See `.cursor/docs/MULTI_AGENT_SKILLS.md` and `.cursor/docs/AGENTS_SETUP.md`.
