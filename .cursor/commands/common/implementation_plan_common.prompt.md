---
agent: agent
--- 

# Implementation Planning Guide

This document provides a structured approach for AI to analyze, plan, and implement features following the project's architecture standards. Use this guide to ensure comprehensive planning before implementation.

## CRITICAL: Comprehensive Detail Requirements

**⚠️ ALL IMPLEMENTATION PLANS MUST BE DETAILED AND COMPREHENSIVE - NO SIMPLIFICATIONS**

When creating implementation plans, you MUST:

1. **Expand Every Section:** Every section must have comprehensive subsections with detailed explanations, examples, and justifications
2. **Provide Complete Specifications:** Every component must have complete specifications (properties, methods, relationships, dependencies)
3. **Document All Decisions:** Every architectural decision must be documented with rationale
4. **Include All Edge Cases:** All edge cases, error scenarios, and failure modes must be planned
5. **Specify All Dependencies:** All dependencies must be listed with versions and justifications
6. **Detail All Flows:** All data flows must be documented step-by-step with error handling
7. **Plan All Components:** All components must be planned with complete structure and responsibilities
8. **Consider Additional Features:** Always consider and document additional features/sections/parts/UI that could match project requirements

**DO NOT:**
- ❌ Simplify or summarize sections
- ❌ Skip subsections or details
- ❌ Provide minimal specifications
- ❌ Ignore edge cases or error scenarios
- ❌ Overlook additional features that could enhance the implementation

**DO:**
- ✅ Provide comprehensive, detailed planning
- ✅ Expand every section with full details
- ✅ Include all subsections and considerations
- ✅ Document additional features/sections/parts/UI that match requirements
- ✅ Provide extensive examples and justifications
- ✅ Create thorough, enterprise-grade implementation plans

## Planning Workflow

When implementing a new feature, follow this systematic approach:

### 1. Requirements Analysis (COMPREHENSIVE)
**Objective:** Deeply understand what needs to be built with complete specifications

#### 1.1 Core Functionality Analysis:
- **Primary Functionality:** [Detailed description of main feature]
- **Secondary Functionality:** [Additional features that enhance the main feature]
- **Nice-to-Have Features:** [Features that could be added for enhanced experience]
- **Feature Dependencies:** [Which features depend on others]
- **Feature Interactions:** [How features work together]

#### 1.2 User Stories & Use Cases (Detailed):
- **Primary User Stories:**
  - As a [user type], I want to [action], so that [benefit]
    - Acceptance criteria: [Detailed list]
    - User flow: [Step-by-step flow]
    - Edge cases: [List edge cases]
- **Secondary User Stories:** [Repeat pattern]
- **Admin/Management Stories:** [If applicable]
- **Use Case Diagrams:** [If applicable, describe use case relationships]

#### 1.3 Acceptance Criteria (Comprehensive):
- **Functional Acceptance Criteria:**
  - [ ] [Criterion 1] - Validation: [How to validate]
  - [ ] [Criterion 2] - Validation: [How to validate]
  - [ ] [Criterion 3] - Validation: [How to validate]
- **Non-Functional Acceptance Criteria:**
  - [ ] Performance: [Specific metrics, e.g., <200ms response time]
  - [ ] Security: [Security requirements]
  - [ ] Accessibility: [WCAG compliance level]
  - [ ] Platform Support: [All supported platforms]
- **Quality Acceptance Criteria:**
  - [ ] Test coverage: [Target percentage]
  - [ ] Code quality: [Lint rules, code standards]
  - [ ] Documentation: [What documentation is required]

#### 1.4 Edge Cases & Error Scenarios (Comprehensive):
- **Data Edge Cases:**
  - Empty data: [How to handle]
  - Invalid data: [Validation and error handling]
  - Large datasets: [Performance considerations]
  - Concurrent modifications: [Conflict resolution]
  - Data corruption: [Recovery strategy]
- **User Edge Cases:**
  - First-time users: [Onboarding]
  - Power users: [Advanced features]
  - Users with disabilities: [Accessibility]
  - Users on slow connections: [Performance]
  - Offline users: [Offline capabilities]
- **System Edge Cases:**
  - Network failures: [Error handling, retry logic]
  - Server errors: [Graceful degradation]
  - Timeout scenarios: [Handling timeouts]
  - Rate limiting: [User feedback]
  - Maintenance windows: [User communication]
