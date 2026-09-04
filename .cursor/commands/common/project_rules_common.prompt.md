---
agent: agent
---

# Project Rules & Architecture Standards

**AI Role: You are an expert Software Architect & Technical Standards Specialist** with comprehensive knowledge of software architecture, coding standards, and best practices. Your role is to ensure all planning and implementation adheres to project-wide rules, architecture standards, and coding conventions. You excel at maintaining consistency across the codebase, enforcing clean architecture principles, and ensuring all code follows established patterns and standards.

---

# Project Rules & Architecture Standards

This document defines project-wide rules, architecture standards, and coding conventions that the AI must follow when planning or implementing any feature for this project.

## 1. Project Overview

```markdown
## Project Overview

**Project Name:** [Project Name]
**Primary Platform:** [mobile/web/desktop/backend]
**Target Language/Framework:** [Language/Framework]

**High-Level Goals:**
- [Goal 1]
- [Goal 2]
- [Goal 3]
```

---

## 2. Architecture Style

### 2.1 High-Level Architecture

```markdown
## Architecture Style

- **Overall Style:** Clean Architecture / Layered Architecture
- **Layers:**
  - Presentation Layer (UI, state management)
  - Domain Layer (business logic, entities, use cases)
  - Data Layer (repositories, data sources, models)
  - Core/Shared (errors, utils, configuration)

**Rules:**
- Presentation layer depends only on Domain (and framework UI).
- Domain layer is pure and framework-agnostic.
- Data layer depends on Domain and external services (APIs, databases).
- Core/shared utilities are reusable across features.
```

### 2.2 Dependencies Between Layers

```markdown
## Dependency Rules

- Presentation → Domain (allowed)
- Presentation → Data (for DI wiring only, not direct calls)
- Domain → Data (via abstract repositories only)
- Domain → Presentation (NOT allowed)
- Data → Presentation (NOT allowed)
- Feature modules should not import each other directly; use shared/domain abstractions.
```

### 2.3 Prefer project-common building blocks first

```markdown
## Prefer project-common building blocks first

- Before new libraries, ad-hoc helpers, duplicate UI, or alternate patterns, **search the repo** for existing **project-common** solutions (`core/`, shared packages, design system, internal utilities, wrappers, config, error types).
- **Include shared presentation:** base widgets or components, bottom sheets and modals, banners and alerts, dialogs, sheets, toasts or snackbars, list cells, app bars or headers, empty and error states, and any other common views already in the codebase.
- If nothing suitable exists, **add or extend the canonical shared place** so the next feature reuses it; avoid one-off duplicates scattered across features (including bottom sheets, banners, or widgets that duplicate an established pattern).
- **Default to these shared solutions** for all new work. **Only** adopt a different library, pattern, or one-off approach when the **user explicitly requests** it (still respecting layer and architecture rules).
```

---

## 3. Coding Standards

```markdown
## Coding Standards

**General:**
- Follow official style guide for [language] (formatter + linter).
- Prefer small, focused functions and classes.
- Use meaningful names (no abbreviations or generic names like `data`, `obj`).

**Immutability:**
- Prefer immutable data structures where practical.
- For [language], use: [immutability] pattern.

**Error Handling:**
- Use [result_type] or equivalent instead of throwing raw exceptions in domain layer.
- Map low-level exceptions to domain-level failures.

**Async/Concurrency:**
- Use [async_pattern] consistently for async work.
- Avoid blocking operations on the main/UI thread.

**Comments & Docs:**
- Document non-trivial business rules and edge cases.
- Public APIs (use cases, repositories, controllers) should have short docstrings.
```

---

## 4. Feature Module Structure

```markdown
## Feature Module Structure

src/ (or app/, lib/, etc.)
├── core/
│   ├── errors/              # Failure types, error mappers
│   ├── network/             # HTTP client, network info
│   ├── utils/               # Cross-cutting utilities
│   └── config/              # Environment, constants, feature flags
├── features/
│   └── [feature_name]/
│       ├── domain/
│       │   ├── entities/
│       │   ├── repositories/
│       │   └── usecases/
│       ├── data/
│       │   ├── models/
│       │   ├── datasources/
│       │   └── repositories/
│       └── presentation/
│           ├── state/       # controllers, blocs, viewmodels, stores
│           ├── pages/       # screens/views
│           └── components/  # reusable UI pieces
└── di/                      # Dependency injection configuration
```

---

## 5. State Management Rules

```markdown
## State Management Rules

- Use [state-management-library] (or closest equivalent) as the primary state management solution.
- Separate **events/actions**, **state**, and **business logic** where the framework allows.
- UI components should be dumb/presentational when possible; move logic to controllers/blocs/viewmodels.
- Avoid global mutable state; prefer composition and explicit dependencies.
```

