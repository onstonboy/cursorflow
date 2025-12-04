---
agent: agent
--- 

# Implementation Planning Guide

This document provides a structured approach for AI to analyze, plan, and implement features following the project's architecture standards. Use this guide to ensure comprehensive planning before implementation.

## Planning Workflow

When implementing a new feature, follow this systematic approach:

### 1. Requirements Analysis
**Objective:** Understand what needs to be built

#### Questions to Answer:
- What is the core functionality being requested?
- What are the user stories or use cases?
- What are the acceptance criteria?
- Are there any edge cases or error scenarios?
- What are the performance requirements?
- Are there any security considerations?
- What platforms need to be supported (iOS, Android, Web, Desktop)?

#### Deliverable:
- Clear feature description
- List of functional requirements
- List of non-functional requirements (performance, security, accessibility)

---

### 2. Architecture Design
**Objective:** Plan the implementation following Clean Architecture

#### Domain Layer Planning:
**Entities:**
- What business objects need to be created?
- What are their properties and relationships?
- Are they immutable? (Use immutability pattern/library appropriate for your language)
- Do they need value objects for complex types?

**Repository Interfaces:**
- What data operations are needed?
- What methods should the repository expose?
- What is the return type? (Use Result<Success, Failure> or Either pattern for error handling)
- Are there pagination requirements?

**Use Cases:**
- What business logic needs to be executed?
- What are the inputs (parameters)?
- What are the outputs (success/failure types)?
- Are there dependencies on other use cases?
- What validations are needed?

#### Data Layer Planning:
**Models:**
- How do models map to entities?
- What JSON serialization is needed? (Serialization library/annotations for your language)
- Are there snake_case to camelCase conversions?
- What are the API response structures?

**Data Sources:**
- What remote APIs need to be called?
- What local storage is required (Key-value storage, Relational database, NoSQL, etc.)?
- What are the endpoints and HTTP methods?
- What headers or authentication is needed?
- How should responses be parsed?

**Repository Implementation:**
- How to handle network connectivity checks?
- What caching strategy should be used?
- How to map models to entities?
- What error handling is required?
- How to handle data synchronization?

#### Presentation Layer Planning:
**State Management:**
- What state management approach is needed? (Redux, MobX, Context API, Vuex, NgRx, Bloc, Cubit, etc.)
- What are the states (initial, loading, success, error)?
- What are the events/actions for state management?
- What side effects need to be handled?
- Are there navigation requirements?

**UI Components:**
- What screens/pages are needed?
- What components will be reused vs. feature-specific?
- What user interactions are required?
- How should errors be displayed?
- What loading indicators are needed?
- Are there any animations or transitions?

#### Deliverable:
- Layer-by-layer component breakdown
- Data flow diagram (conceptual)
- List of files to be created/modified

---

### 3. Dependencies & Infrastructure
**Objective:** Identify required packages and setup

#### Required Packages:
- Are new pub dependencies needed?
- What versions are compatible?
- Are there platform-specific dependencies?

#### Dependency Injection:
- What classes need to be registered with the DI container?
- What should be singleton vs. factory?
- What DI registration approach is needed? (Annotations, manual registration, etc.)
- Are there any initialization requirements?

#### Configuration:
- Are environment variables needed?
- Are there API keys or secrets?
- Is there different config for dev/prod?

#### Deliverable:
- List of dependencies to add to package configuration file (package.json, requirements.txt, pom.xml, etc.)
- Injectable registration plan
- Configuration requirements

---

### 4. Data Flow & Business Logic
**Objective:** Map out how data moves through the system

#### Flow Mapping:
```
User Action → Event/Method Call → Use Case → Repository → Data Source → API/Storage
                                                                            ↓
User Feedback ← State Update ← Either<Failure, Success> ← Model → Response
```

#### For Each Flow:
1. **Trigger:** What initiates this flow?
2. **Input Validation:** What needs to be validated?
3. **Processing Steps:** What happens at each layer?
4. **Success Path:** What happens on success?
5. **Error Path:** What failures can occur and how are they handled?
6. **State Changes:** How does the UI state change?
7. **Side Effects:** Are there navigation, notifications, or logging?

#### Deliverable:
- Sequence of operations for each user action
- Error handling strategy for each flow
- State transition diagram

---

### 5. Error Handling Strategy
**Objective:** Plan comprehensive error management

#### Identify Failure Types:
- **NetworkFailure:** No internet, timeout, connection issues
- **ServerFailure:** API errors, 4xx/5xx responses
- **CacheFailure:** Local storage errors
- **ValidationFailure:** Input validation errors
- **AuthenticationFailure:** Token expired, unauthorized
- **Custom Failures:** Domain-specific errors

#### Error Handling Plan:
- What custom Failure classes are needed?
- How are exceptions caught and mapped to Failures?
- What error messages should users see?
- Should errors be logged/reported?
- Are there retry mechanisms?

#### Deliverable:
- List of Failure classes to create
- Error mapping strategy per layer
- User-facing error messages

---

### 6. Code Analysis & Validation
**Objective:** Ensure code quality through static analysis