- **Integration Edge Cases:**
  - Third-party service failures: [Fallback strategies]
  - API version changes: [Compatibility handling]
  - Data format changes: [Migration strategy]

#### 1.5 Performance Requirements (Detailed):
- **Response Time:**
  - API response: [Target, e.g., <200ms]
  - Page load: [Target, e.g., <2s]
  - Action completion: [Target, e.g., <500ms]
- **Throughput:**
  - Requests per second: [Target]
  - Concurrent users: [Target]
- **Resource Usage:**
  - CPU: [Limits]
  - Memory: [Limits]
  - Storage: [Limits]
  - Network: [Bandwidth considerations]

#### 1.6 Security Considerations (Comprehensive):
- **Authentication:** [Methods required, session management]
- **Authorization:** [Access control, role-based permissions]
- **Data Protection:** [Encryption requirements, data masking]
- **Input Security:** [Validation, sanitization, injection prevention]
- **API Security:** [Rate limiting, API keys, OAuth]
- **Compliance:** [GDPR, HIPAA, PCI-DSS, etc.]

#### 1.7 Platform Support (Detailed):
- **Target Platforms:**
  - iOS: [Versions, devices]
  - Android: [Versions, devices]
  - Web: [Browsers, versions]
  - Desktop: [OS, versions]
- **Platform-Specific Features:** [Features unique to each platform]
- **Responsive Design:** [Breakpoints, adaptive layouts]

#### 1.8 Additional Features & Enhancements:
- **Potential Additional Features:**
  - [Feature 1]: [Description, value, complexity, implementation effort]
  - [Feature 2]: [Description, value, complexity, implementation effort]
- **UI/UX Enhancements:**
  - [Enhancement 1]: [Description, impact, complexity]
  - [Enhancement 2]: [Description, impact, complexity]
- **Performance Optimizations:**
  - [Optimization 1]: [Description, expected impact]
  - [Optimization 2]: [Description, expected impact]

#### Deliverable:
- Comprehensive feature description with all details
- Complete list of functional requirements with specifications
- Detailed list of non-functional requirements (performance, security, accessibility, scalability, reliability)
- Complete edge cases and error scenarios documentation
- Additional features and enhancements analysis

---

### 2. Architecture Design
**Objective:** Plan the implementation following Clean Architecture

#### Domain Layer Planning (Comprehensive):

**Entities (Detailed Specifications):**
- **Entity 1: [Name]**
  - Properties: [Complete list with types, nullable/required, default values]
  - Relationships: [One-to-one, one-to-many, many-to-many with other entities]
  - Immutability: [Yes/No, which immutability pattern/library]
  - Value Objects: [Complex types that should be value objects]
  - Business Rules: [Validation rules, constraints]
  - Methods: [Business logic methods, if any]
  - Equality: [How equality is determined]
- **Entity 2: [Name]** [Repeat pattern]

**Repository Interfaces (Complete Specifications):**
- **Repository 1: [Name]**
  - **Method 1: [Name]**
    - Purpose: [What it does]
    - Parameters: [Complete parameter list with types]
    - Return Type: [Result<Success, Failure> or Either pattern]
    - Pagination: [If applicable, pagination strategy]
    - Error Cases: [What failures can occur]
    - Side Effects: [Any side effects]
  - **Method 2: [Name]** [Repeat pattern]
- **Repository 2: [Name]** [Repeat pattern]

**Use Cases (Complete Specifications):**
- **Use Case 1: [Name]**
  - Purpose: [What business logic it executes]
  - Input Parameters: [Complete parameter class/object with all fields]
  - Output: [Success type, Failure types]
  - Dependencies: [Other use cases, repositories]
  - Validations: [Input validations, business rule validations]
  - Business Logic: [Step-by-step business logic]
  - Error Handling: [How errors are handled]
  - Side Effects: [Navigation, logging, notifications]
- **Use Case 2: [Name]** [Repeat pattern]

#### Data Layer Planning (Comprehensive):

**Models (Complete Specifications):**
- **Model 1: [Name]**
  - Maps to Entity: [Which entity]
  - Fields: [Complete list with types, JSON field names]
  - JSON Serialization: [Library/annotations, fromJSON/toJSON methods]
  - Field Conversions: [snake_case to camelCase, date formats, etc.]
  - API Response Structure: [Complete JSON structure example]
  - toDomain() Method: [How model maps to entity]
  - Validation: [Model-level validations]
