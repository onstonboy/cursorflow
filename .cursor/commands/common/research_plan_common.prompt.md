---
agent: agent
---

# Feature Research & Analysis Guide

This document provides a structured approach for AI to research, analyze, and evaluate multiple implementation approaches for any feature request across any programming language, framework, or technology stack. Use this guide to ensure thorough analysis before selecting the optimal solution.

## CRITICAL: Mandatory Execution

**⚠️ AI MUST COMPLETE ALL STEPS SEQUENTIALLY - NO EXCEPTIONS**

When you receive a feature request, you MUST:
1. Execute ALL 7 steps in order (Steps 1-7)
2. Generate ALL deliverables for each step
3. Create complete documentation as specified
4. Do NOT skip or summarize any step
5. Do NOT ask for permission to proceed - execute automatically
6. Complete the entire workflow before returning results to the user

**Failure to complete all steps is considered incomplete work.**

## Research Workflow

When analyzing a feature request, follow this systematic 7-step approach (ALL STEPS ARE MANDATORY):

---

## Step 1: Analyze Given Requirements (MANDATORY)

**Objective:** Deeply understand the problem and extract all requirements

**⚠️ YOU MUST COMPLETE THIS STEP - Generate the full Requirements Analysis Summary deliverable.**

### Analysis Checklist:

#### 1.1 Problem Statement
**Core Questions:**
- What is the user trying to achieve? (Primary goal)
- What pain point or need does this address? (User pain points, business needs)
- What is the current behavior vs. desired behavior? (Before/after comparison)
- Are there any implicit requirements not explicitly stated? (Hidden needs, assumptions)

**Detailed Analysis:**
- **User Personas:** Who are the target users? (End users, admins, developers, etc.)
- **Use Cases:** What are the primary, secondary, and edge use cases?
- **Business Context:** What business problem does this solve? (Revenue, efficiency, compliance, etc.)
- **Stakeholder Needs:** What do different stakeholders need? (Users, admins, business owners, developers)
- **Current State Analysis:** What exists today? (Existing features, limitations, technical debt)
- **Future State Vision:** What should the ideal solution look like?
- **Success Metrics:** How will success be measured? (User satisfaction, performance, adoption rate)
- **Failure Scenarios:** What happens if this feature doesn't exist or fails?

#### 1.2 Requirement Classification

**Functional Requirements (Detailed Breakdown):**

**Core Features & Capabilities:**
- Primary features (must-have functionality)
- Secondary features (should-have functionality)
- Nice-to-have features (could enhance experience)
- Future features (out of scope but worth noting)
- Feature dependencies (which features depend on others)
- Feature interactions (how features work together)

**User Interactions & Workflows:**
- User journey mapping (step-by-step user flows)
- Entry points (how users access the feature)
- Navigation patterns (how users move through the feature)
- User actions (all possible user interactions)
- System responses (how system responds to each action)
- Error recovery flows (how users recover from errors)
- Onboarding flows (first-time user experience)
- Advanced user flows (power user features)

**Data Inputs & Outputs:**
- Input types (text, files, images, audio, video, sensors, etc.)
- Input validation rules (format, size, type, range, required fields)
- Input sources (user input, API, files, sensors, third-party)
- Output formats (display, export, API response, notifications)
- Output destinations (screen, file, API, email, push notification)
- Data transformation requirements (format conversion, aggregation, filtering)
- Data persistence requirements (what needs to be saved, for how long)

**Business Rules & Validations:**
- Business logic rules (calculation rules, decision trees, workflows)
- Validation rules (input validation, business rule validation)
- Permission rules (who can do what, role-based access)
- Data integrity rules (constraints, relationships, consistency)
- Workflow rules (approval processes, state transitions)
- Compliance rules (regulatory, legal, industry standards)
- Custom business logic (domain-specific rules)

**Non-Functional Requirements (Comprehensive):**

**Performance Requirements:**
- Response time (API response, page load, action completion)
- Throughput (requests per second, transactions per minute)
- Latency (network latency, processing latency)
- Resource usage (CPU, memory, storage, bandwidth)
- Load handling (concurrent users, peak load capacity)
- Performance benchmarks (specific metrics to achieve)
- Performance degradation tolerance (acceptable slowdown under load)

**Scalability Requirements:**
- Data volume (current and projected data size)
- Concurrent users (current and projected user count)
- Geographic distribution (multi-region, global scale)
- Growth projections (expected growth rate, scaling timeline)
- Horizontal vs. vertical scaling needs
- Auto-scaling requirements
- Database scaling strategy

**Security Requirements:**
- Authentication (login methods, session management, multi-factor auth)
- Authorization (role-based access, permission levels, data access control)
- Data protection (encryption at rest, encryption in transit, data masking)
- Input security (SQL injection prevention, XSS prevention, CSRF protection)
- API security (rate limiting, API keys, OAuth, JWT)
- Secure storage (password hashing, token storage, sensitive data handling)
- Security compliance (GDPR, HIPAA, PCI-DSS, SOC 2, etc.)
- Security audit requirements (penetration testing, security reviews)
- Vulnerability management (patch management, security updates)

**Accessibility Requirements:**
- WCAG compliance level (A, AA, AAA)
- Screen reader support (ARIA labels, semantic HTML)
- Keyboard navigation (tab order, keyboard shortcuts, focus management)
- Visual accessibility (color contrast, font sizes, zoom support)
- Motor accessibility (click targets, gesture alternatives)
- Cognitive accessibility (clear language, error messages, help text)
- Platform accessibility features (VoiceOver, TalkBack, etc.)

**Platform Compatibility:**
- Target platforms (Web browsers, iOS, Android, Windows, macOS, Linux, etc.)
- Browser support (Chrome, Firefox, Safari, Edge, versions)
- OS versions (minimum supported versions)
- Device types (desktop, tablet, mobile, wearables, IoT)
- Screen sizes (responsive breakpoints, adaptive layouts)
- Input methods (mouse, keyboard, touch, voice, gestures)
- Hardware requirements (camera, GPS, sensors, etc.)

**Reliability & Availability:**
- Uptime requirements (99.9%, 99.99%, etc.)
- Error rate tolerance (acceptable error percentage)
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- Backup and disaster recovery
- Failover mechanisms
- Monitoring and alerting requirements

**Usability Requirements:**
- User experience goals (ease of use, learnability, efficiency)
- User interface standards (design system, component library)
- User testing requirements (usability testing, A/B testing)
- Help and documentation (in-app help, user guides, tooltips)
- Error message quality (clear, actionable error messages)
- Loading states and feedback (progress indicators, status messages)

**Maintainability Requirements:**
- Code quality standards (linting, code reviews, test coverage)
- Documentation requirements (code comments, API docs, user docs)
- Testing requirements (unit tests, integration tests, E2E tests)
- Monitoring and logging (error tracking, performance monitoring, analytics)
- Deployment requirements (CI/CD, rollback strategy, feature flags)

**Technical Requirements (Detailed):**

**Integration Points:**
- Existing system integrations (APIs, databases, services)
- Third-party service integrations (payment, analytics, email, etc.)
- Legacy system compatibility (if applicable)
- API contracts (REST, GraphQL, gRPC, WebSocket)
- Data format compatibility (JSON, XML, Protocol Buffers, etc.)
- Integration patterns (synchronous, asynchronous, event-driven)
- Error handling for integrations (retry logic, circuit breakers)

**Data Storage & Persistence:**
- Storage type (relational DB, NoSQL, file storage, cache)
- Data volume estimates (current and projected)
- Data retention policies (how long to keep data)
- Backup and recovery requirements
- Data migration needs (if applicable)
- Data archival strategy
- Cache requirements (what to cache, cache invalidation)

**Network Connectivity:**
- Online/offline requirements (online-only, offline-capable, hybrid)
- Network protocol requirements (HTTP/HTTPS, WebSocket, etc.)
- Bandwidth considerations (data transfer size, compression)
- Network reliability handling (retry logic, offline queue)
- API versioning strategy
- Rate limiting and throttling

**Third-Party Dependencies:**
- Required libraries/frameworks (with versions)
- Service dependencies (external APIs, SaaS services)
- License compatibility (open source licenses, commercial licenses)
- Dependency management (version pinning, security updates)
- Vendor lock-in considerations
- Alternative options (backup solutions if primary fails)

#### 1.3 Constraint Identification

**Budget & Resource Constraints:**
- Development budget (team size, timeline, cost per developer)
- Infrastructure costs (hosting, third-party services, API costs)
- Maintenance budget (ongoing costs, support resources)
- Resource availability (developer skills, team capacity)
- External resource needs (designers, QA, DevOps, consultants)
- Cost optimization requirements (free tiers, open source alternatives)

**Time Constraints:**
- Project deadline (hard deadline, soft deadline)
- Sprint/timeline constraints (agile sprints, release cycles)
- Time-to-market requirements (competitive pressure, business needs)
- Phased delivery requirements (MVP timeline, full feature timeline)
- Dependencies on other projects/teams
- Holiday/blackout periods

**Technical Constraints:**
- Hardware capabilities (CPU, memory, storage, network)
- OS versions (minimum supported versions, deprecated APIs)
- Runtime environment (Node.js version, Python version, JVM version, etc.)
- Framework/library versions (compatibility requirements)
- Browser limitations (older browser support, feature availability)
- Mobile device constraints (older devices, performance limitations)
- Network constraints (slow connections, data caps, firewall restrictions)
- Platform-specific limitations (App Store policies, browser restrictions)
- Legacy system constraints (must work with existing systems)

**Compliance & Regulatory Requirements:**
- Data privacy regulations (GDPR, CCPA, LGPD, etc.)
- Industry-specific regulations (HIPAA for healthcare, PCI-DSS for payments)
- Accessibility regulations (ADA, Section 508, EN 301 549)
- Security standards (ISO 27001, SOC 2, NIST)
- Export control regulations (if applicable)
- Regional compliance (country-specific requirements)
- Audit requirements (compliance audits, security audits)
- Documentation requirements (compliance documentation, audit trails)

**Existing Architecture Constraints:**
- Current architecture patterns (must follow existing patterns)
- Technology stack limitations (must use existing stack)
- Database constraints (existing schema, migration limitations)
- API constraints (existing API contracts, versioning)
- Integration constraints (must integrate with existing systems)
- Codebase constraints (must follow existing code style, patterns)
- Deployment constraints (existing CI/CD, infrastructure)
- Team knowledge constraints (team expertise, learning curve)

**Business Constraints:**
- Business rules and policies (company policies, legal requirements)
- Brand guidelines (design system, brand identity)
- Partnership constraints (vendor agreements, exclusivity)
- Market constraints (competitive landscape, market timing)
- User expectations (user base expectations, migration concerns)

**Operational Constraints:**
- Support capacity (support team size, support hours)
- Monitoring capabilities (existing monitoring tools, alerting systems)
- Documentation requirements (user docs, technical docs)
- Training requirements (user training, admin training, developer onboarding)

#### 1.4 Success Criteria

**Success Metrics & KPIs:**

**User Engagement Metrics:**
- Adoption rate (percentage of users using the feature)
- Daily/Monthly Active Users (DAU/MAU)
- Feature usage frequency (how often users use the feature)
- User retention (users returning to use the feature)
- Time spent in feature (engagement duration)
- Feature completion rate (users completing workflows)
- User satisfaction score (NPS, CSAT, user ratings)

**Performance Metrics:**
- Response time (target: e.g., <200ms for API, <2s for page load)
- Error rate (target: e.g., <0.1% error rate)
- Uptime/availability (target: e.g., 99.9% uptime)
- Throughput (target: e.g., handle 1000 requests/second)
- Resource utilization (CPU, memory, storage within limits)

**Business Metrics:**
- Revenue impact (if applicable)
- Cost savings (efficiency gains)
- Conversion rate (if applicable)
- Customer satisfaction improvement
- Support ticket reduction
- Time savings (for users or business processes)

**Technical Metrics:**
- Code quality (test coverage, code review scores)
- Bug rate (bugs per feature, critical bugs)
- Performance benchmarks (meeting performance targets)
- Security (no critical vulnerabilities, passing security audits)
- Scalability (handling projected load)

**Acceptance Criteria (Detailed):**

**Functional Acceptance Criteria:**
- [ ] All primary features work as specified
- [ ] All user workflows complete successfully
- [ ] All input validations work correctly
- [ ] All business rules are enforced
- [ ] All error cases are handled gracefully
- [ ] All edge cases are covered
- [ ] Integration with existing systems works
- [ ] Data persistence works correctly
- [ ] All user roles/permissions work correctly

**Non-Functional Acceptance Criteria:**
- [ ] Performance meets all specified targets
- [ ] Security requirements are met (authentication, authorization, encryption)
- [ ] Accessibility requirements are met (WCAG compliance)
- [ ] Works on all specified platforms/browsers
- [ ] Responsive design works on all screen sizes
- [ ] Uptime/availability meets requirements
- [ ] Error handling and recovery work correctly
- [ ] Monitoring and logging are in place

**Quality Acceptance Criteria:**
- [ ] Code follows project coding standards
- [ ] Test coverage meets requirements (e.g., >80%)
- [ ] All tests pass (unit, integration, E2E)
- [ ] Code review approved
- [ ] Documentation is complete
- [ ] No critical or high-severity bugs
- [ ] Performance testing passed
- [ ] Security review passed

**User Acceptance Criteria:**
- [ ] User testing completed successfully
- [ ] User feedback is positive (above threshold)
- [ ] User documentation is clear and helpful
- [ ] Onboarding flow is intuitive
- [ ] Error messages are clear and actionable
- [ ] Feature is discoverable and easy to use

**Definition of Done:**
- [ ] All acceptance criteria met
- [ ] Code merged to main branch
- [ ] Deployed to production (or staging if applicable)
- [ ] Monitoring and alerts configured
- [ ] Documentation updated (code, API, user docs)
- [ ] Stakeholder sign-off received
- [ ] Post-deployment validation completed

