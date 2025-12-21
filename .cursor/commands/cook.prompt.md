---
agent: agent
---

# Complete Feature Development Workflow: From Requirement to Implementation

This document provides a comprehensive, end-to-end workflow for AI to transform user requirements into a complete, ready-to-implement feature specification with full research, UI/UX design, and implementation planning.

## CRITICAL: Required Prompt Files Reference

**⚠️ AI MUST REFERENCE THESE PROMPT FILES FOR ACCURATE ANALYSIS**

**IMPORTANT:** After Step 0 verification, tech-specific prompt files will be available in `./.cursor/commands/specify/`. These files take precedence over common files.

Before executing this workflow, you MUST have access to and reference these prompt files:

1. **Research & Analysis Prompt**
   - **Primary:** `./.cursor/commands/specify/research_plan_[TECH]_[LANGUAGE].prompt.md` (generated in Step 0)
   - **Fallback:** `./.cursor/commands/common/research_plan_common.prompt.md`
   - Purpose: Provides detailed instructions for Step 2 (Research & Analysis)
   - MUST be referenced for all research activities

2. **UI/UX Design Generator Prompt**
   - **Primary:** `./.cursor/commands/specify/ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md` (generated in Step 0)
   - **Fallback:** `./.cursor/commands/common/ui_ux_design_generator.prompt.md`
   - Purpose: Provides detailed instructions for Step 3 (UI/UX Design)
   - MUST be referenced for all design system generation

3. **UI/UX Bridge Prompt**
   - **Primary:** `./.cursor/commands/specify/ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md` (generated in Step 0)
   - **Fallback:** `./.cursor/commands/common/ui_ux_bridge.prompt.md`
   - Purpose: Provides detailed instructions for Step 4 (Platform-Specific Code)
   - MUST be referenced for all UI code conversion

4. **Implementation Plan Prompt**
   - **Primary:** `./.cursor/commands/specify/implementation_plan_[TECH]_[LANGUAGE].prompt.md` (generated in Step 0)
   - **Fallback:** `./.cursor/commands/common/implementation_plan_common.prompt.md`
   - Purpose: Provides detailed instructions for Step 5 (Implementation Planning)
   - MUST be referenced for all implementation planning

**MANDATORY ACTION:**
- **Step 0:** Verify and generate tech-specific prompt files if missing
- Read and understand ALL four prompt files (prefer tech-specific, fallback to common)
- Reference the appropriate prompt file at each step
- Follow the instructions in each prompt file exactly
- Do NOT deviate from the guidelines in these files

---

## CRITICAL: Mandatory Sequential Execution

**⚠️ AI MUST COMPLETE ALL STEPS IN EXACT ORDER - NO EXCEPTIONS**

When you receive a feature request, you MUST:
1. Execute Step 0 (Verify Commands & Project Rules)
2. **IF UI design images are detected** → Execute Step 0.5 (Process UI Images) → Break into components → Convert each to HTML using @ui_ux_bridge
3. Execute ALL remaining steps sequentially (Step 1 through Step 5)
4. Generate ALL deliverables for each step
5. Store results in specified directories
6. Do NOT skip any step (except Step 0.5 if no images, Step 2.5/3/4 if no UI/UX required)
7. **EXECUTE Step 2.5 (Wireframes) automatically** if UI/UX required, then **WAIT for user review/approval** before proceeding to Step 3
8. Do NOT ask for permission between other steps - execute automatically (except after Step 2.5 wireframe review)
9. ONLY ask for user confirmation AFTER completing Step 5
10. Complete the entire workflow before proceeding to implementation

**Failure to complete all steps is considered incomplete work.**

---

## Complete Workflow Overview

```
Verify Commands (Step 0) → Check commands/specify/ → Generate if missing
         ↓
Detect UI Images (Step 0.5) → IF images provided:
         ↓
    Break into Components → Convert each to HTML (@ui_ux_bridge)
         ↓
    Store Components → Continue to Step 1
         ↓
User Requirement (Step 1) → Include converted UI reference
         ↓
Determine UI/UX Requirement (Step 1.5) → Does feature need UI/UX?
         ↓
Research & Analysis (Step 2) → ./docs/research_plans/
         ↓
    ┌────┴────┐
    │         │
    │    YES  │
    │         │
    ▼         ▼
Generate Wireframes (Step 2.5) → ./docs/ui_ux/wireframes/ ⚠️ USER REVIEW
         ↓
    ┌────┴────┐
    │ APPROVE │
    │         │
    ▼         ▼
UI/UX Design System (Step 3) → ./docs/ui_ux/ (Use converted components)
         ↓
Platform-Specific Code (Step 4) → ./docs/ui_ux/ (Convert HTML to platform)
         ↓
    └────┬────┘
         │
    NO   │
         │
         ▼
Implementation Plan (Step 5) → ./docs/implementation_plans/
         ↓
USER CONFIRMATION REQUIRED ⚠️
         ↓
Execute Implementation (Step 6)
```

---

## STEP 0: Verify & Generate Tech-Specific Commands and Project Rules (MANDATORY - FIRST STEP)

**Objective:** Ensure all required tech/language/framework-specific command files and project rules exist before proceeding with feature generation

**⚠️ THIS STEP MUST BE EXECUTED FIRST - BEFORE ANY OTHER STEP**

### 0.1 Identify Required Tech Stack

**From user requirement (or initial parsing), extract:**
- **Technology:** [Flutter/React Native/Next.js/Vue/etc.]
- **Language:** [Dart/Kotlin/Swift/TypeScript/JavaScript/etc.]
- **Framework:** [Bloc/Provider/Redux/Vuex/etc.]
- **Platform:** [iOS/Android/Web/Desktop/Cross-platform]

**Example:**
```
Technology: Flutter
Language: Dart
Framework: Bloc
Platform: iOS, Android
```

### 0.2 Check commands/specify/ Directory

**MANDATORY: Check for existing tech-specific commands**

**Directory to check:**
```
./.cursor/commands/specify/
```

**Required files to verify:**
1. `research_plan_[TECH]_[LANGUAGE].prompt.md` (e.g., `research_plan_flutter_dart.prompt.md`)
2. `ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md` (e.g., `ui_ux_design_generator_flutter_dart.prompt.md`)
3. `ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md` (e.g., `ui_ux_bridge_flutter_dart.prompt.md`)
4. `implementation_plan_[TECH]_[LANGUAGE].prompt.md` (e.g., `implementation_plan_flutter_dart.prompt.md`)

**Check process:**
1. List all files in `./.cursor/commands/specify/`
2. Identify which required files exist
3. Identify which required files are missing

### 0.3 Generate Missing Command Files

**IF any required files are missing:**

**Source files to reference:**
```
./.cursor/commands/common/
├── research_plan_common.prompt.md
├── ui_ux_design_generator.prompt.md
├── ui_ux_bridge.prompt.md
└── implementation_plan_common.prompt.md
```

**Generation process:**
1. Read the corresponding common command file
2. Adapt it for the specific tech/language/framework
3. Generate tech-specific version with:
   - Technology-specific syntax
   - Language-specific patterns
   - Framework-specific conventions
   - Platform-specific considerations

**File naming convention:**
```
[TYPE]_[TECH]_[LANGUAGE].prompt.md
```

**Examples:**
- `research_plan_flutter_dart.prompt.md`
- `ui_ux_design_generator_nextjs_typescript.prompt.md`
- `ui_ux_bridge_react_native_typescript.prompt.md`
- `implementation_plan_vue_javascript.prompt.md`

### 0.4 Save Generated Files

**⚠️ MANDATORY: Save generated files to:**
```
./.cursor/commands/specify/[FILENAME].prompt.md
```

**Directory Structure After Step 0:**
```
./.cursor/commands/
├── common/
│   ├── research_plan_common.prompt.md
│   ├── ui_ux_design_generator.prompt.md
│   ├── ui_ux_bridge.prompt.md
│   └── implementation_plan_common.prompt.md
└── specify/
    ├── research_plan_[TECH]_[LANGUAGE].prompt.md
    ├── ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md
    ├── ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md
    └── implementation_plan_[TECH]_[LANGUAGE].prompt.md
```

### 0.6 Check rules/ Directory for Project Rules

**MANDATORY: Check for existing tech-specific project rules**

**Directory to check:**
```
./.cursor/rules/
```

**Required file to verify:**
1. `project-rule_[TECH]_[LANGUAGE].mdc` (e.g., `project-rule_flutter_dart.mdc`)

**Check process:**
1. List all files in `./.cursor/rules/`
2. Identify if the required project rule file exists
3. Identify if the project rule file is missing

### 0.7 Generate Missing Project Rule File

**IF the required project rule file is missing:**

**Source file to reference:**
```
./.cursor/rules/common/project_rule_common.mdc
```

**Generation process:**
1. Read the common project rule file from `./.cursor/rules/common/project_rule_common.mdc`
2. Adapt it for the specific tech/language/framework
3. Generate tech-specific version with:
   - Technology-specific syntax examples
   - Language-specific patterns and conventions
   - Framework-specific state management patterns
   - Platform-specific UI/UX guidelines
   - Technology-specific code examples

**File naming convention:**
```
project-rule_[TECH]_[LANGUAGE].mdc
```

**Examples:**
- `project-rule_flutter_dart.mdc`
- `project-rule_nextjs_typescript.mdc`
- `project-rule_react_native_typescript.mdc`
- `project-rule_vue_javascript.mdc`

