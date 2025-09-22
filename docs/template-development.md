# Stable Flow Template Development Guide

This guide is for developers who want to create or modify document templates in Stable Flow. It covers template architecture, Jinja2 patterns, configuration integration, and best practices.

## Table of Contents

- [Template Architecture](#template-architecture)
- [Jinja2 Fundamentals](#jinja2-fundamentals)
- [Configuration Integration](#configuration-integration)
- [Template Patterns](#template-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Testing Templates](#testing-templates)
- [Template Maintenance](#template-maintenance)

## Template Architecture

### Template Hierarchy

Stable Flow uses a hierarchical template system:

```
templates/
├── source/                    # Main template sources
│   ├── prd-template.md        # Product Requirements Document
│   ├── technical-design-template.md
│   ├── features-csv-template.csv
│   ├── development-guide-template.md
│   ├── sprint-planning-template.md
│   ├── sprint-template.md
│   └── master-index-template.md
├── advanced/                  # Advanced/specialized templates
│   ├── adr-template.md       # Architecture Decision Records
│   ├── performance-tracker.md
│   ├── scrum-master-guide.md
│   └── *.md
├── config/                    # Configuration templates
│   └── project-config-template.yaml
└── operations/                # Operations templates
    ├── incident-response.md
    └── data-migration.md
```

### Template Types

#### Core Templates
- **prd-template.md**: Product requirements and features
- **technical-design-template.md**: Architecture and technical decisions
- **features-csv-template.md**: Feature tracking spreadsheet
- **development-guide-template.md**: Coding standards and processes

#### Planning Templates
- **sprint-planning-template.md**: Multi-sprint roadmap and planning
- **sprint-template.md**: Individual sprint execution and tracking

#### Advanced Templates
- **master-index-template.md**: Documentation hub and cross-references
- **adr-template.md**: Architecture decision records
- **performance-tracker.md**: Performance monitoring and optimization
- **security-audit.md**: Security compliance tracking

### Template Structure

Each template follows a consistent structure:

```markdown
# {{ project.name }} - [Document Type]

## Document Information
- **Version**: {{ version }}
- **Last Updated**: {{ last_updated }}
- **Author**: {{ project.author }}

## [Section 1]
Content for section 1...

{% if sections.template_name.section_flag %}
## [Conditional Section]
Content that appears when section is enabled...
{% endif %}

## References
{% for reference in references %}
- {{ reference }}
{% endfor %}
```

## Jinja2 Fundamentals

### Basic Syntax

#### Variables
```jinja2
{{ project.name }}              # Simple variable
{{ project.author | default('Unknown') }}  # With default filter
{{ technical_design.version | default('1.0') }}  # Nested access
```

#### Conditionals
```jinja2
{% if sections.prd.competitive_analysis %}
## Competitive Analysis
Content here...
{% endif %}

{% if tier == 'advanced' %}
## Advanced Features
Special content for advanced tier...
{% endif %}
```

#### Loops
```jinja2
{% for feature in features_list %}
- **{{ feature.name }}**: {{ feature.description }}
{% endfor %}

{% for competitor in prd.competitors %}
### {{ competitor.name }}
- **Strengths**: {{ competitor.strengths | join(', ') }}
- **Weaknesses**: {{ competitor.weaknesses | join(', ') }}
{% endfor %}
```

### Filters

Stable Flow provides custom filters:

#### Built-in Filters
```jinja2
{{ "hello world" | title }}              # Hello World
{{ ["a", "b", "c"] | join(", ") }}       # a, b, c
{{ 123.456 | round(2) }}                # 123.46
{{ "now" | strftime("%Y-%m-%d") }}       # Current date
```

#### Custom Filters
```jinja2
{{ date_string | strftime("%B %d, %Y") }}  # Format dates
{{ items | length }}                       # Count items
{{ text | wordwrap(80) }}                  # Wrap text
```

### Macros and Includes

#### Template Macros
```jinja2
{% macro section_header(title, level=2) -%}
{% set hashes = "#" * level %}
{{ hashes }} {{ title }}
{% endmacro %}

{# Usage #}
{{ section_header("Architecture Overview") }}
{{ section_header("Detailed Design", 3) }}
```

#### Template Includes
```jinja2
{% include "common/footer.md" %}
{% include "sections/security-details.md" %}
```

### Template Inheritance

```jinja2
{# base-template.md #}
# {{ project.name }} - {{ document_type }}

{% block document_info %}
## Document Information
- **Version**: {{ version }}
- **Author**: {{ project.author }}
{% endblock %}

{% block content %}
{# Main content goes here #}
{% endblock %}

{% block references %}
## References
{% for ref in references %}
- {{ ref }}
{% endfor %}
{% endblock %}
```

```jinja2
{# child-template.md #}
{% extends "base-template.md" %}

{% block document_info %}
{{ super() }}
- **Last Updated**: {{ last_updated }}
{% endblock %}

{% block content %}
## Specific Content
This content is specific to this template...
{% endblock %}
```

## Configuration Integration

### Accessing Configuration Data

Templates access configuration through global variables:

```jinja2
{# Project information #}
{{ project.name }}
{{ project.description }}
{{ project.author }}
{{ project.version }}

{# Feature flags #}
{% if features.cascade %}
Cascade updates are enabled.
{% endif %}

{# Section controls #}
{% if sections.prd.competitive_analysis %}
## Competitive Analysis
{{ prd.competitors | tojson(indent=2) }}
{% endif %}

{# Template-specific data #}
{{ technical_design.system_purpose }}
{{ sprint_planning.team.capacity }}
```

### Configuration Structure

Configuration is organized hierarchically:

```yaml
project:           # Project metadata
  name: "string"
  author: "string"

tier: "string"     # minimal | core | advanced | custom

features:          # Global feature flags
  cascade: boolean

sections:          # Section enable/disable flags
  prd:
    competitive_analysis: boolean
  technical_design:
    security_detailed: boolean

templates:         # Template selection
  core:
    prd: boolean
  advanced:
    adr: boolean

# Document-specific data
prd: {...}
technical_design: {...}
sprint_planning: {...}
```

### Conditional Logic Patterns

#### Tier-Based Conditions
```jinja2
{% if tier == 'minimal' %}
This content only appears in minimal tier.
{% elif tier == 'core' %}
This content appears in core and advanced tiers.
{% else %}
This content appears in all tiers.
{% endif %}
```

#### Feature-Based Conditions
```jinja2
{% if features.cascade %}
## Cascade Updates
When enabled, changes to features automatically update related documents.
{% endif %}
```

#### Section-Based Conditions
```jinja2
{% if sections.technical_design.accessibility %}
## Accessibility Requirements
- WCAG 2.2 AA compliance
- Screen reader support
- Keyboard navigation
{% endif %}
```

## Template Patterns

### Document Header Pattern

```jinja2
# {{ project.name }} - {{ document_type | title }}

## Document Information
- **Version**: {{ version | default('1.0.0') }}
- **Last Updated**: {{ last_updated | default('now' | strftime('%Y-%m-%d')) }}
- **Author**: {{ project.author }}
- **Tier**: {{ tier | title }}
{% if features.cascade %}
- **Cascade Updates**: Enabled
{% endif %}

## Executive Summary
{{ summary | default('Brief overview of the ' + document_type) }}
```

### Section Pattern

```jinja2
{% macro section(title, content, required=false) -%}
{% if content or required %}
## {{ title }}

{% if content %}
{{ content }}
{% else %}
*Content for {{ title | lower }} goes here...*
{% endif %}
{% endif %}
{% endmacro %}

{{ section("Architecture Overview", technical_design.architecture_diagram, true) }}
{{ section("Security Design", technical_design.security_details) }}
```

### List Generation Pattern

```jinja2
{% macro item_list(items, title, empty_message="No items defined") -%}
{% if items %}
### {{ title }}
{% for item in items %}
- **{{ item.name }}**: {{ item.description }}
  {% if item.details %}- *{{ item.details }}*{% endif %}
{% endfor %}
{% else %}
### {{ title }}
*{{ empty_message }}*
{% endif %}
{% endmacro %}

{{ item_list(technical_design.components, "System Components") }}
{{ item_list(features_list, "Planned Features", "No features defined yet") }}
```

### Table Generation Pattern

```jinja2
{% macro feature_table(features) -%}
| Feature | Priority | Status | Description |
|---------|----------|--------|-------------|
{% for feature in features %}
| {{ feature.name }} | {{ feature.priority }} | {{ feature.status }} | {{ feature.description }} |
{% endfor %}
{% endmacro %}

### Feature Overview
{{ feature_table(features_list) }}
```

### Mermaid Diagram Pattern

```jinja2
{% macro mermaid_diagram(content, title="") -%}
{% if title %}
### {{ title }}
{% endif %}
```mermaid
{{ content | trim }}
```
{% endmacro %}

{{ mermaid_diagram(technical_design.architecture_diagram, "System Architecture") }}
```

## Advanced Techniques

### Dynamic Content Generation

```jinja2
{% set sections = [] %}
{% if sections.prd.competitive_analysis %}{% do sections.append('competitive_analysis') %}{% endif %}
{% if sections.prd.user_experience %}{% do sections.append('user_experience') %}{% endif %}

## Table of Contents
{% for section in sections %}
- [{{ section | title | replace('_', ' ') }}](#{{ section | lower | replace(' ', '-') }})
{% endfor %}

{% for section in sections %}
## {{ section | title | replace('_', ' ') }}

{% if section == 'competitive_analysis' %}
Content for competitive analysis...
{% elif section == 'user_experience' %}
Content for user experience...
{% endif %}
{% endfor %}
```

### Template Variables and Context

```jinja2
{% set context = {
  'tier_name': tier | title,
  'has_features': features_list | length > 0,
  'total_features': features_list | length,
  'completion_percentage': (features_list | selectattr('status', 'equalto', 'Completed') | list | length / features_list | length * 100) | round(1) if features_list else 0
} %}

## Project Status
- **Tier**: {{ context.tier_name }}
- **Features**: {{ context.total_features }}
- **Completion**: {{ context.completion_percentage }}%
```

### Error Handling in Templates

```jinja2
{% macro safe_get(obj, key, default='') -%}
{% if obj and key in obj %}{{ obj[key] }}{% else %}{{ default }}{% endif %}
{% endmacro %}

{% set system_purpose = safe_get(technical_design, 'system_purpose', 'System purpose not defined') %}
{% set team_size = safe_get(sprint_planning, 'team.members', 'Team size not specified') | length %}
```

### Template Testing Helpers

```jinja2
{% macro assert(condition, message) -%}
{% if not condition %}
{{ "TEMPLATE ERROR: " + message }}
{% endif %}
{% endmacro %}

{{ assert(project.name, "Project name is required") }}
{{ assert(tier in ['minimal', 'core', 'advanced', 'custom'], "Invalid tier: " + tier) }}
```

## Testing Templates

### Template Unit Tests

```python
def test_template_renders_without_errors(template_processor, core_config):
    """Test that template renders without throwing exceptions."""
    content = template_processor.process_template('prd-template', core_config)
    assert content is not None
    assert len(content) > 0

def test_template_includes_required_sections(template_processor, core_config):
    """Test that template includes all required sections."""
    content = template_processor.process_template('prd-template', core_config)

    # Check for required headers
    assert '# Product Requirements Document' in content
    assert '## Document Information' in content
    assert '## Executive Summary' in content

def test_template_handles_missing_data(template_processor, minimal_config):
    """Test that template gracefully handles missing optional data."""
    content = template_processor.process_template('technical-design-template', minimal_config)

    # Should still render even with missing data
    assert content is not None
    assert 'Technical Design Document' in content
```

### Template Integration Tests

```python
def test_template_integration_with_config_validation(template_processor, valid_config):
    """Test template works with validated configuration."""
    # Process all core templates
    templates = ['prd-template', 'technical-design-template', 'features-csv-template']

    for template_name in templates:
        content = template_processor.process_template(template_name, valid_config)
        assert content is not None, f"Failed to process {template_name}"

        # Verify project name appears
        assert valid_config['project']['name'] in content

def test_template_conditional_sections(template_processor, core_config):
    """Test that conditional sections appear/disappear based on config."""
    # Test with section enabled
    core_config['sections']['prd']['competitive_analysis'] = True
    content = template_processor.process_template('prd-template', core_config)
    assert '## Competitive Analysis' in content

    # Test with section disabled
    core_config['sections']['prd']['competitive_analysis'] = False
    content = template_processor.process_template('prd-template', core_config)
    assert '## Competitive Analysis' not in content
```

### Template Content Validation

```python
def test_template_content_quality(template_processor, core_config):
    """Test that generated content meets quality standards."""
    content = template_processor.process_template('prd-template', core_config)

    # Check for basic formatting
    assert content.startswith('# ')
    assert '##' in content  # Has subsections

    # Check for project-specific content
    assert core_config['project']['name'] in content
    assert core_config['project']['author'] in content

    # Check for no template artifacts
    assert '{{' not in content  # No unprocessed variables
    assert '{%' not in content  # No unprocessed tags

def test_template_markdown_validity(template_processor, core_config):
    """Test that generated markdown is valid."""
    content = template_processor.process_template('prd-template', core_config)

    lines = content.split('\n')

    # Check header hierarchy
    headers = [line for line in lines if line.startswith('#')]
    for i in range(len(headers) - 1):
        current_level = len(headers[i]) - headers[i].lstrip('#').find(' ') - 1
        next_level = len(headers[i + 1]) - headers[i + 1].lstrip('#').find(' ') - 1
        assert next_level <= current_level + 1, f"Header level jump: {headers[i]} -> {headers[i+1]}"
```

## Template Maintenance

### Version Control for Templates

```bash
# Template versioning strategy
git tag template-v1.0.0  # Tag template versions
git branch template/feature/new-section  # Feature branches for templates

# Template change tracking
git log --oneline templates/source/  # See template history
```

### Template Documentation

Each template should include:

```jinja2
{#
Template: prd-template.md
Purpose: Generate Product Requirements Document
Configuration: prd.* data structure
Sections: Controlled by sections.prd.* flags
Dependencies: project.*, features.*, sections.prd.*
Version: 1.0.0
Last Updated: 2024-12-09
Author: Template Team
#}
```

### Template Metrics and Monitoring

```python
def analyze_template_complexity(template_path):
    """Analyze template complexity metrics."""
    with open(template_path, 'r') as f:
        content = f.read()

    # Count template elements
    variables = content.count('{{')
    conditionals = content.count('{% if ')
    loops = content.count('{% for ')
    macros = content.count('{% macro ')

    return {
        'variables': variables,
        'conditionals': conditionals,
        'loops': loops,
        'macros': macros,
        'total_complexity': variables + conditionals + loops + macros
    }

def validate_template_syntax(template_path):
    """Validate template syntax."""
    from jinja2 import Template, TemplateSyntaxError

    try:
        with open(template_path, 'r') as f:
            Template(f.read())
        return True, None
    except TemplateSyntaxError as e:
        return False, str(e)
```

### Template Performance Optimization

```jinja2
{# Avoid expensive operations in loops #}
{% set feature_count = features | length %}
{% for feature in features %}
### Feature {{ loop.index }} of {{ feature_count }}
{{ feature.name }}
{% endfor %}

{# Cache expensive computations #}
{% set formatted_date = 'now' | strftime('%Y-%m-%d') %}
{% set project_title = project.name | title %}

{# Use macros for repeated patterns #}
{% macro status_badge(status) -%}
{% if status == 'Completed' %}✅{% elif status == 'In Progress' %}🔄{% else %}⏳{% endif %}
{% endmacro %}

Status: {{ status_badge(feature.status) }} {{ feature.status }}
```

### Template Update Strategy

1. **Backward Compatibility**: Ensure template changes don't break existing configs
2. **Migration Path**: Provide migration guides for breaking changes
3. **Deprecation Warnings**: Warn about deprecated template features
4. **Version Pinning**: Allow users to pin to specific template versions

### Template Contribution Guidelines

#### Adding New Templates

1. **Define Purpose**: Clearly document what the template generates
2. **Configuration Schema**: Define required configuration structure
3. **Default Values**: Provide sensible defaults for optional fields
4. **Validation**: Add configuration validation rules
5. **Testing**: Include comprehensive test coverage
6. **Documentation**: Create user documentation and examples

#### Modifying Existing Templates

1. **Impact Assessment**: Evaluate impact on existing users
2. **Backward Compatibility**: Maintain compatibility with existing configs
3. **Migration Support**: Provide migration utilities if needed
4. **Version Bumping**: Update version numbers appropriately
5. **Changelog**: Document changes in changelog

### Template Best Practices

#### Code Quality
- Use consistent indentation and formatting
- Add comments for complex logic
- Use descriptive variable names
- Follow Jinja2 best practices

#### Performance
- Minimize expensive operations
- Cache repeated computations
- Use efficient loops and conditionals
- Avoid deep nesting

#### Maintainability
- Keep templates focused on single responsibility
- Use includes for shared components
- Document template purpose and usage
- Version control template changes

#### User Experience
- Provide clear error messages
- Handle missing data gracefully
- Use consistent formatting
- Make templates self-documenting

This guide provides the foundation for creating and maintaining high-quality templates in Stable Flow. Remember: templates are the core of the user experience, so focus on clarity, reliability, and extensibility! 🚀</content>
</xai:function_call name="write">
<parameter name="file_path">docs/process-engine.md