### Deliverable:
```markdown
## Requirements Analysis Summary

**Problem Statement:**
[Clear, comprehensive description of the problem]
- User personas affected: [List personas]
- Current pain points: [Detailed list]
- Business impact: [Why this matters]
- Current state vs. desired state: [Comparison]

**Functional Requirements:**

**Primary Features (Must-Have):**
1. [Feature 1] - [Detailed description, user story, acceptance criteria]
2. [Feature 2] - [Detailed description, user story, acceptance criteria]
...

**Secondary Features (Should-Have):**
1. [Feature 1] - [Description]
2. [Feature 2] - [Description]
...

**Nice-to-Have Features:**
1. [Feature 1] - [Description]
...

**User Interactions & Workflows:**
- **Workflow 1:** [Step-by-step user journey]
  - Entry point: [How user starts]
  - Steps: [Detailed steps]
  - Exit points: [How user completes/exits]
  - Error paths: [What happens on errors]
- **Workflow 2:** [Repeat pattern]
...

**Data Requirements:**
- **Input Data:**
  - [Data type 1]: [Format, validation rules, source]
  - [Data type 2]: [Format, validation rules, source]
- **Output Data:**
  - [Output 1]: [Format, destination, transformation]
  - [Output 2]: [Format, destination, transformation]
- **Data Persistence:**
  - What needs to be saved: [List]
  - Retention period: [How long]
  - Backup requirements: [Details]

**Business Rules:**
- [Rule 1]: [Detailed rule, when it applies, exceptions]
- [Rule 2]: [Detailed rule, when it applies, exceptions]
...

**Non-Functional Requirements:**

**Performance:**
- Response time: [Target metrics with specific numbers]
- Throughput: [Requests per second, transactions per minute]
- Resource usage: [CPU, memory, storage limits]
- Load capacity: [Concurrent users, peak load]
- Performance benchmarks: [Specific targets]

**Security:**
- Authentication: [Methods required]
- Authorization: [Access control requirements]
- Data protection: [Encryption requirements]
- Compliance: [Regulatory requirements]
- Security standards: [OWASP, ISO, etc.]

**Scalability:**
- Current scale: [Current data/users]
- Projected scale: [Expected growth]
- Scaling strategy: [Horizontal/vertical, auto-scaling]
- Geographic distribution: [Multi-region requirements]

**Reliability & Availability:**
- Uptime target: [99.9%, 99.99%, etc.]
- Error rate tolerance: [Acceptable error percentage]
- Recovery time: [RTO, RPO]
- Backup strategy: [Details]

**Usability:**
- User experience goals: [Ease of use, learnability]
- Accessibility: [WCAG level, specific requirements]
- Platform support: [Browsers, OS versions, devices]
- Responsive design: [Breakpoints, adaptive layouts]

**Maintainability:**
- Code quality: [Standards, test coverage]
- Documentation: [Requirements]
- Monitoring: [What to monitor]
- Deployment: [CI/CD requirements]

**Constraints:**

**Budget & Resources:**
- Development budget: [Details]
- Timeline: [Deadlines, milestones]
- Team capacity: [Available resources]
- Infrastructure costs: [Limitations]

**Technical Constraints:**
- Platform limitations: [OS versions, browser support]
- Technology stack: [Must use existing stack]
- Integration requirements: [Must work with existing systems]
- Legacy system constraints: [Compatibility requirements]

**Compliance & Regulatory:**
- Data privacy: [GDPR, CCPA, etc.]
- Industry regulations: [HIPAA, PCI-DSS, etc.]
- Accessibility: [ADA, Section 508, etc.]
- Security standards: [ISO, SOC 2, etc.]

**Success Criteria:**

**User Engagement Metrics:**
- Adoption rate: [Target percentage]
- Daily/Monthly Active Users: [Target numbers]
- User satisfaction: [NPS, CSAT targets]
- Feature completion rate: [Target percentage]

**Performance Metrics:**
- Response time: [<200ms, <2s, etc.]
- Error rate: [<0.1%, etc.]
- Uptime: [99.9%, etc.]

**Business Metrics:**
- Revenue impact: [If applicable]
- Cost savings: [Efficiency gains]
- Support ticket reduction: [Target percentage]

**Acceptance Criteria:**
- [ ] All primary features implemented and working
- [ ] Performance targets met
- [ ] Security requirements met
- [ ] Accessibility requirements met
- [ ] All tests passing
- [ ] Documentation complete
- [ ] User testing passed
- [ ] Stakeholder sign-off received

**Edge Cases & Considerations:**

**Data Edge Cases:**
- Empty data: [How to handle]
- Invalid data: [Validation and error handling]
- Large datasets: [Performance considerations]
- Concurrent modifications: [Conflict resolution]
- Data corruption: [Recovery strategy]

**User Edge Cases:**
- First-time users: [Onboarding]
- Power users: [Advanced features]
- Users with disabilities: [Accessibility]
- Users on slow connections: [Performance]
- Offline users: [Offline capabilities]

**System Edge Cases:**
- Network failures: [Error handling, retry logic]
- Server errors: [Graceful degradation]
- Timeout scenarios: [Handling timeouts]
- Rate limiting: [User feedback]
- Maintenance windows: [User communication]

**Integration Edge Cases:**
- Third-party service failures: [Fallback strategies]
- API version changes: [Compatibility handling]
- Data format changes: [Migration strategy]

**Future Considerations:**
- Potential future features: [Ideas for future]
- Scalability considerations: [How to scale]
- Technology evolution: [Future-proofing]

**Additional Features & Enhancements (Based on Project Requirements):**

**Potential Additional Features:**
- [Feature 1]: [Description, why it could be valuable, complexity, implementation effort]
  - User value: [How it benefits users]
  - Business value: [How it benefits business]
  - Technical complexity: [Low/Medium/High]
  - Implementation effort: [Estimated time]
  - Dependencies: [What it depends on]
- [Feature 2]: [Description, why it could be valuable, complexity, implementation effort]
- [Feature 3]: [Description, why it could be valuable, complexity, implementation effort]

**UI/UX Enhancements:**
- [Enhancement 1]: [Description, impact on UX, implementation complexity]
  - Visual impact: [How it improves visual design]
  - User experience impact: [How it improves UX]
  - WOW factor: [Does it create memorable experience]
  - Implementation complexity: [Low/Medium/High]
- [Enhancement 2]: [Description, impact on UX, implementation complexity]
- [Enhancement 3]: [Description, impact on UX, implementation complexity]

**Performance Optimizations:**
- [Optimization 1]: [Description, expected impact, complexity]
  - Performance gain: [Expected improvement percentage]
  - Implementation effort: [Time required]
  - Trade-offs: [Any trade-offs]
- [Optimization 2]: [Description, expected impact, complexity]

**Analytics & Monitoring:**
- [Analytics feature 1]: [What to track, why, implementation]
  - Metrics to track: [Specific metrics]
  - Business value: [Why tracking this matters]
  - Implementation: [How to implement]
- [Monitoring feature 1]: [What to monitor, why, implementation]
  - What to monitor: [Specific metrics/events]
  - Alerting: [When to alert, to whom]
  - Implementation: [How to implement]

**Accessibility Enhancements:**
- [A11y feature 1]: [Description, impact, implementation]
  - WCAG compliance: [Which guidelines it addresses]
  - User impact: [How it helps users with disabilities]
  - Implementation: [How to implement]
- [A11y feature 2]: [Description, impact, implementation]

**Integration Opportunities:**
- [Integration 1]: [What to integrate, value, complexity]
  - Integration type: [API, SDK, service]
  - Value proposition: [Why integrate]
  - Complexity: [Low/Medium/High]
  - Dependencies: [External dependencies]
- [Integration 2]: [What to integrate, value, complexity]

**Security Enhancements:**
- [Security feature 1]: [Description, security benefit, implementation]
  - Security benefit: [How it improves security]
  - Compliance: [Which compliance it helps with]
  - Implementation: [How to implement]
- [Security feature 2]: [Description, security benefit, implementation]

**Developer Experience Enhancements:**
- [DX feature 1]: [Description, how it helps developers]
  - Developer benefit: [How it improves developer experience]
  - Implementation: [How to implement]
- [DX feature 2]: [Description, how it helps developers]

**Future-Proofing Considerations:**
- [Consideration 1]: [How to make feature extensible]
  - Extensibility: [How to extend in future]
  - Backward compatibility: [How to maintain compatibility]
- [Consideration 2]: [How to handle future requirements]
  - Scalability: [How to scale]
  - Evolution: [How feature can evolve]

**Recommended Priority:**
- **High Priority:** [Features that should be included in initial implementation]
- **Medium Priority:** [Features that could be added in next iteration]
- **Low Priority:** [Features that are nice-to-have, can be added later]
```

---

## Step 2: List All Related Technologies & Concepts (MANDATORY)

**Objective:** Identify every technical aspect that needs to be considered

**⚠️ YOU MUST COMPLETE THIS STEP - Generate the full Technology & Concept Inventory deliverable.**

### 2.1 Technology Stack Assessment

#### Architecture Patterns:

**Architectural Layers:**
- **Presentation Layer:** UI components, views, controllers, state management, user input handling
- **Business Logic Layer (Domain):** Entities, use cases, business rules, validations, domain services
- **Data Access Layer:** Repositories, data sources (remote/local), data models, data mapping
- **Infrastructure Layer:** Network clients, database drivers, file system, external services, logging, monitoring
- **Cross-cutting Concerns:** Error handling, logging, dependency injection, configuration, security

**Design Patterns (Comprehensive List):**
- **Creational Patterns:** Factory, Builder, Singleton, Prototype, Abstract Factory
- **Structural Patterns:** Adapter, Decorator, Facade, Proxy, Bridge, Composite, Flyweight
- **Behavioral Patterns:** Observer, Strategy, Command, State, Template Method, Chain of Responsibility, Mediator, Memento, Visitor, Iterator
- **Architectural Patterns:** MVC, MVVM, MVP, MVI, Clean Architecture, Layered Architecture, Hexagonal Architecture, Onion Architecture
- **Data Patterns:** Repository, Unit of Work, Data Mapper, Active Record, CQRS (Command Query Responsibility Segregation)
- **Concurrency Patterns:** Producer-Consumer, Thread Pool, Future/Promise, Actor Model, Reactive Streams

**Feature Context:**
- **New Feature:** Completely new functionality, requires new architecture components
- **Modification:** Extending existing feature, must maintain compatibility
- **Refactoring:** Improving existing feature, may change architecture
- **Integration:** Connecting with existing features, must follow existing patterns

**Architecture Integration:**
- How does this feature fit into the current architecture?
- What existing components can be reused?
- What new components need to be created?
- How does it interact with other features?
- What shared services/utilities does it use?
- Does it require changes to existing architecture?

**Architectural Style:**
- **Layered Architecture:** Traditional layered approach (Presentation → Business → Data)
- **Clean Architecture:** Dependency inversion, domain-centric design
- **Microservices:** Distributed services, service boundaries, inter-service communication
- **Event-Driven:** Event sourcing, CQRS, message queues, event streams
- **Serverless:** Function-as-a-Service, event-driven functions
- **Monolithic:** Single deployable unit, modular monolith
- **Hybrid:** Combination of styles based on feature needs

#### State Management:

**State Management Approach:**
- **Framework-specific:** Redux (React), Vuex/Pinia (Vue), NgRx (Angular), Bloc/Riverpod (Flutter), SwiftUI State (iOS), Jetpack Compose State (Android)
- **Framework-agnostic:** MobX, Zustand, Jotai, Recoil, Valtio, XState
- **Built-in:** React Context API, Vue Composition API, Angular Services, Flutter StatefulWidget/Provider
- **Reactive:** RxJS, RxDart, Combine (Swift), Kotlin Flow, ReactiveX
- **Custom:** Custom state management solution tailored to needs

**State Scope & Organization:**
- **Local State:** Component/widget-level state, form state, UI-only state
- **Global State:** Application-wide state, user session, feature flags, theme
- **Feature State:** Feature-specific state, shared within feature module
- **Shared State:** State shared between multiple features/components
- **Server State:** Cached server data, API response state, synchronization state

**State Dependencies & Relationships:**
- **Independent States:** States that don't affect each other
- **Dependent States:** States that depend on other states (derived state)
- **Cascading Updates:** When one state change triggers multiple updates
- **State Synchronization:** Keeping multiple states in sync
- **State Composition:** Combining multiple states into complex state

**State Persistence:**
- **In-Memory Only:** State lost on app restart (temporary state)
- **Session Persistence:** State persists during session, lost on logout
- **Local Persistence:** State saved to local storage, persists across restarts
- **Selective Persistence:** Only certain state persisted (user preferences, cache)
- **Full Persistence:** All state persisted (offline-first apps)
- **Persistence Strategy:** When to save (on change, on interval, on app close)

**State Synchronization:**
- **No Sync:** Local-only state, no server sync needed
- **One-Way Sync:** Server → Client (fetch and cache)
- **Two-Way Sync:** Client ↔ Server (bidirectional sync)
- **Real-Time Sync:** WebSocket, Server-Sent Events, polling
- **Optimistic Updates:** Update UI immediately, sync in background
- **Conflict Resolution:** Handling conflicts in synchronized state

**State Management Patterns:**
- **Single Source of Truth:** One authoritative state store
- **Immutable Updates:** State updates create new state objects
- **Unidirectional Data Flow:** Data flows in one direction
- **State Normalization:** Normalized state structure (like database)
- **State Machines:** Finite state machines for complex state logic
- **Event Sourcing:** Store events instead of current state

#### Data Layer Technologies:
**Remote Data:**
- REST API, GraphQL, gRPC, WebSockets, SOAP?
- What HTTP client/library? (axios, fetch, OkHttp, Retrofit, HttpClient, etc.)
- API authentication method (JWT, OAuth, API keys, Session-based)
- Response format (JSON, XML, Protocol Buffers, MessagePack)
- Pagination strategy (offset, cursor-based, page-based)
- Rate limiting considerations

**Local Data:**
- Key-Value Storage (LocalStorage, SharedPreferences, UserDefaults, Redis)
- Relational Database (SQLite, PostgreSQL, MySQL, SQL Server)
- NoSQL Database (MongoDB, Hive, Realm, LevelDB, IndexedDB)
- Secure Storage (Keychain, KeyStore, Credential Manager)
- File system (local files, documents, media)
- In-memory caching (LRU cache, Redis, Memcached)

**Data Synchronization:**
- Online-first, offline-first, or hybrid?
- Conflict resolution strategy
- Background sync requirements

#### UI/UX Technologies:
- UI Framework/Library? (React, Vue, Angular, SwiftUI, Jetpack Compose, Flutter, etc.)
- Component library or custom components?
- Animation requirements (CSS animations, JavaScript libraries, framework-specific)
- Responsive design needs (mobile, tablet, desktop, adaptive layouts)
- Theme support (light/dark mode, custom themes)
- Internationalization (i18n) and localization (l10n)
- Accessibility features (ARIA, screen readers, keyboard navigation, semantic HTML)

#### UI/UX Research & Design (MANDATORY for UI/UX features):
**⚠️ For any UI/UX-related feature, MUST check UI Styles Reference AND UI/UX Reference Data FIRST, then research top-tier similar products**

**⚠️ CRITICAL: AI MUST CHECK BOTH UI STYLES REFERENCE AND UI/UX REFERENCE DATA FIRST**