### 0.8 Save Generated Project Rule File

**⚠️ MANDATORY: Save generated project rule file to:**
```
./.cursor/rules/project-rule_[TECH]_[LANGUAGE].mdc
```

**Updated Directory Structure After Step 0:**
```
./.cursor/
├── commands/
│   ├── common/
│   │   ├── research_plan_common.prompt.md
│   │   ├── ui_ux_design_generator.prompt.md
│   │   ├── ui_ux_bridge.prompt.md
│   │   └── implementation_plan_common.prompt.md
│   └── specify/
│       ├── research_plan_[TECH]_[LANGUAGE].prompt.md
│       ├── ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md
│       ├── ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md
│       └── implementation_plan_[TECH]_[LANGUAGE].prompt.md
└── rules/
    ├── common/
    │   └── project_rule_common.mdc
    └── project-rule_[TECH]_[LANGUAGE].mdc
```

### 0.9 Verification Checklist

**Before proceeding to Step 1, verify:**
- ✅ All 4 required tech-specific command files exist in `./.cursor/commands/specify/`
- ✅ Project rule file exists in `./.cursor/rules/`
- ✅ All files are properly named according to tech/language/framework
- ✅ Files contain technology-specific adaptations
- ✅ Files reference correct syntax and patterns for the tech stack

**IF verification fails:**
- Regenerate missing files
- Ensure proper tech-specific adaptations
- Verify file locations

**Deliverable:**
- ✅ Complete set of tech-specific command files in `./.cursor/commands/specify/`
- ✅ Tech-specific project rule file in `./.cursor/rules/`
- ✅ Verification report confirming all files exist

**Action:** Store tech stack information, file locations, and project rule location in memory for use in subsequent steps.

---

## STEP 0.5: Detect & Process UI Design Images (CONDITIONAL - IF UI IMAGES PROVIDED)

**Objective:** Detect, analyze, and convert UI design images to HTML components before proceeding with normal workflow

**⚠️ CONDITIONAL EXECUTION:**
- **IF user provides UI design image(s)** → Execute this step
- **IF user provides text-only requirement** → Skip this step and proceed to Step 1

**⚠️ MANDATORY: Execute this step BEFORE Step 1 if UI images are detected**

### 0.5.1 Detect UI Design Images

**Check user input for:**
- Image files (PNG, JPG, JPEG, SVG, etc.)
- Screenshots or mockups
- Design files (Figma links, Sketch files, etc.)
- Any visual design references

**Detection Criteria:**
- Files attached that are image formats
- User mentions "image", "design", "mockup", "screenshot", "UI", "wireframe"
- URLs pointing to design tools (Figma, Dribbble, Behance, etc.)

**Action:**
- If images detected → Proceed to Step 0.5.2
- If no images → Skip to Step 1

### 0.5.2 Break Down UI Image into Components

**Objective:** Analyze the UI image and identify all distinct components and sections

**⚠️ MANDATORY: AI MUST analyze the image comprehensively and break it down into logical parts**

**Component Identification Process:**

1. **Screen-Level Analysis:**
   - Identify if single screen or multiple screens
   - Identify screen type (onboarding, login, dashboard, detail, etc.)
   - Identify overall layout structure (header, body, footer, sidebar, etc.)

2. **Section-Level Breakdown:**
   - Break into major sections (Header, Navigation, Main Content, Sidebar, Footer, etc.)
   - Identify repeated patterns (card lists, grids, forms, etc.)
   - Identify distinct visual areas

3. **Component-Level Breakdown:**
   - For each section, identify individual components:
     - Buttons, Inputs, Cards, Lists, Modals, Navigation bars, etc.
     - Icons, Images, Typography elements
     - Interactive elements (toggles, sliders, checkboxes, etc.)

4. **Hierarchical Organization:**
   - Organize components in hierarchy:
     - Page/Screen Level
       - Section Level
         - Component Level
           - Element Level (text, icon, image, etc.)

**Deliverable:**
```markdown
## UI Image Breakdown Analysis

**Image Source:** [Image filename/path/URL]
**Analysis Date:** [Date]

### Screen Identification
- **Screen Type:** [Onboarding/Login/Dashboard/Detail/etc.]
- **Platform:** [Mobile/Tablet/Desktop/Responsive]
- **Theme:** [Light/Dark/Custom]

### Section Breakdown
1. **Section 1: [Section Name]**
   - **Location:** [Top/Middle/Bottom/Left/Right]
   - **Purpose:** [Function/Content]
   - **Components:**
     - Component 1.1: [Component Name] - [Description]
     - Component 1.2: [Component Name] - [Description]
     - Component 1.3: [Component Name] - [Description]

2. **Section 2: [Section Name]**
   - **Location:** [Position]
   - **Purpose:** [Function/Content]
   - **Components:**
     - Component 2.1: [Component Name] - [Description]
     - Component 2.2: [Component Name] - [Description]
     - [Additional components...]

[Continue for all sections]

### Component Inventory
**Total Components Identified:** [Number]

| Component ID | Component Name | Section | Type | Description | Priority |
|--------------|---------------|---------|------|-------------|----------|
| C001 | [Name] | [Section] | [Button/Card/Input/etc.] | [Description] | [High/Medium/Low] |
| C002 | [Name] | [Section] | [Type] | [Description] | [Priority] |
| [Continue for all components] |

### Visual Elements Inventory
- **Colors:** [Primary, Secondary, Accent colors identified]
- **Typography:** [Font families, sizes, weights observed]
- **Spacing:** [Margins, padding patterns]
- **Shadows:** [Shadow styles and elevations]
- **Borders:** [Border styles and radius]
- **Icons:** [Icon styles and types]
- **Images:** [Image types and placements]
- **Animations/Effects:** [Observed animations or visual effects]
```

### 0.5.3 Convert Each Component to HTML Using UI/UX Bridge

**Objective:** Convert each identified component to semantic HTML/CSS using UI/UX Bridge workflow

**⚠️ MANDATORY: Reference and use UI/UX Bridge prompt file for conversion**

**Reference File:**
- **Primary:** `./.cursor/commands/specify/ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md`
- **Fallback:** `./.cursor/commands/common/ui_ux_bridge.prompt.md`

**⚠️ CRITICAL: Read UI/UX Bridge prompt file before proceeding**

**Conversion Process for Each Component:**

**For EACH component identified in Step 0.5.2:**

1. **Extract Component Requirements:**
   - Visual appearance (colors, sizes, spacing)
   - Layout and positioning
   - Typography details
   - Interactive states (hover, active, disabled)
   - Responsive behavior
   - Accessibility requirements

2. **Apply UI/UX Bridge Workflow:**
   - **PRE-PHASE:** Check UI styles reference and UI/UX reference data
   - **PHASE 1:** Create semantic HTML structure for component
   - **PHASE 2:** Implement CSS styling with design tokens
   - **PHASE 3:** Convert to target platform code (if needed)

3. **Generate Component HTML/CSS:**
   - Semantic HTML structure
   - Complete CSS with all styling details
   - Include all states and variations
   - Include responsive breakpoints
   - Include accessibility attributes

**Conversion Command Template:**
```
@ui_ux_bridge

Component: [Component Name]
Type: [Button/Card/Input/Navigation/etc.]
Requirements:
- [Visual requirement 1]
- [Visual requirement 2]
- [Interactive requirement]
- [Responsive requirement]
- [Accessibility requirement]

Reference: [Reference to section in breakdown analysis]

Target Platform: [Flutter/React/Web/etc.]
```

**Component Conversion Order:**
- Process components from simplest to most complex
- Atomic components first (buttons, inputs, icons)
- Then molecular components (cards, forms, lists)
- Finally organism components (navigation, headers, complex layouts)

**Deliverable for Each Component:**
```markdown
## Component: [Component Name]

### Component Details
- **Component ID:** [C001, C002, etc.]
- **Section:** [Which section it belongs to]
- **Type:** [Atomic/Molecular/Organism]
- **Priority:** [High/Medium/Low]

### HTML Structure
```html
<!-- Semantic HTML for component -->
[Complete HTML code]
```

### CSS Styling
```css
/* Complete CSS with design tokens */
[Complete CSS code]
```

### Design Tokens Used
- **Colors:** [Token values]
- **Typography:** [Font properties]
- **Spacing:** [Margin/padding values]
- **Shadows:** [Shadow values]
- **Borders:** [Border properties]

### States & Variations
- **Default State:** [Description and CSS]
- **Hover State:** [Description and CSS]
- **Active State:** [Description and CSS]
- **Disabled State:** [Description and CSS]
- **Other Variations:** [If applicable]

### Responsive Behavior
- **Mobile:** [Breakpoint and behavior]
- **Tablet:** [Breakpoint and behavior]
- **Desktop:** [Breakpoint and behavior]

### Accessibility
- **ARIA Labels:** [Applied labels]
- **Keyboard Navigation:** [Support details]
- **Screen Reader:** [Support details]
- **Color Contrast:** [WCAG compliance]

### Platform-Specific Code (if applicable)
```[language]
// Target platform code
[Platform-specific implementation]
```
```

### 0.5.4 Compile All Components into Complete HTML Structure

**Objective:** Combine all converted components into a complete page/screen structure

