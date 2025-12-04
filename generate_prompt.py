#!/usr/bin/env python3
"""
Prompt Generator Tool
Generates specific prompt files from common templates based on language/framework requirements.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class PromptGenerator:
    """Generates customized prompts from common templates."""
    
    # Language/Framework specific mappings
    LANGUAGE_MAPPINGS = {
        'dart': {
            'name': 'Dart',
            'extension': '.dart',
            'package_manager': 'pub',
            'package_file': 'pubspec.yaml',
            'build_command': 'flutter pub run build_runner build',
            'linter': 'dart analyze',
            'code_gen': 'build_runner',
            'di_library': 'injectable',
            'state_management': ['Bloc', 'Cubit', 'Riverpod', 'Provider'],
            'async_pattern': 'Future',
            'result_type': 'Either<Failure, T>',
            'immutability': '@freezed',
            'json_serialization': '@JsonSerializable',
        },
        'flutter': {
            'name': 'Flutter',
            'extension': '.dart',
            'package_manager': 'pub',
            'package_file': 'pubspec.yaml',
            'build_command': 'flutter pub run build_runner build --delete-conflicting-outputs',
            'linter': 'flutter analyze',
            'code_gen': 'build_runner',
            'di_library': 'injectable',
            'state_management': ['Bloc', 'Cubit', 'Riverpod', 'Provider'],
            'async_pattern': 'Future',
            'result_type': 'Either<Failure, T>',
            'immutability': '@freezed',
            'json_serialization': '@JsonSerializable',
        },
        'kotlin': {
            'name': 'Kotlin',
            'extension': '.kt',
            'package_manager': 'gradle',
            'package_file': 'build.gradle.kts',
            'build_command': './gradlew build',
            'linter': 'ktlint',
            'code_gen': 'kapt',
            'di_library': 'Koin',
            'state_management': ['StateFlow', 'Flow', 'LiveData'],
            'async_pattern': 'suspend fun',
            'result_type': 'Result<T, E>',
            'immutability': 'data class',
            'json_serialization': 'kotlinx.serialization',
        },
        'android': {
            'name': 'Android (Kotlin)',
            'extension': '.kt',
            'package_manager': 'gradle',
            'package_file': 'build.gradle.kts',
            'build_command': './gradlew build',
            'linter': 'ktlint',
            'code_gen': 'kapt',
            'di_library': 'Koin',
            'state_management': ['StateFlow', 'Flow', 'LiveData', 'Compose State'],
            'async_pattern': 'suspend fun',
            'result_type': 'Result<T, E>',
            'immutability': 'data class',
            'json_serialization': 'kotlinx.serialization',
        },
        'swift': {
            'name': 'Swift',
            'extension': '.swift',
            'package_manager': 'spm',
            'package_file': 'Package.swift',
            'build_command': 'swift build',
            'linter': 'swiftlint',
            'code_gen': 'Sourcery',
            'di_library': 'Swinject',
            'state_management': ['@State', '@Binding', 'Combine'],
            'async_pattern': 'async/await',
            'result_type': 'Result<T, Error>',
            'immutability': 'struct',
            'json_serialization': 'Codable',
        },
        'ios': {
            'name': 'iOS (Swift)',
            'extension': '.swift',
            'package_manager': 'spm',
            'package_file': 'Package.swift',
            'build_command': 'swift build',
            'linter': 'swiftlint',
            'code_gen': 'Sourcery',
            'di_library': 'Swinject',
            'state_management': ['@State', '@Binding', 'Combine'],
            'async_pattern': 'async/await',
            'result_type': 'Result<T, Error>',
            'immutability': 'struct',
            'json_serialization': 'Codable',
        },
        'typescript': {
            'name': 'TypeScript',
            'extension': '.ts',
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
        },
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
        },
        'python': {
            'name': 'Python',
            'extension': '.py',
            'package_manager': 'pip',
            'package_file': 'requirements.txt',
            'build_command': 'python setup.py build',
            'linter': 'pylint',
            'code_gen': 'dataclasses',
            'di_library': 'dependency-injector',
            'state_management': ['State Machine', 'Event-driven'],
            'async_pattern': 'async/await',
            'result_type': 'Result[T, E]',
            'immutability': '@dataclass(frozen=True)',
            'json_serialization': 'dataclasses_json',
        },
        'java': {
            'name': 'Java',
            'extension': '.java',
            'package_manager': 'maven',
            'package_file': 'pom.xml',
            'build_command': 'mvn clean install',
            'linter': 'checkstyle',
            'code_gen': 'lombok',
            'di_library': 'Dagger',
            'state_management': ['State Pattern', 'Observer'],
            'async_pattern': 'CompletableFuture',
            'result_type': 'Either<L, R>',
            'immutability': 'final fields',
            'json_serialization': 'Jackson',
        },
        'csharp': {
            'name': 'C#',
            'extension': '.cs',
            'package_manager': 'nuget',
            'package_file': '.csproj',
            'build_command': 'dotnet build',
            'linter': 'StyleCop',
            'code_gen': 'Source Generators',
            'di_library': 'Microsoft.Extensions.DependencyInjection',
            'state_management': ['State Pattern', 'MediatR'],
            'async_pattern': 'async/await',
            'result_type': 'Result<T, E>',
            'immutability': 'readonly',
            'json_serialization': 'System.Text.Json',
        },
        'go': {
            'name': 'Go',
            'extension': '.go',
            'package_manager': 'go mod',
            'package_file': 'go.mod',
            'build_command': 'go build',
            'linter': 'golangci-lint',
            'code_gen': 'go generate',
            'di_library': 'wire',
            'state_management': ['State Pattern'],
            'async_pattern': 'goroutines',
            'result_type': '(T, error)',
            'immutability': 'const',
            'json_serialization': 'encoding/json',
        },
        'rust': {
            'name': 'Rust',
            'extension': '.rs',
            'package_manager': 'cargo',
            'package_file': 'Cargo.toml',
            'build_command': 'cargo build',
            'linter': 'clippy',
            'code_gen': 'proc_macro',
            'di_library': 'shaku',
            'state_management': ['State Pattern'],
            'async_pattern': 'async/await',
            'result_type': 'Result<T, E>',
            'immutability': 'immutable by default',
            'json_serialization': 'serde',
        },
    }
    
    PROMPT_TYPES = {
        'research_plan': {
            'template': 'research_plan_common.prompt.md',
            'output_prefix': 'research_plan',
        },
        'implementation_plan': {
            'template': 'implementation_plan_common.prompt.md',
            'output_prefix': 'implementation_plan',
        },
        'ui_ux_design': {
            'template': 'ui_ux_design_generator.prompt.md',
            'output_prefix': 'ui_ux_design',
        },
        'ui_ux_bridge': {
            'template': 'ui_ux_bridge.prompt.md',
            'output_prefix': 'ui_ux_bridge',
        },
        'project_rules': {
            'template': 'project_rules_common.prompt.md',
            'output_prefix': 'project_rules',
        },
        'test_rules': {
            'template': 'test_rules_common.prompt.md',
            'output_prefix': 'test_rules',
        },
    }
    
    def __init__(self, base_dir: Optional[Path] = None):
        """Initialize the generator with base directory."""
        if base_dir is None:
            base_dir = Path(__file__).parent
        self.base_dir = Path(base_dir)
        self.common_dir = self.base_dir / '.cursor' / 'commands' / 'common'
        self.specify_dir = self.base_dir / '.cursor' / 'commands' / 'specify'
        self.specify_dir.mkdir(parents=True, exist_ok=True)
    
    def normalize_language(self, language: str) -> str:
        """Normalize language input to canonical key."""
        lang_lower = language.lower().strip()
        
        # Language aliases mapping common variations to canonical keys
        aliases = {
            # React variations
            'reactjs': 'react',
            'react.js': 'react',
            'reactjs': 'react',
            'react-js': 'react',
            'reactjsx': 'react',
            'react tsx': 'react',
            'react typescript': 'react',
            # TypeScript variations
            'ts': 'typescript',
            'tsx': 'react',  # TSX usually means React with TypeScript
            'typescript react': 'react',
            # Flutter variations
            'dart flutter': 'flutter',
            'flutter dart': 'flutter',
            # Android variations
            'android kotlin': 'kotlin',
            'kotlin android': 'kotlin',
            'android studio': 'kotlin',
            # iOS variations
            'ios swift': 'swift',
            'swift ios': 'swift',
            'swiftui': 'swift',
            'swift ui': 'swift',
            # Other common variations
            'js': 'typescript',  # Default JS to TypeScript
            'javascript': 'typescript',
            'node': 'typescript',
            'nodejs': 'typescript',
            'node.js': 'typescript',
        }
        
        # Check aliases first
        if lang_lower in aliases:
            return aliases[lang_lower]
        
        # Remove common suffixes/prefixes
        lang_clean = re.sub(r'[\.\-\s]+', '', lang_lower)
        if lang_clean in aliases:
            return aliases[lang_clean]
        
        # If it's already a canonical key, return it
        if lang_lower in self.LANGUAGE_MAPPINGS:
            return lang_lower
        
        # Try partial matches
        for key in self.LANGUAGE_MAPPINGS.keys():
            if lang_lower in key or key in lang_lower:
                return key
        
        # If still not found, return as-is (will raise error in get_language_config)
        return lang_lower
    
    def get_language_config(self, language: str) -> Dict:
        """Get language-specific configuration."""
        normalized = self.normalize_language(language)
        if normalized not in self.LANGUAGE_MAPPINGS:
            raise ValueError(
                f"Unsupported language: {language}. "
                f"Supported: {', '.join(sorted(self.LANGUAGE_MAPPINGS.keys()))}\n"
                f"Common variations like 'reactjs', 'react.js' are automatically mapped to 'react'."
            )
        return self.LANGUAGE_MAPPINGS[normalized]
    
    def get_prompt_config(self, prompt_type: str) -> Dict:
        """Get prompt type configuration."""
        if prompt_type not in self.PROMPT_TYPES:
            raise ValueError(
                f"Unsupported prompt type: {prompt_type}. "
                f"Supported: {', '.join(self.PROMPT_TYPES.keys())}"
            )
        return self.PROMPT_TYPES[prompt_type]
    
    def read_template(self, template_name: str) -> str:
        """Read the common template file."""
        template_path = self.common_dir / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        return template_path.read_text(encoding='utf-8')
    
    def customize_content(self, content: str, lang_config: Dict, 
                         requirements: Optional[str] = None,
                         language_key: Optional[str] = None) -> str:
        """Customize template content with language-specific replacements."""
        
        # Get normalized language key for conditional sections
        if language_key is None:
            language_key = self.normalize_language(lang_config['name'].lower())
        
        # Step 1: Handle conditional sections (<!-- BEGIN:LANG --> ... <!-- END:LANG -->)
        content = self._process_conditional_sections(content, language_key)
        
        # Step 2: Replace generic placeholders with language-specific values
        replacements = {
            '[language]': lang_config['name'].lower(),
            '[Language]': lang_config['name'],
            '[extension]': lang_config['extension'],
            '[package-manager-format]': self._get_package_format(lang_config),
            '[package-manager]': lang_config['package_manager'],
            '[package_file]': lang_config['package_file'],
            '[build_command]': lang_config['build_command'],
            '[linter]': lang_config['linter'],
            '[code-gen-tool]': lang_config['code_gen'],
            '[di-library]': lang_config['di_library'],
            '[state-management-library]': lang_config['state_management'][0],
            '[async_pattern]': lang_config['async_pattern'],
            '[result_type]': lang_config['result_type'],
            '[immutability]': lang_config['immutability'],
            '[json_serialization]': lang_config['json_serialization'],
        }
        
        # Apply replacements
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, str(value))
        
        # Step 3: Replace code block language tags - handle multiple patterns
        # Pattern 1: ```[language]
        content = re.sub(
            r'```\[language\]',
            f"```{lang_config['name'].lower()}",
            content,
            flags=re.IGNORECASE
        )
        # Pattern 2: ```[Language] (capitalized)
        content = re.sub(
            r'```\[Language\]',
            f"```{lang_config['name']}",
            content
        )
        
        # Step 4: Replace language-specific terminology
        content = self._replace_language_terminology(content, language_key, lang_config)
        
        # Add language-specific notes
        if requirements:
            content = self._add_requirements_section(content, requirements, lang_config)
        
        # Add generation metadata
        content = self._add_metadata(content, lang_config)
        
        return content
    
    def _process_conditional_sections(self, content: str, target_lang: str) -> str:
        """
        Process conditional sections in templates.
        
        Supports patterns like:
        <!-- BEGIN:FLUTTER -->...<!-- END:FLUTTER -->
        <!-- BEGIN:REACT -->...<!-- END:REACT -->
        
        Only includes sections matching the target language, removes others.
        """
        # Language aliases for conditional sections
        lang_aliases = {
            'react': ['react', 'typescript', 'tsx', 'jsx'],
            'flutter': ['flutter', 'dart'],
            'kotlin': ['kotlin', 'android'],
            'swift': ['swift', 'ios'],
            'python': ['python', 'py'],
            'java': ['java'],
            'csharp': ['csharp', 'c#', 'dotnet'],
            'go': ['go', 'golang'],
            'rust': ['rust'],
        }
        
        # Find all conditional sections
        pattern = r'<!--\s*BEGIN:(\w+)\s*-->.*?<!--\s*END:\1\s*-->'
        
        def should_include_section(section_lang: str) -> bool:
            """Check if a section should be included for target language."""
            section_lang_lower = section_lang.lower()
            target_lang_lower = target_lang.lower()
            
            # Direct match
            if section_lang_lower == target_lang_lower:
                return True
            
            # Check aliases
            for key, aliases in lang_aliases.items():
                if target_lang_lower == key and section_lang_lower in aliases:
                    return True
                if section_lang_lower == key and target_lang_lower in aliases:
                    return True
            
            # Partial match (e.g., "REACT" matches "react")
            if section_lang_lower in target_lang_lower or target_lang_lower in section_lang_lower:
                return True
            
            return False
        
        def replace_section(match):
            section_lang = match.group(1)
            section_content = match.group(0)
            
            if should_include_section(section_lang):
                # Include the section, but remove the markers
                return re.sub(r'<!--\s*(BEGIN|END):\w+\s*-->', '', section_content)
            else:
                # Remove the entire section
                return ''
        
        # Process all conditional sections
        content = re.sub(pattern, replace_section, content, flags=re.DOTALL | re.IGNORECASE)
        
        return content
    
    def _replace_language_terminology(self, content: str, language_key: str, lang_config: Dict) -> str:
        """
        Replace language-specific terminology that might be hardcoded.
        
        Examples:
        - "pub dependencies" → "npm dependencies" (for React)
        - "StatefulWidget" → "React.Component" (for React)
        - "Future<Either<...>>" → "Promise<Result<...>>" (for React)
        """
        # Language-specific terminology replacements
        terminology_map = {
            'react': {
                r'\bpub dependencies\b': 'npm dependencies',
                r'\bpubspec\.yaml\b': 'package.json',
                r'\bflutter pub\b': 'npm',
                r'\bStatefulWidget\b': 'React.Component',
                r'\bStatelessWidget\b': 'React.FC',
                r'\bFuture<Either<': 'Promise<Result<',
                r'\bEither<Failure, T>': 'Result<T, E>',
                r'\b@freezed\b': 'readonly',
                r'\b@JsonSerializable\b': 'class-transformer',
                r'\bimport \'package:': 'import {',
                r'\b\.dart\b': '.tsx',
            },
            'flutter': {
                r'\bnpm dependencies\b': 'pub dependencies',
                r'\bpackage\.json\b': 'pubspec.yaml',
                r'\bnpm\b': 'flutter pub',
                r'\bPromise<Result<': 'Future<Either<',
                r'\bResult<T, E>': 'Either<Failure, T>',
            },
            'kotlin': {
                r'\bpub dependencies\b': 'gradle dependencies',
                r'\bpubspec\.yaml\b': 'build.gradle.kts',
                r'\bFuture<Either<': 'suspend fun',
                r'\bEither<Failure, T>': 'Result<T, E>',
            },
        }
        
        if language_key in terminology_map:
            for pattern, replacement in terminology_map[language_key].items():
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        return content
    
    def _get_package_format(self, lang_config: Dict) -> str:
        """Get package manager format string."""
        pm = lang_config['package_manager']
        if pm == 'pub':
            return 'yaml'
        elif pm == 'npm':
            return 'json'
        elif pm == 'gradle':
            return 'kotlin'
        elif pm == 'maven':
            return 'xml'
        elif pm == 'pip':
            return 'txt'
        elif pm == 'cargo':
            return 'toml'
        else:
            return 'text'
    
    def _add_requirements_section(self, content: str, requirements: str, 
                                  lang_config: Dict) -> str:
        """Add a requirements section at the beginning."""
        requirements_section = f"""