**Step 1: Check UI Styles Reference & UI/UX Reference Data (MANDATORY)**
1. **Read and analyze** `.cursor/commands/common/ui_styles_reference.md`
2. **Read and analyze** `.cursor/uiux_reference/data/` folder for additional UI/UX context:
   - `styles.csv` - UI style patterns and specifications
   - `colors.csv` - Color palettes and schemes
   - `typography.csv` - Typography guidelines and font recommendations
   - `ux-guidelines.csv` - UX best practices and guidelines
   - `landing.csv` - Landing page patterns and examples
   - `products.csv` - Product page patterns and examples
   - `charts.csv` - Data visualization patterns
   - `prompts.csv` - UI/UX prompt templates and examples
   - `stacks/[FRAMEWORK].csv` - Framework-specific UI/UX patterns (check relevant framework)
3. **Extract project/feature requirements** from the user's request
4. **Match project type** with suitable UI styles from both references using the "Suitable Project Types" attribute
5. **Cross-reference** data from both sources to find comprehensive UI/UX solutions
6. **Select best-fit UI styles** that match the project requirements
7. **Document selected styles** with their WOW factor, complexity, and performance ratings

**UI Styles Reference Analysis Process:**
```markdown
### UI Styles Reference Analysis

**Project/Feature Requirements:**
- Project Type: [SaaS, E-commerce, Portfolio, Gaming, etc.]
- Target Audience: [Description]
- Brand Personality: [Modern, Luxury, Playful, Professional, etc.]
- Key Features: [List main features]
- Performance Requirements: [Mobile, Desktop, Both]
- Complexity Constraints: [Low, Medium, High]

**UI Styles Reference Check:**
1. Reviewed `.cursor/commands/common/ui_styles_reference.md`
2. Reviewed `.cursor/uiux_reference/data/` folder:
   - Checked `styles.csv` for style patterns
   - Checked `colors.csv` for color schemes
   - Checked `typography.csv` for typography guidelines
   - Checked `ux-guidelines.csv` for UX best practices
   - Checked `landing.csv` for landing page patterns (if applicable)
   - Checked `products.csv` for product page patterns (if applicable)
   - Checked `charts.csv` for data visualization patterns (if applicable)
   - Checked `prompts.csv` for UI/UX prompt examples
   - Checked `stacks/[FRAMEWORK].csv` for framework-specific patterns
3. Identified relevant styles based on "Suitable Project Types" attribute from both sources
4. Cross-referenced data from both sources with project requirements
5. Evaluated WOW factor, complexity, and performance ratings from both references
6. Synthesized findings from both sources for comprehensive UI/UX approach

**Animation & Effect Research (PRIMARY FOCUS):**
- **Background Effects:** Animated gradients, particle systems, video backgrounds, parallax, geometric patterns, glass morphism, mesh gradients, noise textures
- **Page Transitions:** Smooth transitions, fade effects, slide animations, reveal effects
- **Micro-interactions:** Button hover effects, card animations, loading states, icon animations
- **Scroll Animations:** Parallax scrolling, reveal animations, sticky effects, scroll-triggered animations
- **Hover Effects:** Transform effects, shadow changes, color transitions, glow effects
- **Loading Animations:** Skeleton screens, progress indicators, creative loaders, animated spinners
- **Special Effects:** Glass morphism, blur effects, glow effects, 3D transforms, particle systems
- **Performance:** How do they achieve smooth 60fps animations? What optimization techniques?

**Matching UI Styles Found:**
- [Style Name 1] - WOW Factor: X/10, Complexity: [Low/Medium/High], Performance: [Excellent/Good/Fair]
  - Match Score: [High/Medium/Low]
  - Why it fits: [Explanation]
  - Suitable Project Types: [List from reference]
  - Visual Description: [From reference]
  - Technical Specifications: [From reference]
  
- [Style Name 2] - [Same structure]

**Selected Best-Fit UI Styles:**
1. **Primary Style:** [Style Name] - [Brief justification]
2. **Secondary Style (optional):** [Style Name] - [Brief justification]
3. **Combination Approach:** [If combining multiple styles]

**UI/UX Reference Data Insights:**
- **Colors:** [Key color schemes from colors.csv that match project]
- **Typography:** [Typography recommendations from typography.csv]
- **UX Guidelines:** [Relevant UX best practices from ux-guidelines.csv]
- **Page Patterns:** [Relevant patterns from landing.csv, products.csv, charts.csv if applicable]
- **Framework Patterns:** [Framework-specific patterns from stacks/[FRAMEWORK].csv]
- **Prompt Examples:** [Relevant UI/UX prompts from prompts.csv]
```

**Step 2: Internet Research (MANDATORY)**
- **Research on Internet** (if possible) to validate style choices and find additional inspiration
- Identify 3-5 top-tier similar products on the internet
- **🎨 PRIORITIZE:** Analyze their animations, backgrounds, and visual effects in detail
- Compare findings with UI Styles Reference selections
- Validate that selected styles align with current industry trends
- Analyze their design patterns, color palettes, typography, and interactions
- Extract modern design trends and best practices
- Document common patterns and successful UX approaches
- **Focus on WOW factor:** What creates visual attraction? What makes users say "WOW"?

**Animation & Effect Research (PRIMARY FOCUS):**
- **Background Effects:** Animated gradients, particle systems, video backgrounds, parallax, geometric patterns, glass morphism, mesh gradients, noise textures
- **Page Transitions:** Smooth transitions, fade effects, slide animations, reveal effects
- **Micro-interactions:** Button hover effects, card animations, loading states, icon animations
- **Scroll Animations:** Parallax scrolling, reveal animations, sticky effects, scroll-triggered animations
- **Hover Effects:** Transform effects, shadow changes, color transitions, glow effects
- **Loading Animations:** Skeleton screens, progress indicators, creative loaders, animated spinners
- **Special Effects:** Glass morphism, blur effects, glow effects, 3D transforms, particle systems
- **Performance:** How do they achieve smooth 60fps animations? What optimization techniques?

**Design Style Determination:**
- **If user specifies a style:** Use the specified style (e.g., glass morphism, neumorphism, material design)
- **If user does NOT specify a style:** Default to **MODERN** design style

**Modern Design Default Characteristics:**
- Clean, minimalist aesthetics
- Generous white space
- Subtle shadows and depth
- **🎬 Smooth, impressive animations (200-300ms, with WOW entrance animations 400-600ms)**
- Contemporary color palettes
- Modern typography (sans-serif, clean hierarchy)
- Rounded corners (8-16px for cards, 4-8px for buttons)
- Card-based layouts
- **✨ Micro-interactions with WOW factor**
- Responsive, mobile-first approach
- Accessibility-first (WCAG AA compliance)
- Consistent spacing system (4px or 8px base unit)

**🎨 WOW Background & Animation Strategy (MANDATORY):**

**Based on user requirements, create corresponding WOW backgrounds and animations:**

**Background Design Requirements:**
- **Match Theme:** Background must align with user's product/theme requirements
  - Tech/SaaS: Futuristic gradients, particle systems, geometric patterns
  - E-commerce: Product-focused backgrounds, subtle animations, elegant textures
  - Creative/Portfolio: Bold gradients, artistic patterns, dynamic effects
  - Luxury: Elegant textures, subtle animations, sophisticated color schemes
  - Nature/Wellness: Organic patterns, flowing gradients, natural textures
  - Gaming/Entertainment: Dynamic effects, vibrant colors, energetic animations
- **Visual Impact:** Create backgrounds that immediately grab attention and create WOW
- **Animation Integration:** Backgrounds should have subtle or dynamic animations based on theme
- **Types:** Animated gradients, particle systems, video backgrounds, parallax layers, geometric patterns, glass morphism, mesh gradients, noise textures, custom illustrations

**Animation Design Requirements:**
- **Entrance Animations:** WOW first impression (fade-in with scale, slide-in with bounce, reveal effects, stagger animations)
- **Interactive Animations:** Respond to user actions with impressive feedback (hover, click, focus effects)
- **Scroll Animations:** Elements animate as user scrolls (parallax, reveal, fade-in, sticky effects)
- **Loading States:** Creative, engaging loading animations matching theme
- **Page Transitions:** Smooth, impressive transitions between pages/sections
- **Micro-interactions:** Delightful small animations (button press, card flip, icon animation)

**WOW Factor Requirements:**
- **Visual Attraction:** Design must immediately catch user's eye and create memorable first impression
- **Memorable:** Create unique, memorable visual experiences that users remember
- **Performance:** Smooth 60fps animations (optimize for performance, use GPU acceleration)
- **Purposeful:** Every animation should have a purpose (guide attention, provide feedback, create delight)
- **Thematic Match:** Animations/backgrounds must match user's product theme and requirements exactly
- **Balance:** Balance WOW factor with usability (don't sacrifice usability for effects)

**Research Deliverable:**
- Competitive analysis document with focus on animations, backgrounds, and effects
- Design pattern library from research (especially animation/effect patterns)
- Style determination (specified or modern default)
- Key design insights and best practices
- **WOW background and animation strategy matching user requirements**
- Performance optimization techniques for smooth animations

#### Algorithms & Logic:

**Search Algorithms:**
- **Linear Search:** Simple iteration through data (O(n))
- **Binary Search:** Sorted data search (O(log n))
- **Hash-based Search:** O(1) lookup using hash tables
- **Fuzzy Search:** Approximate matching (Levenshtein, Jaro-Winkler)
- **Full-Text Search:** Elasticsearch, Lucene, database full-text search
- **Graph Search:** BFS, DFS, A* for graph traversal
- **Pattern Matching:** Regex, string matching algorithms (KMP, Boyer-Moore)

**Sorting Algorithms:**
- **Comparison Sorts:** Quicksort, Mergesort, Heapsort, Timsort
- **Non-Comparison Sorts:** Counting sort, Radix sort, Bucket sort
- **Custom Comparators:** Multi-field sorting, locale-aware sorting
- **Stable vs. Unstable:** Maintaining relative order of equal elements
- **In-Place vs. Extra Space:** Memory efficiency considerations

**Data Processing:**
- **Filtering:** Filter data based on conditions
- **Mapping:** Transform data from one format to another
- **Reducing/Aggregation:** Combine data into single result (sum, average, etc.)
- **Grouping:** Group data by key (GROUP BY equivalent)
- **Joining:** Combine data from multiple sources
- **Pagination:** Split data into pages/chunks
- **Streaming:** Process data in streams (large datasets)

**Validation Logic:**
- **Input Validation:** Format validation (email, phone, URL)
- **Business Rule Validation:** Domain-specific validation rules
- **Data Integrity Validation:** Referential integrity, constraints
- **Regex Patterns:** Pattern matching for validation
- **Custom Validators:** Complex validation logic
- **Client-Side vs. Server-Side:** Where validation occurs
- **Validation Feedback:** How to present validation errors

**Business Logic Complexity:**
- **Simple Logic:** Straightforward if-else, calculations
- **Complex Logic:** Multi-step workflows, decision trees
- **Rule Engines:** External rule engines for complex business rules
- **Workflow Engines:** State machines, workflow orchestration
- **Business Process Modeling:** BPMN, workflow diagrams
- **Event-Driven Logic:** Event handlers, event processing

**Computational Complexity:**
- **Time Complexity:** O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- **Space Complexity:** Memory usage analysis
- **Optimization Needs:** When to optimize, trade-offs
- **Big Data Considerations:** Handling large datasets efficiently
- **Caching Strategy:** What to cache, cache invalidation
- **Lazy Evaluation:** Defer computation until needed

#### Database Design:

**Schema Design:**
- **Tables/Collections:** Entity tables, junction tables, lookup tables
- **Relationships:** One-to-one, one-to-many, many-to-many
- **Primary Keys:** Single key, composite key, UUID vs. auto-increment
- **Foreign Keys:** Referential integrity, cascade rules (CASCADE, SET NULL, RESTRICT)
- **Constraints:** NOT NULL, UNIQUE, CHECK constraints, default values
- **Data Types:** Appropriate types for each field (INT, VARCHAR, TEXT, BLOB, JSON, etc.)
- **Normalization:** Normal form (1NF, 2NF, 3NF, BCNF), when to normalize/denormalize

**Indexing Strategy:**
- **Primary Index:** Primary key index (automatic)
- **Secondary Indexes:** Indexes on foreign keys, frequently queried columns
- **Composite Indexes:** Multi-column indexes for complex queries
- **Unique Indexes:** Enforcing uniqueness constraints
- **Partial Indexes:** Indexes on filtered subsets of data
- **Full-Text Indexes:** For text search capabilities
- **Index Maintenance:** Index rebuild, index fragmentation, index statistics

**Query Optimization:**
- **Query Analysis:** EXPLAIN plans, query profiling
- **Query Patterns:** Common queries, query frequency
- **Join Optimization:** Join types (INNER, LEFT, RIGHT, FULL), join order
- **Subquery Optimization:** Correlated vs. non-correlated subqueries
- **Query Caching:** Result caching, query result caching
- **Connection Pooling:** Managing database connections efficiently
- **Batch Operations:** Bulk inserts, bulk updates, batch processing

**Migration Strategy:**
- **Schema Migrations:** Version-controlled schema changes
- **Data Migrations:** Moving/transforming existing data
- **Rollback Strategy:** How to rollback migrations if needed
- **Zero-Downtime Migrations:** Migrating without service interruption
- **Migration Tools:** Framework-specific migration tools (Laravel, Django, Rails, etc.)
- **Migration Testing:** Testing migrations on staging before production

**Data Normalization vs. Denormalization:**
- **Normalization Benefits:** Data consistency, reduced redundancy, easier updates
- **Denormalization Benefits:** Faster reads, simpler queries, reduced joins
- **When to Normalize:** High write frequency, data consistency critical
- **When to Denormalize:** Read-heavy workloads, performance critical, analytics
- **Hybrid Approach:** Normalized for writes, denormalized views for reads

**Database Types & Selection:**
- **Relational (SQL):** PostgreSQL, MySQL, SQL Server, SQLite
- **NoSQL Document:** MongoDB, CouchDB, Firebase Firestore
- **NoSQL Key-Value:** Redis, DynamoDB, Memcached
- **NoSQL Column:** Cassandra, HBase
- **NoSQL Graph:** Neo4j, ArangoDB
- **Time-Series:** InfluxDB, TimescaleDB
- **Search Engines:** Elasticsearch, Solr
- **Selection Criteria:** Data structure, query patterns, scalability needs, consistency requirements

#### Performance Considerations:

**Data Loading Strategies:**
- **Lazy Loading:** Load data on-demand, when needed
- **Eager Loading:** Load all data upfront
- **Progressive Loading:** Load data incrementally as user scrolls/interacts
- **Prefetching:** Load data before it's needed (predictive loading)
- **Background Loading:** Load data in background while user interacts
- **Selective Loading:** Load only visible/necessary data
- **Caching Strategy:** What to cache, cache duration, cache invalidation

**Pagination Strategies:**
- **Offset-Based Pagination:** Traditional page numbers (LIMIT/OFFSET)
- **Cursor-Based Pagination:** Using cursor/token for next page (more efficient)
- **Infinite Scroll:** Automatically load more as user scrolls
- **Load More Button:** User-triggered pagination
- **Virtual Scrolling:** Render only visible items (for large lists)
- **Windowed Lists:** Render visible window + buffer

**Image Optimization:**
- **Image Formats:** WebP, AVIF, JPEG, PNG, SVG (format selection)
- **Image Compression:** Lossy vs. lossless compression
- **Responsive Images:** Different sizes for different screen sizes (srcset)
- **Lazy Loading Images:** Load images when in viewport
- **Image Caching:** Browser cache, CDN cache, service worker cache
- **Image CDN:** Using CDN for image delivery (Cloudinary, Imgix, etc.)
- **Image Sprites:** Combining multiple images into one sprite sheet

**Memory Management:**
- **Memory Leaks:** Identifying and preventing memory leaks
- **Garbage Collection:** Understanding GC behavior, minimizing allocations
- **Object Pooling:** Reusing objects instead of creating new ones
- **Memory Profiling:** Tools for memory analysis
- **Memory Limits:** Handling memory constraints (mobile devices, browsers)
- **Large Object Handling:** Streaming, chunking large data

**Network Optimization:**
- **Request Batching:** Combining multiple requests into one
- **Request Deduplication:** Preventing duplicate requests
- **Compression:** Gzip, Brotli compression for responses
- **HTTP/2 & HTTP/3:** Multiplexing, server push, improved performance
- **CDN Usage:** Content Delivery Network for static assets
- **API Response Optimization:** Minimizing response size, only return needed data
- **Connection Pooling:** Reusing HTTP connections
- **Request Prioritization:** Critical requests first

**Rendering Performance:**
- **Virtual DOM Optimization:** Minimizing DOM updates (React, Vue)
- **Component Memoization:** Preventing unnecessary re-renders
- **Code Splitting:** Splitting code into chunks, lazy loading routes
- **Tree Shaking:** Removing unused code from bundle
- **Bundle Size Optimization:** Minimizing JavaScript bundle size
- **Critical CSS:** Inlining critical CSS, deferring non-critical CSS
- **Font Loading:** Font display strategies, font subsetting

**Database Performance:**
- **Query Optimization:** Optimizing database queries
- **Connection Pooling:** Managing database connections
- **Read Replicas:** Using read replicas for read-heavy workloads
- **Database Sharding:** Horizontal partitioning for scalability
- **Caching Layer:** Redis, Memcached for frequently accessed data
- **Database Indexing:** Proper indexes for query performance

**Monitoring & Profiling:**
- **Performance Monitoring:** Real User Monitoring (RUM), APM tools
- **Performance Budgets:** Setting performance targets (Lighthouse scores)
- **Performance Profiling:** Identifying bottlenecks
- **Load Testing:** Testing under load, stress testing
- **Performance Metrics:** Core Web Vitals, Time to Interactive, First Contentful Paint

#### Security Aspects:

**Data Encryption:**
- **Encryption at Rest:** Encrypting stored data (database encryption, file encryption)
- **Encryption in Transit:** TLS/SSL for network communication
- **Encryption Algorithms:** AES-256, RSA, ECC (Elliptic Curve Cryptography)
- **Key Management:** Secure key storage, key rotation, key derivation
- **End-to-End Encryption:** Encrypting data so only sender/receiver can read

**Authentication & Authorization:**
- **Authentication Methods:** Password, OAuth, OAuth2, OpenID Connect, SAML, JWT, API keys
- **Multi-Factor Authentication (MFA):** SMS, TOTP, authenticator apps, hardware tokens
- **Biometric Authentication:** Fingerprint, Face ID, Touch ID, voice recognition
- **Session Management:** Session tokens, refresh tokens, session expiration
- **Password Security:** Hashing (bcrypt, Argon2), password policies, password reset flows
- **Authorization Models:** Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), Permission-based
- **OAuth Flows:** Authorization Code, Implicit, Client Credentials, Device Code