- **Model 2: [Name]** [Repeat pattern]

**Remote Data Source (Complete Specifications):**
- **Base URL:** [API base URL]
- **Endpoints:**
  - **Endpoint 1: [Path]**
    - HTTP Method: [GET/POST/PUT/DELETE/PATCH]
    - Purpose: [What it does]
    - Request Headers: [Complete list with values]
    - Request Body: [Structure if applicable]
    - Query Parameters: [List with types]
    - Response Structure: [Complete JSON structure]
    - Status Codes: [200, 400, 401, 404, 500, etc.]
    - Error Responses: [Error response structure]
    - Authentication: [JWT, OAuth, API key, etc.]
    - Rate Limiting: [Limits, handling]
  - **Endpoint 2: [Path]** [Repeat pattern]
- **HTTP Client:** [Library, configuration]
- **Response Parsing:** [How responses are parsed, error handling]

**Local Data Source (Complete Specifications):**
- **Storage Type:** [Key-value, SQLite, NoSQL, File system, etc.]
- **Storage Structure:**
  - **Table/Collection 1: [Name]**
    - Schema: [Complete schema with fields, types, constraints]
    - Indexes: [Required indexes]
    - Relationships: [Foreign keys, relationships]
  - **Table/Collection 2: [Name]** [Repeat pattern]
- **Operations:**
  - **Operation 1: [Name]**
    - Purpose: [What it does]
    - Parameters: [Complete parameter list]
    - Return Type: [What it returns]
    - Error Handling: [How errors are handled]
  - **Operation 2: [Name]** [Repeat pattern]
- **Migration Strategy:** [If applicable, how schema changes are handled]

**Repository Implementation (Complete Strategy):**
- **Network Connectivity:**
  - Check Method: [How connectivity is checked]
  - Offline Behavior: [What happens when offline]
  - Retry Logic: [Retry strategy, exponential backoff]
- **Caching Strategy:**
  - What to Cache: [List of cacheable data]
  - Cache Duration: [TTL, expiration]
  - Cache Invalidation: [When and how cache is invalidated]
  - Cache Storage: [Where cache is stored]
- **Data Mapping:**
  - Model to Entity: [Mapping logic, transformations]
  - Entity to Model: [If applicable]
  - Error Mapping: [How exceptions map to Failures]
- **Error Handling:**
  - Network Errors: [How network errors are handled]
  - Server Errors: [How server errors are handled]
  - Local Storage Errors: [How local errors are handled]
  - Error Mapping: [Exception to Failure mapping]
- **Data Synchronization:**
  - Sync Strategy: [Online-first, offline-first, hybrid]
  - Conflict Resolution: [How conflicts are resolved]
  - Background Sync: [If applicable, sync strategy]

#### Presentation Layer Planning (Comprehensive):

**State Management (Complete Specifications):**
- **Approach:** [Redux, MobX, Context API, Vuex, NgRx, Bloc, Cubit, etc.]
  - Rationale: [Why this approach]
  - Scope: [Global, feature-specific, local]
- **States (Complete State Definitions):**
  - **State 1: [Name]**
    - Type: [Initial, Loading, Success, Error, etc.]
    - Properties: [Complete list with types]
    - Immutability: [Yes/No, pattern used]
    - When Used: [When this state is active]
  - **State 2: [Name]** [Repeat pattern]
- **Events/Actions (Complete Event Definitions):**
  - **Event 1: [Name]**
    - Purpose: [What it triggers]
    - Payload: [Complete payload structure]
    - Side Effects: [What happens when triggered]
  - **Event 2: [Name]** [Repeat pattern]
- **State Transitions:**
  - [State A] → [Event] → [State B]
  - [Complete state transition diagram]
- **Side Effects:**
  - Navigation: [When navigation occurs, to where]
  - Notifications: [When notifications are shown]
  - Logging: [What is logged]
  - Analytics: [What events are tracked]

**UI Components (Complete Specifications):**
- **Pages/Screens:**
  - **Page 1: [Name]**
    - Purpose: [What it displays/does]
    - Layout: [Layout structure, sections]
    - Components Used: [List of child components]
    - User Interactions: [All user actions]
    - State Dependencies: [Which states it depends on]
    - Navigation: [Where it navigates to/from]
    - Error Display: [How errors are shown]
    - Loading States: [Loading indicators, skeleton screens]
    - Animations: [Entrance, transitions, micro-interactions]
  - **Page 2: [Name]** [Repeat pattern]