**Assembly Process:**
1. Create base HTML document structure
2. Add global styles and design tokens
3. Assemble components in order based on original layout
4. Link component CSS files or inline styles
5. Add JavaScript for interactivity (if needed)
6. Ensure proper semantic structure and accessibility

**Deliverable:**
```markdown
## Complete UI Implementation from Image

### Page Structure
[Complete HTML document with all components assembled]

### Global Styles
[CSS for base styling, design tokens, reset styles]

### Component Library
[List of all components with their HTML/CSS]

### Design System Summary
[Extracted design tokens and patterns from image]
```

### 0.5.5 Store Converted HTML/Components

**⚠️ MANDATORY: Save converted UI components to:**
```
./docs/ui_ux/image_conversions/[FEATURE_NAME]_[DATE]/
├── image_breakdown_analysis.md
├── components/
│   ├── [COMPONENT_01]_[NAME].html
│   ├── [COMPONENT_01]_[NAME].css
│   ├── [COMPONENT_02]_[NAME].html
│   ├── [COMPONENT_02]_[NAME].css
│   └── [Additional component files...]
├── complete_page.html
├── complete_page.css
├── design_tokens.json
└── component_index.md
```

### 0.5.6 Document Converted Components

**Action:** Store the converted components and design information for use in subsequent workflow steps:
- Use in Step 3 (UI/UX Design System) as reference
- Use in Step 4 (Platform-Specific Code) as source
- Reference in Step 2 (Research & Analysis) for requirements

**Deliverable:**
```markdown
## UI Image Conversion Summary

**Image Source:** [Source]
**Conversion Date:** [Date]
**Components Converted:** [Number]
**Total Files Generated:** [Number]

### Components Converted
1. [Component Name] - [Status: Complete/Partial]
2. [Component Name] - [Status: Complete/Partial]
[Continue list...]

### Design Tokens Extracted
- Colors: [Number] tokens identified
- Typography: [Number] styles identified
- Spacing: [Number] scale values identified
- [Additional tokens...]

### Next Steps
- Use this conversion in Step 2 (Research & Analysis)
- Reference in Step 3 (UI/UX Design System)
- Apply in Step 4 (Platform-Specific Code)
```

### 0.5.7 Continue with Normal Workflow

**After completing image conversion:**
- Proceed to Step 1: Receive & Analyze User Requirement
- Include converted UI components in requirements analysis
- Use converted components as design reference
- Integrate extracted design tokens into design system

**Integration Notes:**
- The converted HTML/CSS serves as the design specification
- Design tokens extracted from image inform the design system
- Component breakdown informs the component library structure
- Continue workflow normally but use image analysis as primary design reference

---

## STEP 1: Receive & Analyze User Requirement (MANDATORY)

**Objective:** Extract and document complete user requirements

### 1.1 Capture User Input

**User provides:**
- Feature description
- Target platform(s): Web/Mobile (iOS/Android)/Desktop/Cross-platform
- Design style preferences (if any)
- Technology stack preferences (if any)
- Timeline constraints (if any)
- Any specific requirements
- **UI design images (processed in Step 0.5 if present)**

**Example Input:**
```
"I want to build a shoe shopping e-commerce app for iOS and Android 
with a modern glass morphism design style. Users should be able to 
browse shoes, filter by categories, add to cart, and checkout."
```

### 1.2 Parse Requirements

**Extract:**
- **Primary Goal:** [What the user wants to achieve]
- **Platform(s):** [iOS/Android/Web/Desktop/Flutter/React Native/etc.]
- **Design Style:** [Glass morphism/Material/Minimal/Custom/None specified]
- **Core Features:** [List all mentioned features]
- **Tech Stack:** [Flutter/React Native/Native/etc.]
- **Language:** [Dart/Kotlin/Swift/TypeScript/etc.]
- **Constraints:** [Timeline/Budget/Technical limitations]

### 1.3 Clarify Ambiguities (if needed)

**If critical information is missing:**
- Ask ONE clarification question
- Provide default assumptions if no response
- Document assumptions clearly

**Deliverable:**
```markdown
# Feature Requirement Summary

**Date:** [Current date]
**Project:** [Feature name]
**Platforms:** [Target platforms]
**Tech Stack:** [Technology choices]
**Design Style:** [Design approach]

## Core Requirements
[Detailed list]

## Assumptions
[Any assumptions made]

## Constraints
[Known limitations]
```

**Action:** Store this summary in memory for use in subsequent steps.

---

## STEP 1.5: Determine UI/UX Requirement (MANDATORY)

**Objective:** Accurately determine if the feature requires UI/UX components

**⚠️ CRITICAL: This determination must be accurate - do not skip UI/UX if it's actually needed**

### 1.5.1 UI/UX Requirement Analysis

**Analyze the feature requirements to determine if UI/UX is needed:**

**Features that DO NOT require UI/UX:**
- **Backend-only features:** API endpoints, server-side logic, database migrations, background jobs
- **Pure business logic:** Domain services, calculations, data processing without user interaction
- **Infrastructure features:** DevOps scripts, CI/CD configurations, deployment scripts
- **Data layer only:** Database schemas, data migrations, ETL processes
- **API-only features:** REST/GraphQL endpoints, webhooks, integrations without UI
- **Library/package development:** Reusable libraries, SDKs without UI components
- **Testing infrastructure:** Test utilities, mocking frameworks, test data generators
- **Configuration-only:** Environment setup, config files, feature flags (without UI toggles)

**Features that DO require UI/UX:**
- **User-facing features:** Any feature that users interact with directly
- **Admin panels:** Management interfaces, dashboards, control panels
- **Forms and inputs:** User data entry, search interfaces, filters
- **Display components:** Lists, cards, tables, charts, visualizations
- **Navigation:** Menus, tabs, routing, page transitions
- **Interactive elements:** Buttons, modals, dialogs, tooltips
- **Mobile apps:** Any mobile application feature
- **Web applications:** Any web application feature with user interface
- **Desktop applications:** Any desktop application feature
- **Data visualization:** Charts, graphs, reports with visual representation
- **Settings/Preferences:** User preference interfaces, configuration UIs
- **Onboarding flows:** User onboarding, tutorials, walkthroughs

### 1.5.2 Determination Criteria

**Ask these questions:**
1. **Will users interact with this feature through a visual interface?**
   - YES → UI/UX required
   - NO → Continue to question 2

2. **Does this feature display information to users?**
   - YES → UI/UX required
   - NO → Continue to question 3

3. **Does this feature require user input through forms, buttons, or other UI elements?**
   - YES → UI/UX required
   - NO → Continue to question 4

4. **Is this feature purely backend/infrastructure/data processing?**
   - YES → UI/UX NOT required
   - NO → UI/UX likely required

### 1.5.3 Decision Logic

**IF any of the following are TRUE, UI/UX is REQUIRED:**
- ✅ Feature has user-facing components
- ✅ Feature displays data to users
- ✅ Feature requires user interaction (clicks, inputs, gestures)
- ✅ Feature is part of a mobile/web/desktop application
- ✅ Feature includes forms, buttons, navigation, or visual elements
- ✅ Feature is an admin panel, dashboard, or management interface

**IF all of the following are TRUE, UI/UX is NOT REQUIRED:**
- ✅ Feature is backend-only (API, server logic, database)
- ✅ Feature has no user-facing components
- ✅ Feature does not display information to users
- ✅ Feature does not require user interaction
- ✅ Feature is infrastructure, configuration, or data processing only

### 1.5.4 Document Decision

**Deliverable:**
```markdown
## UI/UX Requirement Determination

**Feature:** [Feature Name]
**Requires UI/UX:** [YES/NO]

**Determination Rationale:**
- [Reason 1]
- [Reason 2]
- [Reason 3]

**Feature Type:** [User-facing/Backend-only/Infrastructure/Data processing/etc.]

**Decision Confidence:** [High/Medium/Low]
- High: Clear backend-only or clear user-facing feature
- Medium: Some ambiguity, but determination is reasonable
- Low: Unclear - may need clarification

**If Low Confidence:**
- Document assumptions
- Proceed with conservative choice (include UI/UX if uncertain)
- Note in requirements that UI/UX determination may need review
```

### 1.5.5 Store Decision

**Action:** Store UI/UX requirement decision in memory:
- `requires_ui_ux: true/false`
- `ui_ux_rationale: [explanation]`
- `decision_confidence: [High/Medium/Low]`

**This decision will be used to:**
- Skip Step 3 (UI/UX Design System) if `requires_ui_ux: false`
- Skip Step 4 (Platform-Specific UI Code) if `requires_ui_ux: false`
- Include UI/UX steps if `requires_ui_ux: true`

**⚠️ IMPORTANT:** If confidence is LOW, default to including UI/UX steps to avoid missing requirements.

---

## STEP 2: Execute Research & Analysis Plan (MANDATORY)

**Objective:** Perform comprehensive feature research following tech-specific research plan prompt

**⚠️ MANDATORY: READ AND REFERENCE THE RESEARCH PLAN PROMPT FILE**

**File Path (from Step 0):**
- **Primary:** `./.cursor/commands/specify/research_plan_[TECH]_[LANGUAGE].prompt.md`
- **Fallback:** `./.cursor/commands/common/research_plan_common.prompt.md`