**Secure Storage:**
- **Token Storage:** Secure storage for authentication tokens (Keychain, KeyStore, SecureStorage)
- **Credential Storage:** Secure storage for passwords, API keys, secrets
- **Sensitive Data:** Encrypting sensitive data before storage
- **Environment Variables:** Using environment variables for secrets (not hardcoding)
- **Secret Management:** Using secret management services (AWS Secrets Manager, HashiCorp Vault)

**Input Validation & Sanitization:**
- **Input Validation:** Validating all user inputs (type, format, length, range)
- **SQL Injection Prevention:** Parameterized queries, ORM usage, input sanitization
- **XSS Prevention:** Output encoding, Content Security Policy (CSP), input sanitization
- **CSRF Protection:** CSRF tokens, SameSite cookies, origin validation
- **Command Injection Prevention:** Avoiding shell commands, using safe APIs
- **File Upload Security:** File type validation, size limits, virus scanning, sandboxing

**API Security:**
- **API Authentication:** API keys, OAuth, JWT tokens
- **API Rate Limiting:** Preventing abuse, DDoS protection
- **API Versioning:** Versioning strategy, backward compatibility
- **CORS Configuration:** Proper CORS settings for web APIs
- **API Gateway Security:** Using API gateway for security (authentication, rate limiting)
- **Request Validation:** Validating API requests (schema validation)

**Network Security:**
- **HTTPS/TLS:** Enforcing HTTPS, TLS version requirements
- **SSL Pinning:** Certificate pinning for mobile apps (preventing MITM attacks)
- **Certificate Validation:** Proper certificate validation, certificate pinning
- **Network Security Config:** Android network security configuration
- **App Transport Security:** iOS ATS requirements

**Security Headers:**
- **Content Security Policy (CSP):** Preventing XSS attacks
- **HTTP Strict Transport Security (HSTS):** Enforcing HTTPS
- **X-Frame-Options:** Preventing clickjacking
- **X-Content-Type-Options:** Preventing MIME type sniffing
- **Referrer-Policy:** Controlling referrer information

**Security Compliance:**
- **OWASP Top 10:** Addressing common security vulnerabilities
- **Security Standards:** ISO 27001, SOC 2, PCI-DSS (if handling payments)
- **Privacy Regulations:** GDPR, CCPA compliance (data protection, user rights)
- **Security Audits:** Regular security audits, penetration testing
- **Vulnerability Management:** Security patch management, dependency scanning

**Error Handling & Information Disclosure:**
- **Error Messages:** Not exposing sensitive information in error messages
- **Stack Traces:** Not exposing stack traces in production
- **Logging Security:** Not logging sensitive data (passwords, tokens, PII)
- **Debug Mode:** Disabling debug mode in production

**Security Monitoring:**
- **Security Logging:** Logging security events (failed logins, suspicious activity)
- **Intrusion Detection:** Monitoring for suspicious activity
- **Security Alerts:** Alerting on security incidents
- **Audit Trails:** Maintaining audit logs for compliance

#### Third-Party Dependencies:
- Existing libraries/packages/modules that could help
- Package/library reliability and maintenance status
- License compatibility
- Bundle/binary size impact
- Dependency conflicts and version compatibility

### Deliverable:
```markdown
## Technology & Concept Inventory

**Architecture:**
- Layers: [Domain/Data/Presentation details]
- Patterns: [List applicable patterns]

**State Management:**
- Type: [State management approach]
- Scope: [Local/Global]
- Persistence: [Yes/No]

**Data Layer:**
- Remote: [API details, endpoints, methods]
- Local: [Storage type, structure]
- Sync Strategy: [Online-first/Offline-first/Hybrid]

**UI/UX:**
- Components: [Custom/Standard components needed]
- Animations: [Types and complexity]
- Responsive: [Breakpoints, layouts]

**Algorithms:**
- [Algorithm 1]: [Purpose, complexity]
- [Algorithm 2]: [Purpose, complexity]

**Database:**
- Schema: [Tables/collections design]
- Indexes: [Required indexes]
- Queries: [Complex queries needed]

**Performance:**
- [Optimization technique 1]
- [Optimization technique 2]

**Security:**
- [Security measure 1]
- [Security measure 2]

**Dependencies:**
- [Library/Package 1]: [Version, purpose]
- [Library/Package 2]: [Version, purpose]
```

---

## Step 3: Identify 2-3 Different Approaches (MANDATORY)

**Objective:** Explore multiple valid solutions with different trade-offs

**⚠️ YOU MUST COMPLETE THIS STEP - Generate AT LEAST 2-3 complete approach documentations with all sections filled.**

### 3.1 Approach Generation Framework

For each approach, consider different dimensions:

#### Dimension 1: Architecture Complexity
- **Simple/Lightweight:** Minimal layers, direct implementation
- **Moderate:** Standard Clean Architecture
- **Complex/Robust:** Advanced patterns, extensive error handling

#### Dimension 2: Data Strategy
- **Approach A:** Remote-only (always fetch from server)
- **Approach B:** Local-first (cache everything, sync later)
- **Approach C:** Hybrid (intelligent caching with fallback)

#### Dimension 3: State Management
- **Approach A:** Simple state container with minimal state
- **Approach B:** Robust state management with comprehensive event handling
- **Approach C:** Multiple coordinated state managers with complex orchestration

#### Dimension 4: UI Complexity
- **Approach A:** Simple, functional UI
- **Approach B:** Enhanced UX with animations
- **Approach C:** Premium experience with advanced features

### 3.2 Approach Template

For each approach, document comprehensively:

```markdown
### Approach [Number]: [Name/Description]

**Philosophy:**
[Overall approach philosophy and key characteristics]
- Core principles: [What principles guide this approach]
- Design philosophy: [Why this approach was chosen]
- Key differentiators: [What makes this approach unique]

**Architecture:**
- **Layers:** [How layers are structured, detailed breakdown]
  - Presentation Layer: [Components, structure, responsibilities]
  - Domain Layer: [Entities, use cases, business logic]
  - Data Layer: [Repositories, data sources, models]
  - Infrastructure Layer: [External services, utilities]
- **Patterns:** [Which patterns used and why]
  - Design patterns: [List with justification]
  - Architectural patterns: [List with justification]
- **Complexity:** [Low/Medium/High] - [Justification]
- **Separation of Concerns:** [How concerns are separated]
- **Dependency Direction:** [How dependencies flow]

**State Management:**
- **Strategy:** [State management implementation details]
  - Approach: [Redux, Bloc, Context API, etc.]
  - Rationale: [Why this approach]
- **State Structure:** [How state is organized]
  - Global state: [What's global, why]
  - Local state: [What's local, why]
  - Derived state: [Computed/derived state]
- **State Persistence:** [What persists, how, when]
- **State Synchronization:** [If applicable, how state syncs]

**Data Flow (Detailed):**
1. **User Action:** [What user does]
   - Triggers: [What event/action]
   - Input: [What data is provided]
2. **Presentation Layer:** [What happens in UI]
   - Component: [Which component handles it]
   - State update: [What state changes]
3. **Domain Layer:** [Business logic processing]
   - Use case: [Which use case handles it]
   - Validation: [What validations occur]
   - Business rules: [What rules are applied]
4. **Data Layer:** [Data access]
   - Repository: [Which repository method]
   - Data source: [Remote or local]
   - Data transformation: [How data is transformed]
5. **Response Flow:** [How response flows back]
   - Success path: [What happens on success]
   - Error path: [What happens on error]
6. **UI Update:** [How UI reflects changes]
   - State update: [Final state]
   - UI rendering: [What user sees]

**Technology Choices (Detailed):**
- **Remote Data:**
  - Protocol: [REST, GraphQL, gRPC, WebSocket]
  - Client: [axios, fetch, OkHttp, etc.]
  - Authentication: [JWT, OAuth, etc.]
  - Rationale: [Why these choices]
- **Local Data:**
  - Storage: [SQLite, SharedPreferences, LocalStorage, etc.]
  - Structure: [How data is organized]
  - Rationale: [Why this storage]
- **State Management:**
  - Library: [Redux, Bloc, MobX, etc.]
  - Version: [Specific version if important]
  - Rationale: [Why this library]
- **UI Framework:**
  - Framework: [React, Vue, Flutter, etc.]
  - Component library: [Material UI, Ant Design, etc.]
  - Rationale: [Why these choices]
- **Other Dependencies:**
  - [Dependency 1]: [Purpose, version, rationale]
  - [Dependency 2]: [Purpose, version, rationale]

**Pros (Comprehensive):**
✅ **Advantage 1:** [Detailed explanation of advantage]
✅ **Advantage 2:** [Detailed explanation of advantage]
✅ **Advantage 3:** [Detailed explanation of advantage]
✅ **Advantage 4:** [Additional advantages]
✅ **Advantage 5:** [Additional advantages]

**Cons (Comprehensive):**
❌ **Disadvantage 1:** [Detailed explanation, impact, workarounds]
❌ **Disadvantage 2:** [Detailed explanation, impact, workarounds]
❌ **Disadvantage 3:** [Detailed explanation, impact, workarounds]
❌ **Disadvantage 4:** [Additional disadvantages]

**Complexity Analysis:**
- **Development Time:** [Low/Medium/High] - [Estimated hours/days, justification]
- **Code Complexity:** [Low/Medium/High] - [Lines of code estimate, complexity factors]
- **Learning Curve:** [Low/Medium/High] - [Time to become productive]
- **Maintenance:** [Easy/Moderate/Complex] - [Ongoing maintenance effort]
- **Performance:** [Good/Excellent/Outstanding] - [Performance characteristics]
- **Scalability:** [How well it scales, limitations]

**Trade-offs (Detailed):**
- **Trade-off 1:** [What is traded off, why, impact]
- **Trade-off 2:** [What is traded off, why, impact]
- **Trade-off 3:** [Additional trade-offs]

**Best For:**
- **Scenario 1:** [When this approach is ideal, why]
- **Scenario 2:** [When this approach is ideal, why]
- **Project Type:** [What types of projects benefit]
- **Team Size:** [Ideal team size for this approach]
- **Timeline:** [When this approach makes sense]

**Not Ideal For:**
- **Scenario 1:** [When this approach is not ideal, why]
- **Scenario 2:** [When this approach is not ideal, why]

**Code Structure Preview:**
```
src/ (or appropriate source directory)
├── core/
│   ├── errors/
│   ├── network/
│   └── utils/
├── features/
│   └── [feature]/
│       ├── domain/
│       │   ├── entities/
│       │   ├── repositories/
│       │   └── usecases/
│       ├── data/
│       │   ├── models/
│       │   ├── datasources/
│       │   └── repositories/
│       └── presentation/
│           ├── state/
│           ├── pages/
│           └── components/
└── [entry_point]
```

**File Count Estimate:**
- Domain layer: [X files]
- Data layer: [X files]
- Presentation layer: [X files]
- Total: [X files]

**Algorithm/Logic Summary:**
- **Algorithm 1:** [Name, purpose, complexity, implementation approach]
- **Algorithm 2:** [Name, purpose, complexity, implementation approach]
- **Business Logic:** [Key business logic, complexity]
- **Validation Logic:** [Validation approach, rules]

**Database Schema (if applicable):**
```sql
-- Detailed schema with relationships
-- Include indexes, constraints, relationships
-- Explain design decisions
```

**API Design (if applicable):**
- **Endpoints:** [List endpoints with methods]
- **Request/Response:** [Format, structure]
- **Authentication:** [How auth is handled]
- **Error Handling:** [Error response format]

**Error Handling Strategy:**
- **Error Types:** [What errors are handled]
- **Error Propagation:** [How errors flow through layers]
- **User Feedback:** [How errors are shown to users]
- **Recovery:** [How errors are recovered]

**Testing Strategy:**
- **Unit Tests:** [What to test, coverage target]
- **Integration Tests:** [What to test]
- **E2E Tests:** [What to test]
- **Test Complexity:** [Low/Medium/High]

**Performance Characteristics:**
- **Response Time:** [Expected response times]
- **Resource Usage:** [CPU, memory, network]
- **Scalability:** [How it handles growth]
- **Bottlenecks:** [Potential performance issues]

**Security Considerations:**
- **Authentication:** [How auth is handled]
- **Authorization:** [How permissions are checked]
- **Data Protection:** [How data is protected]
- **Vulnerabilities:** [Potential security concerns]

**Migration Path (if applicable):**
- **From Current State:** [How to migrate from existing]
- **To Future State:** [How to evolve this approach]
- **Breaking Changes:** [What would break if changed]
```

