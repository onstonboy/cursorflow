## CursorFlow Prompt Generator

Generate language- and framework-specific Cursor command prompts from a single set of shared templates.

This repository provides a small Python CLI (and interactive wizard) that reads common prompt templates from `.cursor/commands/common/` and generates customized versions for your target stack in `.cursor/commands/specify/`. It is designed to keep your Cursor workflows consistent across projects and languages.

---

## Features

- **Language-aware prompt generation**: Applies language-specific details (file extensions, package managers, build commands, linters, state management, DI, async style, result types, JSON serialization, and more).
- **Shared templates, specialized outputs**: Start from one canonical template and generate prompts tailored to Flutter, Kotlin, Swift, React/TypeScript, Python, Java, C#, Go, or Rust.
- **Interactive project wizard**: Run the tool with no arguments to get a friendly Q&A flow that infers a good tech stack and generates a full set of prompts and rules.
- **Batch generation**: Create research plans, implementation plans, UI/UX design systems, UI/UX bridges, project rules, and test rules in one shot.
- **Cursor-native structure**: Writes outputs into `.cursor/commands/specify/` (or a custom folder), ready to be used as commands inside Cursor.
- **Zero external dependencies**: Uses only the Python standard library.

---

## Requirements

- **Python**: 3.7 or higher  
- **OS**: Any platform where Python 3.7+ is available (tested on macOS)
- **Dependencies**: No third‑party packages required (standard library only)

If you are using Cursor, simply clone this repo into a workspace; no additional setup is needed.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/CursorFlow.git
cd CursorFlow
```

Make sure you can run the script:

```bash
python3 generate_prompt.py --help
```

If you prefer, you can also mark it as executable:

```bash
chmod +x generate_prompt.py
./generate_prompt.py --help
```

---

## Quick Start

### Option 1: Interactive Project Wizard (Recommended)

Run the script with **no arguments**:

```bash
python3 generate_prompt.py
```

You will be guided through:

1. **Project idea** – high-level description of what you want to build.  
2. **Target users** – who the product is for.  
3. **Platforms** – mobile, web, backend, etc.  
4. **Constraints / preferences** – offline-first, budget, performance, etc.  
5. **Tech stack** – suggested automatically (you can override).  
6. **Project name** – used to name the generated files.  
7. **Output folder** – default is `~/Desktop/CursorFlow` (you can change it).

At the end, the wizard generates:

- Research plan  
- Implementation plan  
- UI/UX design system  
- UI/UX bridge  
- Project rules  
- Test rules  

All as Markdown files that you can open and run as commands in Cursor.

---

### Option 2: Direct CLI Usage

Basic syntax:

```bash
python3 generate_prompt.py <prompt_type> <language> [options]
```

**Prompt types:**

- `research_plan` – feature research and analysis guide  
- `implementation_plan` – detailed implementation planning guide  
- `ui_ux_design` – design system & layout planning guide  
- `ui_ux_bridge` – design-to-code conversion & implementation guide  
- `all` – generate all of the above at once  

**Supported languages / frameworks:**

- `dart`, `flutter`
- `kotlin`, `android`
- `swift`, `ios`
- `typescript`, `react`
- `python`
- `java`
- `csharp`
- `go`
- `rust`

The tool also understands common aliases like `reactjs`, `react.js`, `ts`, `tsx`, `javascript`, `node`, etc., and normalizes them to the closest supported language.

#### Common examples

- **Generate a research plan for Flutter:**

```bash
python3 generate_prompt.py research_plan flutter \
  --requirements "User authentication feature with email/password login" \
  --feature "auth"
```

- **Generate an implementation plan for Kotlin/Android:**

```bash
python3 generate_prompt.py implementation_plan kotlin \
  --requirements "Shopping cart feature with offline support and sync" \
  --feature "shopping_cart"