Before proceeding, you MUST:
1. Read the complete tech-specific research plan prompt file (generated in Step 0)
2. If tech-specific file doesn't exist, use common file as fallback
3. Understand all 7 steps and their requirements
4. Follow the instructions exactly as specified in that file
5. Generate all deliverables as defined in that file

**⚠️ EXECUTE ALL 7 STEPS FROM THE RESEARCH PLAN PROMPT FILE**

### 2.1 Reference Document
Follow the research plan prompt file exactly:
- Step 1: Analyze Given Requirements
- Step 2: List All Related Technologies & Concepts
- Step 3: Identify 2-3 Different Approaches
- Step 4: Conclude Final Approach
- Step 5: Write Details & Flow Diagrams
- Step 6: Describe in Human-Friendly Language
- Step 7: Create Implementation Plan

### 2.2 Generate Complete Research Document

**File naming convention:**
```
[FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
```

**Example:**
```
SHOE_SHOP_ECOMMERCE_RESEARCH_PLAN_2025-12-03.md
```

### 2.3 Output Location

**⚠️ MANDATORY: Save research plan to:**
```
./docs/research_plans/[FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
```

**Deliverable:**
Complete research document with:
- ✅ Requirements Analysis Summary
- ✅ Technology & Concept Inventory
- ✅ 2-3 Implementation Approaches (fully documented)
- ✅ Final Approach Selection (with rationale)
- ✅ Complete Technical Specification (with diagrams)
- ✅ Human-Friendly Explanation
- ✅ Implementation Plan (high-level overview)

**Directory Structure After Step 2:**
```
./docs/
└── research_plans/
    └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
```

---

## STEP 2.5: Generate UI Wireframes (CONDITIONAL - ONLY IF UI/UX REQUIRED)

**Objective:** Create wireframe layouts for all screens/pages to allow user review before detailed UI/UX design

**⚠️ CONDITIONAL EXECUTION:**
- **IF `requires_ui_ux: true`** → Execute this step
- **IF `requires_ui_ux: false`** → Skip this step and proceed to Step 5

**⚠️ MANDATORY USER REVIEW CHECKPOINT:**
- After generating wireframes, **MUST present them to user for review**
- **WAIT for user approval** before proceeding to Step 3 (UI/UX Design System)
- User can request changes, which will be incorporated before proceeding

### 2.5.1 Wireframe Generation Process

**Input from Step 2:**
- Use selected approach from research plan
- Reference functional requirements
- Consider user workflows and navigation
- Apply platform constraints (mobile/tablet/desktop)

### 2.5.2 Create Wireframes for Each Screen

**For EACH screen/page identified in research plan:**

**Wireframe Components:**
1. **Layout Structure:** Header, navigation, main content area, sidebar (if applicable), footer
2. **Component Placement:** Position of buttons, inputs, cards, lists, images, etc.
3. **Content Hierarchy:** Primary content, secondary content, supporting elements
4. **Navigation Elements:** Menus, tabs, buttons, links, breadcrumbs
5. **Interactive Elements:** Buttons, inputs, dropdowns, modals, tooltips
6. **Spacing Relationships:** Margins, padding, alignment between elements
7. **Responsive Breakpoints:** Layout variations for different screen sizes (if applicable)

**Wireframe Format Requirements:**

**ASCII Art Format (Text Symbols):**
- Use box-drawing characters (┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼) for structure
- Use text labels for components ([Button], [Input], [Card], etc.)
- Show hierarchy through indentation and nesting
- Include annotations for spacing, alignment, and relationships
- Mark interactive elements clearly
- Show responsive variations side-by-side or separately

**Example Wireframe Format:**
```
┌─────────────────────────────────────────────────┐
│                    HEADER                       │
│  [Logo]              [Nav Items]    [User Menu] │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  [Search Bar with Filters]              │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │  [Card]   │  │  [Card]   │  │  [Card]   │  │
│  │           │  │           │  │           │  │
│  │  [Image]  │  │  [Image]  │  │  [Image]  │  │
│  │  [Title]  │  │  [Title]  │  │  [Title]  │  │
│  │  [Price]  │  │  [Price]  │  │  [Price]  │  │
│  │  [Button] │  │  [Button] │  │  [Button] │  │
│  └───────────┘  └───────────┘  └───────────┘  │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  [Pagination Controls]                  │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
├─────────────────────────────────────────────────┤
│                    FOOTER                       │
│  [Links]  [Social]  [Copyright]                │
└─────────────────────────────────────────────────┘
```

### 2.5.3 Wireframe Documentation

**For each wireframe, include:**

1. **Screen/Page Information:**
   - Screen name and purpose
   - User flow position (entry point, intermediate, exit point)
   - Primary user goal for this screen

2. **Layout Description:**
   - Overall layout structure
   - Grid system (if applicable)
   - Column structure and widths

3. **Component Inventory:**
   - List of all components with labels
   - Component hierarchy and nesting
   - Component relationships

4. **User Flow Integration:**
   - Where user comes from (previous screen)
   - Where user can go (next screens/actions)
   - Navigation paths and interactions

5. **Responsive Considerations:**
   - Mobile layout variations
   - Tablet layout variations
   - Desktop layout variations
   - Breakpoints for layout changes

6. **Accessibility Considerations:**
   - Focus order
   - Keyboard navigation paths
   - Screen reader considerations

### 2.5.4 Generate Complete Wireframe Document

**File naming convention:**
```
[FEATURE_NAME]_WIREFRAMES_[DATE].md
```

**Example:**
```
SHOE_SHOP_ECOMMERCE_WIREFRAMES_2025-12-03.md
```

### 2.5.5 Output Location

**⚠️ MANDATORY: Save wireframes to:**
```
./docs/ui_ux/wireframes/[FEATURE_NAME]_WIREFRAMES_[DATE].md
```

**Deliverable:**
Complete wireframe document with:
- ✅ All screen/page wireframes (ASCII art format)
- ✅ Layout descriptions for each screen
- ✅ Component inventory and hierarchy
- ✅ Navigation flow diagrams
- ✅ Responsive layout variations
- ✅ User flow integration notes
- ✅ Accessibility considerations

**Directory Structure After Step 2.5:**
```
./docs/
├── research_plans/
│   └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
└── ui_ux/
    └── wireframes/
        └── [FEATURE_NAME]_WIREFRAMES_[DATE].md
```

### 2.5.6 Present Wireframes for User Review

**⚠️ MANDATORY: After generating wireframes, present them to user and WAIT for approval**

**Presentation Format:**
```markdown
# Wireframe Review: [Feature Name]

## Generated Wireframes

[Display all wireframes here]

## Screen Inventory

1. **Screen 1:** [Screen Name] - [Purpose]
2. **Screen 2:** [Screen Name] - [Purpose]
3. **Screen 3:** [Screen Name] - [Purpose]
[Continue list...]

## User Flow Overview

[Flow diagram showing screen transitions]

## ⚠️ REVIEW REQUIRED

Please review the wireframes above and provide feedback:

👉 **APPROVE** - Wireframes look good, proceed to detailed UI/UX design (Step 3)
👉 **REVISE** - I want changes to: [specify which screens/components]
👉 **CLARIFY** - I have questions about: [specify questions]

**Valid responses:**
- "APPROVE" / "OK" / "GOOD" / "PROCEED" → Continue to Step 3
- "REVISE [specific changes]" → Update wireframes based on feedback, then present again
- "CHANGE [screen/component] [description]" → Make requested changes
```

### 2.5.7 Handle User Feedback

**IF user APPROVES:**
- Proceed to Step 3 (UI/UX Design System)
- Use approved wireframes as layout foundation

**IF user requests REVISIONS:**
- Update wireframes based on user feedback
- Regenerate affected wireframe sections
- Present updated wireframes for review again
- **WAIT for approval** before proceeding

**IF user has QUESTIONS:**
- Answer questions clearly
- Update wireframes if needed based on clarifications
- Present again for approval

**⚠️ DO NOT proceed to Step 3 until user explicitly approves wireframes**

---

## STEP 3: Generate UI/UX Design System (CONDITIONAL - ONLY IF UI/UX REQUIRED)

**Objective:** Create comprehensive UI/UX specifications following tech-specific UI/UX design generator prompt

**⚠️ CONDITIONAL EXECUTION:**
- **IF `requires_ui_ux: true`** → Execute this step
- **IF `requires_ui_ux: false`** → Skip this step and proceed to Step 5

**⚠️ MANDATORY: READ AND REFERENCE THE UI/UX DESIGN GENERATOR PROMPT FILE (ONLY IF UI/UX REQUIRED)**

**⚠️ CRITICAL: The UI/UX Design Generator Prompt includes checking `.cursor/commands/common/ui_styles_reference.md` AND `.cursor/uiux_reference/data/` folder first to match project requirements with suitable UI styles. This step is mandatory and must be completed before proceeding.**

**File Path (from Step 0):**
- **Primary:** `./.cursor/commands/specify/ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md`
- **Fallback:** `./.cursor/commands/common/ui_ux_design_generator.prompt.md`

**UI Styles Reference:**
- **Location:** `./.cursor/commands/common/ui_styles_reference.md`
- **Purpose:** Contains 102 top-tier UI styles with "Suitable Project Types" attribute
- **Action:** The UI/UX Design Generator Prompt will check this reference first to find best-fit styles