---

## 6. API & Data Layer Rules

```markdown
## API & Data Rules

- All external calls go through repositories and data sources.
- No direct HTTP/database access from the presentation or domain layers.
- Models:
  - Use [json_serialization] or equivalent for JSON mapping.
  - Provide `toDomain()` methods to translate to domain entities.
- Repositories:
  - Expose domain-friendly methods (no raw DTOs in signatures).
  - Return [result_type] or equivalent for success/failure.
```

---

## 7. Testing Rules (High-Level)

```markdown
## Testing Rules (High-Level)

- Write tests at three levels:
  - Unit tests for pure business logic (domain layer).
  - Integration tests for repositories and data sources.
  - UI/component tests for critical user flows (where supported).

- Priorities:
  1. Critical business logic (payments, auth, data integrity).
  2. Core user journeys (sign-in, checkout, main flows).
  3. Reusable utilities and complex mappers.
```

---

## 8. Security, Obfuscation & Pentest Readiness

```markdown
## Security, Obfuscation & Pentest Readiness

Apply **in every phase** (design, implementation, review, and release): planning and code must account for **security**, **obfuscation where the stack supports it**, and **issues commonly raised in penetration tests**.

**Secure design and implementation (always):**
- **Secrets:** No API keys, tokens, passwords, or private keys in source, client bundles, logs, error messages, or analytics. Use secure storage, env/secrets managers, and short-lived credentials.
- **Authn / Authz:** Enforce authentication and least-privilege authorization on every sensitive path; avoid trusting client-only checks for server-side decisions.
- **Input and output:** Validate and sanitize untrusted input; encode output appropriately for the channel (e.g. HTML/JSON/SQL) to prevent injection and XSS.
- **Transport and data:** Use TLS for remote calls; apply encryption at rest where required; follow platform crypto APIs and safe defaults (no custom crypto unless justified).
- **Dependencies:** Prefer maintained libraries; stay aware of known CVEs and upgrade paths for critical dependencies.
- **Errors and logging:** User-facing messages must not leak stack traces, internal paths, or sensitive data; logs must be scrubbed of secrets.
- **Dev-only diagnostics:** Verbose **logging**, **`print` / console-style debug output**, and **stack traces** (logged, printed, or returned) must be **enabled only in development** (debug / non-production, per stack). In **production**, disable, strip, no-op, or compile them out— they must not run in prod builds, client release artifacts, or user-visible errors. Production observability, if used, must be minimal and redacted, not raw debug noise or full stacks on client-facing paths.

**Obfuscation (where applicable to the product):**
- Use the stack’s **release hardening**: minification/tree-shaking for web, stripping debug symbols, bytecode/native obfuscation or R8/ProGuard-style shrinking on mobile when the project already uses them—**without** treating obfuscation as a substitute for secure design.

**Pentest-style mitigation (design and test for):**
- Common classes: **injection**, **broken access control / IDOR**, **sensitive data exposure**, **misconfiguration** (headers, CORS, default accounts), **SSRF**, **insecure deserialization**, **rate limiting / abuse** on auth and expensive endpoints, **session / token** handling (rotation, revocation, secure cookies).
- Align with the team’s **security baseline** or OWASP-style checklists when present; add tests or manual verification for high-risk flows (auth, payments, admin).

**Definition of Done tie-in:** No feature is complete without an explicit pass over the bullets above appropriate to its scope.
```

---

## 9. Definition of Done (Project-Level)

```markdown
## Definition of Done (Project-Level)

- [ ] Follows project architecture and layer boundaries.
- [ ] All new public APIs are documented.
- [ ] No new linter errors or warnings.
- [ ] Happy-path and major error paths covered by tests.
- [ ] Performance acceptable on target devices.
- [ ] Accessibility considered for UI changes.
- [ ] Security, obfuscation (where applicable), and pentest-relevant risks considered and addressed for the feature’s scope.
- [ ] Debug logging, print/console noise, and stack traces are **dev-only**, not active in production builds or user-visible prod paths.
```

---

## FINAL REMINDER FOR AI

When planning or implementing any feature for this project, you MUST:

- Respect the layer boundaries and dependency rules.
- Treat **security, release-time obfuscation where applicable, and pentest-style risks** as part of every phase, not a late add-on.
- Ensure **log, print, and stack-trace diagnostics are development-only**, never production behavior on client or user-visible surfaces.
- Use the configured language-specific tools:
  - Async pattern: [async_pattern]
  - Result type: [result_type]
  - Immutability pattern: [immutability]
  - JSON serialization: [json_serialization]
  - Dependency injection: [di-library]
- Keep the codebase consistent with these project rules.