### 3.3 Minimum Required Approaches

Generate at least 2-3 distinct approaches focusing on:

1. **Approach 1: Simple & Fast (MVP)**
   - Minimal complexity
   - Quick to implement
   - Core functionality only
   - Suitable for prototypes or simple use cases

2. **Approach 2: Balanced (Recommended)**
   - Clean Architecture adherence
   - Proper separation of concerns
   - Good balance of features and maintainability
   - Suitable for production apps

3. **Approach 3: Advanced & Robust (Enterprise)**
   - Maximum flexibility and scalability
   - Comprehensive error handling
   - Advanced features (offline support, caching, etc.)
   - Suitable for complex, large-scale applications

### Deliverable:
Complete documentation for 2-3 distinct approaches with all sections filled.

---

## Step 4: Conclude Final Approach (MANDATORY)

**Objective:** Select the optimal solution based on analysis

**⚠️ YOU MUST COMPLETE THIS STEP - Generate evaluation matrix, decision matrix, and final decision with full justification.**

### 4.1 Evaluation Criteria

Score each approach (1-10) on comprehensive criteria:

| Criteria | Weight | Approach 1 | Approach 2 | Approach 3 | Notes |
|----------|--------|------------|------------|------------|-------|
| **Requirements Fulfillment** | 25% | [score] | [score] | [score] | |
| Meets all functional requirements | | | | | [Justification] |
| Meets non-functional requirements | | | | | [Justification] |
| Handles edge cases | | | | | [Justification] |
| Future extensibility | | | | | [Justification] |
| **Maintainability** | 20% | [score] | [score] | [score] | |
| Code clarity and organization | | | | | [Justification] |
| Ease of future modifications | | | | | [Justification] |
| Testability | | | | | [Justification] |
| Documentation needs | | | | | [Justification] |
| Code complexity | | | | | [Justification] |
| **Performance** | 15% | [score] | [score] | [score] | |
| Response time | | | | | [Justification] |
| Resource efficiency (CPU, memory) | | | | | [Justification] |
| Scalability under load | | | | | [Justification] |
| Network efficiency | | | | | [Justification] |
| **Development Cost** | 15% | [score] | [score] | [score] | |
| Implementation time | | | | | [Justification] |
| Required expertise level | | | | | [Justification] |
| Learning curve | | | | | [Justification] |
| Infrastructure costs | | | | | [Justification] |
| **Scalability** | 10% | [score] | [score] | [score] | |
| Handles data growth | | | | | [Justification] |
| Handles user growth | | | | | [Justification] |
| Extensibility | | | | | [Justification] |
| **Security** | 5% | [score] | [score] | [score] | |
| Security best practices | | | | | [Justification] |
| Vulnerability risk | | | | | [Justification] |
| **User Experience** | 5% | [score] | [score] | [score] | |
| Ease of use | | | | | [Justification] |
| Performance from user perspective | | | | | [Justification] |
| Error handling UX | | | | | [Justification] |
| **Reliability** | 5% | [score] | [score] | [score] | |
| Error handling | | | | | [Justification] |
| Failure recovery | | | | | [Justification] |
| Data consistency | | | | | [Justification] |
| **Total Weighted Score** | 100% | [total] | [total] | [total] | |

**Scoring Guidelines:**
- **9-10:** Excellent - Exceeds expectations, best-in-class
- **7-8:** Good - Meets expectations well, solid choice
- **5-6:** Acceptable - Meets minimum requirements, some trade-offs
- **3-4:** Poor - Significant concerns, major trade-offs
- **1-2:** Unacceptable - Critical issues, not viable

### 4.2 Decision Matrix

**Context Factors:**
- Project maturity (new/existing)
- Team experience level
- Time constraints
- Budget constraints
- Expected user load
- Future expansion plans

**Risk Assessment:**

| Approach | Technical Risk | Schedule Risk | Cost Risk | Integration Risk | Maintenance Risk | Overall Risk | Mitigation Strategy |
|----------|---------------|---------------|-----------|------------------|------------------|-------------|-------------------|
| 1 | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Strategy details] |
| 2 | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Strategy details] |
| 3 | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Low/Med/High] | [Strategy details] |

**Risk Categories Explained:**

**Technical Risk:**
- **Low:** Proven technology, well-documented, team has experience
- **Medium:** Some unknowns, may require research, moderate complexity
- **High:** Unproven technology, high complexity, significant unknowns

**Schedule Risk:**
- **Low:** Clear timeline, well-understood scope, minimal dependencies
- **Medium:** Some uncertainty in estimates, moderate dependencies
- **High:** Unclear scope, many unknowns, complex dependencies

**Cost Risk:**
- **Low:** Predictable costs, minimal infrastructure needs
- **Medium:** Some cost uncertainty, moderate infrastructure needs
- **High:** High cost uncertainty, significant infrastructure needs

**Integration Risk:**
- **Low:** Simple integration, well-defined interfaces
- **Medium:** Moderate integration complexity, some interface work needed
- **High:** Complex integration, unclear interfaces, potential conflicts

**Maintenance Risk:**
- **Low:** Simple to maintain, well-structured, good documentation
- **Medium:** Moderate maintenance complexity, some technical debt
- **High:** Complex maintenance, high technical debt, poor structure

### 4.3 Final Decision

```markdown
## Selected Approach: [Number and Name]

**Rationale:**
[Detailed explanation of why this approach was selected]

**Key Deciding Factors:**
1. [Factor 1]: [Explanation]
2. [Factor 2]: [Explanation]
3. [Factor 3]: [Explanation]

**Alignment with Project Goals:**
- [Goal 1]: [How approach supports it]
- [Goal 2]: [How approach supports it]

**Accepted Trade-offs:**
- [Trade-off 1]: [Why it's acceptable]
- [Trade-off 2]: [Why it's acceptable]

**Rejected Alternatives:**
- **Approach [X]**: [Why not selected]
- **Approach [Y]**: [Why not selected]

**Risk Mitigation:**
- [Risk 1]: [Mitigation strategy]
- [Risk 2]: [Mitigation strategy]
```

### Deliverable:
Clear decision with comprehensive justification.

---

## Step 5: Write Details & Flow Diagrams (MANDATORY)

**Objective:** Document the complete technical specification

**⚠️ YOU MUST COMPLETE THIS STEP - Generate complete architecture specification with ALL flow diagrams, database schemas, API specs, and file structures.**

### 5.1 Detailed Architecture

```markdown
## Detailed Architecture Specification

### Layer Breakdown

#### Domain Layer
**Entities:**
```[language]
// Entity definitions with all properties
class [EntityName] {
  // Properties
  // Methods
  // Business rules
}
```

**Repository Interfaces:**
```[language]
interface [RepositoryName] {
  async [method1]([params]): Promise<Result<[Type], Failure>>;
  async [method2]([params]): Promise<Result<[Type], Failure>>;
}
```

**Use Cases:**
```[language]
class [UseCaseName] implements UseCase<[ReturnType], [Params]> {
  // Implementation details
  // Business logic
  // Validation rules
}
```

#### Data Layer
**Models:**
```[language]
class [ModelName] {
  // Properties with serialization support
  // fromJSON/toJSON methods (or equivalent)
  // toDomain() method
}
```

**Data Sources:**
```[language]
interface [RemoteDataSource] {
  async [method]([params]): Promise<[Model]>;
}

interface [LocalDataSource] {
  async [method]([params]): Promise<[Model]>;
}
```

**Repository Implementation:**
```[language]
class [RepositoryImpl] implements [Repository] {
  // Dependencies
  // Method implementations
  // Error handling
  // Data mapping
}
```

#### Presentation Layer
**States:**
```[language]
enum StateType { Initial, Loading, Success, Error }

class [FeatureState] {
  type: StateType;
  data?: [Data];
  error?: Failure;
}
```

**Events/Actions:**
```[language]
type [FeatureEvent] = 
  | { type: 'ACTION_NAME', params: [Params] }
  | { type: 'ANOTHER_ACTION' };
```

**State Manager/Controller:**
```[language]
class [FeatureController] {
  // Dependencies
  // Event/Action handlers
  // Business logic coordination
}
```

**UI Components:**
```[language]
class [ComponentName] {
  // Component structure
  // State subscription/binding
  // User interaction handlers
}
```
```

### 5.2 Data Flow Diagrams

Create detailed flow diagrams for each major operation:

#### Flow Diagram 1: [Operation Name]
```
┌─────────────┐
│   User UI   │
└──────┬──────┘
       │ 1. User Action (click, input, etc.)
       ▼
┌─────────────────┐
│  View/Page      │
└──────┬──────────┘
       │ 2. Trigger Event/Method
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
       ▼                      │
┌─────────────────┐           │
│   Repository    │           │
└──────┬──────────┘           │
       │ 5. Check network/cache strategy
       ▼                      │
   ┌───┴────┐                │
   │ Remote │ Local          │
   │ Source │ Source         │
   └───┬────┴────┬───────────┘
       │ 6. Fetch│ 6. Fetch
       ▼         ▼        
   ┌─────────────────┐   
   │   Data/Error    │   
   └──────┬──────────┘   
          │ 7. Map to Entity
          ▼              
   ┌─────────────────┐   
   │ Result<Success, │   
   │     Failure>    │   
   └──────┬──────────┘   
          │ 8. Return result
          └──────────────┘

Legend:
─► Flow direction
◄─ Return path
```

#### Flow Diagram 2: [Error Handling Flow]
```
┌────────────────┐
│  Any Layer     │
└───────┬────────┘
        │ Exception occurs
        ▼
    ┌───┴────┐
    │ Catch  │
    └───┬────┘
        │ Map to Failure
        ▼
┌────────────────┐
│ Error(Failure) │
└───────┬────────┘
        │ Propagate up
        ▼
┌────────────────┐
│   Controller   │
└───────┬────────┘
        │ setState(error)
        ▼
┌────────────────┐
│  UI Component  │
└───────┬────────┘
        │ Display error
        ▼
┌────────────────┐
│  User Feedback │
└────────────────┘
```

### 5.3 State Transition Diagram

```
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

### 5.4 Database Schema (if applicable)

```sql
-- Table definitions with relationships

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_users_email ON users(email);
```

### 5.5 API Specification (if applicable)

```markdown
## API Endpoints

### 1. Get User
**Endpoint:** `GET /api/v1/users/{id}`
**Headers:**
- Authorization: Bearer {token}
- Content-Type: application/json

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": "123",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

**Error Responses:**
- 401: Unauthorized
- 404: User not found
- 500: Server error
```

### 5.6 Algorithm Specification

```markdown
## Key Algorithms

### Algorithm 1: [Name]
**Purpose:** [What it does]
**Complexity:** Time O([complexity]), Space O([complexity])

**Pseudocode:**
```
function algorithm(input):
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]
    return result
```

**Implementation Details:**
- [Detail 1]
- [Detail 2]

**Edge Cases:**
- [Edge case 1]: [How handled]
- [Edge case 2]: [How handled]
```

### 5.7 File Structure

```
src/ (or lib/, app/, etc. - adjust based on language/framework)
├── core/ (or common/, shared/)
│   ├── errors/
│   │   ├── [failure_classes]         # [New] Custom error/exception classes
│   │   └── [error_handlers]          # [New] Error handling utilities
│   ├── network/ (or api/, services/)
│   │   ├── [network_checker]         # [Existing] Network utilities
│   │   └── [api_client]              # [Modified] HTTP client/API interface
│   ├── utils/
│   │   └── [utilities]               # [New] Helper functions
│   └── config/
│       └── [configuration]           # [New] App configuration
├── features/ (or modules/, components/)
│   └── [feature_name]/
│       ├── domain/ (or business/, models/)
│       │   ├── entities/ (or models/)
│       │   │   └── [entity]                  # [New] Domain models
│       │   ├── repositories/ (or interfaces/)
│       │   │   └── [repository]              # [New] Data access interfaces
│       │   └── usecases/ (or services/)
│       │       ├── [usecase_1]               # [New] Business logic
│       │       └── [usecase_2]               # [New] Business logic
│       ├── data/ (or infrastructure/, persistence/)
│       │   ├── models/ (or dtos/)
│       │   │   └── [model]                   # [New] Data transfer objects
│       │   ├── datasources/ (or repositories/)
│       │   │   ├── [remote_ds]               # [New] Remote data access
│       │   │   └── [local_ds]                # [New] Local data access
│       │   └── repositories/
│       │       └── [repository_impl]         # [New] Repository implementation
│       └── presentation/ (or ui/, views/, controllers/)
│           ├── state/ (or store/, viewmodels/)
│           │   ├── [controller]              # [New] State/ViewModel
│           │   ├── [events]                  # [New] Events/Actions
│           │   └── [state]                   # [New] State definitions
│           ├── pages/ (or views/, screens/)
│           │   └── [page]                    # [New] Main views
│           └── components/
│               ├── [component_1]             # [New] UI components
│               └── [component_2]             # [New] UI components
├── di/ (or ioc/, container/)
│   └── [dependency_config]                   # [Modified] Dependency injection
└── [entry_point]                             # [Modified] Application entry point
```

### Deliverable:
Complete technical specification with diagrams and code structures.

---

## Step 6: Describe in Human-Friendly Language (MANDATORY)

**Objective:** Translate technical details into clear, understandable explanation

**⚠️ YOU MUST COMPLETE THIS STEP - Generate ALL subsections (6.1-6.6): Executive Summary, User Journey, Technical Narrative, Key Decisions, Risk Discussion, and Future Considerations.**

### 6.1 Executive Summary

```markdown
## Feature Implementation Summary