**UI/UX Reference Data:**
- **Location:** `./.cursor/uiux_reference/data/`
- **Purpose:** Contains comprehensive UI/UX reference data including:
  - `styles.csv` - UI style patterns and specifications
  - `colors.csv` - Color palettes and schemes
  - `typography.csv` - Typography guidelines and font recommendations
  - `ux-guidelines.csv` - UX best practices and guidelines
  - `landing.csv` - Landing page patterns and examples
  - `products.csv` - Product page patterns and examples
  - `charts.csv` - Data visualization patterns
  - `prompts.csv` - UI/UX prompt templates and examples
  - `stacks/[FRAMEWORK].csv` - Framework-specific UI/UX patterns
- **Action:** The UI/UX Design Generator Prompt will check this reference data folder to provide additional context and comprehensive UI/UX solutions

Before proceeding, you MUST:
1. Read the complete tech-specific UI/UX design generator prompt file (generated in Step 0)
2. If tech-specific file doesn't exist, use common file as fallback
3. Understand all 6 steps and their requirements (including Step 0.0: UI Styles Reference Check)
4. Follow the instructions exactly as specified in that file
5. Generate all deliverables as defined in that file

**⚠️ EXECUTE ALL 6 STEPS FROM THE UI/UX DESIGN GENERATOR PROMPT FILE**

### 3.1 Reference Document
Follow the UI/UX design generator prompt file exactly:
- Step 1: Analyze User Requirements
- Step 2: Define Design Atomic Components
- Step 3: Define Molecular Components
- Step 4: Define Organism Components
- Step 5: Define Templates & Layouts
- Step 6: Generate Animation & Interaction Patterns

### 3.2 Use Previous Steps' Results

**Input from Step 2 (Research Plan):**
- Use selected approach from research plan
- Reference platform requirements
- Apply design style preferences
- Consider technical constraints

**Input from Step 2.5 (Wireframes):**
- Use approved wireframe layouts as foundation
- Reference layout structure and component hierarchy
- Apply spacing and positioning from wireframes
- Ensure design system aligns with wireframe structure

### 3.3 Generate Complete Design System

**File naming convention:**
```
[FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
```

**Example:**
```
SHOE_SHOP_ECOMMERCE_UI_UX_DESIGN_SYSTEM_2025-12-03.md
```

### 3.4 Output Location

**⚠️ MANDATORY: Save UI/UX design system to:**
```
./docs/ui_ux/[FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
```

**Deliverable:**
Complete design system with:
- ✅ Design Tokens (Colors, Typography, Spacing, Shadows)
- ✅ Atomic Components (Buttons, Inputs, etc.)
- ✅ Molecular Components (Cards, Forms, etc.)
- ✅ Organism Components (Navigation, Modals, etc.)
- ✅ Page Templates & Layouts
- ✅ Animation & Interaction Patterns
- ✅ Responsive Design Rules
- ✅ Accessibility Guidelines

**Directory Structure After Step 3:**
```
./docs/
├── research_plans/
│   └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
└── ui_ux/
    └── [FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
```

---

## STEP 4: Generate Platform-Specific UI Code (CONDITIONAL - ONLY IF UI/UX REQUIRED)

**Objective:** Convert UI/UX design to platform-specific code following tech-specific UI/UX bridge prompt

**⚠️ CONDITIONAL EXECUTION:**
- **IF `requires_ui_ux: true`** → Execute this step
- **IF `requires_ui_ux: false`** → Skip this step and proceed to Step 5

**⚠️ MANDATORY: READ AND REFERENCE THE UI/UX BRIDGE PROMPT FILE (ONLY IF UI/UX REQUIRED)**

**⚠️ CRITICAL: The UI/UX Bridge Prompt includes checking `.cursor/commands/common/ui_styles_reference.md` AND `.cursor/uiux_reference/data/` folder first in the PRE-PHASE to match project requirements with suitable UI styles. This step is mandatory and must be completed before proceeding to Phase 1.**

**File Path (from Step 0):**
- **Primary:** `./.cursor/commands/specify/ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md`
- **Fallback:** `./.cursor/commands/common/ui_ux_bridge.prompt.md`

**UI Styles Reference:**
- **Location:** `./.cursor/commands/common/ui_styles_reference.md`
- **Purpose:** Contains 102 top-tier UI styles with "Suitable Project Types" attribute
- **Action:** The UI/UX Bridge Prompt will check this reference first in PRE-PHASE Step 0.0 to find best-fit styles

**UI/UX Reference Data:**
- **Location:** `./.cursor/uiux_reference/data/`
- **Purpose:** Contains comprehensive UI/UX reference data including:
  - `styles.csv` - UI style patterns and specifications
  - `colors.csv` - Color palettes and schemes
  - `typography.csv` - Typography guidelines and font recommendations
  - `ux-guidelines.csv` - UX best practices and guidelines
  - `landing.csv` - Landing page patterns and examples
  - `products.csv` - Product page patterns and examples
  - `charts.csv` - Data visualization patterns
  - `prompts.csv` - UI/UX prompt templates and examples
  - `stacks/[FRAMEWORK].csv` - Framework-specific UI/UX patterns
- **Action:** The UI/UX Bridge Prompt will check this reference data folder in PRE-PHASE Step 0.0 to provide additional context and comprehensive UI/UX solutions

Before proceeding, you MUST:
1. Read the complete tech-specific UI/UX bridge prompt file (generated in Step 0)
2. If tech-specific file doesn't exist, use common file as fallback
3. Understand all 3 phases and PRE-PHASE requirements (including Step 0.0: UI Styles Reference Check)
4. Follow the instructions exactly as specified in that file
5. Generate all deliverables as defined in that file

**⚠️ MANDATORY: WIREFRAME DESCRIPTION BEFORE IMPLEMENTATION**

**Before executing Phase 1, you MUST:**
1. Create a wireframe description using text symbols/ASCII art for each UI component/screen
2. The wireframe must clearly show:
   - Layout structure (header, content, footer, sidebars, etc.)
   - Component placement and hierarchy
   - Spacing and alignment relationships
   - Navigation flow and interactive elements
   - Responsive breakpoints (if applicable)
3. Present the wireframe for review
4. **DO NOT proceed with Phase 1 implementation until wireframe is reviewed and approved**

**Wireframe Format Example:**
```
┌─────────────────────────────────────┐
│           HEADER                    │
│  [Logo]  [Nav Items]  [User Menu]   │
├─────────────────────────────────────┤
│                                     │
│  ┌──────────┐  ┌──────────┐        │
│  │  Card 1   │  │  Card 2   │        │
│  │           │  │           │        │
│  └──────────┘  └──────────┘        │
│                                     │
│           CONTENT AREA              │
│                                     │
├─────────────────────────────────────┤
│           FOOTER                    │
└─────────────────────────────────────┘
```

**⚠️ EXECUTE ALL 3 PHASES FROM THE UI/UX BRIDGE PROMPT FILE**

### 4.1 Reference Document
Follow the UI/UX bridge prompt file exactly:
- Phase 1: Design Analysis & Semantic HTML Structure
- Phase 2: CSS Implementation (Intermediate Format)
- Phase 3: Platform-Specific Conversion

### 4.2 Use Previous Results

**Input from Step 3:**
- Use complete design system specification
- Reference all design tokens
- Apply all component specifications
- Follow animation guidelines

**Input from Step 2:**
- Use selected platform from research plan
- Apply technical constraints
- Follow architecture decisions

### 4.3 Generate Complete UI Implementation

**File naming convention:**
```
[FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
```

**Example:**
```
SHOE_SHOP_ECOMMERCE_UI_IMPLEMENTATION_FLUTTER_2025-12-03.md
```

### 4.4 Output Location

**⚠️ MANDATORY: Save UI implementation to:**
```
./docs/ui_ux/[FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
```

**Deliverable:**
Complete platform-specific UI code with:
- ✅ Semantic HTML Structure (intermediate format)
- ✅ Complete CSS with Design Tokens
- ✅ JavaScript for Interactivity (if needed)
- ✅ Platform-Specific Code (Flutter/Kotlin/Swift/etc.)
- ✅ Component Mapping Documentation
- ✅ Conversion Quality Checklist
- ✅ Usage Examples

**Additional Files:**
If generating actual code files, also create:
```
./docs/ui_ux/code_samples/[PLATFORM]/
```

**Directory Structure After Step 4:**
```
./docs/
├── research_plans/
│   └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
└── ui_ux/
    ├── [FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
    ├── [FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
    └── code_samples/
        └── [PLATFORM]/
            ├── index.html
            ├── styles.css
            ├── script.js
            └── [platform_specific_files]
```

---

## STEP 5: Generate Complete Implementation Plan (MANDATORY)

**Objective:** Create detailed implementation plan following tech-specific implementation plan prompt

**⚠️ MANDATORY: READ AND REFERENCE THE IMPLEMENTATION PLAN PROMPT FILE**

**File Path (from Step 0):**
- **Primary:** `./.cursor/commands/specify/implementation_plan_[TECH]_[LANGUAGE].prompt.md`
- **Fallback:** `./.cursor/commands/common/implementation_plan_common.prompt.md`

Before proceeding, you MUST:
1. Read the complete tech-specific implementation plan prompt file (generated in Step 0)
2. If tech-specific file doesn't exist, use common file as fallback
3. Understand all 8 planning sections and their requirements
4. Follow the instructions exactly as specified in that file
5. Generate all deliverables as defined in that file

