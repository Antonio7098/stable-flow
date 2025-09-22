# Stable Flow Testing Guide

This guide covers the comprehensive testing strategy for Stable Flow, including unit tests, integration tests, end-to-end tests, and testing best practices.

## Table of Contents

- [Testing Strategy](#testing-strategy)
- [Test Structure](#test-structure)
- [Unit Testing](#unit-testing)
- [Integration Testing](#integration-testing)
- [End-to-End Testing](#end-to-end-testing)
- [Template Testing](#template-testing)
- [Configuration Testing](#configuration-testing)
- [Performance Testing](#performance-testing)
- [Test Automation](#test-automation)
- [Continuous Integration](#continuous-integration)

## Testing Strategy

### Testing Pyramid

Stable Flow follows a testing pyramid approach:

```
End-to-End Tests (10-20%)
    ↗
Integration Tests (20-30%)
    ↗
Unit Tests (40-60%)
    ↗
Static Analysis (10-20%)
```

### Test Categories

#### Functional Tests
- **Template Processing**: Verify templates render correctly
- **Configuration Validation**: Ensure config validation works
- **Document Generation**: Test complete document workflows

#### Non-Functional Tests
- **Performance**: Test processing speed and memory usage
- **Security**: Validate input sanitization and secure defaults
- **Usability**: Test error messages and user experience

#### Regression Tests
- **Backward Compatibility**: Ensure changes don't break existing functionality
- **Template Compatibility**: Verify template changes work with existing configs

## Test Structure

### Directory Layout

```
tests/
├── conftest.py              # Test configuration and fixtures
├── test_cli.py              # CLI interface tests
├── test_templates.py        # Template processing tests
├── test_integration.py      # Integration tests
├── test_e2e.py              # End-to-end tests
├── test_validation.py       # Configuration validation tests
├── test_performance.py      # Performance tests
├── fixtures/                # Test data and fixtures
│   ├── configs/             # Sample configurations
│   ├── templates/           # Test templates
│   └── outputs/             # Expected outputs
└── utils/                   # Test utilities
    ├── template_utils.py    # Template testing helpers
    ├── config_utils.py      # Configuration testing helpers
    └── assertions.py        # Custom assertions
```

### Test Naming Convention

```python
# Unit tests
test_function_name()
test_function_name_with_condition()
test_function_name_returns_expected_value()

# Integration tests
test_feature_integration()
test_workflow_integration()

# End-to-end tests
test_complete_user_workflow()
test_full_document_generation()

# Template tests
test_template_renders_correctly()
test_template_handles_edge_cases()
```

### Test File Organization

```python
# test_cli.py
def test_cli_help_command():
    """Test CLI help command displays correctly."""

def test_cli_generate_command():
    """Test CLI generate command with valid config."""

def test_cli_validate_command():
    """Test CLI validate command."""

# test_templates.py
def test_template_processor_init():
    """Test TemplateProcessor initialization."""

def test_template_rendering():
    """Test basic template rendering."""

def test_template_error_handling():
    """Test template error handling."""
```

## Unit Testing

### Template Processor Tests

```python
import pytest
from pathlib import Path
from stable_flow.template_processor import TemplateProcessor

class TestTemplateProcessor:

    def test_init_with_valid_path(self, tmp_path):
        """Test processor initializes with valid path."""
        processor = TemplateProcessor(tmp_path)
        assert processor.project_root == tmp_path
        assert processor.templates_dir == tmp_path / "templates"

    def test_init_with_invalid_path(self):
        """Test processor raises error with invalid path."""
        with pytest.raises(ValueError):
            TemplateProcessor(Path("/nonexistent/path"))

    def test_load_template_success(self, template_processor, sample_template):
        """Test successful template loading."""
        template = template_processor._load_template("sample")
        assert template is not None

    def test_load_template_not_found(self, template_processor):
        """Test template loading failure."""
        with pytest.raises(TemplateNotFound):
            template_processor._load_template("nonexistent")

    @pytest.mark.parametrize("tier", ["minimal", "core", "advanced", "custom"])
    def test_get_templates_for_tier(self, template_processor, tier):
        """Test template selection for different tiers."""
        config = {"tier": tier, "templates": {}}
        templates = template_processor._get_templates_for_tier(config)
        assert isinstance(templates, list)
        assert len(templates) > 0
```

### Configuration Validation Tests

```python
import pytest
from stable_flow.config_validator import ConfigValidator

class TestConfigValidation:

    def test_valid_minimal_config(self, validator):
        """Test validation of valid minimal config."""
        config = {
            "project": {"name": "Test", "author": "Tester"},
            "tier": "minimal"
        }
        errors = validator.validate(config)
        assert len(errors) == 0

    def test_missing_required_field(self, validator):
        """Test validation fails with missing required field."""
        config = {"project": {"name": "Test"}}  # Missing author
        errors = validator.validate(config)
        assert len(errors) > 0
        assert "author" in str(errors[0])

    def test_invalid_tier(self, validator):
        """Test validation fails with invalid tier."""
        config = {
            "project": {"name": "Test", "author": "Tester"},
            "tier": "invalid"
        }
        errors = validator.validate(config)
        assert len(errors) > 0
        assert "tier" in str(errors[0])

    @pytest.mark.parametrize("tier,required_fields", [
        ("core", ["sprint_planning.team.capacity"]),
        ("advanced", ["ai_agents.system_prompt"]),
    ])
    def test_tier_specific_requirements(self, validator, tier, required_fields):
        """Test tier-specific validation requirements."""
        config = {
            "project": {"name": "Test", "author": "Tester"},
            "tier": tier
            # Missing required fields for tier
        }
        errors = validator.validate(config)
        for field in required_fields:
            assert any(field in error for error in errors)
```

### Template Rendering Tests

```python
class TestTemplateRendering:

    def test_simple_variable_rendering(self, template_processor):
        """Test basic variable substitution."""
        template_content = "Project: {{ project.name }}"
        config = {"project": {"name": "Test Project"}}

        result = template_processor._render_template_string(template_content, config)
        assert "Project: Test Project" in result

    def test_conditional_rendering(self, template_processor):
        """Test conditional template sections."""
        template_content = """
        {% if features.cascade %}
        Cascade enabled
        {% endif %}
        {% if tier == 'advanced' %}
        Advanced features
        {% endif %}
        """

        # Test with cascade enabled, core tier
        config = {"features": {"cascade": True}, "tier": "core"}
        result = template_processor._render_template_string(template_content, config)
        assert "Cascade enabled" in result
        assert "Advanced features" not in result

    def test_loop_rendering(self, template_processor):
        """Test loop constructs in templates."""
        template_content = """
        {% for feature in features %}
        - {{ feature.name }}
        {% endfor %}
        """

        config = {"features": [
            {"name": "Feature 1"},
            {"name": "Feature 2"}
        ]}

        result = template_processor._render_template_string(template_content, config)
        assert "Feature 1" in result
        assert "Feature 2" in result

    def test_filter_usage(self, template_processor):
        """Test custom filter usage."""
        template_content = "{{ 'hello world' | title }}"
        config = {}

        result = template_processor._render_template_string(template_content, config)
        assert "Hello World" in result
```

## Integration Testing

### Template Processing Integration

```python
class TestTemplateProcessingIntegration:

    def test_full_template_processing(self, template_processor, core_config):
        """Test complete template processing workflow."""
        content = template_processor.process_template("prd-template", core_config)

        assert content is not None
        assert len(content) > 100  # Reasonable content length
        assert "# Product Requirements Document" in content
        assert core_config["project"]["name"] in content

    def test_template_with_dependencies(self, template_processor, core_config):
        """Test template that depends on other templates."""
        # Process PRD template first
        prd_content = template_processor.process_template("prd-template", core_config)
        assert prd_content is not None

        # Process technical design template
        tdd_content = template_processor.process_template("technical-design-template", core_config)
        assert tdd_content is not None

        # Verify cross-references if any
        # (This would depend on specific template implementation)

    def test_configuration_cascade(self, template_processor, cascade_config):
        """Test cascade feature integration."""
        # Enable cascade
        cascade_config["features"]["cascade"] = True

        # Process multiple templates
        templates = ["prd-template", "technical-design-template", "features-csv-template"]
        contents = {}

        for template in templates:
            content = template_processor.process_template(template, cascade_config)
            assert content is not None
            contents[template] = content

        # Verify cascade effects (specific to implementation)
        # For example, check if features from PRD appear in other docs
```

### CLI Integration Tests

```python
class TestCLIIntegration:

    def test_cli_generate_integration(self, tmp_path, core_config):
        """Test full CLI generate workflow."""
        # Create config file
        config_file = tmp_path / "config.yaml"
        with open(config_file, 'w') as f:
            yaml.dump(core_config, f)

        # Create output directory
        output_dir = tmp_path / "docs"
        output_dir.mkdir()

        # Run CLI command
        result = subprocess.run([
            "python", "scripts/process_templates.py",
            "--config", str(config_file),
            "--output", str(output_dir)
        ], capture_output=True, text=True)

        # Verify success
        assert result.returncode == 0
        assert "Documents generated successfully" in result.stdout

        # Verify output files
        expected_files = ["prd-template.md", "technical-design-template.md"]
        for filename in expected_files:
            assert (output_dir / filename).exists()

    def test_cli_validation_integration(self, tmp_path):
        """Test CLI validation with various configs."""
        test_cases = [
            ("valid_minimal", True),
            ("invalid_missing_project", False),
            ("invalid_bad_tier", False),
        ]

        for config_name, should_pass in test_cases:
            config_file = tmp_path / f"{config_name}.yaml"
            config = get_test_config(config_name)
            with open(config_file, 'w') as f:
                yaml.dump(config, f)

            result = subprocess.run([
                "python", "scripts/process_templates.py",
                "--config", str(config_file),
                "--validate-only"
            ], capture_output=True, text=True)

            if should_pass:
                assert result.returncode == 0
                assert "Configuration is valid" in result.stdout
            else:
                assert result.returncode != 0
                assert "Configuration validation failed" in result.stderr
```

## End-to-End Testing

### Complete Workflow Tests

```python
class TestEndToEnd:

    def test_minimal_tier_workflow(self, tmp_path):
        """Test complete minimal tier workflow."""
        # Setup
        config = create_minimal_config()
        config_file = tmp_path / "config.yaml"
        with open(config_file, 'w') as f:
            yaml.dump(config, f)

        output_dir = tmp_path / "docs"

        # Execute
        result = run_cli_generate(config_file, output_dir)

        # Verify
        assert result.returncode == 0
        assert output_dir.exists()

        # Check generated files
        prd_file = output_dir / "prd-template.md"
        tdd_file = output_dir / "technical-design-template.md"
        features_file = output_dir / "features-csv-template.md"

        assert prd_file.exists()
        assert tdd_file.exists()
        assert features_file.exists()

        # Verify content quality
        prd_content = prd_file.read_text()
        assert config["project"]["name"] in prd_content
        assert "Product Requirements Document" in prd_content

    def test_core_tier_workflow(self, tmp_path):
        """Test complete core tier workflow."""
        # Similar to minimal but with additional templates
        config = create_core_config()
        config_file = tmp_path / "config.yaml"
        output_dir = tmp_path / "docs"

        result = run_cli_generate(config_file, output_dir)

        assert result.returncode == 0

        # Check all core templates
        expected_files = [
            "prd-template.md",
            "technical-design-template.md",
            "features-csv-template.md",
            "development-guide-template.md",
            "sprint-planning-template.md",
            "sprint-template.md"
        ]

        for filename in expected_files:
            assert (output_dir / filename).exists()

    def test_error_handling_workflow(self, tmp_path):
        """Test error handling in complete workflow."""
        # Create invalid config
        config = {"invalid": "config"}
        config_file = tmp_path / "config.yaml"
        with open(config_file, 'w') as f:
            yaml.dump(config, f)

        output_dir = tmp_path / "docs"

        result = run_cli_generate(config_file, output_dir)

        # Should fail gracefully
        assert result.returncode != 0
        assert "Error" in result.stderr

        # Should not create output directory or files
        assert not output_dir.exists()

    def test_custom_tier_workflow(self, tmp_path):
        """Test custom tier with selective templates."""
        config = create_custom_config()
        config_file = tmp_path / "config.yaml"
        output_dir = tmp_path / "docs"

        result = run_cli_generate(config_file, output_dir)

        assert result.returncode == 0

        # Only selected templates should be generated
        selected_templates = config["templates"]["core"]
        expected_files = [
            f"{template}-template.md"
            for template, enabled in selected_templates.items()
            if enabled
        ]

        for filename in expected_files:
            assert (output_dir / filename).exists()
```

### Performance Tests

```python
class TestPerformance:

    def test_large_project_performance(self, template_processor, large_config):
        """Test performance with large configuration."""
        import time

        start_time = time.time()

        # Process all templates
        templates = template_processor._get_templates_for_tier(large_config)
        for template in templates:
            content = template_processor.process_template(template, large_config)
            assert content is not None

        end_time = time.time()
        duration = end_time - start_time

        # Should complete within reasonable time (adjust threshold as needed)
        assert duration < 30.0, f"Processing took too long: {duration:.2f}s"

    def test_memory_usage(self, template_processor, large_config):
        """Test memory usage during processing."""
        import psutil
        import os

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        # Process templates
        templates = template_processor._get_templates_for_tier(large_config)
        for template in templates:
            content = template_processor.process_template(template, large_config)

        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_used = final_memory - initial_memory

        # Should not use excessive memory (adjust threshold as needed)
        assert memory_used < 500, f"Used too much memory: {memory_used:.1f}MB"

    def test_template_caching(self, template_processor, core_config):
        """Test template caching performance."""
        import time

        # First run (cache miss)
        start_time = time.time()
        content1 = template_processor.process_template("prd-template", core_config)
        first_duration = time.time() - start_time

        # Second run (cache hit - should be faster)
        start_time = time.time()
        content2 = template_processor.process_template("prd-template", core_config)
        second_duration = time.time() - start_time

        # Results should be identical
        assert content1 == content2

        # Second run should be faster (caching benefit)
        # Allow some variance for CI environments
        assert second_duration <= first_duration * 1.5, \
            f"No caching benefit: first={first_duration:.3f}s, second={second_duration:.3f}s"
```

## Template Testing

### Template Content Validation

```python
def test_template_content_quality(template_processor, core_config):
    """Test that generated content meets quality standards."""
    content = template_processor.process_template("prd-template", core_config)

    # Basic structure checks
    assert content.startswith("# ")
    assert "## " in content  # Has sections

    # Project information
    assert core_config["project"]["name"] in content
    assert core_config["project"]["author"] in content

    # No template artifacts
    assert "{{" not in content  # No unprocessed variables
    assert "{%" not in content  # No unprocessed tags

    # Valid markdown (basic checks)
    lines = content.split("\n")
    headers = [line for line in lines if line.startswith("#")]
    for i in range(len(headers) - 1):
        current_level = len(headers[i]) - headers[i].lstrip("#").find(" ") - 1
        next_level = len(headers[i + 1]) - headers[i + 1].lstrip("#").find(" ") - 1
        assert next_level <= current_level + 1, f"Header level jump: {headers[i]} -> {headers[i+1]}"

def test_template_section_conditional_rendering(template_processor, core_config):
    """Test that sections appear/disappear based on configuration."""
    # Test with section enabled
    core_config["sections"]["prd"]["competitive_analysis"] = True
    content = template_processor.process_template("prd-template", core_config)
    assert "## Competitive Analysis" in content

    # Test with section disabled
    core_config["sections"]["prd"]["competitive_analysis"] = False
    content = template_processor.process_template("prd-template", core_config)
    assert "## Competitive Analysis" not in content

def test_template_variable_substitution(template_processor):
    """Test various variable substitution scenarios."""
    test_cases = [
        ("{{ project.name }}", {"project": {"name": "Test"}}, "Test"),
        ("{{ tier | title }}", {"tier": "minimal"}, "Minimal"),
        ("{{ features.cascade | lower }}", {"features": {"cascade": True}}, "true"),
        ("{{ 'now' | strftime('%Y') }}", {}, str(datetime.now().year)),
    ]

    for template_str, config, expected in test_cases:
        result = template_processor._render_template_string(template_str, config)
        assert expected in result, f"Failed for template: {template_str}"
```

### Template Error Handling

```python
def test_template_missing_variable_graceful_handling(template_processor):
    """Test that missing variables are handled gracefully."""
    # Template with potentially missing variables
    template_content = """
    Project: {{ project.name | default('Unknown') }}
    Author: {{ project.author | default('Anonymous') }}
    Tier: {{ tier | default('minimal') }}
    """

    # Config missing some fields
    config = {"project": {"name": "Test"}}  # Missing author, tier

    result = template_processor._render_template_string(template_content, config)

    assert "Project: Test" in result
    assert "Author: Anonymous" in result  # Default used
    assert "Tier: minimal" in result  # Default used

def test_template_invalid_syntax_error_handling(template_processor):
    """Test handling of invalid template syntax."""
    # Template with syntax error
    template_content = """
    {% for item in items %}
    {{ item.name }}
    {% endfor %}  {# Missing endfor #}
    """

    config = {"items": [{"name": "test"}]}

    # Should either handle gracefully or raise clear error
    try:
        result = template_processor._render_template_string(template_content, config)
        # If it succeeds, that's fine too
    except TemplateSyntaxError as e:
        # Should provide clear error message
        assert "endfor" in str(e) or "for" in str(e)
```

## Configuration Testing

### Schema Validation Tests

```python
def test_config_schema_validation(validator):
    """Test configuration against JSON schema."""
    # Valid minimal config
    valid_config = {
        "project": {
            "name": "Test Project",
            "author": "Test Author"
        },
        "tier": "minimal"
    }

    errors = validator.validate_schema(valid_config)
    assert len(errors) == 0

    # Invalid config - missing required field
    invalid_config = {
        "project": {
            "name": "Test Project"
            # Missing author
        }
    }

    errors = validator.validate_schema(invalid_config)
    assert len(errors) > 0
    assert any("author" in error for error in errors)

def test_config_tier_requirements(validator):
    """Test tier-specific configuration requirements."""
    tier_requirements = {
        "minimal": ["project.name", "project.author", "tier"],
        "core": ["project.name", "project.author", "tier", "sprint_planning.team.capacity"],
        "advanced": ["project.name", "project.author", "tier", "ai_agents.system_prompt"]
    }

    for tier, required_paths in tier_requirements.items():
        config = create_minimal_config()
        config["tier"] = tier

        # Add tier-specific requirements
        if tier == "core":
            config.setdefault("sprint_planning", {}).setdefault("team", {})["capacity"] = "20 points"
        elif tier == "advanced":
            config.setdefault("ai_agents", {})["system_prompt"] = "Test prompt"

        errors = validator.validate_tier_requirements(config)
        assert len(errors) == 0, f"Tier {tier} validation failed: {errors}"

def test_config_cross_field_validation(validator):
    """Test validation of relationships between config fields."""
    # Test cascade feature with custom tier
    config = {
        "project": {"name": "Test", "author": "Tester"},
        "tier": "custom",
        "features": {"cascade": True},
        "templates": {"core": {"prd": True}}
    }

    errors = validator.validate_cross_field_rules(config)
    # Should pass if cascade is allowed in custom tier
    assert len(errors) == 0

    # Test conflicting settings
    config["templates"]["core"] = {}  # No templates selected
    errors = validator.validate_cross_field_rules(config)
    assert len(errors) > 0  # Should require at least one template
```

### Configuration Migration Tests

```python
def test_config_migration_from_v1_to_v2():
    """Test configuration migration between versions."""
    v1_config = {
        "project": {"name": "Test", "author": "Tester"},
        "tier": "minimal",
        "enable_cascade": True  # Old field name
    }

    migrated_config = migrate_config(v1_config, from_version="1.0", to_version="2.0")

    # Should rename fields
    assert "enable_cascade" not in migrated_config
    assert migrated_config["features"]["cascade"] == True

    # Should add new required fields with defaults
    assert "version" in migrated_config.get("project", {})

def test_config_backward_compatibility():
    """Test that old configs still work."""
    old_config = {
        "project": {"name": "Test", "author": "Tester"},
        "tier": "minimal"
        # Missing new fields that have defaults
    }

    # Should process without errors
    processor = TemplateProcessor(Path("."))
    content = processor.process_template("prd-template", old_config)
    assert content is not None
    assert "Test" in content
```

## Test Automation

### Test Fixtures

```python
# conftest.py
@pytest.fixture
def template_processor(tmp_path):
    """Create a template processor for testing."""
    # Create minimal template structure
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    source_dir = templates_dir / "source"
    source_dir.mkdir()

    # Create a simple test template
    test_template = source_dir / "test-template.md"
    test_template.write_text("# Test Template\n\nProject: {{ project.name }}")

    return TemplateProcessor(tmp_path)

@pytest.fixture
def minimal_config():
    """Minimal valid configuration."""
    return {
        "project": {
            "name": "Test Project",
            "author": "Test Author",
            "version": "1.0.0"
        },
        "tier": "minimal",
        "features": {"cascade": False}
    }

@pytest.fixture
def core_config():
    """Core tier configuration."""
    return {
        "project": {
            "name": "Test Project",
            "author": "Test Author",
            "version": "1.0.0"
        },
        "tier": "core",
        "features": {"cascade": True},
        "sprint_planning": {
            "team": {"capacity": "20 story points"}
        },
        "development_guide": {
            "git": {"branching_strategy": "GitFlow"}
        }
    }
```

### Test Utilities

```python
# tests/utils/template_utils.py
def create_test_template(name: str, content: str, tmp_path: Path) -> Path:
    """Create a test template file."""
    template_dir = tmp_path / "templates" / "source"
    template_dir.mkdir(parents=True, exist_ok=True)

    template_file = template_dir / f"{name}.md"
    template_file.write_text(content)

    return template_file

def render_template_string(processor: TemplateProcessor, template_str: str, config: dict) -> str:
    """Render a template string directly."""
    from jinja2 import Template
    template = Template(template_str)
    return template.render(**config)

# tests/utils/config_utils.py
def create_minimal_config(**overrides) -> dict:
    """Create a minimal valid configuration."""
    config = {
        "project": {
            "name": "Test Project",
            "author": "Test Author"
        },
        "tier": "minimal",
        "features": {"cascade": False}
    }
    config.update(overrides)
    return config

def validate_config_silent(config: dict) -> list:
    """Validate config and return errors without raising."""
    try:
        from stable_flow.config_validator import ConfigValidator
        validator = ConfigValidator()
        return validator.validate(config)
    except Exception as e:
        return [str(e)]
```

### Test Data Management

```python
# tests/fixtures/configs/core_config.yaml
project:
  name: "Core Test Project"
  author: "Test Author"
  version: "1.0.0"
  created: "2024-12-09"

tier: "core"

features:
  cascade: true

sections:
  prd:
    competitive_analysis: true
    user_experience: true
  technical_design:
    security_detailed: true

sprint_planning:
  team:
    capacity: "25 story points"
    velocity: "22 points/sprint"
    ai_velocity: "28 points/sprint"
    velocity_multiplier: "1.27x"
    members: "Alice, Bob, Carol"

development_guide:
  git:
    branching_strategy: "GitFlow"
    commit_convention: "Conventional commits"
```

## Continuous Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Run tests
      run: |
        python -m pytest tests/ --cov=stable_flow --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  lint:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install linting tools
      run: |
        pip install flake8 black mypy

    - name: Run linters
      run: |
        flake8 stable_flow tests
        black --check stable_flow tests
        mypy stable_flow
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
```

### Test Coverage Requirements

```python
# setup.cfg or pyproject.toml
[tool:coverage:run]
source = stable_flow
omit =
    */tests/*
    */venv/*
    setup.py

[tool:coverage:report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

[tool:coverage:html]
directory = htmlcov
```

### Performance Benchmarks

```python
# tests/test_performance.py
def test_processing_benchmarks(benchmark, template_processor, large_config):
    """Benchmark template processing performance."""

    def process_templates():
        templates = template_processor._get_templates_for_tier(large_config)
        for template in templates:
            content = template_processor.process_template(template, large_config)
            assert content is not None

    # Run benchmark
    result = benchmark(process_templates)

    # Assert reasonable performance
    assert result.stats.mean < 10.0  # Average < 10 seconds
    assert result.stats.max < 15.0   # Max < 15 seconds
```

This comprehensive testing guide ensures Stable Flow maintains high quality and reliability. The testing strategy covers all aspects of the system from unit tests to end-to-end workflows, with automated CI/CD integration for continuous quality assurance. 🚀</content>
</xai:function_call name="write">
<parameter name="file_path">docs/troubleshooting.md