## Generated Requirements

**Target Language/Framework:** {lang_config['name']}
**Generation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**User Requirements:**
{requirements}

---

"""
        # Insert after frontmatter or at the beginning
        if content.startswith('---'):
            # Find end of frontmatter
            end_idx = content.find('---', 3)
            if end_idx != -1:
                insert_pos = end_idx + 3
                return content[:insert_pos] + requirements_section + content[insert_pos:]
        return requirements_section + content
    
    def _add_metadata(self, content: str, lang_config: Dict) -> str:
        """Add generation metadata at the end."""
        metadata = f"""

---

## Generation Metadata

**Generated for:** {lang_config['name']}
**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Language Extension:** {lang_config['extension']}
**Package Manager:** {lang_config['package_manager']}
**Build Command:** `{lang_config['build_command']}`
**Linter:** `{lang_config['linter']}`

**Language-Specific Features:**
- State Management: {', '.join(lang_config['state_management'])}
- Async Pattern: {lang_config['async_pattern']}
- Result Type: {lang_config['result_type']}
- Immutability: {lang_config['immutability']}
- JSON Serialization: {lang_config['json_serialization']}
- Dependency Injection: {lang_config['di_library']}

"""
        return content + metadata
    
    def generate_filename(self, prompt_type: str, language: str, 
                         feature_name: Optional[str] = None) -> str:
        """Generate output filename."""
        prompt_config = self.get_prompt_config(prompt_type)
        # Normalize language to ensure consistent filenames
        normalized_lang = self.normalize_language(language)
        
        parts = [prompt_config['output_prefix'], normalized_lang]
        if feature_name:
            # Sanitize feature name for filename
            safe_name = re.sub(r'[^\w\s-]', '', feature_name).strip()
            safe_name = re.sub(r'[-\s]+', '_', safe_name)
            parts.append(safe_name)
        
        return f"{'_'.join(parts)}.prompt.md"
    
    def generate(self, prompt_type: str, language: str, 
                requirements: Optional[str] = None,
                feature_name: Optional[str] = None,
                output_path: Optional[Path] = None) -> Path:
        """Generate a customized prompt file."""
        # Get configurations
        lang_config = self.get_language_config(language)
        prompt_config = self.get_prompt_config(prompt_type)
        
        # Normalize language key for conditional sections
        language_key = self.normalize_language(language)
        
        # Read template
        template_content = self.read_template(prompt_config['template'])
        
        # Customize content
        customized_content = self.customize_content(
            template_content, 
            lang_config, 
            requirements,
            language_key
        )
        
        # Determine output path
        if output_path is None:
            filename = self.generate_filename(prompt_type, language, feature_name)
            output_path = self.specify_dir / filename
        else:
            output_path = Path(output_path)
            if output_path.is_dir():
                filename = self.generate_filename(prompt_type, language, feature_name)
                output_path = output_path / filename
        
        # Write output
        output_path.write_text(customized_content, encoding='utf-8')
        
        return output_path
    
    def generate_all(
        self,
        language: str,
        requirements: Optional[str] = None,
        feature_name: Optional[str] = None,
        output_dir: Optional[Path] = None,
    ) -> List[Path]:
        """Generate all prompt and rule types for a language."""
        generated_files = []
        for prompt_type in self.PROMPT_TYPES.keys():
            try:
                output_path = self.generate(
                    prompt_type, 
                    language, 
                    requirements, 
                    feature_name,
                    output_dir,
                )
                generated_files.append(output_path)
                print(f"✓ Generated: {output_path.name}")
            except Exception as e:
                print(f"✗ Failed to generate {prompt_type}: {e}")
        return generated_files


def _infer_language_from_description(description: str) -> str:
    """Best-effort inference of language/framework from a project description."""
    text = description.lower()

    mobile_keywords = ['mobile app', 'ios app', 'android app', 'react native']
    web_keywords = ['web app', 'website', 'web application', 'spa', 'react', 'next.js', 'vue', 'angular']
    backend_keywords = ['api', 'backend', 'microservice', 'server']

    if 'flutter' in text or 'dart' in text:
        return 'flutter'
    if 'react native' in text:
        return 'react'
    if 'jetpack compose' in text or 'android' in text or 'kotlin' in text:
        return 'kotlin'
    if 'swiftui' in text or 'swift' in text or 'ios' in text:
        return 'swift'
    if any(k in text for k in web_keywords):
        return 'react'
    if any(k in text for k in backend_keywords):
        return 'python'
    if any(k in text for k in mobile_keywords):
        return 'flutter'

    # Default choice: React/TypeScript for generic projects
    return 'react'


def _ask_yes_no(prompt: str, default: bool = False) -> bool:
    """Simple yes/no question on stdin."""
    suffix = ' [Y/n]: ' if default else ' [y/N]: '
    answer = input(prompt + suffix).strip().lower()
    if not answer:
        return default
    return answer.startswith('y')


def _run_project_wizard() -> int:
    """Interactive mode: friendly, step-by-step project wizard."""
    print("────────────────────────────────────────")
    print("  CursorFlow Project Wizard")
    print("────────────────────────────────────────")
    print("I'll ask a few simple questions about your project,")
    print("then generate research plan, implementation plan,")
    print("UI/UX design system, UI/UX bridge, project rules,")
    print("and test rules for you.\n")

    # Step 1: high-level idea
    print("1) What do you want to build?")
    print("   (Example: \"I want to create a shopping mobile app\")")
    description = input("> ").strip()
    if not description:
        print("No description provided, aborting.")
        return 1

    # Step 2: target users
    print("\n2) Who is this for? (target users / audience)")
    print("   (Example: \"Young adults buying sneakers\", or press Enter to skip)")
    target_users = input("> ").strip()

    # Step 3: main platforms
    print("\n3) Which platforms do you care about most?")
    print("   (Examples: \"mobile\", \"web\", \"mobile + web\", or press Enter to skip)")
    platforms = input("> ").strip()

    # Step 4: any extra constraints or preferences
    print("\n4) Any important constraints or preferences?")
    print("   (Examples: \"offline first\", \"small budget\", \"must be very fast\",")
    print("    or press Enter to skip)")
    extra_notes = input("> ").strip()

    # Step 5: tech stack (language/framework)
    inferred_lang = _infer_language_from_description(description + " " + platforms)
    print(f"\n5) About the tech stack")
    print(f"   Based on your answers, a good default could be: {inferred_lang}")
    if _ask_yes_no("   Do you want to choose a different language/framework?", default=False):
        print("   Some options you can type:")
        print("     flutter, dart, kotlin, android, swift, ios")
        print("     typescript, react, reactjs, python, java, csharp, go, rust")
        lang_input = input("   Enter language/framework (or press Enter to keep the default): ").strip()
        if not lang_input:
            lang = inferred_lang
        else:
            # Normalize the language input
            generator_temp = PromptGenerator()
            try:
                normalized = generator_temp.normalize_language(lang_input)
                if normalized in generator_temp.LANGUAGE_MAPPINGS:
                    lang = normalized
                    print(f"   ✓ Using: {generator_temp.LANGUAGE_MAPPINGS[normalized]['name']}")
                else:
                    print(f"   ⚠ Could not recognize '{lang_input}', using default: {inferred_lang}")
                    lang = inferred_lang
            except Exception:
                print(f"   ⚠ Could not recognize '{lang_input}', using default: {inferred_lang}")
                lang = inferred_lang
    else:
        lang = inferred_lang

    # Project name (used in filenames)
    default_name = re.sub(r'[^\\w\\s-]', '', description).strip()
    default_name = re.sub(r'[-\\s]+', '_', default_name.lower())[:40] or 'project'
    print("\n6) Give this project a short name (used only for filenames).")
    project_name = input(f"   Project name [{default_name}]: ").strip()
    if not project_name:
        project_name = default_name

    # Output directory selection
    desktop_default = Path.home() / "Desktop" / "CursorFlow"
    print("\n7) Where should I save the generated files?")
    print(f"   Press Enter to use the default folder: {desktop_default}")
    output_str = input("   Output folder: ").strip()
    if not output_str:
        output_dir = desktop_default
    else:
        output_dir = Path(output_str).expanduser()

    output_dir.mkdir(parents=True, exist_ok=True)

    # Build a richer requirements block from answers
    requirements_lines = [
        "## Project Idea",
        description,
        "",
        "## Target Users",
        target_users or "Not specified",
        "",
        "## Platforms",
        platforms or "Not specified",
        "",
        "## Extra Notes",
        extra_notes or "None",
    ]
    combined_requirements = "\n".join(requirements_lines)

    # Initialize generator early to verify and normalize language
    generator = PromptGenerator()
    try:
        lang_config = generator.get_language_config(lang)
        actual_lang_name = lang_config['name']
        # Update lang to normalized version
        lang = generator.normalize_language(lang)
    except Exception as e:
        print(f"\n✗ Error with language '{lang}': {e}")
        return 1

    # Summary before generating
    print("\n────────────────────────────────────────")
    print("Summary")
    print("────────────────────────────────────────")
    print(f"Project name   : {project_name}")
    print(f"Tech stack     : {actual_lang_name}")
    print(f"Output folder  : {output_dir}")
    print("I'll now generate:")
    print("  - Research plan")
    print("  - Implementation plan")
    print("  - UI/UX design system")
    print("  - UI/UX bridge")
    print("  - Project rules")
    print("  - Test rules")

    if not _ask_yes_no("\nProceed with generation?", default=True):
        print("Cancelled. No files generated.")
        return 0

    print(f"\nGenerating files for '{project_name}' ({lang}) ...\n")

    try:
        generated = generator.generate_all(
            language=lang,
            requirements=combined_requirements,
            feature_name=project_name,
            output_dir=output_dir,
        )
    except Exception as e:
        print(f"✗ Error while generating prompts: {e}", file=sys.stderr)
        return 1

    print("Done. Generated files:")
    for path in generated:
        print(f"  - {path}")

    print("\nYou can open these markdown files in Cursor and run them as commands.")
    return 0


def main():
    """Main CLI entry point."""
    # If no arguments are provided, run interactive project wizard.
    if len(sys.argv) == 1:
        return _run_project_wizard()

    parser = argparse.ArgumentParser(
        description='Generate customized prompt files from common templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate research plan for Flutter
  python generate_prompt.py research_plan flutter --requirements "User authentication feature"
  
  # Generate all prompts for Kotlin
  python generate_prompt.py all kotlin --feature "Shopping Cart"
  
  # Generate implementation plan for TypeScript
  python generate_prompt.py implementation_plan typescript --requirements "Dashboard component"
        """
    )
    
    parser.add_argument(
        'prompt_type',
        choices=['research_plan', 'implementation_plan', 'ui_ux_design', 
                'ui_ux_bridge', 'all'],
        help='Type of prompt to generate'
    )
    
    parser.add_argument(
        'language',
        help='Target language/framework (e.g., flutter, kotlin, swift, typescript)'
    )
    
    parser.add_argument(
        '--requirements', '-r',
        help='User requirements/description for the feature'
    )
    
    parser.add_argument(
        '--feature', '-f',
        help='Feature name (used in filename)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Output file path (default: .cursor/commands/specify/)'
    )
    
    parser.add_argument(
        '--base-dir',
        type=Path,
        help='Base directory (default: script directory)'
    )
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = PromptGenerator(args.base_dir)
    
    try:
        if args.prompt_type == 'all':
            # Generate all prompt types
            print(f"Generating all prompts for {args.language}...")
            generated_files = generator.generate_all(
                args.language,
                args.requirements,
                args.feature
            )
            print(f"\n✓ Generated {len(generated_files)} files in {generator.specify_dir}")
        else:
            # Generate single prompt type
            output_path = generator.generate(
                args.prompt_type,
                args.language,
                args.requirements,
                args.feature,
                args.output
            )
            print(f"✓ Generated: {output_path}")
            print(f"  Location: {output_path.absolute()}")
    
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