- **Reusable Components:**
  - **Component 1: [Name]**
    - Purpose: [What it does]
    - Props/Parameters: [Complete list with types]
    - States: [Internal states if any]
    - Styling: [Style specifications]
    - Accessibility: [ARIA labels, keyboard navigation]
  - **Component 2: [Name]** [Repeat pattern]
- **Feature-Specific Components:**
  - **Component 1: [Name]** [Same structure as reusable]
  - **Component 2: [Name]** [Same structure]
- **User Interactions (Complete List):**
  - [Interaction 1]: [What user does, what happens]
  - [Interaction 2]: [What user does, what happens]
- **Error Display Strategy:**
  - Error Types: [List of error types]
  - Display Method: [Toast, inline, modal, etc.]
  - Error Messages: [User-friendly messages]
  - Recovery Actions: [Retry, dismiss, etc.]
- **Loading Indicators:**
  - Types: [Skeleton screens, spinners, progress bars]
  - When Shown: [When each type is used]
  - Styling: [Visual specifications]
- **Animations & Transitions:**
  - Entrance Animations: [How elements appear]
  - Page Transitions: [Transitions between pages]
  - Micro-interactions: [Button presses, hovers, etc.]
  - Scroll Animations: [Parallax, reveal, etc.]
  - Performance: [60fps target, optimization]

#### Deliverable:
- Complete layer-by-layer component breakdown with full specifications
- Detailed data flow diagrams (success paths, error paths, state transitions)
- Complete list of files to be created/modified with file paths
- Complete component specifications (properties, methods, relationships)
- Complete state management specifications (states, events, transitions)
- Complete UI component specifications (pages, components, interactions)

---

### 3. Dependencies & Infrastructure (COMPREHENSIVE)
**Objective:** Identify all required packages, infrastructure, and setup with complete specifications

#### 3.1 Required Packages (Complete List):
- **State Management:**
  - Package: [Name, version]
  - Purpose: [Why needed]
  - Compatibility: [Compatible with other packages]
- **HTTP Client:**
  - Package: [Name, version]
  - Purpose: [Why needed]
  - Features: [Required features]
- **Local Storage:**
  - Package: [Name, version]
  - Purpose: [Why needed]
  - Storage Type: [What it provides]
- **Dependency Injection:**
  - Package: [Name, version]
  - Purpose: [Why needed]
  - Features: [Code generation, annotations, etc.]
- **Serialization:**
  - Package: [Name, version]
  - Purpose: [Why needed]
  - Features: [JSON serialization, code generation]
- **Utilities:**
  - Package: [Name, version]
  - Purpose: [Why needed]
- **Platform-Specific Dependencies:**
  - iOS: [If applicable]
  - Android: [If applicable]
  - Web: [If applicable]
- **Dev Dependencies:**
  - Build Tools: [List]
  - Code Generation: [List]
  - Testing: [List]
  - Linting: [List]

#### 3.2 Dependency Injection (Complete Registration Plan):
- **Registration Approach:** [Annotations, manual, code generation]
- **Classes to Register:**
  - **Class 1: [Name]**
    - Registration Type: [Singleton, Factory, LazySingleton]
    - Dependencies: [What it depends on]
    - Purpose: [Why registered]
    - Lifecycle: [When created, when disposed]
  - **Class 2: [Name]** [Repeat pattern]
- **Module Organization:** [How DI modules are organized]
- **Initialization:**
  - Setup Steps: [Step-by-step initialization]
  - Order: [Initialization order]
  - Error Handling: [How initialization errors are handled]

#### 3.3 Configuration (Complete Configuration Plan):
- **Environment Variables:**
  - Variable 1: [Name, purpose, default value, required]
  - Variable 2: [Name, purpose, default value, required]
- **API Keys & Secrets:**
  - Key 1: [Name, purpose, storage method, security]
  - Key 2: [Name, purpose, storage method, security]
- **Environment-Specific Config:**
  - Development: [Config values]
  - Staging: [Config values]
  - Production: [Config values]
- **Configuration Management:**
  - Config Files: [Location, format]
  - Loading Strategy: [How config is loaded]
  - Validation: [Config validation]

#### 3.4 Infrastructure Setup:
- **Build Configuration:**
  - Build Scripts: [List]
  - Code Generation: [Commands, when to run]
  - Build Variants: [If applicable]
