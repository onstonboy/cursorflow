# Project rule templates

Copy a template to `.claude/rules/project-rule_<stack>.mdc` (or your team’s naming), set `alwaysApply: true` when active, and replace placeholders (`{{APP_NAME}}`, package names, routers).

## Choosing a tier

| Tier | Typical context | Architecture | Testing & ops |
|------|-----------------|--------------|----------------|
| **Small** | MVP, prototype, internal tool, solo/small team | Pragmatic layers; speed and clarity | Smoke + critical paths; basic CI |
| **Medium** | Production SaaS / mobile app, product team | Feature-first + clean boundaries | Unit + integration; analyze/lint in CI |
| **Big** | Enterprise, compliance, many teams, long lifecycle | Strict modules, explicit contracts | Full pyramid, observability, security gates |

Each `.template.mdc` file contains **three tier sections**. When generating a project rule (e.g. via `/cook`), **copy only the tier that matches the product** or merge Medium as default and pull Small/Big bullets as needed.

## Available templates

| File | Stack |
|------|--------|
| `flutter-project-rule.template.mdc` | Flutter / Dart |
| `swift-ios-project-rule.template.mdc` | Swift / iOS (SwiftUI-first) |
| `kotlin-android-project-rule.template.mdc` | Kotlin / Android (Jetpack) |
| `java-spring-project-rule.template.mdc` | Java / Spring Boot (backend APIs) |
| `nodejs-typescript-project-rule.template.mdc` | Node.js / TypeScript (services & APIs) |
| `nextjs-typescript-project-rule.template.mdc` | Next.js / React / TypeScript (web apps) |

Align all templates with `.claude/rules/common/project_rule_common.mdc` for topic coverage; these files add **stack-specific** and **scale-specific** detail.

**Medium tier (all stacks):** each template’s **Medium** section now includes **dev / staging / prod** (or platform equivalent), **crash/error + performance** observability, and **feature flags** — see the labeled subsection in each file (e.g. Flutter §15).