```

- **Generate a UI/UX design system for React/TypeScript:**

```bash
python3 generate_prompt.py ui_ux_design react \
  --requirements "E-commerce product listing page with glass morphism style"
```

- **Generate a UI/UX bridge for Swift/iOS:**

```bash
python3 generate_prompt.py ui_ux_bridge swift \
  --requirements "Product detail screen with image gallery and add to cart"
```

- **Generate all prompt types at once for TypeScript:**

```bash
python3 generate_prompt.py all typescript \
  --requirements "Dashboard component with real-time data updates" \
  --feature "dashboard"
```

By default, generated files go to:

```text
.cursor/commands/specify/
```

You can override the output location with `--output`:

```bash
python3 generate_prompt.py research_plan swift \
  --requirements "Offline-first todo list" \
  --feature "todo_app" \
  --output ./custom/path/
```

For more usage patterns, see `USAGE_EXAMPLES.md`.

---

## Folder Structure

The most relevant parts of this repo:

- `.cursor/commands/common/` – canonical shared templates used as sources.  
- `.cursor/commands/specify/` – generated language- and feature-specific prompts (output).  
- `.cursor/rules/common/` – shared project rules used by Cursor.  
- `generate_prompt.py` – main Python CLI and interactive wizard.  
- `README_PROMPT_GENERATOR.md` – in‑depth documentation of the generator.  
- `HOW_IT_WORKS.md` – explanation of the internals and language mappings.  
- `USAGE_EXAMPLES.md` – additional concrete examples of CLI usage.  
- `TEMPLATE_CUSTOMIZATION_LIMITATIONS.md` – current limitations and future improvements for template customization.

You can safely add your own templates to `.cursor/commands/common/` and have them generated into `.cursor/commands/specify/`.

---

## Customization & Extensibility

- **Add a new language/framework**  
  Edit `LANGUAGE_MAPPINGS` in `generate_prompt.py` and add an entry with:
  - file extension  
  - package manager + build command  
  - linter  
  - DI library  
  - state management tools  
  - async pattern, result type, immutability, JSON serialization  

- **Add a new prompt type**  
  Edit `PROMPT_TYPES` in `generate_prompt.py` and point it at a new template in `.cursor/commands/common/`.

- **Use conditional template sections**  
  Templates can contain language‑specific blocks:

  ```markdown
  <!-- BEGIN:FLUTTER -->
  ... Flutter-specific content ...
  <!-- END:FLUTTER -->

  <!-- BEGIN:REACT -->
  ... React-specific content ...
  <!-- END:REACT -->
  ```

  The generator will keep only the sections matching the target language/framework and strip the rest.

For more detail on current limitations and future ideas, see `TEMPLATE_CUSTOMIZATION_LIMITATIONS.md` and `HOW_IT_WORKS.md`.

---

## Using with Cursor

- Point Cursor at this repository as a workspace.  
- Use the CLI or interactive wizard to generate prompts into `.cursor/commands/specify/` (or another folder).  
- Open those `.prompt.md` files in Cursor and run them as commands to guide research, implementation, testing, and UI/UX work.

This makes it easy to keep a consistent, language-aware workflow across multiple projects in Cursor.

---

## Contributing

- **Bug reports / ideas**: Open an issue describing the problem, desired behavior, and your environment.  
- **Improvements**: Pull requests to extend `LANGUAGE_MAPPINGS`, `PROMPT_TYPES`, or the templates in `.cursor/commands/common/` are very welcome.  
- **Docs**: Clarifications and additional examples for the Markdown documentation files in this repo are appreciated.

Before submitting a PR, please:

- Keep the tool dependency‑free (standard library only).  
- Follow the existing coding style in `generate_prompt.py`.  
- Add or update examples if your change affects usage.

---

## License

No explicit license has been defined yet.  
Before publishing this repository publicly, you should add a `LICENSE` file (for example, MIT, Apache‑2.0, or another license that matches your intended usage).