- **Project Structure:**
  - Directory Layout: [Complete structure]
  - File Naming: [Conventions]
- **Development Tools:**
  - IDE Setup: [Required plugins, settings]
  - Debugging: [Debug configuration]
  - Testing: [Test setup]

#### Deliverable:
- Complete list of dependencies with versions and justifications
- Complete dependency injection registration plan with all classes
- Complete configuration requirements (environment variables, API keys, secrets)
- Complete infrastructure setup plan
- Package configuration file updates (package.json, requirements.txt, pom.xml, etc.)

---

### 4. Data Flow & Business Logic (COMPREHENSIVE)
**Objective:** Map out complete data flows through the system with detailed specifications

#### 4.1 Flow Mapping (Complete Diagrams):
```
Detailed Flow Diagram:
┌─────────────┐
│   User UI   │
└──────┬──────┘
       │ 1. User Action (detailed description)
       ▼
┌─────────────────┐
│  View/Page      │
└──────┬──────────┘
       │ 2. Trigger Event/Method (event name, payload)
       ▼
┌─────────────────────┐
│ Controller/Manager  │◄──────┐
└──────┬──────────────┘       │
       │ 3. setState(loading) │ 9. setState(success/error)
       ▼                      │
┌─────────────────┐           │
│    Use Case     │           │
└──────┬──────────┘           │
       │ 4. Call repository   │
       │    (with validation)  │
       ▼                      │
┌─────────────────┐           │
│   Repository    │           │
└──────┬──────────┘           │
       │ 5. Check network/    │
       │    cache strategy     │
       ▼                      │
   ┌───┴────┐                │
   │ Remote │ Local          │
   │ Source │ Source         │
   └───┬────┴────┬───────────┘
       │ 6. Fetch│ 6. Fetch
       ▼         ▼        
   ┌─────────────────┐   
   │   Data/Error     │   
   └──────┬──────────┘   
          │ 7. Map to Entity
          ▼              
   ┌─────────────────┐   
   │ Result<Success, │   
   │     Failure>    │   
   └──────┬──────────┘   
          │ 8. Return result
          └──────────────┘
```

#### 4.2 For Each Flow (Complete Specifications):

**Flow 1: [Flow Name]**
- **Trigger:**
  - User Action: [Detailed description]
  - Event/Method: [Event name or method name]
  - Payload: [Complete payload structure]
- **Input Validation:**
  - Validation Rules: [Complete list of validations]
  - Validation Errors: [What errors can occur]
  - Error Handling: [How validation errors are handled]
- **Processing Steps (Detailed):**
  1. **Presentation Layer:**
     - Component: [Which component]
     - Action: [What happens]
     - State Change: [What state changes]
  2. **Domain Layer:**
     - Use Case: [Which use case]
     - Business Logic: [Step-by-step logic]
     - Validations: [Business rule validations]
  3. **Data Layer:**
     - Repository: [Which repository method]
     - Data Source: [Remote or local]
     - Data Transformation: [How data is transformed]
  4. **Response Processing:**
     - Success: [How success is processed]
     - Error: [How error is processed]
- **Success Path (Detailed):**
  - Data Flow: [How data flows back]
  - State Updates: [All state changes]
  - UI Updates: [What UI changes]
  - Side Effects: [Navigation, notifications, etc.]
- **Error Path (Detailed):**
  - Error Types: [All possible errors]
  - Error Handling: [How each error is handled]
  - Error Mapping: [Exception to Failure mapping]
  - User Feedback: [How errors are shown to user]
  - Recovery: [Retry logic, fallback strategies]
- **State Changes:**
  - Initial State: [Starting state]
  - Intermediate States: [Loading, processing, etc.]
  - Final States: [Success, error states]
  - State Transition Diagram: [Visual representation]
- **Side Effects:**
  - Navigation: [Where navigation occurs, when]
  - Notifications: [What notifications are shown]
  - Logging: [What is logged]
  - Analytics: [What events are tracked]
  - Background Tasks: [Any background processing]

**Flow 2: [Flow Name]** [Repeat complete pattern]