#### Analysis Strategy:
- Run static analysis/linter after completing implementation (lint, analyze, check, etc.)
- Check for compile errors, warnings, and hints
- Verify no type errors or null safety issues
- Ensure all imports are used and properly organized
- Confirm lint rules compliance

#### Commands:
```bash
# Run static analysis (examples for different languages)
# JavaScript/TypeScript: npm run lint or eslint .
# Python: pylint . or flake8 .
# Java: ./gradlew check or mvn verify
# C#: dotnet build --no-incremental
# Go: go vet ./...
# Rust: cargo clippy
# [Adjust based on your language/framework]
```

#### Validation Checklist:
- [ ] No compilation errors
- [ ] No analysis warnings
- [ ] All imports are valid and used
- [ ] Null safety properly implemented
- [ ] Lint rules compliance verified

#### Deliverable:
- Clean analysis output with zero errors
- List of any warnings that need attention
- Documentation of intentional lint suppressions (if any)

---

### 7. Implementation Checklist
**Objective:** Step-by-step implementation order

#### Recommended Order:
1. **Setup:**
   - [ ] Add dependencies to package configuration file (package.json, requirements.txt, pom.xml, etc.)
   - [ ] Install dependencies using package manager (npm install, pip install, etc.)
   - [ ] Create directory structure

2. **Core/Shared Components:**
   - [ ] Create Failure classes (if new ones needed)
   - [ ] Create custom exceptions
   - [ ] Add utility functions/extensions

3. **Domain Layer:**
   - [ ] Define entities (with immutability support)
   - [ ] Create repository interfaces
   - [ ] Implement use cases

4. **Data Layer:**
   - [ ] Create models (with JsonSerializable)
   - [ ] Implement data sources (remote/local)
   - [ ] Implement repository

5. **Presentation Layer:**
   - [ ] Create state classes (immutable)
   - [ ] Create event/action classes
   - [ ] Implement state manager/controller
   - [ ] Create UI components
   - [ ] Wire up state subscription/binding

6. **Dependency Injection:**
   - [ ] Add DI annotations/configuration
   - [ ] Run build tools (if applicable)
   - [ ] Verify DI setup

7. **Code Analysis:**
   - [ ] Run code analysis using your language's linter/analyzer
   - [ ] Fix all compilation errors and warnings
   - [ ] Verify null safety compliance
   - [ ] Ensure lint rules are followed

8. **Integration & Deployment:**
   - [ ] Test on device/emulator
   - [ ] Handle edge cases
   - [ ] Fix any issues

#### Deliverable:
- Ordered task list
- Clear action items

---

### 8. Code Generation Requirements
**Objective:** Identify what code needs to be generated

#### Required Generators:
- [ ] **Immutability code generation (if applicable):** For immutable states, events, entities
- [ ] **JsonSerializable:** For models with JSON conversion
- [ ] **Injectable:** For dependency injection setup

#### Build/Generation Commands:
```bash
# Generate code (examples for different stacks)
# Flutter/Dart: flutter pub run build_runner build --delete-conflicting-outputs
# TypeScript: npm run build or tsc
# Java: mvn generate-sources or ./gradlew generateSources
# C#: dotnet build
# Python: python setup.py build (if needed)
# Go: go generate ./...
# Rust: cargo build
# [Adjust based on your language/framework]
```

#### Deliverable:
- List of files requiring code generation
- Annotations to be used

---

## Implementation Template

Use this template when planning a feature:

```markdown
## Feature: [Feature Name]

### 1. Requirements
- **Description:** [Brief description]
- **User Story:** As a [user], I want to [action], so that [benefit]
- **Acceptance Criteria:**
  - [ ] Criterion 1
  - [ ] Criterion 2

### 2. Architecture Components

#### Domain Layer
**Entities:**
- `EntityName`: Properties: [list], Immutable: Yes/No

**Repositories:**
- `RepositoryName`: Methods: [list with signatures]

**Use Cases:**
- `UseCaseName`: Input: [type], Output: Either<Failure, [type]>

#### Data Layer
**Models:**
- `ModelName`: Maps to [Entity], Fields: [list], JsonSerializable: Yes

**Data Sources:**
- `RemoteDataSource`: APIs: [list endpoints]
- `LocalDataSource`: Storage: [type], Operations: [list]

**Repository Implementation:**
- Handles: [list scenarios]

#### Presentation Layer
**State Management:**
- Type: [State management approach]
- States: [list]
- Events: [list] (if applicable)

**UI:**
- Pages: [list]
- Components: [list]

### 3. Dependencies
- New packages: [list]
- DI registrations: [list classes]

### 4. Data Flows
**Flow 1: [Name]**
1. User [action]
2. Event: [event name]
3. Use case: [name]
4. Repository: [method]
5. Data source: [method]
6. Result: [success/failure]
7. State: [new state]

### 5. Error Handling
- Failures: [list custom failures]
- Error messages: [map failure to message]

### 6. Code Analysis
- Run code analysis and testing after implementation
- Fix all errors and warnings
- Verify null safety compliance

### 7. Implementation Steps
1. [Step 1]
2. [Step 2]
...

### 8. Code Generation
- Files requiring immutability code generation: [list]
- Files requiring JsonSerializable: [list]
- Run: Build/generation commands for your stack (if applicable)
```

