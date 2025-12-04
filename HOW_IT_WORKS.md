# How the Prompt Generator Works

## Your Question

> "How do you know exactly many information about other language, tech to generate specific commands?"

## The Honest Answer

The tool has **two levels of knowledge**:

### Level 1: Basic Language Properties ✅ (Currently Implemented)

The tool has a **dictionary** (`LANGUAGE_MAPPINGS`) with ~15 basic properties per language:

```python
'react': {
    'name': 'React (TypeScript)',
    'extension': '.tsx',
    'package_manager': 'npm',
    'package_file': 'package.json',
    'build_command': 'npm run build',
    'linter': 'eslint',
    'code_gen': 'tsc',
    'di_library': 'inversify',
    'state_management': ['Redux', 'MobX', 'Zustand', 'Context API'],
    'async_pattern': 'Promise',
    'result_type': 'Result<T, E>',
    'immutability': 'readonly',
    'json_serialization': 'class-transformer',
}
```

**What this replaces:**
- Simple placeholders like `[language]`, `[extension]`, `[package-manager]`
- Basic terminology like `[build_command]`, `[linter]`

**What this does NOT replace:**
- Entire code examples
- Language-specific sections
- Detailed implementation patterns

### Level 2: Conditional Template Sections ✅ (Just Implemented)

I just added support for **conditional sections** in templates. Templates can now have:

```markdown
<!-- BEGIN:FLUTTER -->
### Step 3.2: Flutter Conversion (Dart)
```dart
// Flutter-specific code here
```
<!-- END:FLUTTER -->

<!-- BEGIN:REACT -->
### Step 3.2: React Conversion (TypeScript)
```typescript
// React-specific code here
```
<!-- END:REACT -->
```

**What this does:**
- When generating for React, only the `<!-- BEGIN:REACT -->` section is included
- When generating for Flutter, only the `<!-- BEGIN:FLUTTER -->` section is included
- Other language sections are automatically removed

### Level 3: Terminology Replacement ✅ (Just Implemented)

Added automatic replacement of common terminology:

- `pub dependencies` → `npm dependencies` (for React)
- `pubspec.yaml` → `package.json` (for React)
- `Future<Either<` → `Promise<Result<` (for React)
- `StatefulWidget` → `React.Component` (for React)

## Current Status

### ✅ What Works Now

1. **Basic placeholder replacement** - Simple properties are replaced
2. **Conditional sections** - Language-specific sections are included/excluded
3. **Terminology replacement** - Common terms are automatically converted
4. **Language normalization** - "reactjs", "react.js" → "react"

### ⚠️ What Still Needs Work

The **templates themselves** need to be updated to use conditional sections. Currently:

- `ui_ux_bridge.prompt.md` has hardcoded Flutter code examples (lines 508-750)
- Other templates may have language-specific examples that should be conditional

## Next Steps to Fully Fix This

### Step 1: Update Templates with Conditional Sections

Edit the common templates to wrap language-specific content:

**Before:**
```markdown
### Step 3.2: Flutter Conversion (Dart)
```dart
// 200 lines of Flutter code
```
```

**After:**
```markdown
<!-- BEGIN:FLUTTER -->
### Step 3.2: Flutter Conversion (Dart)
```dart
// 200 lines of Flutter code
```
<!-- END:FLUTTER -->

<!-- BEGIN:REACT -->
### Step 3.2: React Conversion (TypeScript)
```typescript
// 200 lines of React code
```
<!-- END:REACT -->

<!-- BEGIN:KOTLIN -->
### Step 3.2: Kotlin Conversion (Jetpack Compose)
```kotlin
// 200 lines of Kotlin code
```
<!-- END:KOTLIN -->
```

### Step 2: Add More Language-Specific Examples

For each language, add:
- Code examples
- File structure examples
- Command examples
- Best practices

### Step 3: Expand Language Knowledge Base

Add more properties to `LANGUAGE_MAPPINGS`:
- Common file structures
- Testing frameworks
- Architecture patterns
- Code style guides

## The Reality

**The tool doesn't "know" everything** - it relies on:

1. **The language mapping dictionary** (basic properties)
2. **Conditional sections in templates** (language-specific content)
3. **Terminology replacement rules** (common conversions)

To generate truly accurate, language-specific prompts, the templates need to be updated with conditional sections for each supported language.

## Would You Like Me To?

1. **Update the templates** to use conditional sections?
2. **Add React/Kotlin/Swift code examples** to replace the Flutter ones?
3. **Expand the language knowledge base** with more properties?
4. **Create a template editor** to make it easier to add language-specific content?

Let me know which approach you'd prefer!