#### 4.3 State Transition Diagrams:
```
Complete State Machine:
                    ┌─────────┐
                    │ Initial │
                    └────┬────┘
                         │ Event triggered
                         ▼
                    ┌─────────┐
              ┌────►│ Loading │◄────┐
              │     └────┬────┘     │
              │          │          │ Retry
              │          ▼          │
         ┌────┴─────┬─────────┬────┴────┐
         │          │         │         │
    ┌────▼───┐ ┌───▼────┐ ┌──▼─────┐   │
    │Success │ │ Error  │ │ Empty  │   │
    └────┬───┘ └───┬────┘ └──┬─────┘   │
         │         │         │          │
         └─────────┴─────────┴──────────┘
           Refresh/New Action
```

#### Deliverable:
- Complete sequence of operations for each user action with detailed steps
- Comprehensive error handling strategy for each flow with all error types
- Complete state transition diagrams for all flows
- Complete data flow diagrams (success paths, error paths)
- Complete side effects documentation

---

### 5. Error Handling Strategy (COMPREHENSIVE)
**Objective:** Plan comprehensive error management with complete specifications

#### 5.1 Identify Failure Types (Complete List):
- **NetworkFailure:**
  - Scenarios: [No internet, timeout, connection issues, DNS failures]
  - User Message: [User-friendly message]
  - Recovery: [Retry logic, offline handling]
- **ServerFailure:**
  - Scenarios: [API errors, 4xx/5xx responses, service unavailable]
  - Status Codes: [400, 401, 403, 404, 500, 502, 503, etc.]
  - User Message: [User-friendly message per status code]
  - Recovery: [Retry logic, fallback]
- **CacheFailure:**
  - Scenarios: [Local storage errors, read/write failures, corruption]
  - User Message: [User-friendly message]
  - Recovery: [Clear cache, fallback to remote]
- **ValidationFailure:**
  - Scenarios: [Input validation errors, business rule violations]
  - Validation Types: [Field-level, form-level, business rules]
  - User Message: [User-friendly message per validation]
  - Recovery: [User correction, inline validation]
- **AuthenticationFailure:**
  - Scenarios: [Token expired, unauthorized, invalid credentials]
  - User Message: [User-friendly message]
  - Recovery: [Re-login, token refresh]
- **Custom Failures:**
  - **Failure 1: [Name]**
    - Scenarios: [When it occurs]
    - User Message: [User-friendly message]
    - Recovery: [How to recover]
  - **Failure 2: [Name]** [Repeat pattern]

#### 5.2 Error Handling Plan (Complete Strategy):
- **Custom Failure Classes:**
  - **Class 1: [Name]**
    - Extends: [Base Failure class]
    - Properties: [Message, code, details]
    - When Used: [When this failure occurs]
  - **Class 2: [Name]** [Repeat pattern]
- **Exception to Failure Mapping:**
  - **Layer: Data Source**
    - Exception Type: [NetworkException, HttpException, etc.]
    - Maps To: [NetworkFailure, ServerFailure, etc.]
    - Mapping Logic: [How exception is converted]
  - **Layer: Repository**
    - Exception Type: [CacheException, etc.]
    - Maps To: [CacheFailure, etc.]
    - Mapping Logic: [How exception is converted]
  - **Layer: Use Case**
    - Validation: [How validation errors become ValidationFailure]
    - Business Rules: [How business rule violations become Failures]
- **User-Facing Error Messages:**
  - **Failure Type → Message Mapping:**
    - NetworkFailure: "[User-friendly message]"
    - ServerFailure: "[User-friendly message]"
    - [All failure types with messages]
  - **Message Localization:** [If applicable, i18n strategy]
- **Error Logging & Reporting:**
  - What to Log: [Error details, stack traces, user context]
  - Logging Level: [Error, warning, info]
  - Error Reporting: [Crash reporting, analytics]
  - Privacy: [What not to log - PII, sensitive data]
- **Retry Mechanisms:**
  - Retry Strategy: [Exponential backoff, fixed interval]
  - Max Retries: [Number of retries]
  - Retry Conditions: [When to retry, when not to]
  - User Feedback: [How retry status is shown]

#### 5.3 Error Display Strategy:
- **Error Display Methods:**
  - Toast/Snackbar: [For transient errors]
  - Inline Errors: [For form validation]
  - Modal/Dialog: [For critical errors]
  - Error Page: [For fatal errors]
- **Error Recovery Actions:**
  - Retry Button: [When shown, what it does]
  - Dismiss: [When errors can be dismissed]
  - Go Back: [Navigation on error]
  - Contact Support: [For persistent errors]

#### Deliverable:
- Complete list of Failure classes with full specifications
- Complete error mapping strategy per layer with all exception types
- Complete user-facing error messages for all failure types
- Complete error logging and reporting strategy
- Complete retry mechanism specifications
- Complete error display and recovery strategy

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