---

## Best Practices for Planning

### Do:
- ✅ Start with the domain layer (business logic first)
- ✅ Define clear interfaces before implementations
- ✅ Plan error handling from the start
- ✅ Consider edge cases and error scenarios
- ✅ Keep components small and focused
- ✅ Follow SOLID principles in design
- ✅ Document complex business logic

### Don't:
- ❌ Skip requirement analysis
- ❌ Start with UI before domain logic
- ❌ Mix responsibilities between layers
- ❌ Forget about error handling
- ❌ Create tightly coupled components
- ❌ Ignore dependency injection setup
- ❌ Overlook code generation requirements

---

## Quick Reference: Decision Tree

### State Management: Which Approach?
- **Use Event-Driven/Complex State Manager (e.g., Bloc, Redux) when:**
  - Complex event-driven logic
  - Multiple events trigger same state
  - Need event transformation (debounce, throttle)
  - External events (streams, timers)

- **Use Simple State Manager (e.g., Cubit, Context API) when:**
  - Simple state management
  - Direct method calls to change state
  - Less boilerplate needed
  - Straightforward data fetching

### Data Source: Remote or Local?
- **Remote:** Network API calls
- **Local:** 
  - SharedPreferences: Simple key-value pairs
  - SQLite/Hive: Complex data structures
  - Secure Storage: Sensitive data (tokens, passwords)

### Repository Pattern:
- Always use when accessing data
- Single source of truth
- Handles network/cache logic
- Maps models to entities

---

## Example: Planning a "Login Feature"

### 1. Requirements
- User can login with email and password
- Show loading indicator during login
- Display error messages for invalid credentials
- Navigate to home screen on success
- Store authentication token locally

### 2. Architecture

#### Domain Layer
- **Entity:** `User` (id, email, name, token)
- **Repository:** `AuthRepository` with `login(email, password)`
- **Use Case:** `LoginUser` with email/password params

#### Data Layer
- **Model:** `UserModel` with JSON serialization
- **Remote:** `AuthRemoteDataSource.login()` → POST /api/login
- **Local:** `AuthLocalDataSource.saveToken()`
- **Repository:** Handle network errors, map model to entity

#### Presentation Layer
- **State Manager:** `AuthController` with events (LoginRequested) and states (Initial, Loading, Authenticated, Error)
- **Page:** `LoginPage` with email/password fields and login button

### 3. Dependencies
- http: For API calls
- shared_preferences: For token storage
- formz or validators: For input validation

### 4. Data Flow
1. User enters email/password and taps login
2. LoginRequested event triggered
3. LoginUser use case executed
4. AuthRepository.login() called
5. AuthRemoteDataSource makes API call
6. Token saved locally on success
7. AuthController updates state to Authenticated
8. Navigate to home screen

### 5. Error Handling
- ValidationFailure: Empty email/password
- NetworkFailure: No internet
- ServerFailure: Wrong credentials (401)
- AuthenticationFailure: Invalid token format

### 6. Files to Create
```
lib/
├── blocs/                                   # Bloc/Cubit state management
│   ├── auth_bloc.dart                      # [New] @injectable
│   ├── auth_event.dart                     # [New] @freezed
│   └── auth_state.dart                     # [New] @freezed
├── core/
│   ├── error/
│   │   └── failures.dart                   # [Modified] Add AuthenticationFailure
│   ├── utils/
│   │   └── [util].dart                     # [New] Utility functions
│   ├── widgets/
│   │   └── [common_widget].dart            # [New] Reusable widgets
│   └── di/
│       ├── injection_container.dart        # [New] DI configuration
│       └── injection_container.config.dart # [Generated] Injectable config
├── source/                                  # Data management
│   ├── local/
│   │   └── auth_local_data_source.dart     # [New] @injectable
│   ├── remote/
│   │   └── auth_remote_data_source.dart    # [New] @injectable
│   └── models/
│       └── user_model.dart                 # [New] @JsonSerializable
├── domain/                                  # Domain layer
│   ├── entities/
│   │   └── user.dart                       # [New] @freezed
│   ├── repositories/
│   │   ├── auth_repository.dart            # [New] Abstract interface
│   │   └── auth_repository_impl.dart       # [New] @injectable
│   └── usecases/
│       └── login_user.dart                 # [New] @injectable
└── pages/                                   # UI pages
    ├── widgets/
    │   └── [auth_widget].dart              # [New] Page-specific widgets
    └── login_page.dart                     # [New] Main page
```

---

## Conclusion

This implementation planning guide ensures:
- Systematic approach to feature development
- Adherence to Clean Architecture principles
- Comprehensive error handling
- Efficient implementation order
- Code quality and maintainability

Always complete the planning phase before writing code. A well-planned feature is easier to implement and maintain.