**⚠️ EXECUTE ALL SECTIONS FROM THE IMPLEMENTATION PLAN PROMPT FILE**

### 5.1 Reference Document
Follow the implementation plan prompt file exactly:
1. Requirements Analysis
2. Architecture Design
3. Dependencies & Infrastructure
4. Data Flow & Business Logic
5. Error Handling Strategy
6. Code Analysis & Validation
7. Implementation Checklist
8. Code Generation Requirements

### 5.2 Synthesize All Previous Results

**Input from Step 2 (Research Plan):**
- Selected implementation approach
- Architecture decisions
- Technology choices
- Data flow specifications
- Error handling strategies

**Input from Step 3 (UI/UX Design):**
- Design system tokens
- Component specifications
- Page templates
- Animation requirements

**Input from Step 4 (UI Implementation):**
- Platform-specific UI code
- Component mapping
- Widget/View structure

### 5.3 Generate Complete Implementation Plan

**File naming convention:**
```
[FEATURE_NAME]_IMPLEMENTATION_PLAN_[DATE].md
```

**Example:**
```
SHOE_SHOP_ECOMMERCE_IMPLEMENTATION_PLAN_2025-12-03.md
```

### 5.4 Split into Child Plans

**MANDATORY: Create 6 child plans as specified in `research_plan.prompt.md` Step 7.7:**

**Reference:** See Step 7.7 in research_plan.prompt.md for detailed child plan specifications.

**⚠️ CRITICAL: Each child plan MUST be broken down into very detailed, granular task breakdowns:**

**Granularity Requirements:**
- Each major task must be broken into 3-7 detailed sub-steps
- Each sub-step must include:
  - Specific file paths to create/modify
  - Code structure examples
  - Property/method definitions
  - Verification criteria
  - Checklist items
- Total granular steps per child plan:
  - Setup & Infrastructure: ~100+ individual actionable steps
  - Core Layer: ~80+ individual actionable steps
  - Domain Layer: ~120+ individual actionable steps
  - Data Layer: ~100+ individual actionable steps
  - Presentation Layer: ~150+ individual actionable steps
  - Integration & Validation: ~60+ individual actionable steps

**Example Task Breakdown Pattern:**
```markdown
### Task 1.1: Create Color Constants File
**Step 1.1.1:** Create app_colors.dart
- [ ] Create file `lib/core/theme/app_colors.dart`
- [ ] Add file header comment with description

**Step 1.1.2:** Define dark theme colors
- [ ] Add class `AppColors` with static const Color fields
- [ ] Add `backgroundPrimary = Color(0xFF1A1A2E)`
- [ ] Add `backgroundSecondary = Color(0xFF1E1E2E)`
- [ ] [Continue with all color definitions...]

**Step 1.1.3:** Define light theme colors
- [ ] Add `AppColorsLight` class
- [ ] Add all light theme color definitions
- [ ] [Continue pattern...]
```

1. **Setup & Infrastructure**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_01_SETUP_[DATE].md`
   - Must include: ~100+ granular steps broken down from major tasks

2. **Core Layer**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_02_CORE_[DATE].md`
   - Must include: ~80+ granular steps broken down from major tasks

3. **Domain Layer**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_03_DOMAIN_[DATE].md`
   - Must include: ~120+ granular steps broken down from major tasks

4. **Data Layer**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_04_DATA_[DATE].md`
   - Must include: ~100+ granular steps broken down from major tasks

