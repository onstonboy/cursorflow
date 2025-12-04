# Prompt Generator Tool

A Python command-line tool that generates customized prompt files from common templates, tailored to specific programming languages and frameworks.

## Overview

This tool reads common prompt templates from `.cursor/commands/common/` and generates language/framework-specific versions in `.cursor/commands/specify/`. It automatically customizes:

- Code examples and syntax
- Package manager commands
- Build tools and linters
- State management libraries
- Dependency injection frameworks
- Code generation tools
- And more language-specific details

## Installation

No external dependencies required! This tool uses only Python standard library.

**Requirements:**
- Python 3.7 or higher

## Usage

### Basic Syntax

```bash
python generate_prompt.py <prompt_type> <language> [options]
```

### Prompt Types

- `research_plan` - Feature research and analysis guide
- `implementation_plan` - Implementation planning guide
- `ui_ux_design` - UI/UX design system generator
- `ui_ux_bridge` - UI/UX design-to-code conversion system
- `all` - Generate all prompt types at once

### Supported Languages/Frameworks

- `dart` / `flutter` - Flutter/Dart development
- `kotlin` / `android` - Android (Kotlin/Jetpack Compose)
- `swift` / `ios` - iOS (Swift/SwiftUI)
- `typescript` / `react` - React/TypeScript
- `python` - Python
- `java` - Java
- `csharp` - C# (.NET)
- `go` - Go
- `rust` - Rust

### Examples

#### Generate Research Plan for Flutter

```bash
python generate_prompt.py research_plan flutter \
  --requirements "User authentication feature with email/password login" \
  --feature "auth"
```

**Output:** `.cursor/commands/specify/research_plan_flutter_auth.prompt.md`

#### Generate Implementation Plan for Kotlin

```bash
python generate_prompt.py implementation_plan kotlin \
  --requirements "Shopping cart feature with offline support" \
  --feature "shopping_cart"
```

**Output:** `.cursor/commands/specify/implementation_plan_kotlin_shopping_cart.prompt.md`

#### Generate UI/UX Design System for React

```bash
python generate_prompt.py ui_ux_design react \
  --requirements "E-commerce product listing page with glass morphism style"
```

**Output:** `.cursor/commands/specify/ui_ux_design_react.prompt.md`

#### Generate All Prompts for TypeScript

```bash
python generate_prompt.py all typescript \
  --requirements "Dashboard component with real-time data updates" \
  --feature "dashboard"
```

**Output:** Four files in `.cursor/commands/specify/`:
- `research_plan_typescript_dashboard.prompt.md`
- `implementation_plan_typescript_dashboard.prompt.md`
- `ui_ux_design_typescript_dashboard.prompt.md`
- `ui_ux_bridge_typescript_dashboard.prompt.md`

#### Generate with Custom Output Path

```bash
python generate_prompt.py research_plan swift \
  --requirements "Offline-first todo list" \
  --output ./custom/path/
```

## Command-Line Options

```
positional arguments:
  prompt_type           Type of prompt to generate
                        (research_plan, implementation_plan, ui_ux_design, 
                         ui_ux_bridge, all)
  language              Target language/framework

optional arguments:
  -h, --help            Show help message
  -r, --requirements    User requirements/description for the feature
  -f, --feature         Feature name (used in filename)
  -o, --output          Output file path 
                        (default: .cursor/commands/specify/)
  --base-dir            Base directory (default: script directory)
```

## How It Works

1. **Reads Common Template**: Loads the appropriate template from `.cursor/commands/common/`
2. **Language Configuration**: Applies language-specific mappings (syntax, tools, libraries)
3. **Customization**: Replaces placeholders with language-specific values:
   - `[language]` → Language name
   - `[extension]` → File extension
   - `[package-manager]` → Package manager name
   - `[build_command]` → Build command
   - `[linter]` → Linter command
   - Code block language tags
   - And many more...
