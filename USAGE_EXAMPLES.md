# Quick Usage Examples

## Basic Usage

### Generate a Research Plan for Flutter
```bash
python3 generate_prompt.py research_plan flutter \
  --requirements "User authentication feature with email/password login" \
  --feature "auth"
```

### Generate an Implementation Plan for Kotlin/Android
```bash
python3 generate_prompt.py implementation_plan kotlin \
  --requirements "Shopping cart feature with offline support and sync" \
  --feature "shopping_cart"
```

### Generate UI/UX Design System for React
```bash
python3 generate_prompt.py ui_ux_design react \
  --requirements "E-commerce product listing page with glass morphism style"
```

### Generate UI/UX Bridge for Swift/iOS
```bash
python3 generate_prompt.py ui_ux_bridge swift \
  --requirements "Product detail screen with image gallery and add to cart"
```

### Generate All Prompt Types at Once
```bash
python3 generate_prompt.py all typescript \
  --requirements "Dashboard component with real-time data updates" \
  --feature "dashboard"
```

## Output Location

All generated files are saved to:
```
.cursor/commands/specify/
```

## File Naming Convention

Files are named as:
```
{prompt_type}_{language}[_{feature}].prompt.md
```

Examples:
- `research_plan_flutter_auth.prompt.md`
- `implementation_plan_kotlin_shopping_cart.prompt.md`
- `ui_ux_design_react.prompt.md`
- `ui_ux_bridge_swift.prompt.md`

## What Gets Customized

The tool automatically replaces:
- Code language tags (`[language]` → `flutter`, `kotlin`, etc.)
- Package manager commands
- Build commands
- Linter commands
- State management libraries
- Dependency injection frameworks
- Code generation tools
- File extensions
- And more language-specific details

## Supported Languages

- `flutter` / `dart` - Flutter/Dart
- `kotlin` / `android` - Android (Kotlin/Jetpack Compose)
- `swift` / `ios` - iOS (Swift/SwiftUI)
- `typescript` / `react` - React/TypeScript
- `python` - Python
- `java` - Java
- `csharp` - C# (.NET)
- `go` - Go
- `rust` - Rust

## Help

For full documentation:
```bash
python3 generate_prompt.py --help
```

Or see `README_PROMPT_GENERATOR.md` for detailed documentation.