5. **Presentation Layer**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_05_PRESENTATION_[DATE].md`
   - Must include: ~150+ granular steps broken down from major tasks

6. **Integration & Validation**
   - File: `[FEATURE_NAME]_IMPLEMENTATION_PLAN_06_INTEGRATION_[DATE].md`
   - Must include: ~60+ granular steps broken down from major tasks

### 5.5 Output Location

**⚠️ MANDATORY: Save all implementation plans to:**
```
./docs/implementation_plans/[FEATURE_NAME]/
```

**Structure:**
```
./docs/implementation_plans/[FEATURE_NAME]/
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_[DATE].md (Main plan)
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_01_SETUP_[DATE].md
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_02_CORE_[DATE].md
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_03_DOMAIN_[DATE].md
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_04_DATA_[DATE].md
├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_05_PRESENTATION_[DATE].md
└── [FEATURE_NAME]_IMPLEMENTATION_PLAN_06_INTEGRATION_[DATE].md
```

**Deliverable:**
Complete implementation plans with:
- ✅ Main Implementation Plan (comprehensive overview)
- ✅ 6 Child Plans (detailed task breakdowns)
- ✅ Complete architecture specifications
- ✅ File structure mapping
- ✅ Code templates for all components
- ✅ Dependency lists
- ✅ Validation checklists
- ✅ Timeline and milestones

**Directory Structure After Step 5:**
```
./docs/
├── research_plans/
│   └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
├── ui_ux/
│   ├── [FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
│   ├── [FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
│   └── code_samples/
│       └── [PLATFORM]/
└── implementation_plans/
    └── [FEATURE_NAME]/
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_[DATE].md
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_01_SETUP_[DATE].md
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_02_CORE_[DATE].md
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_03_DOMAIN_[DATE].md
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_04_DATA_[DATE].md
        ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_05_PRESENTATION_[DATE].md
        └── [FEATURE_NAME]_IMPLEMENTATION_PLAN_06_INTEGRATION_[DATE].md
```

---

## ⚠️ MANDATORY USER CONFIRMATION CHECKPOINT ⚠️

**BEFORE PROCEEDING TO STEP 6, AI MUST:**

### Generate Workflow Completion Summary

```markdown
# Feature Development Workflow - Completion Summary

**Feature:** [Feature Name]
**Date:** [Date]
**Status:** ✅ Planning Complete - Awaiting Implementation Approval

---

## Workflow Execution Summary

### ✅ Step 0: Command & Project Rule Verification
**Status:** Completed
**Output:** Tech-specific command files and project rule verified/generated
**Command Files Location:** `./.cursor/commands/specify/`
**Project Rule Location:** `./.cursor/rules/`
**Tech Stack:** [Technology/Language/Framework]

### ✅ Step 1: Requirement Analysis
**Status:** Completed
**Output:** Requirements documented

### ✅ Step 1.5: UI/UX Requirement Determination
**Status:** Completed
**Requires UI/UX:** [YES/NO]
**Rationale:** [Brief explanation]

### ✅ Step 2: Research & Analysis
**Status:** Completed
**Output:** Research plan generated
**Location:** `./docs/research_plans/[FEATURE_NAME]_RESEARCH_PLAN_[DATE].md`
**Selected Approach:** [Approach name and brief rationale]

### ✅ Step 2.5: UI Wireframes
**Status:** [Completed/Skipped]
**Requires UI/UX:** [YES/NO]
**Output:** [Wireframes for [X] screens with layout structures / N/A - Feature does not require UI/UX]
**Location:** [`./docs/ui_ux/wireframes/[FEATURE_NAME]_WIREFRAMES_[DATE].md` / N/A]
**User Review:** [Approved/Revised/Pending]
**Screens:** [List of screens with wireframes / N/A]

### ✅ Step 3: UI/UX Design System
**Status:** [Completed/Skipped]
**Requires UI/UX:** [YES/NO]
**Output:** [Complete design system with [X] components / N/A - Feature does not require UI/UX]
**Location:** [`./docs/ui_ux/[FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md` / N/A]
**Design Style:** [Style name / N/A]

### ✅ Step 4: Platform-Specific UI Code
**Status:** [Completed/Skipped]
**Requires UI/UX:** [YES/NO]
**Output:** [[Platform] implementation with code samples / N/A - Feature does not require UI/UX]
**Location:** [`./docs/ui_ux/[FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md` / N/A]
**Platform:** [Platform name / N/A]

### ✅ Step 5: Implementation Plans
**Status:** Completed
**Output:** 1 main plan + 6 child plans
**Location:** `./docs/implementation_plans/[FEATURE_NAME]/`

**Plans Generated:**
1. ✅ Main Implementation Plan
2. ✅ Setup & Infrastructure Plan
3. ✅ Core Layer Plan
4. ✅ Domain Layer Plan
5. ✅ Data Layer Plan
6. ✅ Presentation Layer Plan
7. ✅ Integration & Validation Plan

---

## Implementation Overview

### Estimated Effort
- **Total Files to Create:** [Number]
- **Estimated Duration:** [X days/weeks]
- **Complexity:** [Low/Medium/High]

### Architecture Summary
- **Layers:** Domain, Data, Presentation
- **State Management:** [Bloc/Cubit]
- **Platform:** [Platform]
- **Language:** [Language]

### Key Components
- **Entities:** [Number]
- **Use Cases:** [Number]
- **Repositories:** [Number]
- **UI Screens:** [Number]
- **Widgets:** [Number]

### Dependencies
**New packages to add:** [Number]
- [Package 1]: [Version]
- [Package 2]: [Version]
- [Additional packages...]

---

## Generated Documentation

### Research Documentation
📄 `./docs/research_plans/[FEATURE_NAME]_RESEARCH_PLAN_[DATE].md`
- Requirements analysis
- Technology evaluation
- Approach comparison
- Technical specifications
- Flow diagrams

### UI/UX Documentation
[IF UI/UX Required:]
📄 `./docs/ui_ux/wireframes/[FEATURE_NAME]_WIREFRAMES_[DATE].md`
- Wireframe layouts for all screens
- Layout structure and component placement
- Navigation flow diagrams
- Responsive layout variations

📄 `./docs/ui_ux/[FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md`
- Complete design system
- Component library
- Design tokens
- Animation guidelines

📄 `./docs/ui_ux/[FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md`
- Platform-specific UI code
- Component mapping
- Code samples

[IF UI/UX NOT Required:]
ℹ️ UI/UX documentation skipped - Feature does not require user interface components

### Implementation Documentation
📄 `./docs/implementation_plans/[FEATURE_NAME]/`
- Main implementation plan
- 6 detailed child plans
- Code templates
- Validation checklists

---

## Next Steps

### Implementation Execution Order
If approved, implementation will proceed in this order:
1. **Setup & Infrastructure** (Day 1)
2. **Core Layer** (Day 1)
3. **Domain Layer** (Day 2)
4. **Data Layer** (Day 3-4)
5. **Presentation Layer** (Day 5-6)
6. **Integration & Validation** (Day 7)

### Definition of Done
- [ ] All code follows project standards
- [ ] Clean Architecture layers properly separated
- [ ] All acceptance criteria met
- [ ] Error handling implemented
- [ ] Code analysis passes (flutter analyze)
- [ ] UI matches design specifications
- [ ] All tests pass (if applicable)
- [ ] Documentation updated

---

## ⚠️ USER CONFIRMATION REQUIRED

Please review the generated documentation and confirm:

**Do you want to proceed with implementation?**

👉 **YES** - I will execute all 6 implementation plans in order
👉 **NO** - Please specify what needs to be adjusted
👉 **REVIEW** - I need to review the plans first (specify which files)

**Reply with:**
- "YES" or "PROCEED" to start implementation
- "NO" or "ADJUST [details]" to request changes
- "REVIEW [plan name]" to discuss specific plans
```

### Present Summary to User

**AI MUST:**
1. Generate the complete summary above
2. Display it to the user
3. **WAIT for explicit user confirmation**
4. Do NOT proceed to Step 6 without user approval

**Valid user responses:**
- ✅ "YES" / "PROCEED" / "GO AHEAD" / "START IMPLEMENTATION"
- ❌ "NO" / "WAIT" / "STOP"
- 🔄 "REVIEW [specific plan]" / "ADJUST [details]" / "CHANGE [something]"

---

## STEP 6: Execute Implementation (ONLY AFTER USER APPROVAL)

**⚠️ THIS STEP REQUIRES USER CONFIRMATION FROM STEP 5**

**DO NOT EXECUTE WITHOUT USER SAYING "YES" OR "PROCEED"**

### 6.1 Verify User Approval

**IF user said YES:**
- Proceed with implementation execution

**IF user said NO or WAIT:**
- Stop and ask what needs adjustment
- Go back to relevant step to make changes
- Regenerate affected documentation

**IF user said REVIEW:**
- Provide detailed explanation of requested plan
- Answer questions
- Wait for confirmation

### 6.2 Execute All Implementation Plans

**Reference document:** execute_implementation_plan.instructions.md

**Follow exact execution order:**
1. Execute Plan 01: Setup & Infrastructure
2. Execute Plan 02: Core Layer
3. Execute Plan 03: Domain Layer
4. Execute Plan 04: Data Layer
5. Execute Plan 05: Presentation Layer
6. Execute Plan 06: Integration & Validation

**For each plan:**
- Read complete plan
- Execute all tasks
- Create all files
- Implement all code
- Validate completion
- Mark plan as complete

### 6.3 Track Implementation Progress

**Create progress tracking file:**
```
./docs/implementation_plans/[FEATURE_NAME]/IMPLEMENTATION_PROGRESS.md
```

**Track:**
- Current plan being executed
- Completed tasks
- Files created
- Issues encountered
- Next steps

### 6.4 Final Validation

**After completing all plans:**
- Run `flutter analyze`
- Fix all errors and warnings
- Verify all files created
- Test on device/emulator
- Document any issues
- Generate completion report

---

## Directory Structure - Final State

After completing entire workflow:

```
./docs/
├── research_plans/
│   └── [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
├── ui_ux/
│   ├── wireframes/
│   │   └── [FEATURE_NAME]_WIREFRAMES_[DATE].md
│   ├── [FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
│   ├── [FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
│   └── code_samples/
│       └── [PLATFORM]/
│           ├── index.html
│           ├── styles.css
│           ├── script.js
│           └── [platform_files].dart
├── implementation_plans/
│   └── [FEATURE_NAME]/
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_01_SETUP_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_02_CORE_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_03_DOMAIN_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_04_DATA_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_05_PRESENTATION_[DATE].md
│       ├── [FEATURE_NAME]_IMPLEMENTATION_PLAN_06_INTEGRATION_[DATE].md
│       ├── IMPLEMENTATION_PROGRESS.md
│       └── IMPLEMENTATION_COMPLETION_REPORT.md
└── others/
    └── [any additional documentation]
```

---

## Best Practices

### Do:
✅ Execute all steps in order (0→1→2→2.5→3→4→5→CONFIRM→6)
✅ Verify and generate tech-specific commands FIRST (Step 0)
✅ Generate wireframes for UI/UX features (Step 2.5) and wait for user approval
✅ Store all outputs in specified directories
✅ Use consistent naming conventions
✅ Generate complete documentation at each step
✅ Wait for user confirmation at wireframe review (Step 2.5) and before implementation (Step 5)
✅ Track progress throughout execution
✅ Validate at each step
✅ Generate comprehensive reports
✅ Prefer tech-specific prompts over common ones

### Don't:
❌ Skip any step in the workflow (especially Step 0)
❌ Proceed to Step 1 without verifying commands
❌ Proceed to implementation without user approval
❌ Store files in wrong directories
❌ Use inconsistent naming
❌ Generate incomplete documentation
❌ Forget to create child plans
❌ Skip validation steps
❌ Use generic prompts when tech-specific ones should exist

---

## Troubleshooting

### Issue: User requirement is too vague
**Solution:** Ask ONE clarification question, then proceed with reasonable assumptions documented clearly

### Issue: Design style not specified
**Solution:** Use modern Material Design as default, document assumption in Step 1

### Issue: Platform not specified
**Solution:** Ask user to specify platform before proceeding to Step 4

### Issue: User wants to adjust plans after Step 5
**Solution:** Go back to relevant step, regenerate affected documentation, present updated summary

### Issue: Implementation encounters errors
**Solution:** Document in IMPLEMENTATION_PROGRESS.md, attempt fixes, escalate if critical

---

## Quick Reference

### File Naming Patterns
```
Research:       [FEATURE_NAME]_RESEARCH_PLAN_[DATE].md
UI/UX Design:   [FEATURE_NAME]_UI_UX_DESIGN_SYSTEM_[DATE].md
UI Code:        [FEATURE_NAME]_UI_IMPLEMENTATION_[PLATFORM]_[DATE].md
Main Plan:      [FEATURE_NAME]_IMPLEMENTATION_PLAN_[DATE].md
Child Plans:    [FEATURE_NAME]_IMPLEMENTATION_PLAN_0[1-6]_[PHASE]_[DATE].md
```

### Directory Paths
```
Research Plans:         ./docs/research_plans/
UI/UX Documentation:    ./docs/ui_ux/
UI Code Samples:        ./docs/ui_ux/code_samples/[PLATFORM]/
Implementation Plans:   ./docs/implementation_plans/[FEATURE_NAME]/
Other Documentation:    ./docs/others/
```

### Checkpoint
```
Step 0: Verify and generate tech-specific commands and project rules (execute automatically)
Steps 1-5: Execute automatically
After Step 5: STOP and ask user confirmation
Step 6: Execute ONLY if user approves
```

---

## FINAL REMINDER FOR AI

**MANDATORY PROMPT FILE REFERENCES (from Step 0):**
- Step 0: Verify and generate tech-specific files in:
  - `./.cursor/commands/specify/` (command files)
  - `./.cursor/rules/` (project rule)
- Step 2: `./.cursor/commands/specify/research_plan_[TECH]_[LANGUAGE].prompt.md` (or common fallback)
- Step 3: `./.cursor/commands/specify/ui_ux_design_generator_[TECH]_[LANGUAGE].prompt.md` (or common fallback)
- Step 4: `./.cursor/commands/specify/ui_ux_bridge_[TECH]_[LANGUAGE].prompt.md` (or common fallback)
- Step 5: `./.cursor/commands/specify/implementation_plan_[TECH]_[LANGUAGE].prompt.md` (or common fallback)
- Project Rule: `./.cursor/rules/project-rule_[TECH]_[LANGUAGE].mdc` (or common fallback: `./.cursor/rules/common/project_rule_common.mdc`)

---

## CRITICAL: Comprehensive Detail Requirements Across All Steps

**⚠️ ALL STEPS MUST PRODUCE DETAILED AND COMPREHENSIVE OUTPUTS - NO SIMPLIFICATIONS**

This workflow orchestrates multiple steps, each of which must produce comprehensive, detailed outputs:

### Step 2: Research & Analysis
- **MUST produce:** Complete requirements analysis, comprehensive technology inventory, detailed approach comparisons, complete technical specifications
- **Reference:** `research_plan_common.prompt.md` (or tech-specific version) - Follow ALL comprehensive detail requirements in that file
- **Output Quality:** Research plan should be so detailed that implementation can proceed without questions

### Step 3: UI/UX Design System
- **MUST produce:** Complete design system with all atomic, molecular, and organism components fully specified
- **Reference:** `ui_ux_design_generator.prompt.md` (or tech-specific version) - Follow ALL comprehensive detail requirements in that file
- **Output Quality:** Design system should have specific values (not placeholders) for all properties

### Step 4: Platform-Specific Code
- **MUST produce:** Complete, production-ready platform-specific code
- **Reference:** `ui_ux_bridge.prompt.md` (or tech-specific version) - Follow ALL comprehensive detail requirements in that file
- **Output Quality:** Code should be immediately usable without additional questions

### Step 5: Implementation Plan
- **MUST produce:** Complete implementation plan with all layers, components, and flows fully specified
- **Reference:** `implementation_plan_common.prompt.md` (or tech-specific version) - Follow ALL comprehensive detail requirements in that file
- **Output Quality:** Implementation plan should enable developers to implement without asking questions

**Cross-Step Consistency:**
- All steps must reference and build upon previous steps
- Additional features/sections/parts/UI identified in research must be considered in design and implementation
- All deliverables must be comprehensive and detailed
- No step should produce simplified or summarized outputs

**When you receive a feature request, you MUST:**

✅ **Step 0:** Verify tech-specific commands and project rule exist:
   - Commands in `./.cursor/commands/specify/` → Generate missing files from `./.cursor/commands/common/`
   - Project rule in `./.cursor/rules/` → Generate missing file from `./.cursor/rules/common/`
✅ **Step 0.5:** [IF UI design images detected] Process UI images:
   - Detect UI design images in user input
   - Break image into logical components/sections
   - Convert each component to HTML/CSS using @ui_ux_bridge workflow
   - Store converted components to `./docs/ui_ux/image_conversions/[FEATURE_NAME]_[DATE]/`
   - Use converted components as design reference in subsequent steps
✅ **Step 1:** Parse and document user requirements (include converted UI components if Step 0.5 executed)
✅ **Step 1.5:** Determine if feature requires UI/UX (analyze requirements carefully)
✅ **Step 2:** Execute complete research plan (following tech-specific research plan prompt) → Save to `./docs/research_plans/` (reference converted components if available)
✅ **Step 2.5:** [IF UI/UX required] Generate wireframes for all screens → Save to `./docs/ui_ux/wireframes/` → **PRESENT TO USER FOR REVIEW** → **WAIT FOR APPROVAL** before proceeding [ELSE] Skip wireframe step
✅ **Step 3:** [IF UI/UX required] Generate complete UI/UX design (following tech-specific UI/UX design generator prompt) → Save to `./docs/ui_ux/` (use approved wireframes and converted HTML/components as reference) [ELSE] Skip UI/UX design step
✅ **Step 4:** [IF UI/UX required] Create platform-specific UI code (following tech-specific UI/UX bridge prompt) → Save to `./docs/ui_ux/` (convert HTML from Step 0.5 to platform code) [ELSE] Skip UI/UX code step
✅ **Step 5:** Generate all implementation plans (following tech-specific implementation plan prompt - 1 main + 6 child) → Save to `./docs/implementation_plans/[FEATURE_NAME]/`
✅ **STOP:** Present completion summary and **WAIT FOR USER CONFIRMATION**
✅ **Step 6:** Execute implementation ONLY if user approves

**DO NOT:**
❌ Skip any step (0-5 must complete before asking user, except Step 0.5 if no images, Step 3 & 4 if UI/UX not required)
❌ Proceed to Step 1 without verifying/generating tech-specific commands and project rule
❌ Skip Step 0.5 if UI images are detected (must process images first)
❌ Skip breaking down UI images into components (must analyze comprehensively)
❌ Skip converting components to HTML using @ui_ux_bridge (each component must be converted)
❌ Skip Step 1.5 UI/UX determination (must analyze requirements carefully)
❌ Skip Step 2.5 wireframe generation if UI/UX required (must generate wireframes for user review)
❌ Skip presenting wireframes to user for review (MANDATORY checkpoint)
❌ Proceed to Step 3 without wireframe approval (must wait for user approval)
❌ Skip UI/UX steps if feature actually needs UI/UX (be conservative - if uncertain, include UI/UX)
❌ Include UI/UX steps for clearly backend-only features (waste of resources)
❌ Proceed to Step 6 without user saying "YES" or "PROCEED"
❌ Store files in wrong locations
❌ Generate incomplete documentation
❌ Skip child plan generation
❌ Use generic prompts/rules when tech-specific ones should be generated

**REMEMBER:**
- Step 0 is MANDATORY and must execute FIRST
- Step 0 must verify BOTH command files AND project rules
- Step 0.5 is CONDITIONAL (execute ONLY if UI design images detected in user input)
- Step 0.5 must break images into components and convert each to HTML using @ui_ux_bridge
- Step 1.5 is MANDATORY to determine UI/UX requirement (analyze carefully, be conservative)
- Step 2.5 is CONDITIONAL (execute ONLY if UI/UX required) and REQUIRES USER REVIEW/APPROVAL
- Steps 0-2 are AUTOMATIC (no user confirmation needed)
- Step 2.5 requires USER REVIEW/APPROVAL before proceeding (wireframe checkpoint)
- Steps 3 & 4 are CONDITIONAL (only execute if UI/UX required) and AUTOMATIC after wireframe approval
- Step 5 is AUTOMATIC (no user confirmation needed)
- USER CONFIRMATION is MANDATORY before Step 6
- All documentation must be complete and stored correctly
- Implementation execution only happens after user approval
- Always prefer tech-specific prompts and rules over common ones
- If uncertain about UI/UX requirement, default to including UI/UX steps (better safe than sorry)
- Converted HTML/components from Step 0.5 must be used as design reference in subsequent steps

**WORKFLOW = Verify Commands & Rules → [Process UI Images if present → Break into Components → Convert to HTML (@ui_ux_bridge)] → Parse → Determine UI/UX → Research → [Generate Wireframes → **USER REVIEW/APPROVE** → Design → Code] (if UI/UX) → Plan → **CONFIRM** → Implement**

---

## Example Execution

**User Input:**
```
"Build a shoe shop e-commerce app for Flutter with glass morphism design"
```

**AI Execution:**
1. ✅ **Step 0:** Verify commands and project rule for Flutter/Dart
   - Check `./.cursor/commands/specify/` → Generate missing files from `./.cursor/commands/common/`
     - Generate: `research_plan_flutter_dart.prompt.md`
     - Generate: `ui_ux_design_generator_flutter_dart.prompt.md`
     - Generate: `ui_ux_bridge_flutter_dart.prompt.md`
     - Generate: `implementation_plan_flutter_dart.prompt.md`
   - Check `./.cursor/rules/` → Generate missing file from `./.cursor/rules/common/`
     - Generate: `project-rule_flutter_dart.mdc`
2. ✅ **Step 1:** Parse requirements
3. ✅ **Step 1.5:** Determine UI/UX requirement
   - Analysis: "Shoe shopping e-commerce app" → User-facing feature with browsing, filtering, cart, checkout
   - Decision: **Requires UI/UX: YES** (High confidence)
4. ✅ **Step 2:** Generate research plan → `./docs/research_plans/SHOE_SHOP_RESEARCH_PLAN_2025-12-03.md`
5. ✅ **Step 2.5:** Generate wireframes → `./docs/ui_ux/wireframes/SHOE_SHOP_WIREFRAMES_2025-12-03.md` (UI/UX required)
6. ⏸️ **PRESENT WIREFRAMES FOR USER REVIEW**
7. ⏸️ **WAIT FOR USER APPROVAL** (user approves wireframes)
8. ✅ **Step 3:** Generate UI/UX design → `./docs/ui_ux/SHOE_SHOP_UI_UX_DESIGN_SYSTEM_2025-12-03.md` (UI/UX required, uses approved wireframes)
9. ✅ **Step 4:** Generate Flutter UI code → `./docs/ui_ux/SHOE_SHOP_UI_IMPLEMENTATION_FLUTTER_2025-12-03.md` (UI/UX required)
10. ✅ **Step 5:** Generate 7 implementation plans → `./docs/implementation_plans/SHOE_SHOP/`
11. ⏸️ **PRESENT SUMMARY AND ASK: "Do you want to proceed with implementation?"**
12. ⏸️ **WAIT FOR USER RESPONSE**
13. ✅ (If user confirms) Execute all 6 implementation plans in order

**Example: Backend-Only Feature**
```
User Input: "Create a REST API endpoint for user authentication with JWT tokens"

AI Execution:
1. ✅ Step 0: Verify commands
2. ✅ Step 1: Parse requirements
3. ✅ Step 1.5: Determine UI/UX requirement
   - Analysis: "REST API endpoint" → Backend-only, no user interface
   - Decision: **Requires UI/UX: NO** (High confidence)
4. ✅ Step 2: Generate research plan
5. ⏭️ Step 3: SKIP (UI/UX not required)
6. ⏭️ Step 4: SKIP (UI/UX not required)
7. ✅ Step 5: Generate implementation plans
8. ⏸️ Present summary
```

---

```
Break down the next task into smaller pieces and update the file in small chucks. Continue with each section until complete.
```

**End of Workflow Instructions**
