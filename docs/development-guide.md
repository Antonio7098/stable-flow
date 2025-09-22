# Stable Flow Development Guide

This guide is for developers who want to contribute to Stable Flow. It covers the codebase architecture, development workflow, coding standards, and contribution guidelines.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Development Environment Setup](#development-environment-setup)
- [Code Organization](#code-organization)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Contribution Guidelines](#contribution-guidelines)
- [Release Process](#release-process)

## Architecture Overview

### Core Components

Stable Flow is built with a modular architecture focused on template processing and document generation.

#### Main Modules

- **`scripts/process_templates.py`**: Main CLI application and template processor
- **`scripts/stable-flow`**: CLI entry point script
- **`tests/`**: Comprehensive test suite
- **`templates/source/`**: Jinja2 template sources
- **`templates/config/`**: Configuration templates
- **`examples/`**: Example configurations and generated docs
- **`docs/`**: Documentation and guides

#### Key Classes

```python
class TemplateProcessor:
    """Main template processing engine"""
    - Loads Jinja2 templates
    - Processes configuration data
    - Generates documents
    - Handles template inheritance and includes

class CLI Interface:
    """Command-line interface"""
    - generate: Generate documents from config
    - validate: Validate configuration files
    - init: Initialize new projects
    - Custom commands for specific workflows
```

#### Data Flow

```
Configuration YAML → TemplateProcessor → Jinja2 Rendering → Markdown Documents
                                      ↓
                              Validation & Error Handling
```

### Template System

Stable Flow uses Jinja2 templating with custom extensions:

- **Conditional sections**: `{% if sections.prd.competitive_analysis %}`
- **Feature flags**: `{% if features.cascade %}`
- **Custom filters**: `{{ date | strftime('%Y-%m-%d') }}`
- **Template inheritance**: Base templates with section overrides
- **Macros and includes**: Reusable template components

### Configuration System

YAML-based configuration with validation:

- **Schema validation**: JSON Schema for structure validation
- **Dependency checking**: Cross-field validation rules
- **Tier enforcement**: Tier-specific requirements
- **Error reporting**: Detailed validation messages

## Development Environment Setup

### Prerequisites

- **Python 3.8+**: Core runtime
- **Git**: Version control
- **Virtual Environment**: Isolated dependencies

### Quick Setup

```bash
# Clone repository
git clone https://github.com/your-org/stable-flow.git
cd stable-flow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run tests to verify setup
python -m pytest tests/
```

### Development Dependencies

```txt
# requirements.txt
Jinja2>=3.0.0          # Template engine
PyYAML>=6.0            # YAML processing
Click>=8.0.0           # CLI framework
Rich>=13.0.0           # Rich terminal output
pytest>=7.0.0          # Testing framework
pytest-cov>=4.0.0      # Coverage reporting
black>=22.0.0          # Code formatting
flake8>=6.0.0          # Linting
mypy>=1.0.0            # Type checking
```

### IDE Configuration

#### VS Code Settings

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

#### PyCharm Configuration

- Set Python interpreter to virtual environment
- Enable pytest as test runner
- Configure Black as code formatter
- Enable mypy type checking

## Code Organization

### Directory Structure

```
stable-flow/
├── scripts/                    # Main application code
│   ├── process_templates.py    # Core template processor
│   └── stable-flow             # CLI entry point
├── templates/                  # Template system
│   ├── source/                 # Jinja2 template sources
│   ├── config/                 # Configuration templates
│   └── advanced/               # Advanced template types
├── tests/                      # Test suite
│   ├── conftest.py             # Test configuration
│   ├── test_*.py              # Test modules
│   └── fixtures/               # Test data
├── examples/                   # Example configurations
│   ├── minimal-project/        # Minimal tier example
│   ├── core-project/           # Core tier example
│   └── advanced-project/       # Advanced tier example
├── docs/                       # Documentation
│   ├── getting-started.md      # User guide
│   ├── development-guide.md    # This file
│   └── *.md                    # Other docs
├── requirements.txt            # Python dependencies
├── setup.py                    # Package configuration
├── pyproject.toml              # Build configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # Project overview
```

### Module Organization

#### `scripts/process_templates.py`

Main application module containing:

```python
class TemplateProcessor:
    def __init__(self, project_root: Path)
    def process_template(self, template_name: str, config: Dict) -> str
    def generate_documents(self, config: Dict) -> None
    def validate_config(self, config: Dict) -> List[str]

def load_config(config_path: Path) -> Dict[str, Any]
def save_config(config: Dict, config_path: Path) -> None
def create_project_structure(project_root: Path) -> None
```

#### Template Structure

Templates follow a hierarchical organization:

- **Base templates**: Common structure and sections
- **Section templates**: Specialized content blocks
- **Macro libraries**: Reusable template components
- **Include files**: Shared template fragments

### Configuration Schema

Configuration validation uses JSON Schema:

```python
CONFIG_SCHEMA = {
    "type": "object",
    "required": ["project", "tier"],
    "properties": {
        "project": {
            "type": "object",
            "required": ["name", "author"],
            "properties": {
                "name": {"type": "string"},
                "author": {"type": "string"},
                # ... more properties
            }
        },
        "tier": {
            "enum": ["minimal", "core", "advanced", "custom"]
        },
        # ... more schema definitions
    }
}
```

## Development Workflow

### Git Workflow

Stable Flow uses GitFlow branching strategy:

```bash
# Feature development
git checkout develop
git checkout -b feature/add-new-template

# Make changes
git add .
git commit -m "feat: add new template type

- Add template processing logic
- Add configuration validation
- Add test coverage
- Update documentation"

# Push feature branch
git push origin feature/add-new-template

# Create pull request
# Code review and testing
# Merge to develop

# Release preparation
git checkout develop
git pull origin develop
git checkout -b release/v1.1.0

# Final testing and documentation
# Merge to main and develop
```

### Commit Convention

Follow conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

Examples:
```
feat(templates): add support for custom template variables
fix(validation): handle empty configuration files
docs(readme): update installation instructions
```

### Pull Request Process

1. **Create feature branch** from `develop`
2. **Implement changes** with tests
3. **Run full test suite** locally
4. **Update documentation** as needed
5. **Create pull request** with description
6. **Code review** by maintainers
7. **CI/CD checks** pass
8. **Merge** to `develop`

### Code Review Guidelines

#### For Reviewers
- Check code follows style guidelines
- Verify test coverage is adequate
- Ensure documentation is updated
- Validate configuration changes
- Test functionality manually

#### For Contributors
- Write clear commit messages
- Include tests for new features
- Update documentation
- Follow coding standards
- Respond promptly to review feedback

## Coding Standards

### Python Style Guide

Follow PEP 8 with these additions:

#### Naming Conventions

```python
# Classes
class TemplateProcessor:
    """Process templates."""

# Functions and methods
def process_template(template_name: str, config: Dict[str, Any]) -> str:
    """Process a single template."""

# Variables
template_name = "example"
config_data = {}

# Constants
DEFAULT_TIER = "minimal"
TEMPLATE_DIR = "templates"
```

#### Type Hints

Use comprehensive type hints:

```python
from typing import Dict, List, Optional, Any, Union
from pathlib import Path

def process_template(
    self,
    template_name: str,
    config: Dict[str, Any]
) -> Optional[str]:
    """Process a template with configuration."""

def load_config(config_path: Path) -> Dict[str, Any]:
    """Load configuration from YAML file."""
```

#### Error Handling

Use specific exception types:

```python
class TemplateError(Exception):
    """Base exception for template processing errors."""

class ValidationError(Exception):
    """Configuration validation error."""

def process_template(self, template_name: str, config: Dict[str, Any]) -> Optional[str]:
    try:
        # Processing logic
        return content
    except TemplateNotFound:
        logger.error(f"Template {template_name} not found")
        return None
    except ValidationError as e:
        logger.error(f"Configuration validation failed: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing template {template_name}: {e}")
        return None
```

#### Logging

Use structured logging:

```python
import logging

logger = logging.getLogger(__name__)

def process_template(self, template_name: str, config: Dict[str, Any]) -> Optional[str]:
    logger.info(f"Processing template: {template_name}")
    logger.debug(f"Configuration: {config}")

    # Processing logic

    logger.info(f"Successfully processed template: {template_name}")
    return content
```

### Documentation Standards

#### Docstrings

Use Google-style docstrings:

```python
def process_template(
    self,
    template_name: str,
    config: Dict[str, Any]
) -> Optional[str]:
    """Process a single template with configuration data.

    Args:
        template_name: Name of the template to process
        config: Configuration dictionary

    Returns:
        Processed template content as string, or None if processing fails

    Raises:
        TemplateError: If template processing fails
        ValidationError: If configuration is invalid
    """
```

#### Code Comments

```python
# Process each template in the tier
for template_name in templates_to_process:
    # Update progress bar
    progress.update(task, description=f"Processing {template_name}...")

    # Process template with configuration
    content = self.process_template(template_name, config)

    # Skip if processing failed
    if content is None:
        continue

    # Write to output file
    output_path = output_dir / f"{template_name}.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
```

### Template Standards

#### Jinja2 Best Practices

```jinja2
{# Use descriptive variable names #}
{% set document_title = project.name + " - Technical Design" %}

{# Use filters for data transformation #}
{% set formatted_date = "now" | strftime("%Y-%m-%d") %}

{# Use macros for reusable components #}
{% macro section_header(title, level=2) -%}
{% set hashes = "#" * level %}
{{ hashes }} {{ title }}
{% endmacro %}

{# Use conditional sections #}
{% if sections.technical_design.security_detailed %}
## Security Design
{{ technical_design.security | tojson(indent=2) }}
{% endif %}

{# Use loops appropriately #}
{% for component in technical_design.components %}
### {{ component.name }}
- **Purpose**: {{ component.purpose }}
- **Technologies**: {{ component.technologies | join(", ") }}
{% endfor %}
```

#### Template Organization

```
{# Header section #}
# {{ project.name }} - {{ document_type }}

## Document Information
- **Version**: {{ version }}
- **Author**: {{ project.author }}

{# Main content sections #}
{% if sections.section_name %}
## Section Name
Content here...
{% endif %}

{# Appendices #}
## References
{% for reference in references %}
- {{ reference }}
{% endfor %}
```

## Testing Guidelines

### Test Structure

```
tests/
├── conftest.py              # Test configuration and fixtures
├── test_cli.py              # CLI interface tests
├── test_templates.py        # Template processing tests
├── test_integration.py      # Integration tests
├── test_e2e.py              # End-to-end tests
└── test_validation.py       # Configuration validation tests
```

### Test Categories

#### Unit Tests

Test individual functions and classes:

```python
def test_template_processor_init():
    """Test TemplateProcessor initialization."""
    processor = TemplateProcessor(Path("templates"))
    assert processor.project_root == Path("templates")
    assert processor.jinja_env is not None

def test_config_validation():
    """Test configuration validation."""
    config = {"project": {"name": "Test"}, "tier": "minimal"}
    errors = validate_config(config)
    assert len(errors) == 0
```

#### Integration Tests

Test component interactions:

```python
def test_template_processing_integration():
    """Test full template processing workflow."""
    config = load_test_config("core")
    processor = TemplateProcessor(Path("."))

    # Process template
    content = processor.process_template("prd-template", config)

    # Verify content
    assert content is not None
    assert "Product Requirements Document" in content
    assert config["project"]["name"] in content
```

#### End-to-End Tests

Test complete user workflows:

```python
def test_full_document_generation():
    """Test complete document generation."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config = create_test_config("core")
        output_dir = Path(temp_dir) / "docs"

        # Generate documents
        processor = TemplateProcessor(Path("."))
        processor.generate_documents(config)

        # Verify all expected files exist
        expected_files = ["prd.md", "technical-design.md", "features.csv"]
        for filename in expected_files:
            assert (output_dir / filename).exists()
```

### Test Fixtures

Use pytest fixtures for test data:

```python
@pytest.fixture
def minimal_config():
    """Minimal tier configuration for testing."""
    return {
        "project": {
            "name": "Test Project",
            "author": "Test Author"
        },
        "tier": "minimal",
        "features": {"cascade": False}
    }

@pytest.fixture
def template_processor():
    """Template processor instance."""
    return TemplateProcessor(Path("templates"))
```

### Test Coverage

Maintain high test coverage:

```bash
# Run tests with coverage
pytest --cov=scripts --cov-report=html

# Coverage targets
# - Unit tests: 90%+ coverage
# - Integration tests: 80%+ coverage
# - End-to-end tests: 70%+ coverage
# - Overall: 85%+ coverage
```

### Test Data Management

```python
# Use factories for test data
def create_test_config(tier="minimal"):
    """Create test configuration."""
    config = {
        "project": {
            "name": f"Test {tier.title()} Project",
            "author": "Test Author"
        },
        "tier": tier
    }

    if tier == "core":
        config.update({
            "sprint_planning": {"team": {"capacity": "20 points"}},
            "development_guide": {"git": {"branching_strategy": "GitFlow"}}
        })

    return config
```

## Contribution Guidelines

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** from `develop`
4. **Set up development environment**
5. **Run tests** to ensure everything works

### Types of Contributions

#### Code Contributions
- Bug fixes
- New features
- Performance improvements
- Code refactoring

#### Template Contributions
- New document templates
- Template improvements
- Template customization options

#### Documentation Contributions
- User guides
- API documentation
- Code documentation
- Examples and tutorials

#### Test Contributions
- Additional test cases
- Test improvements
- CI/CD improvements

### Contribution Process

1. **Choose an issue** or create a new one
2. **Discuss approach** with maintainers if needed
3. **Implement changes** following coding standards
4. **Write tests** for new functionality
5. **Update documentation** as needed
6. **Run full test suite** locally
7. **Create pull request** with clear description
8. **Respond to review feedback** promptly

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers learn
- Focus on code quality and user experience
- Follow the established processes

## Release Process

### Version Numbering

Stable Flow uses semantic versioning:

```
MAJOR.MINOR.PATCH

- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)
```

### Release Checklist

#### Pre-Release
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Release notes written
- [ ] Version number updated

#### Release Steps
1. **Create release branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/v1.1.0
   ```

2. **Update version numbers**
   ```python
   # Update version in setup.py
   version = "1.1.0"

   # Update version in docs
   ```

3. **Run final tests**
   ```bash
   python -m pytest tests/ --cov=scripts --cov-report=html
   ```

4. **Create release commit**
   ```bash
   git add .
   git commit -m "chore: release v1.1.0"
   ```

5. **Merge to main**
   ```bash
   git checkout main
   git merge release/v1.1.0
   git push origin main
   git tag -a v1.1.0 -m "Release v1.1.0"
   git push origin v1.1.0
   ```

6. **Merge back to develop**
   ```bash
   git checkout develop
   git merge release/v1.1.0
   git push origin develop
   ```

7. **Create GitHub release**
   - Go to GitHub releases
   - Create new release from tag
   - Copy release notes
   - Publish release

### Post-Release
- [ ] Update changelog
- [ ] Announce release
- [ ] Monitor for issues
- [ ] Plan next release

## Support and Resources

### Getting Help

- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions
- **Documentation**: Check docs/ directory for guides
- **Examples**: Review examples/ directory for usage patterns

### Development Resources

- **Architecture Decisions**: Check `templates/advanced/adr-*.md`
- **Code Examples**: Review existing templates and scripts
- **Test Patterns**: Look at existing test files
- **Configuration Schema**: See `docs/configuration-reference.md`

### Community Guidelines

- **Communication**: Be clear and concise
- **Collaboration**: Work together constructively
- **Quality**: Maintain high standards
- **Inclusivity**: Welcome all contributors

Remember: This is a community project. Your contributions help make Stable Flow better for everyone! 🚀</content>
</xai:function_call">Now let me create the template development guide.</content>
</xai:function_call name="write">
<parameter name="file_path">docs/template-development.md