4. **Requirements Injection**: Adds user requirements section at the top
5. **Metadata Addition**: Appends generation metadata at the bottom
6. **File Generation**: Saves customized prompt to `.cursor/commands/specify/`

## Language-Specific Customizations

Each language configuration includes:

- **File Extensions**: `.dart`, `.kt`, `.swift`, `.ts`, etc.
- **Package Managers**: `pub`, `npm`, `gradle`, `cargo`, etc.
- **Build Commands**: Language-specific build commands
- **Linters**: `dart analyze`, `ktlint`, `eslint`, etc.
- **State Management**: Bloc, Redux, StateFlow, etc.
- **Dependency Injection**: Injectable, Koin, Swinject, etc.
- **Code Generation**: build_runner, kapt, tsc, etc.
- **Async Patterns**: Future, Promise, async/await, etc.
- **Result Types**: Either, Result, etc.
- **Immutability**: @freezed, data class, struct, etc.
- **JSON Serialization**: JsonSerializable, Codable, serde, etc.

## Output Structure

Generated files are saved to `.cursor/commands/specify/` with naming convention:

```
{prompt_type}_{language}[_{feature}].prompt.md
```

Examples:
- `research_plan_flutter.prompt.md`
- `implementation_plan_kotlin_shopping_cart.prompt.md`
- `ui_ux_design_react.prompt.md`

## File Format

Each generated file includes:

1. **Original Frontmatter**: Preserved from template
2. **Generated Requirements Section**: User requirements (if provided)
3. **Customized Content**: Template with language-specific replacements
4. **Generation Metadata**: Language config and generation timestamp

## Extending the Tool

### Adding a New Language

Edit `generate_prompt.py` and add to `LANGUAGE_MAPPINGS`:

```python
'newlang': {
    'name': 'New Language',
    'extension': '.new',
    'package_manager': 'newpm',
    'package_file': 'newfile.ext',
    'build_command': 'new build',
    'linter': 'newlint',
    'code_gen': 'newgen',
    'di_library': 'newdi',
    'state_management': ['State1', 'State2'],
    'async_pattern': 'async',
    'result_type': 'Result<T, E>',
    'immutability': 'immutable',
    'json_serialization': 'jsonlib',
},
```

### Adding a New Prompt Type

Edit `generate_prompt.py` and add to `PROMPT_TYPES`:

```python
'new_prompt': {
    'template': 'new_prompt_common.prompt.md',
    'output_prefix': 'new_prompt',
},
```

## Troubleshooting

### Template Not Found

Ensure the common template file exists in `.cursor/commands/common/`

### Unsupported Language

Check that your language is in the `LANGUAGE_MAPPINGS` dictionary. Use the exact key name (lowercase).

### Output Directory Issues

The tool automatically creates `.cursor/commands/specify/` if it doesn't exist. Ensure you have write permissions.

## Examples in Practice

### Workflow: Flutter Feature Development

```bash
# 1. Generate research plan
python generate_prompt.py research_plan flutter \
  --requirements "User profile editing with photo upload" \
  --feature "profile_edit"

# 2. After research, generate implementation plan
python generate_prompt.py implementation_plan flutter \
  --requirements "Based on research plan, implement profile editing" \
  --feature "profile_edit"

# 3. Generate UI/UX design if needed
python generate_prompt.py ui_ux_design flutter \
  --requirements "Profile editing screen with material design"
```

### Workflow: Multi-Platform Feature

```bash
# Generate for all platforms
python generate_prompt.py all flutter --feature "auth"
python generate_prompt.py all kotlin --feature "auth"
python generate_prompt.py all swift --feature "auth"
```

## Contributing

To improve language support or add new features:

1. Update `LANGUAGE_MAPPINGS` for better language support
2. Update `PROMPT_TYPES` for new prompt types
3. Enhance `customize_content()` for more sophisticated replacements
4. Add validation and error handling as needed

## License

This tool is part of the CursorFlow project.