### What We're Building
[2-3 sentence plain-English description of the feature]

### Why This Approach
[Explain the chosen approach in simple terms, avoiding jargon]

### How It Works
[Step-by-step explanation of the user experience and behind-the-scenes flow]
```

### 6.2 User Journey

```markdown
## User's Perspective

### Step 1: [User Action]
**What the user does:**
[Description in plain language]

**What happens behind the scenes:**
[Simple explanation of technical process]

**What the user sees:**
[Visual feedback, UI changes]

### Step 2: [Next Action]
[Repeat pattern]

### Step 3: [Result]
[Final outcome from user's perspective]
```

### 6.3 Technical Narrative

```markdown
## How the System Works (Technical Overview)

### The Journey of Data

**Starting Point:**
When a user [action], the app starts a process that involves several layers working together.

**Step 1: User Interface (Presentation Layer)**
The user interface captures the action and communicates with the "brain" of this feature - the Controller/ViewModel/State Manager. Think of it as pressing a button that starts a chain reaction.

**Step 2: Business Logic Layer**
The Controller/Presenter/ViewModel doesn't do the heavy lifting itself. Instead, it delegates to a "Use Case" or "Service" - a specialized component that knows exactly how to handle this specific task. The Use Case/Service applies business rules and validation (like checking if the input is valid).

**Step 3: Data Management (Data Layer)**
The Use Case then asks the Repository to fetch or save data. The Repository is smart - it decides whether to:
- Get fresh data from the internet (Remote Data Source)
- Use cached data from the device (Local Data Source)
- Or a combination of both

**Step 4: The Return Journey**
Once the data is retrieved (or an error occurs), it travels back through the layers:
1. Repository wraps the result (success or failure)
2. Use Case/Service receives and processes it
3. Controller/ViewModel/State Manager updates the state
4. UI automatically updates to show the result

**Error Handling:**
If anything goes wrong at any step (no internet, invalid data, server error), the system gracefully catches the error, wraps it in a user-friendly message, and displays it to the user.

### Why This Architecture?

**Separation of Concerns:**
Each layer has one job and does it well. The UI doesn't need to know about APIs, and the business logic doesn't care about UI components.

**Maintainability:**
When requirements change (and they will), we only need to modify the relevant layer. Want to switch from REST to GraphQL? Just change the Data Layer. Need to add a new validation rule? Only touch the Domain Layer.

**Scalability:**
As the app grows, this structure scales beautifully. Adding new features follows the same pattern, making it easier for the team to understand and contribute.
```

### 6.4 Key Decisions Explained

```markdown
## Important Design Decisions

### Decision 1: [Decision Name]
**What we chose:** [Choice]
**Why:** [Explanation in simple terms]
**Alternative considered:** [Other option]
**Why we didn't choose it:** [Reasoning]
**Impact:** [How this affects the user/developer]

### Decision 2: [Decision Name]
[Repeat pattern]

### Decision 3: [Decision Name]
[Repeat pattern]
```

### 6.5 What Could Go Wrong (Risk Discussion)

```markdown
## Potential Challenges & Mitigations

### Challenge 1: [Scenario]
**What could happen:**
[Plain-English explanation of the problem]

**How we're handling it:**
[Mitigation strategy in simple terms]

**Worst case scenario:**
[What happens if mitigation fails]

### Challenge 2: [Scenario]
[Repeat pattern]
```

### 6.6 Future Considerations

```markdown
## Looking Ahead

### Extensibility
[How this feature can be extended in the future]

### Scaling
[How this solution handles growth]

### Lessons Learned
[What we learned from this analysis]

### Recommendations
[Suggestions for future similar features]
```

### Deliverable:
Complete human-readable documentation explaining the entire feature implementation.

---

## Step 7: Create Implementation Plan (MANDATORY)

**Objective:** Translate the selected approach into a detailed, actionable implementation plan

**⚠️ YOU MUST COMPLETE THIS STEP - Generate the COMPLETE implementation plan following implementation_plan.instructions.md, then split it into child plans (Step 7.7).**

### 7.1 Prerequisites

Before creating the implementation plan, ensure you have:
- Completed Steps 1-6 of the research process
- Selected and justified the final approach
- Documented all technical specifications and flow diagrams

### 7.2 Implementation Plan Guidelines

Now that you have selected the optimal approach, use the **implementation_plan.instructions.md** guide to create a comprehensive implementation plan. This plan should follow the **project_rule.instructions.md** architecture standards.

### 7.3 Integration Process

**Reference Documents:**
1. **project_rule.instructions.md** (or project coding standards): For architecture standards, coding conventions, and best practices
2. **implementation_plan.instructions.md**: For systematic planning workflow and templates

**Mapping Research to Implementation:**

#### From Research Step 1 (Requirements) → Implementation Section 1 (Requirements Analysis)
- Transfer functional and non-functional requirements
- Convert success criteria into acceptance criteria
- Map constraints to technical limitations

#### From Research Step 2 (Technology Inventory) → Implementation Section 2 (Architecture Design)
- Map identified technologies to specific layers (Domain/Data/Presentation)
- Determine exact packages/libraries and versions needed
- Specify state management approach and implementation

#### From Research Step 3-4 (Approaches & Decision) → Implementation Section 3-4 (Dependencies & Data Flow)
- Document chosen technology stack
- Detail data flow for the selected approach
- List required dependencies from package configuration

#### From Research Step 5 (Technical Spec) → Implementation Section 5-7 (Error Handling, Code Analysis, Checklist, Code Gen)
- Transfer detailed architecture to implementation structure
- Convert flow diagrams to implementation steps
- Map database schema to data layer implementation
- Define error handling strategy per layer

#### From Research Step 6 (Human-Friendly) → Implementation Documentation
- Use as context for code comments and documentation
- Reference in PR descriptions and technical documentation

### 7.4 Implementation Plan Template

Following the **implementation_plan.instructions.md** structure, create:

```markdown
# Implementation Plan: [Feature Name]

## Overview
[Brief summary from Research Step 6.1 Executive Summary]

## 1. Requirements Analysis
**Feature Description:**
[From Research Step 1]

**User Story:**
As a [user type], I want to [action], so that [benefit]

**Acceptance Criteria:**
- [ ] [Criterion from success criteria]
- [ ] [Criterion from success criteria]
...

**Functional Requirements:**
[From Research Step 1.2]

**Non-Functional Requirements:**
[From Research Step 1.2]

---

## 2. Architecture Design

### Domain Layer

**Entities:**
[From Research Step 5.1, selected approach]

| Entity Name | Properties | Immutable | Description |
|-------------|------------|-----------|-------------|
| [Entity] | [props] | Yes/No | [purpose] |

**Repository Interfaces:**
[From Research Step 5.1, selected approach]

```[language]
interface [RepositoryName] {
  async [method]([params]): Promise<Result<[Type], Failure>>;
}
```

**Use Cases:**
[From Research Step 5.1, selected approach]

| Use Case | Input | Output | Purpose |
|----------|-------|--------|---------|
| [Name] | [Type] | Either<Failure, [Type]> | [description] |

### Data Layer

**Models:**
[From Research Step 5.1, selected approach]

```[language]
class [ModelName] {
  // Fields from selected approach
  // Serialization/Deserialization methods
}
```

**Data Sources:**

**Remote Data Source:**
- Base URL: [from approach]
- Endpoints: [from Research Step 5.5]
- Authentication: [from Research Step 2]

**Local Data Source:**
- Storage type: [from selected approach]
- Schema: [from Research Step 5.4]

**Repository Implementation:**
[Caching strategy, error handling from selected approach]

### Presentation Layer

**State Management:**
- Type: [State management approach from selected approach]
- Scope: [Local/Global]

**States:**
```[language]
enum StateType { Initial, Loading, Success, Error }

class [FeatureState] {
  type: StateType;
  data?: [Data];
  error?: Failure;
}
```

**Events/Actions:**
```[language]
type [FeatureAction] = 
  | { type: 'ACTION_NAME', payload: [Params] }
  | { type: 'ANOTHER_ACTION' };
```

**UI Components:**
- Views/Pages: [from selected approach]
- Components: [from selected approach]
- Animations: [from Research Step 2]

---

## 3. Dependencies & Infrastructure

**Required Packages:**
[From Research Step 2 and selected approach]

```[package-manager-format]
dependencies:
  # State Management
  [state-management-library]: [version]
  
  # Utilities
  [utility-library]: [version]
  
  # Dependency Injection
  [di-library]: [version]
  
  # Data Layer
  [http-client]: [version]
  [database-library]: [version]
  
  # [Other categories]

dev_dependencies:
  # Build Tools
  [build-tool]: [version]
  # Code Generation (if applicable)
  [code-gen-tool]: [version]
  # Testing
  [test-framework]: [version]
```

**Dependency Injection Setup:**
[Classes to register from selected approach]

| Class | Registration Type | Purpose |
|-------|------------------|---------|
| [ClassName] | @singleton | [reason] |
| [ClassName] | @lazySingleton | [reason] |
| [ClassName] | DI registration | [reason] |

---

## 4. Data Flow & Business Logic

**Primary Flows:**
[From Research Step 5.2, selected approach]

### Flow 1: [Operation Name]
**Trigger:** [User action]

**Sequence:**
1. User [action] → Triggers [Event/Method]
2. [Controller/Manager] receives event → Sets loading state
3. [Controller/Manager] calls [UseCase] with parameters
4. [UseCase] validates input → Calls [Repository]
5. [Repository] checks [strategy] → Calls [DataSource]
6. [DataSource] fetches/saves data → Returns result
7. [Repository] maps [Model] to [Entity] → Returns Result
8. [UseCase] processes result → Returns to [Controller/Manager]
9. [Controller/Manager] updates state (success/error)
10. UI updates to reflect new state

**Success Path:**
[From Research Step 5.2]

**Error Path:**
[From Research Step 5.2]

**State Transitions:**
```
Initial → Loading → Success/Error → [next states]
```

[Repeat for each major flow]

---

## 5. Error Handling Strategy

**Failure Classes:**
[From Research Step 5 and selected approach]

```[language]
// Custom failures for this feature
class [FeatureSpecificFailure] extends Failure {
  constructor(message: string = '...') {
    super(message);
  }
}
```

**Error Mapping:**

| Layer | Exception Type | Maps To | User Message |
|-------|---------------|---------|--------------|
| Data Source | [Exception] | [Failure] | "[Message]" |
| Repository | [Exception] | [Failure] | "[Message]" |
| Use Case | [Validation] | ValidationFailure | "[Message]" |

**Error Display Strategy:**
[From project coding standards - use appropriate UI error display patterns]

---

## 6. Code Analysis & Validation
**Objective:** Ensure code quality through static analysis

#### Analysis Strategy:
- Run language/framework-specific linter/analyzer after completing implementation
- Check for compile/build errors, warnings, and hints
- Verify type safety and null safety (if applicable)
- Ensure all imports/modules are used and properly organized
- Confirm code style and lint rules compliance

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

## 7. Implementation Checklist

### Phase 1: Setup (Day 1)
- [ ] Create feature directory structure
- [ ] Add dependencies to package configuration file (package.json, requirements.txt, pom.xml, etc.)
- [ ] Install dependencies using package manager (npm install, pip install, etc.)
- [ ] Setup DI module

### Phase 2: Core Layer (Day 1)
- [ ] Create/update Failure classes in core/error/
- [ ] Create custom exceptions if needed
- [ ] Add utility functions/extensions

### Phase 3: Domain Layer (Day 2)
- [ ] Create entities (with immutability support)
  - [ ] [Entity 1]
  - [ ] [Entity 2]
- [ ] Define repository interfaces
  - [ ] [Repository 1]
- [ ] Implement use cases
  - [ ] [UseCase 1]
  - [ ] [UseCase 2]

### Phase 4: Data Layer (Day 3-4)
- [ ] Create models with serialization support
  - [ ] [Model 1]
  - [ ] [Model 2]
- [ ] Implement remote data source
  - [ ] [Method 1]
  - [ ] [Method 2]
- [ ] Implement local data source
  - [ ] [Method 1]
  - [ ] [Method 2]
- [ ] Implement repository
  - [ ] [Method 1]
  - [ ] [Method 2]

### Phase 5: Presentation Layer (Day 5-6)
- [ ] Create state classes (immutable)
  - [ ] [State class]
- [ ] Create event/action classes
  - [ ] [Event 1]
  - [ ] [Event 2]
- [ ] Implement state manager/controller
  - [ ] [Event handler 1]
  - [ ] [Event handler 2]
- [ ] Create UI views/pages
  - [ ] [Page 1]
- [ ] Create UI components
  - [ ] [Component 1]
  - [ ] [Component 2]
- [ ] Wire up state subscription/binding

### Phase 6: Integration (Day 7)
- [ ] Setup dependency injection
  - [ ] Add DI annotations/configuration
  - [ ] Run build tools (if applicable)
  - [ ] Verify DI container registration
- [ ] Run code generation (if applicable)
  - [ ] Execute build/generation commands
- [ ] Code analysis
  - [ ] Run linter/analyzer to check for errors
  - [ ] Fix all compilation errors and warnings
  - [ ] Verify type safety compliance
  - [ ] Ensure code style rules are followed
- [ ] Integration validation
  - [ ] Verify on development environment
  - [ ] Verify on target platform(s)

### Phase 7: Polish & Review (Day 8)
- [ ] Code review and refactoring
- [ ] Documentation
- [ ] Performance validation
- [ ] Accessibility validation
- [ ] Final validation on all platforms

---

## 8. Code Generation Requirements

**Files Requiring Code Generation (if applicable):**
- [ ] Entity/model files requiring serialization code generation
- [ ] State management files requiring boilerplate generation
- [ ] Dependency injection configuration files
- [ ] API client files requiring stub/mock generation
- [ ] ORM/database mapping files

**Build/Generation Commands:**
```bash
# Examples for different stacks:
# TypeScript: npm run build or tsc
# Java: mvn generate-sources
# C#: dotnet build
# GraphQL: npm run codegen
# Protobuf: protoc --[language]_out=.
# [Adjust based on your language/framework]
```

---

## 9. File Structure

```
src/ (or lib/, app/, etc. - adjust based on language/framework)
├── state/                                   # State management
│   ├── [feature]_controller.[ext]          # [New] State controller/manager
│   ├── [feature]_actions.[ext]             # [New] Actions/Events
│   └── [feature]_state.[ext]               # [New] State definitions
├── core/                                    # Shared/common code
│   ├── errors/
│   │   ├── failures.[ext]                  # [Modified] Add [NewFailure]
│   │   └── exceptions.[ext]                # [Modified] Add [NewException]
│   ├── network/
│   │   └── network_info.[ext]              # [Existing] Network utilities
│   ├── utils/
│   │   └── [util].[ext]                    # [New] Utility functions
│   ├── components/
│   │   └── [common_component].[ext]        # [New] Reusable components
│   └── di/
│       └── injection_container.[ext]       # [New] DI configuration
├── data/                                    # Data management
│   ├── local/
│   │   └── [feature]_local_data_source.[ext]  # [New] Local data access
│   ├── remote/
│   │   └── [feature]_remote_data_source.[ext] # [New] Remote data access
│   └── models/
│       ├── [model_1].[ext]                 # [New] With serialization
│       └── [model_2].[ext]                 # [New] With serialization
├── domain/                                  # Domain layer
│   ├── entities/
│   │   ├── [entity_1].[ext]                # [New] Immutable entities
│   │   └── [entity_2].[ext]                # [New] Immutable entities
│   ├── repositories/
│   │   ├── [repository].[ext]              # [New] Abstract interface
│   │   └── [repository]_impl.[ext]         # [New] Implementation
│   └── usecases/
│       ├── [usecase_1].[ext]               # [New] Business logic
│       └── [usecase_2].[ext]               # [New] Business logic
├── views/                                   # UI views/pages
│   ├── components/
│   │   ├── [component_1].[ext]             # [New] Page-specific components
│   │   └── [component_2].[ext]             # [New] Page-specific components
│   └── [page].[ext]                        # [New] Main view/page
├── [entry_point].[ext]                      # [Modified] Application entry point
├── [dev_entry_point].[ext]                  # [New] Development environment entry
└── [prod_entry_point].[ext]                 # [New] Production environment entry
```

---

## 10. Algorithm Implementations

[From Research Step 5.6 - if applicable]

### Algorithm 1: [Name]
**Purpose:** [Description]
**Complexity:** Time O([complexity]), Space O([complexity])

**Implementation Location:** [file path]

**Pseudocode:**
```
[Pseudocode from research]
```

**Implementation:**
```[language]
[Actual implementation following project coding standards]
```

---

## 11. Database Schema & Migrations

[From Research Step 5.4 - if applicable]

**Schema:**
```sql
[SQL from research]
```

**Migration Steps:**
1. [Step 1]
2. [Step 2]

**Repository Methods:**
- `[method]`: [Purpose]

---

## 12. API Integration Details

[From Research Step 5.5 - if applicable]

**Base URL:** [URL]

**Endpoints:**

| Method | Endpoint | Purpose | Request | Response |
|--------|----------|---------|---------|----------|
| GET | [path] | [purpose] | [params] | [response] |
| POST | [path] | [purpose] | [body] | [response] |

**Authentication:**
[Details from research]

**Error Codes:**
[From research and mapped to Failures]

---

## 13. Acceptance Criteria & Testing Scenarios

**Acceptance Criteria:**
[From Research Step 1]

- [ ] [Criterion 1] - Validation: [Validation scenario]
- [ ] [Criterion 2] - Validation: [Validation scenario]
- [ ] [Criterion 3] - Validation: [Validation scenario]

**Manual Validation Checklist:**
- [ ] Happy path: [Scenario]
- [ ] Error case 1: [Scenario]
- [ ] Error case 2: [Scenario]
- [ ] Edge case 1: [Scenario]
- [ ] Edge case 2: [Scenario]
- [ ] Performance: [Scenario]
- [ ] Offline behavior: [Scenario]

---

## 14. Risk Mitigation

[From Research Step 6.5]

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Risk 1] | [L/M/H] | [L/M/H] | [Strategy] | [Team member] |
| [Risk 2] | [L/M/H] | [L/M/H] | [Strategy] | [Team member] |