### 7. Implementation Checklist (COMPREHENSIVE)
**Objective:** Step-by-step implementation order with complete task breakdown

#### 7.1 Phase 1: Setup & Infrastructure
- [ ] **Project Structure:**
  - [ ] Create directory structure (all layers)
  - [ ] Set up feature directory
  - [ ] Create placeholder files if needed
- [ ] **Dependencies:**
  - [ ] Add dependencies to package configuration file (package.json, requirements.txt, pom.xml, etc.)
  - [ ] Add dev dependencies
  - [ ] Install dependencies using package manager (npm install, pip install, etc.)
  - [ ] Verify dependency versions are compatible
- [ ] **Configuration:**
  - [ ] Set up environment variables
  - [ ] Configure API keys/secrets
  - [ ] Set up environment-specific configs (dev/staging/prod)
- [ ] **Build Setup:**
  - [ ] Configure build scripts
  - [ ] Set up code generation (if applicable)
  - [ ] Configure linting/formatting

#### 7.2 Phase 2: Core/Shared Components
- [ ] **Failure Classes:**
  - [ ] Create base Failure class (if not exists)
  - [ ] Create NetworkFailure
  - [ ] Create ServerFailure
  - [ ] Create CacheFailure
  - [ ] Create ValidationFailure
  - [ ] Create AuthenticationFailure
  - [ ] Create custom failures: [List all custom failures]
- [ ] **Exception Classes:**
  - [ ] Create custom exceptions: [List all exceptions]
- [ ] **Utility Functions:**
  - [ ] Add utility functions/extensions: [List all utilities]
- [ ] **Common Components:**
  - [ ] Create reusable UI components: [List components]

#### 7.3 Phase 3: Domain Layer
- [ ] **Entities:**
  - [ ] Create Entity 1: [Name] (with immutability support)
    - [ ] Define all properties
    - [ ] Add business logic methods (if any)
    - [ ] Implement equality/comparison
    - [ ] Run code generation (if applicable)
  - [ ] Create Entity 2: [Name] [Repeat pattern]
- [ ] **Repository Interfaces:**
  - [ ] Create Repository 1: [Name]
    - [ ] Define all methods with signatures
    - [ ] Document each method
  - [ ] Create Repository 2: [Name] [Repeat pattern]
- [ ] **Use Cases:**
  - [ ] Create UseCase 1: [Name]
    - [ ] Define parameters class
    - [ ] Implement business logic
    - [ ] Add validations
    - [ ] Add DI registration
  - [ ] Create UseCase 2: [Name] [Repeat pattern]

#### 7.4 Phase 4: Data Layer
- [ ] **Models:**
  - [ ] Create Model 1: [Name] (with JsonSerializable)
    - [ ] Define all fields
    - [ ] Add JSON annotations
    - [ ] Implement fromJSON/toJSON
    - [ ] Implement toDomain()
    - [ ] Run code generation
  - [ ] Create Model 2: [Name] [Repeat pattern]
- [ ] **Remote Data Source:**
  - [ ] Create RemoteDataSource: [Name]
    - [ ] Implement method 1: [Name]
    - [ ] Implement method 2: [Name]
    - [ ] Add error handling
    - [ ] Add request/response parsing
  - [ ] Create RemoteDataSource: [Name] [Repeat if multiple]
- [ ] **Local Data Source:**
  - [ ] Create LocalDataSource: [Name]
    - [ ] Set up storage (database/file)
    - [ ] Implement method 1: [Name]
    - [ ] Implement method 2: [Name]
    - [ ] Add error handling
  - [ ] Create LocalDataSource: [Name] [Repeat if multiple]
- [ ] **Repository Implementation:**
  - [ ] Create RepositoryImpl: [Name]
    - [ ] Implement all repository methods
    - [ ] Add network connectivity checks
    - [ ] Implement caching strategy
    - [ ] Add error mapping
    - [ ] Add data synchronization (if applicable)

#### 7.5 Phase 5: Presentation Layer
- [ ] **State Management:**
  - [ ] Create state classes (immutable)
    - [ ] State 1: [Name]
    - [ ] State 2: [Name]
  - [ ] Create event/action classes
    - [ ] Event 1: [Name]
    - [ ] Event 2: [Name]
  - [ ] Implement state manager/controller
    - [ ] Implement event handler 1
    - [ ] Implement event handler 2
    - [ ] Add side effects (navigation, logging, etc.)
