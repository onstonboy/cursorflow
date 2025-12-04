---
agent: agent
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

## 8. Definition of Done (Project-Level)

```markdown
## Definition of Done (Project-Level)

- [ ] Follows project architecture and layer boundaries.
- [ ] All new public APIs are documented.
- [ ] No new linter errors or warnings.
- [ ] Happy-path and major error paths covered by tests.
- [ ] Performance acceptable on target devices.
- [ ] Accessibility considered for UI changes.
```

---

## FINAL REMINDER FOR AI

When planning or implementing any feature for this project, you MUST:

- Respect the layer boundaries and dependency rules.
- Use the configured language-specific tools:
  - Async pattern: [async_pattern]
  - Result type: [result_type]
  - Immutability pattern: [immutability]
  - JSON serialization: [json_serialization]
  - Dependency injection: [di-library]
- Keep the codebase consistent with these project rules.