---

## 15. Timeline & Milestones

**Estimated Duration:** [X days/weeks]

| Milestone | Duration | Deliverables | Dependencies |
|-----------|----------|--------------|--------------|
| Setup | [time] | Project structure, dependencies | None |
| Domain Layer | [time] | Entities, repos, use cases + tests | Setup |
| Data Layer | [time] | Models, data sources, repos + tests | Domain |
| Presentation | [time] | State manager, UI, components + tests | Data |
| Integration | [time] | DI, code gen, E2E testing | Presentation |
| Polish | [time] | Review, docs, performance | Integration |

---

## 16. Definition of Done

- [ ] All code follows project coding standards and conventions
- [ ] Clean Architecture layers properly separated
- [ ] All acceptance criteria met
- [ ] Error handling implemented
- [ ] Code generation successful (no errors)
- [ ] Dependency injection verified
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] No lint warnings or errors
- [ ] Performance acceptable (no jank)
- [ ] Works on all specified target platforms

---

## Conclusion

This implementation plan translates the research findings into actionable development tasks. Follow the project's coding standards and architecture patterns throughout implementation.

**Next Steps:**
1. Review and approve this implementation plan
2. Assign tasks to team members
3. Begin Phase 1: Setup
4. Conduct daily stand-ups to track progress
5. Perform code reviews after each phase
6. Update this document with any changes or learnings
```

### 7.5 Key Principles

When creating the implementation plan:

1. **Adherence to Standards:**
   - Follow all architecture guidelines from **project_rule.instructions.md**
   - Use Clean Architecture layers strictly
   - Apply SOLID principles
   - Use proper state management approach

2. **Completeness:**
   - Every component from the selected approach must have an implementation task
   - All dependencies must be listed
   - All error scenarios must be handled
   - All tests must be planned

3. **Traceability:**
   - Each implementation task should trace back to research findings
   - Reference research step numbers when applicable
   - Maintain consistency with selected approach

4. **Actionability:**
   - Tasks should be specific and measurable
   - Include file paths and class names
   - Provide code templates where helpful
   - Define clear acceptance criteria

### 7.6 Quality Checklist

Before finalizing the implementation plan, verify:

- [ ] All requirements from research are addressed
- [ ] Selected approach is fully detailed
- [ ] All three layers (Domain/Data/Presentation) are planned
- [ ] Dependencies are compatible and necessary
- [ ] Error handling strategy is comprehensive
- [ ] File structure follows project standards
- [ ] Timeline is realistic and accounts for dependencies
- [ ] Code generation requirements are clear
- [ ] DI setup is properly planned

### 7.7 Split Implementation Plan into Child Plans (MANDATORY)

**Objective:** Break down the comprehensive implementation plan into focused, manageable child plans

**⚠️ YOU MUST COMPLETE THIS STEP - After creating the main implementation plan, generate ALL 6 child plans with complete task breakdowns.**

After completing the main implementation plan, create detailed child plans for each major component. This ensures focused execution and better task management.

#### Child Plan Structure

Based on the **implementation_plan.instructions.md** guide, split the main plan into the following child plans:

**1. Setup & Infrastructure Plan**
- Project structure creation
- Dependency management
- DI configuration setup
- Build runner configuration
- File: `IMPLEMENTATION_PLAN_01_SETUP.md`

**2. Core Layer Plan**
- Failure classes creation/modification
- Exception classes creation/modification
- Utility functions and extensions
- Common components (if any)
- File: `IMPLEMENTATION_PLAN_02_CORE.md`

**3. Domain Layer Plan**
- Entity definitions (with immutability support)
- Repository interfaces
- Use case implementations
- Business logic and validations
- File: `IMPLEMENTATION_PLAN_03_DOMAIN.md`

**4. Data Layer Plan**
- Model classes with JsonSerializable
- Remote data source implementation
- Local data source implementation
- Repository implementations
- Data mapping logic
- File: `IMPLEMENTATION_PLAN_04_DATA.md`

**5. Presentation Layer Plan**
- State classes (immutable)
- Event classes (if applicable)
- State manager/controller implementations
- UI pages and components
- Wire up state subscription/binding
- File: `IMPLEMENTATION_PLAN_05_PRESENTATION.md`

**6. Integration & Validation Plan**
- Code generation execution
- Dependency injection verification
- Code analysis and validation
- Manual validation scenarios
- Edge case validation
- File: `IMPLEMENTATION_PLAN_06_INTEGRATION.md`

#### Child Plan Template

Each child plan should follow this structure:

```markdown
# [Child Plan Name] - [Feature Name]

## Overview
Brief description of what this child plan covers and its role in the overall implementation.

## Prerequisites
- [ ] Previous child plans completed (if any)
- [ ] Required dependencies installed
- [ ] [Other prerequisites]

## Scope
**Included:**
- [Item 1]
- [Item 2]

**Excluded (handled in other plans):**
- [Item 1]
- [Item 2]

## Detailed Tasks

### Task 1: [Task Name]
**Objective:** [Clear objective]

**Steps:**
1. [Detailed step 1]
2. [Detailed step 2]
3. [Detailed step 3]

**File Path:** `src/[path]/[filename].[ext]`

**Code Template:**
```[language]
// Actual code implementation
[Code here]
```

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Dependencies:**
- Depends on: [Task/File]
- Required by: [Task/File]

---

### Task 2: [Task Name]
[Repeat pattern]

---

## Code Generation (if applicable)

**Files Requiring Generation:**
- [ ] [File 1] - [Generator type]
- [ ] [File 2] - [Generator type]

**Command:**
```bash
# Run code generation command for your stack (if applicable)
# Examples: npm run build, mvn generate-sources, etc.
```

## Validation Checklist

- [ ] All files created in correct locations
- [ ] Imports are correct and minimal
- [ ] Null safety properly implemented
- [ ] No compilation errors
- [ ] Follows project coding standards
- [ ] Code generation successful
- [ ] [Specific validations for this layer]

## Next Steps
After completing this child plan:
1. Verify all checklist items are completed
2. Run code analysis using your language's linter/analyzer
3. Proceed to: `IMPLEMENTATION_PLAN_0X_[NEXT].md`

## Notes & Considerations
- [Important note 1]
- [Important note 2]
- [Gotchas or edge cases to watch for]
```

#### Child Plan Guidelines

**1. Granularity:**
- Each child plan should be completable in 1-2 days
- Focus on a single layer or cohesive component set
- Clear entry and exit criteria

**2. Dependencies:**
- Clearly document dependencies between child plans
- Follow the natural architecture flow (Domain → Data → Presentation)
- Ensure each plan can be validated independently

**3. Self-Contained:**
- Include all necessary code templates
- Reference specific sections from main implementation plan
- Provide complete context for that component

**4. Traceability:**
- Link back to main implementation plan sections
- Reference research findings where applicable
- Maintain consistency with selected approach

**5. Practical Focus:**
- Emphasize actionable steps over theory
- Include actual file paths and class names
- Provide concrete code examples

#### Example: Child Plan for Domain Layer

```markdown
# Domain Layer Implementation - [Feature Name]

## Overview
This plan covers the implementation of the domain layer, including entities, repository interfaces, and use cases. This is the core business logic layer that is independent of external frameworks.

## Prerequisites
- [ ] Setup & Infrastructure Plan completed
- [ ] Core Layer Plan completed (Failure classes available)
- [ ] Project structure created
- [ ] Dependencies installed

## Scope
**Included:**
- Entity definitions
- Repository interfaces
- Use case implementations
- Business validation logic

**Excluded:**
- Repository implementations (Data Layer Plan)
- Data models (Data Layer Plan)
- UI components (Presentation Layer Plan)

## Detailed Tasks

### Task 1: Create User Entity
**Objective:** Define the User entity with immutable properties

**Steps:**
1. Create file: `src/domain/entities/user.[ext]`
2. Import immutability support library (if applicable)
3. Define User class with immutability pattern
4. Add properties: id, email, name, createdAt
5. Generate code if needed (run build tools if applicable)

**File Path:** `src/domain/entities/user.[ext]`

**Code Template:**
```[language]
// Using immutable data pattern
class User {
  final String id;
  final String email;
  final String name;
  final DateTime createdAt;
  
  User({
    required this.id,
    required this.email,
    required this.name,
    required this.createdAt,
  });
}
```

**Acceptance Criteria:**
- [ ] File created at correct location
- [ ] All required properties defined
- [ ] Immutability pattern applied
- [ ] Generated code compiles without errors
- [ ] Const constructor available

**Dependencies:**
- Depends on: Core Layer (none for this task)
- Required by: UserModel (Data Layer), LoginUser use case

---

### Task 2: Define AuthRepository Interface
**Objective:** Create the abstract repository interface for authentication operations

**Steps:**
1. Create file: `src/domain/repositories/auth_repository.[ext]`
2. Import result type library (for error handling)
3. Import User entity and Failure classes
4. Define abstract methods with Result return types
5. Document each method's purpose

**File Path:** `src/domain/repositories/auth_repository.[ext]`

**Code Template:**
```[language]
import '../entities/user';
import '../../core/error/failures';

abstract class AuthRepository {
  /// Authenticates user with email and password
  /// Returns [User] on success or [Failure] on error
  Future<Either<Failure, User>> login({
    required String email,
    required String password,
  });

  /// Logs out current user
  /// Returns [Unit] on success or [Failure] on error
  Future<Either<Failure, Unit>> logout();

  /// Gets currently authenticated user
  /// Returns [User] on success or [Failure] if not authenticated
  Future<Either<Failure, User>> getCurrentUser();
}
```

**Acceptance Criteria:**
- [ ] Interface properly abstracted
- [ ] All methods return Either<Failure, T>
- [ ] Method signatures match requirements
- [ ] Documentation added
- [ ] No implementation details (just interface)

**Dependencies:**
- Depends on: User entity, Failure classes (Core Layer)
- Required by: Use cases, Repository implementation (Data Layer)

---

### Task 3: Implement LoginUser Use Case
**Objective:** Create the use case for user login with validation

**Steps:**
1. Create file: `src/domain/usecases/login_user.[ext]`
2. Define parameters class with email and password
3. Implement UseCase interface
4. Add input validation
5. Call repository login method
6. Add DI registration annotation for dependency injection