- [ ] **UI Components:**
  - [ ] Create pages/screens
    - [ ] Page 1: [Name]
      - [ ] Layout structure
      - [ ] State binding
      - [ ] User interactions
      - [ ] Error handling
      - [ ] Loading states
    - [ ] Page 2: [Name] [Repeat pattern]
  - [ ] Create reusable components
    - [ ] Component 1: [Name]
    - [ ] Component 2: [Name]
  - [ ] Create feature-specific components
    - [ ] Component 1: [Name]
    - [ ] Component 2: [Name]
- [ ] **State Integration:**
  - [ ] Wire up state subscription/binding
  - [ ] Add navigation logic
  - [ ] Add error display logic
  - [ ] Add loading indicators

#### 7.6 Phase 6: Dependency Injection & Code Generation
- [ ] **Dependency Injection:**
  - [ ] Add DI annotations/configuration to all classes
  - [ ] Register all dependencies
  - [ ] Set up DI modules (if applicable)
  - [ ] Run build tools (if applicable)
  - [ ] Verify DI container registration
  - [ ] Test dependency resolution
- [ ] **Code Generation:**
  - [ ] Run immutability code generation (if applicable)
  - [ ] Run JSON serialization code generation
  - [ ] Run DI code generation
  - [ ] Verify all generated code compiles
  - [ ] Fix any generation errors

#### 7.7 Phase 7: Code Analysis & Quality
- [ ] **Static Analysis:**
  - [ ] Run code analysis using your language's linter/analyzer
  - [ ] Fix all compilation errors
  - [ ] Fix all warnings
  - [ ] Fix all hints/suggestions
- [ ] **Code Quality:**
  - [ ] Verify null safety compliance
  - [ ] Ensure lint rules are followed
  - [ ] Check code style consistency
  - [ ] Verify naming conventions
  - [ ] Check for unused imports/code
- [ ] **Documentation:**
  - [ ] Add code comments for complex logic
  - [ ] Document public APIs
  - [ ] Update README if needed

#### 7.8 Phase 8: Testing & Integration
- [ ] **Unit Tests:**
  - [ ] Test entities
  - [ ] Test use cases
  - [ ] Test repositories
  - [ ] Test state management
- [ ] **Integration Tests:**
  - [ ] Test data flow
  - [ ] Test error handling
  - [ ] Test state transitions
- [ ] **Manual Testing:**
  - [ ] Test on device/emulator
  - [ ] Test all user flows
  - [ ] Test error scenarios
  - [ ] Test edge cases
  - [ ] Test on all target platforms
- [ ] **Performance Testing:**
  - [ ] Test response times
  - [ ] Test memory usage
  - [ ] Test with large datasets
- [ ] **Accessibility Testing:**
  - [ ] Test with screen readers
  - [ ] Test keyboard navigation
  - [ ] Test color contrast
  - [ ] Verify WCAG compliance

#### 7.9 Phase 9: Polish & Finalization
- [ ] **Edge Cases:**
  - [ ] Handle all identified edge cases
  - [ ] Add error recovery
  - [ ] Add fallback strategies
- [ ] **Performance Optimization:**
  - [ ] Optimize rendering
  - [ ] Optimize data loading
  - [ ] Optimize animations
- [ ] **Final Review:**
  - [ ] Code review
  - [ ] Architecture review
  - [ ] UI/UX review
  - [ ] Fix any issues found

#### Deliverable:
- Complete ordered task list with all subtasks
- Clear action items with acceptance criteria
- Phase-by-phase breakdown with dependencies
- Complete testing checklist

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

---

## CRITICAL: Comprehensive Detail Requirements Reminder

**⚠️ ALL IMPLEMENTATION PLANS MUST BE DETAILED AND COMPREHENSIVE**

**The implementation plan should be so comprehensive that a developer can implement the feature without asking additional questions.**

**Remember:**
- ✅ Expand every section with full details
- ✅ Include all subsections and considerations
- ✅ Document additional features/sections/parts/UI that match requirements
- ✅ Provide extensive examples and justifications
- ✅ Create thorough, enterprise-grade implementation plans
- ❌ DO NOT simplify or summarize
- ❌ DO NOT skip details or subsections
- ❌ DO NOT overlook additional features that could enhance the implementation
