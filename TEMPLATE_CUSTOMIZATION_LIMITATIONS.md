# Template Customization Limitations & Current Status

## The Problem You Identified

You're absolutely right to question this! The current system has a **significant limitation**:

### What the Tool Currently Does ✅

The tool only replaces **simple placeholders** with basic language properties:

- `[language]` → "react" or "flutter"
- `[extension]` → ".tsx" or ".dart"
- `[package-manager]` → "npm" or "pub"
- `[build_command]` → "npm run build" or "flutter pub run build_runner build"
- `[linter]` → "eslint" or "flutter analyze"
- `[di-library]` → "inversify" or "injectable"
- `[state-management-library]` → "Redux" or "Bloc"
- etc. (about 15 basic properties)

### What the Tool Does NOT Do ❌

The templates contain **hardcoded language-specific content** that is NOT being replaced:

1. **Entire code examples** (e.g., Flutter widget code in `ui_ux_bridge.prompt.md` lines 508-750)
2. **Language-specific sections** (e.g., "Step 3.2: Flutter Conversion" should become "Step 3.2: React Conversion")
3. **File structure examples** (e.g., `lib/` structure for Flutter vs `src/` for React)
4. **Command examples** with language-specific syntax
5. **Package manager examples** (e.g., "pub dependencies" should become "npm dependencies")
6. **Code patterns** (e.g., `Future<Either<Failure, T>>` for Flutter vs `Promise<Result<T, E>>` for React)

## Example of the Problem

In `ui_ux_bridge.prompt.md`, there's a hardcoded section:

```markdown
### Step 3.2: Flutter Conversion (Dart)

```dart
import 'package:flutter/material.dart';
class ComponentNameWidget extends StatefulWidget {
  // ... 200+ lines of Flutter code
}
```

When you generate for React, this entire Flutter section is still there! It should be replaced with React/TypeScript code.

## Current Language Knowledge

The tool only knows **15 basic properties** per language from the `LANGUAGE_MAPPINGS` dictionary:

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

This is **not enough** to generate proper language-specific:
- Code examples
- File structures
- Architecture patterns
- Best practices
- Complete implementation examples

## Proposed Solutions

### Option 1: Conditional Template Sections (Recommended)

Use template markers to include/exclude language-specific sections:

```markdown
<!-- BEGIN:FLUTTER -->
### Step 3.2: Flutter Conversion (Dart)
```dart
// Flutter code here
```
<!-- END:FLUTTER -->

<!-- BEGIN:REACT -->
### Step 3.2: React Conversion (TypeScript)
```typescript
// React code here
```
<!-- END:REACT -->
```

The tool would:
1. Parse these markers
2. Include only sections matching the target language
3. Remove sections for other languages

### Option 2: Language-Specific Template Variants

Create separate template files per language:
- `ui_ux_bridge_flutter.prompt.md`
- `ui_ux_bridge_react.prompt.md`
- `ui_ux_bridge_kotlin.prompt.md`
- etc.

Then select the appropriate template based on language.

### Option 3: Template Engine with Code Generation

Use a proper template engine (like Jinja2) with:
- Conditional blocks
- Loops
- Language-specific code generators
- More sophisticated replacements

### Option 4: Hybrid Approach

1. Keep common templates with placeholders for simple replacements
2. Add language-specific "snippet libraries" for code examples
3. Use conditional markers for major sections
4. Generate code examples dynamically based on language config

## Recommendation

**Option 1 (Conditional Sections)** is the best balance of:
- ✅ Maintainability (one template file)
- ✅ Flexibility (easy to add new languages)
- ✅ Clarity (clear what gets included)
- ✅ Implementation simplicity

## Next Steps

Would you like me to:
1. Implement conditional section markers in the templates?
2. Update the tool to parse and filter these sections?
3. Add more language-specific code examples?
4. Create a more comprehensive language knowledge base?