**File Path:** `src/domain/usecases/login_user.[ext]`

**Code Template:**
```[language]
// Import result type for error handling
// Import immutability/equality utilities if needed
import '../entities/user';
import '../repositories/auth_repository';
import '../../core/error/failures';
import '../../core/usecases/usecase';

// Register with dependency injection container
class LoginUser implements UseCase<User, LoginUserParams> {
  final AuthRepository repository;

  LoginUser(this.repository);

  @override
  Future<Either<Failure, User>> call(LoginUserParams params) async {
    // Validate email
    if (params.email.isEmpty || !params.email.contains('@')) {
      return const Left(ValidationFailure('Invalid email address'));
    }

    // Validate password
    if (params.password.isEmpty || params.password.length < 6) {
      return const Left(ValidationFailure('Password must be at least 6 characters'));
    }

    // Call repository
    return await repository.login(
      email: params.email,
      password: params.password,
    );
  }
}

class LoginUserParams {
  final String email;
  final String password;

  const LoginUserParams({
    required this.email,
    required this.password,
  });
  
  // Implement equality comparison if needed by language
}
```

**Acceptance Criteria:**
- [ ] Use case implements UseCase interface
- [ ] Input validation implemented
- [ ] Proper error handling with Either
- [ ] DI registration annotation added
- [ ] Parameters class is immutable
- [ ] No direct dependency on data layer

**Dependencies:**
- Depends on: AuthRepository interface, User entity, Failure classes
- Required by: AuthController (Presentation Layer)

---

## Code Generation

**Files Requiring Generation:**
- [ ] `src/domain/entities/user.[ext]` - Immutability code generation (if applicable)

**Command:**
```bash
# Run code generation command for your stack (if applicable)
# Examples: npm run build, mvn generate-sources, etc.
```

**Verification:**
- Check that generated files are created
- No compilation/build errors in generated files

## Validation Checklist

- [ ] All entity files created in `src/domain/entities/`
- [ ] All repository interfaces in `src/domain/repositories/`
- [ ] All use cases in `src/domain/usecases/`
- [ ] Immutability patterns applied where needed
- [ ] DI registrations on all use cases
- [ ] Proper imports with relative paths
- [ ] No implementation details in interfaces
- [ ] Null safety properly implemented
- [ ] No compilation errors
- [ ] Code follows project standards
- [ ] Generated code successful

## Next Steps
After completing this child plan:
1. Verify all checklist items completed
2. Run code analysis using your language's linter/analyzer
3. Proceed to: `IMPLEMENTATION_PLAN_04_DATA.md`

## Notes & Considerations
- Keep business logic layer pure - no framework-specific dependencies
- Entities/models should be immutable where possible
- Use cases/services should follow single responsibility principle
- All async operations should have proper error handling
- Validation belongs in use cases/services, not entities
```

### Deliverable:
A complete, actionable implementation plan that can be directly used by developers to build the feature according to project standards, along with a set of focused child plans that break down the implementation into manageable, sequential tasks.

---

## Complete Research Template

Use this template for any feature research:

```markdown
# Feature Research: [Feature Name]

## 1. Requirements Analysis
[Complete Step 1 deliverable]

## 2. Technology & Concept Inventory
[Complete Step 2 deliverable]

## 3. Implementation Approaches

### Approach 1: [Name]
[Complete approach documentation]

### Approach 2: [Name]
[Complete approach documentation]

### Approach 3: [Name]
[Complete approach documentation]

## 4. Final Decision
[Complete Step 4 deliverable]

## 5. Technical Specification
[Complete Step 5 deliverable with all diagrams]

## 6. Human-Friendly Explanation
[Complete Step 6 deliverable]

## 7. Implementation Plan
[Complete Step 7 deliverable - detailed implementation plan following implementation_plan.instructions.md and project_rule.instructions.md]

---

## Appendix

### Research Metadata
- Researched by: [AI/Team member]
- Date: [Date]
- Review status: [Pending/Approved]
- Estimated effort: [Person-hours]

### References
- [Reference 1]
- [Reference 2]
- project_rule.instructions.md
- implementation_plan.instructions.md

### Open Questions
- [Question 1]
- [Question 2]
```

---

## Best Practices for Research

### Do:
✅ Be thorough in requirement analysis
✅ Consider multiple valid approaches
✅ Evaluate trade-offs objectively
✅ Think about edge cases and errors
✅ Consider both short-term and long-term implications
✅ Document assumptions clearly
✅ Use diagrams to clarify complex flows
✅ Explain technical decisions in simple terms
✅ Consider the entire team (developers, testers, stakeholders)

### Don't:
❌ Rush to a solution without analysis
❌ Only consider one approach
❌ Ignore non-functional requirements
❌ Overcomplicate simple problems
❌ Use jargon without explanation
❌ Skip the risk assessment
❌ Ignore existing architecture patterns

---

## Example: Research for "Offline-First Todo List"

### 1. Requirements Analysis

**Problem Statement:**
Users need to create and manage todos even without internet connection. Changes should sync automatically when connection is restored.

**Functional Requirements:**
1. Create, read, update, delete todos
2. Work completely offline
3. Auto-sync when online
4. Handle sync conflicts
5. Show sync status to user

**Non-Functional Requirements:**
- Performance: Instant local operations (<50ms)
- Reliability: No data loss during sync
- Usability: Clear indication of sync status

**Constraints:**
- Must work on target platforms (mobile, web, desktop, etc.)
- Database technology for local storage
- API protocol for backend communication

**Success Criteria:**
- 100% offline functionality
- <3 second sync time for typical usage
- Conflict resolution without data loss

### 2. Technology Inventory

**Architecture:** Full Clean Architecture (Domain, Data, Presentation)
**State Management:** State management with complex sync logic
**Local Storage:** SQLite with sqflite package
**Remote:** REST API with Dio
**Sync Strategy:** Last-write-wins with conflict detection
**Data Model:** Todo entity with timestamp and sync status

### 3. Approaches

**Approach 1: Simple Offline-First**
- Always write to local DB first
- Background sync every 5 minutes
- Simple conflict resolution (server wins)
- Pros: Easy to implement, reliable
- Cons: Possible data loss in conflicts

**Approach 2: Conflict-Aware Sync**
- Local DB with sync metadata
- Intelligent conflict detection
- User-driven conflict resolution
- Pros: No data loss, user control
- Cons: More complex, requires UI for conflicts

**Approach 3: CRDT-Based Sync**
- Conflict-free replicated data types
- Automatic merging
- Real-time sync with WebSocket
- Pros: Automatic resolution, real-time
- Cons: Complex implementation, requires CRDT support

### 4. Final Decision: Approach 2 (Conflict-Aware)

**Rationale:**
Balances reliability (no data loss) with reasonable complexity. Gives users control over conflicts while maintaining good UX for the 99% case of no conflicts.

### 5. Technical Specification

[Flow Diagrams]
```
Create Todo Flow:
User Input → Controller → UseCase → Repository → Local DB → setState(success)
                                          ↓
                                  Queue for sync → Background Worker
```

[Database Schema]
```sql
CREATE TABLE todos (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL,
    synced INTEGER NOT NULL DEFAULT 0,
    server_updated_at INTEGER
);
```

### 6. Human-Friendly Explanation

**What We're Building:**
A todo list that works perfectly even when you're offline. All your changes are saved instantly on your device, and when you get internet back, everything syncs automatically.

**How It Works:**
Imagine having a notebook that you can write in anytime, anywhere. That's the local database on your device. When you connect to WiFi, a helpful assistant (the sync manager) checks your notebook against the master copy (the server) and makes sure both are up-to-date.

If you changed the same todo on two devices, instead of randomly picking one, the app will politely ask you which version to keep. This way, you never lose work.

**Why This Approach:**
We chose this method because it guarantees you'll never lose data while keeping things simple for most users. The conflict resolution UI only appears in the rare case where you actually edited the same item on multiple devices.
```

---

## Conclusion

This research guide ensures:
- Comprehensive analysis before implementation
- Multiple perspectives on problem-solving
- Informed decision-making with clear rationale
- Complete technical and non-technical documentation
- Shared understanding across team members
- Seamless transition from research to implementation

**Complete Workflow (ALL MANDATORY):**
1. **Research Phase (Steps 1-6):** Analyze requirements, explore approaches, select optimal solution
2. **Planning Phase (Step 7):** Create detailed implementation plan following project standards
3. **Child Plans Creation (Step 7.7):** Split implementation plan into 6 detailed child plans
4. **Implementation Phase:** Execute the plan using project_rule.instructions.md guidelines and implementation_plan.instructions.md templates

---

## FINAL REMINDER FOR AI

**When you receive a feature request, you MUST:**

✅ **Step 1:** Complete Requirements Analysis (all subsections 1.1-1.4, full deliverable)
✅ **Step 2:** Complete Technology & Concept Inventory (all subsections 2.1, full deliverable)
✅ **Step 3:** Generate 2-3 Complete Approaches (using template, all sections filled)
✅ **Step 4:** Conclude Final Approach (evaluation criteria, decision matrix, final decision)
✅ **Step 5:** Write Complete Technical Specification (architecture, flow diagrams, schemas, APIs, file structure)
✅ **Step 6:** Describe in Human-Friendly Language (all subsections 6.1-6.6)
✅ **Step 7:** Create Complete Implementation Plan (following implementation_plan.instructions.md template)
✅ **Step 7.7:** Generate ALL 6 Child Plans (Setup, Core, Domain, Data, Presentation, Integration & Validation)

**DO NOT:**
❌ Skip any step or subsection
❌ Provide summaries instead of complete content
❌ Ask for permission to continue
❌ Stop before completing all steps
❌ Generate partial deliverables

**OUTPUT FORMAT:**
Present all results in a single, comprehensive markdown document following the "Complete Research Template" structure. Include all sections, all deliverables, all diagrams, all code templates, and all child plans.

Always complete thorough research and planning before beginning implementation. The time invested in research and planning saves exponentially more time during development and maintenance.

**Remember: Incomplete execution of this guide is considered unacceptable. Complete ALL steps for EVERY feature request.**

---

## CRITICAL: Comprehensive Detail Requirements

**⚠️ ALL RESEARCH MUST BE DETAILED AND COMPREHENSIVE - NO SIMPLIFICATIONS**

When creating research plans, you MUST:

### Detail Requirements:

1. **Expand Every Section:**
   - Every section must have comprehensive subsections
   - Every subsection must have detailed explanations
   - Every explanation must include examples, justifications, and considerations
   - DO NOT summarize - provide full details

2. **Requirements Analysis Must Include:**
   - Detailed user personas and use cases
   - Comprehensive functional requirements breakdown
   - Extensive non-functional requirements (performance, security, scalability, etc.)
   - All constraints (budget, time, technical, compliance)
   - Detailed success criteria with specific metrics
   - Comprehensive edge cases and considerations
   - **Additional features/sections/parts/UI that could match project requirements**

3. **Technology Inventory Must Include:**
   - Detailed architecture patterns and justifications
   - Comprehensive state management analysis
   - Complete data layer analysis (remote, local, sync)
   - Extensive UI/UX research (styles, animations, effects)
   - Detailed algorithm and logic analysis
   - Comprehensive database design considerations
   - Extensive performance optimization strategies
   - Complete security analysis
   - All third-party dependencies with justifications

4. **Approaches Must Include:**
   - At least 2-3 fully detailed approaches
   - Complete architecture breakdown for each
   - Detailed data flow diagrams
   - Comprehensive pros/cons with explanations
   - Detailed complexity analysis
   - Complete trade-off analysis
   - Full technology stack justification
   - Code structure previews
   - Algorithm/logic summaries
   - Database schemas (if applicable)

5. **Final Decision Must Include:**
   - Comprehensive evaluation matrix with justifications
   - Detailed risk assessment (technical, schedule, cost, integration, maintenance)
   - Complete decision rationale
   - Detailed alignment with project goals
   - Comprehensive trade-off acceptance
   - Complete risk mitigation strategies

6. **Technical Specification Must Include:**
   - Complete layer breakdown (Domain, Data, Presentation)
   - Detailed code examples for each layer
   - Multiple flow diagrams (success, error, state transitions)
   - Complete database schema with relationships
   - Full API specification (if applicable)
   - Detailed algorithm specifications
   - Complete file structure with explanations

7. **Human-Friendly Explanation Must Include:**
   - Comprehensive executive summary
   - Detailed user journey with all steps
   - Complete technical narrative
   - All key decisions explained
   - Comprehensive risk discussion
   - Detailed future considerations

8. **Implementation Plan Must Include:**
   - Complete requirements analysis
   - Detailed architecture design for all layers
   - Comprehensive dependencies list
   - Complete data flow documentation
   - Detailed error handling strategy
   - Complete code analysis requirements
   - Comprehensive implementation checklist (all phases)
   - Complete code generation requirements
   - Detailed file structure
   - Algorithm implementations (if applicable)
   - Complete database schema and migrations
   - Full API integration details
   - Comprehensive acceptance criteria
   - Detailed risk mitigation
   - Complete timeline and milestones
   - All 6 child plans (Setup, Core, Domain, Data, Presentation, Integration)

### Additional Features & Sections:

**When analyzing requirements, ALWAYS consider and document:**

1. **Additional Features:**
   - Features that enhance core functionality
   - Features that improve user experience
   - Features that provide competitive advantage
   - Features that future-proof the solution
   - Features that improve developer experience

2. **Additional Sections:**
   - Analytics and monitoring sections
   - Performance optimization sections
   - Security enhancement sections
   - Accessibility improvement sections
   - Integration opportunity sections
   - Future-proofing sections

3. **Additional UI/UX Elements:**
   - Enhanced animations and effects
   - Additional micro-interactions
   - Advanced visual effects
   - Premium UI components
   - Enhanced accessibility features
   - Advanced responsive design patterns

4. **Additional Technical Components:**
   - Caching strategies
   - Background processing
   - Real-time features
   - Offline capabilities
   - Advanced error handling
   - Performance monitoring
   - Analytics integration

**DO NOT:**
- ❌ Simplify or summarize sections
- ❌ Skip subsections
- ❌ Provide minimal details
- ❌ Ignore potential enhancements
- ❌ Overlook additional features that could match requirements
- ❌ Create simple, basic research plans

**DO:**
- ✅ Provide comprehensive, detailed analysis
- ✅ Expand every section with full details
- ✅ Include all subsections and considerations
- ✅ Document additional features/sections/parts/UI that match requirements
- ✅ Provide extensive examples and justifications
- ✅ Create thorough, enterprise-grade research plans

**The research plan should be so comprehensive that a developer can implement the feature without asking additional questions.**
