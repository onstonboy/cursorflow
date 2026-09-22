# Multi-agent packages

CursorFlow packages are authored once under `.cursor/`, then mirrored so every supported coding agent can load them from its native paths.

## Canonical source

**Edit only under `.cursor/`**, then run:

```bash
./scripts/sync-packages.sh
```

(`./scripts/sync-skills.sh` is a deprecated alias for the same script.)

| Package | Source (Cursor) | Typical mirror |
|---------|-----------------|----------------|
| Rules | `.cursor/rules/` | `<agent>/rules/` |
| Commands / workflows | `.cursor/commands/` | `<agent>/commands/` (Codex: `.agents/workflows/`) |
| Skills | `.cursor/skills/` | `<agent>/skills/` |
| UI/UX reference | `.cursor/uiux_reference/` | `<agent>/uiux_reference/` |
| Docs (this guide) | `.cursor/docs/` | `<agent>/docs/` (verbatim) |

Sync **rewrites** internal path references in rules/commands/skills/uiux so each mirror points at its own tree. Docs are copied **verbatim** so the multi-agent map stays accurate.

## Agent map

| Agent | Root | Root instruction file | Notes |
|-------|------|----------------------|-------|
| Cursor | `.cursor/` | — | Source of truth |
| Codex / Antigravity | `.agents/` | `AGENTS.md` | Commands → `workflows/` |
| Claude Code | `.claude/` | `CLAUDE.md` | Full package set |
| Devin | `.devin/` | `AGENTS.md` | Rules + skills; commands via `.claude/` import |
| Trae | `.trae/` | `AGENTS.md` | Rules, commands, skills |
| Grok | `.grok/` | `AGENTS.md` | Rules + skills (also reads `.claude/` / `.cursor/`) |
| OpenCode | `.opencode/` | `AGENTS.md` | Commands + skills; `opencode.json` instructions → rules |
| Qwen Code | `.qwen/` | `QWEN.md` | Rules, commands, skills |
| Kimi Code | `.kimi-code/` | `AGENTS.md` + `.kimi/AGENTS.md` | Skills first-class |
| Oh My Pi (omp) | `.omp/` | `AGENTS.md` + `.omp/AGENTS.md` | Rules, commands, skills |
| Pi | `.pi/` | `AGENTS.md` | Rules + skills |

## Agent notes

### Cursor
Uses `.cursor/` natively. No root instruction file required for discovery.

### Codex (OpenAI) / Antigravity (Google)
- Skills + shared packages: `.agents/`
- Commands synced as `.agents/workflows/`
- Optional root: `AGENTS.md`

### Claude Code
- Rules / commands / skills: `.claude/`
- Optional root: `CLAUDE.md`

### Devin
- Native: `.devin/rules/`, `.devin/skills/`
- Also imports `AGENTS.md`, `.cursor/rules`, and `.claude/` commands by default

### Trae
- `.trae/rules/`, `.trae/commands/`, `.trae/skills/`
- Also reads root `AGENTS.md` / `CLAUDE.md`

### Grok (xAI)
- `.grok/rules/`, `.grok/skills/`
- Also discovers `AGENTS.md`, `.claude/`, and `.cursor/rules/`

### OpenCode
- `.opencode/commands/`, `.opencode/skills/`
- Rules via `AGENTS.md` and `.opencode/opencode.json` → `instructions`
- Also reads `.agents/skills/` and `.claude/skills/`

### Qwen Code
- `.qwen/rules/`, `.qwen/commands/`, `.qwen/skills/`
- Root: `QWEN.md` (also accepts `AGENTS.md`)

### Kimi Code
- `.kimi-code/skills/` (also `.agents/skills/`)
- Instructions: root `AGENTS.md` and `.kimi/AGENTS.md`

### Oh My Pi (omp)
- `.omp/rules/`, `.omp/commands/`, `.omp/skills/`
- Also discovers many other tool layouts (`.claude/`, `.agents/`, …)

### Pi
- `.pi/skills/` (also `.agents/skills/`)
- Context: root `AGENTS.md` / `CLAUDE.md`; optional `.pi/rules/`

## Skill package shape

```
<skill-name>/
├── SKILL.md          # required
├── reference.md      # optional
└── scripts/          # optional
```

## Adding or changing a package checklist

1. Edit under `.cursor/` (rules, commands, skills, uiux_reference, or docs).
2. Run `./scripts/sync-packages.sh`.
3. Confirm mirrors under each agent root you care about.
4. Smoke-test at least one non-Cursor agent if that path matters for your team.

## Verify discovery

| Agent | Quick check |
|-------|-------------|
| Cursor | Rules/commands/skills under `.cursor/` |
| Codex / Antigravity | `.agents/skills`, `.agents/workflows`, `.agents/rules` |
| Claude Code | `/skills`; `.claude/rules`, `.claude/commands`, `.claude/skills` |
| Devin | `.devin/rules`, `.devin/skills`; `AGENTS.md` |
| Trae | `.trae/rules`, `.trae/commands`, `.trae/skills` |
| Grok | `grok inspect`; `.grok/rules`, `.grok/skills` |
| OpenCode | `.opencode/commands`, `.opencode/skills` |
| Qwen | `QWEN.md`; `.qwen/rules`, `.qwen/skills` |
| Kimi | `/skill:…`; `.kimi-code/skills` |
| OMP | `/extensions`; `.omp/rules`, `.omp/skills` |
| Pi | `.pi/skills`; `AGENTS.md` |
