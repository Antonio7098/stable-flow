# Stable Flow Troubleshooting Guide

This guide helps you diagnose and resolve common issues when using Stable Flow. Start with the quick solutions, then move to detailed troubleshooting if needed.

## Table of Contents

- [Quick Solutions](#quick-solutions)
- [Installation Issues](#installation-issues)
- [Configuration Problems](#configuration-problems)
- [Template Errors](#template-errors)
- [Generation Failures](#generation-failures)
- [Performance Issues](#performance-issues)
- [CLI Problems](#cli-problems)
- [Advanced Debugging](#advanced-debugging)

## Quick Solutions

### "Command not found" or "Module not found"
```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Verify installation
python -c "import stable_flow; print('Stable Flow installed')"
```

### "Configuration validation failed"
```bash
# Validate your config
python scripts/process_templates.py --config config.yaml --validate-only

# Check for common issues:
# - Missing required fields (project.name, project.author, tier)
# - Invalid tier value (must be: minimal, core, advanced, custom)
# - Malformed YAML syntax
```

### "Template not found" errors
```bash
# Check template directory structure
ls -la templates/source/

# Verify template files exist
ls templates/source/*.md

# Check file permissions
chmod +r templates/source/*.md
```

### Generated documents are empty or malformed
```bash
# Check configuration syntax
python -m py_compile your-config.yaml

# Verify template syntax
python scripts/process_templates.py --config config.yaml --validate-templates

# Try with minimal config first
cp examples/minimal-project-config.yaml test-config.yaml
python scripts/process_templates.py --config test-config.yaml
```

## Installation Issues

### Python Version Compatibility

**Problem**: Import errors or syntax errors
```
ModuleNotFoundError: No module named 'stable_flow'
```

**Solutions**:
```bash
# Check Python version (requires 3.8+)
python --version

# Install correct Python version
# On Ubuntu/Debian:
sudo apt install python3.9 python3.9-venv

# On macOS:
brew install python@3.9

# On Windows:
# Download from python.org

# Create fresh virtual environment
python3.9 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Dependency Installation Failures

**Problem**: Pip install fails with dependency conflicts
```
ERROR: Cannot install stable-flow because these package versions have conflicting dependencies
```

**Solutions**:
```bash
# Update pip
pip install --upgrade pip

# Install in isolated environment
python -m venv --clear venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt

# Check for conflicting packages
pip check

# Use specific versions if needed
pip install Jinja2==3.1.2 PyYAML==6.0 Click==8.1.3 Rich==13.3.5
```

### Permission Errors

**Problem**: Permission denied when installing
```
PermissionError: [Errno 13] Permission denied
```

**Solutions**:
```bash
# Don't use sudo with pip
# sudo pip install ...  # WRONG

# Use virtual environment instead
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Or install to user directory
pip install --user -r requirements.txt

# On Linux/macOS, fix permissions if needed
chmod +x scripts/*.py
```

## Configuration Problems

### YAML Syntax Errors

**Problem**: Configuration file has invalid YAML syntax
```
yaml.scanner.ScannerError: while scanning a simple key
```

**Solutions**:
```yaml
# Check YAML syntax online: https://yaml-online-parser.appspot.com/

# Common mistakes:
# Wrong indentation (use spaces, not tabs)
project:
  name: "My Project"    # Correct
  name: "My Project"    # Wrong (inconsistent indentation)

# Missing quotes around strings with special characters
name: "Project: My App"  # Correct
name: Project: My App    # Wrong (colon interpreted as mapping)

# Incorrect boolean values
cascade: true   # Correct
cascade: True   # Wrong (should be lowercase)
cascade: yes    # Wrong (use true/false)
```

### Missing Required Fields

**Problem**: Configuration missing required fields
```
Configuration validation failed:
- Missing required field: project.name
- Missing required field: project.author
```

**Required fields by tier**:
```yaml
# All tiers require:
project:
  name: "string"      # Required
  author: "string"    # Required
tier: "minimal|core|advanced|custom"  # Required

# Core tier additionally requires:
sprint_planning:
  team:
    capacity: "string"  # Required

# Advanced tier additionally requires:
ai_agents:
  system_prompt: "string"  # Required
```

### Invalid Tier Configuration

**Problem**: Tier-specific validation fails
```
Configuration validation failed:
- Core tier requires sprint_planning.team.capacity
```

**Tier requirements**:
```yaml
# Minimal: No additional requirements
tier: "minimal"

# Core: Requires team capacity
tier: "core"
sprint_planning:
  team:
    capacity: "20 story points per sprint"

# Advanced: Requires AI prompt
tier: "advanced"
ai_agents:
  system_prompt: "You are a senior software architect..."
```

### Cross-Field Validation Errors

**Problem**: Configuration has conflicting or invalid field relationships
```
Configuration validation failed:
- Custom tier requires at least one template to be enabled
```

**Common validation rules**:
```yaml
# Custom tier must enable at least one core template
tier: "custom"
templates:
  core:
    prd: true  # At least one must be true

# Cascade feature requires compatible tier
tier: "minimal"  # Cascade not available in minimal
features:
  cascade: false  # Must be false

# Section flags must be valid for tier
tier: "minimal"
sections:
  prd:
    competitive_analysis: false  # Must be false for minimal tier
```

## Template Errors

### Template Not Found

**Problem**: Template file cannot be located
```
TemplateNotFound: No template found for prd-template
```

**Solutions**:
```bash
# Check template directory structure
find . -name "*template*" -type f

# Verify templates/source/ directory exists
ls -la templates/source/

# Check for correct file extensions (.md or .csv)
ls templates/source/*.md
ls templates/source/*.csv

# Verify file permissions
ls -l templates/source/prd-template.md
```

### Template Syntax Errors

**Problem**: Jinja2 template has syntax errors
```
TemplateSyntaxError: unexpected end of template
```

**Common syntax errors**:
```jinja2
{# Missing endfor #}
{% for item in items %}
{{ item }}
{% endfor %}  {# This is missing #}

{# Incorrect conditional syntax #}
{% if condition %}  {# Correct #}
{% if condition %]  {# Wrong - should be %} #}

{# Unclosed tags #}
{% macro my_macro() %}  {# Missing endmacro #}
```

**Debug template syntax**:
```bash
# Validate template syntax
python -c "
from jinja2 import Template
with open('templates/source/prd-template.md', 'r') as f:
    try:
        Template(f.read())
        print('Template syntax is valid')
    except Exception as e:
        print(f'Template syntax error: {e}')
"
```

### Variable Resolution Errors

**Problem**: Template variables not resolving correctly
```
UndefinedError: 'project' is undefined
```

**Solutions**:
```jinja2
{# Use default filters for safety #}
{{ project.name | default('Unknown Project') }}
{{ project.author | default('Unknown Author') }}

{# Check variable existence #}
{% if project %}
Project: {{ project.name }}
{% endif %}

{# Debug variables #}
{# Debug: {{ config | tojson(indent=2) }} #}
```

**Common variable issues**:
```yaml
# Configuration missing nested objects
project:
  name: "Test"  # Missing other required fields

# Should be:
project:
  name: "Test"
  author: "Tester"
  version: "1.0.0"
```

### Filter Errors

**Problem**: Custom filters not working
```
Filter 'strftime' is not defined
```

**Solutions**:
```python
# Check filter registration in TemplateProcessor
def _get_custom_filters(self):
    return {
        'strftime': self._strftime_filter,
        'markdown_escape': self._markdown_escape_filter,
        # Add missing filters here
    }

# Test filter functionality
python -c "
from stable_flow.template_processor import TemplateProcessor
from pathlib import Path
processor = TemplateProcessor(Path('.'))
template = processor.jinja_env.from_string('{{ \"2024-01-01\" | strftime(\"%B %d, %Y\") }}')
print(template.render())
"
```

## Generation Failures

### Process Crashes

**Problem**: Generation process crashes with exceptions
```
Traceback (most recent call last):
  File "scripts/process_templates.py", line 42, in generate_documents
    raise TemplateError(f"Processing failed: {e}")
```

**Debug steps**:
```bash
# Enable verbose logging
export PYTHONPATH=.
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
from stable_flow.template_processor import TemplateProcessor
# Add your debugging code here
"

# Test with minimal config first
python scripts/process_templates.py --config examples/minimal-project-config.yaml --verbose

# Check system resources
df -h  # Disk space
free -h  # Memory (Linux)
vm_stat  # Memory (macOS)
```

### Output File Issues

**Problem**: Output files not created or corrupted
```
FileNotFoundError: [Errno 2] No such file or directory: 'docs/prd-template.md'
```

**Solutions**:
```bash
# Create output directory
mkdir -p docs

# Check write permissions
touch docs/test.txt  # Should work
rm docs/test.txt

# Check disk space
df -h .

# Use absolute paths if needed
python scripts/process_templates.py --config config.yaml --output /tmp/stable-flow-output
```

### Memory Issues

**Problem**: Process runs out of memory with large configurations
```
MemoryError: Unable to allocate memory
```

**Solutions**:
```python
# Process templates individually
templates = ['prd-template', 'technical-design-template']  # etc.
for template in templates:
    subprocess.run([
        'python', 'scripts/process_templates.py',
        '--config', 'config.yaml',
        '--template', template
    ])

# Increase system memory limits (if possible)
# Or use smaller batch sizes in configuration
```

## Performance Issues

### Slow Template Processing

**Problem**: Document generation takes too long
```
Processing 10 templates took 120 seconds
```

**Performance optimizations**:
```python
# Enable template caching
class TemplateProcessor:
    def __init__(self, use_cache=True):
        self.use_cache = use_cache
        self._template_cache = {}

# Profile performance
import cProfile
cProfile.run('processor.generate_documents(config)', 'profile_output.prof')

# Analyze profile
python -m pstats profile_output.prof
# sort cumulative
# stats 10
```

### Large File Handling

**Problem**: Very large generated documents cause issues

**Solutions**:
```python
# Split large templates into smaller ones
# Use include statements
{% include "sections/header.md" %}
{% include "sections/content.md" %}

# Stream processing for very large outputs
with open(output_path, 'w') as f:
    # Write in chunks instead of all at once
    for chunk in generate_chunks(template, config):
        f.write(chunk)
```

## CLI Problems

### Command Line Argument Errors

**Problem**: CLI arguments not recognized
```
Error: No such option: --config
```

**Solutions**:
```bash
# Check CLI help
python scripts/process_templates.py --help

# Verify script is executable
ls -la scripts/process_templates.py

# Use correct Python interpreter
python3 scripts/process_templates.py --help

# Check for typos in arguments
python scripts/process_templates.py --config=config.yaml  # Correct
python scripts/process_templates.py --config config.yaml  # Also correct
```

### Path Resolution Issues

**Problem**: File paths not resolved correctly
```
FileNotFoundError: [Errno 2] No such file or directory: 'config.yaml'
```

**Solutions**:
```bash
# Use absolute paths
python scripts/process_templates.py --config /full/path/to/config.yaml

# Check current working directory
pwd

# Use relative paths from project root
cd /path/to/stable-flow
python scripts/process_templates.py --config examples/minimal-project-config.yaml

# Verify file exists
ls -la config.yaml
```

### Encoding Issues

**Problem**: Unicode characters in templates cause encoding errors
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff
```

**Solutions**:
```python
# Ensure all files are UTF-8 encoded
file -i templates/source/*.md

# Convert files to UTF-8
iconv -f latin1 -t utf8 input.md > output.md

# Force UTF-8 in Python
with open('template.md', 'r', encoding='utf-8') as f:
    content = f.read()
```

## Advanced Debugging

### Debug Logging

Enable detailed logging:
```python
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

# Enable in TemplateProcessor
class TemplateProcessor:
    def __init__(self, debug=False):
        self.debug = debug
        if debug:
            logging.getLogger().setLevel(logging.DEBUG)
```

### Template Debugging

Add debug information to templates:
```jinja2
{# Debug configuration #}
{% if debug %}
## Debug Information
```yaml
{{ config | tojson(indent=2) }}
```
{% endif %}

{# Debug variables #}
{% macro debug_var(name, value) -%}
{% if debug %}
**{{ name }}**: {{ value }}
{% endif %}
{% endmacro %}

{{ debug_var('project_name', project.name) }}
```

### Configuration Debugging

```python
# Validate configuration step by step
def debug_config_validation(config_path):
    """Debug configuration validation process."""
    import yaml

    # Load config
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    print("Loaded configuration:")
    print(yaml.dump(config, indent=2))

    # Test validation
    from stable_flow.config_validator import ConfigValidator
    validator = ConfigValidator()

    errors = validator.validate(config)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Configuration is valid")

# Run debug
debug_config_validation('config.yaml')
```

### Performance Profiling

```python
import cProfile
import pstats
from io import StringIO

def profile_template_processing():
    """Profile template processing performance."""
    pr = cProfile.Profile()
    pr.enable()

    # Your processing code here
    processor = TemplateProcessor(Path('.'))
    processor.generate_documents(config)

    pr.disable()

    # Print results
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

profile_template_processing()
```

### Memory Profiling

```python
# Install memory profiler
pip install memory-profiler

# Add decorator to functions
from memory_profiler import profile

class TemplateProcessor:
    @profile
    def process_template(self, template_name: str, config: Dict[str, Any]):
        # Processing code...

# Run with memory profiling
python -m memory_profiler scripts/process_templates.py --config config.yaml
```

### Interactive Debugging

```python
# Add breakpoint for debugging
import pdb

class TemplateProcessor:
    def process_template(self, template_name: str, config: Dict[str, Any]):
        if self.debug and template_name == 'problem-template':
            pdb.set_trace()  # Breakpoint here

        # Rest of processing...

# Run with debugging
python -c "
import sys
sys.path.insert(0, '.')
from stable_flow.template_processor import TemplateProcessor
processor = TemplateProcessor(debug=True)
processor.generate_documents(config)
"
```

### Common Debug Commands

```bash
# Check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Check installed packages
pip list | grep -E "(Jinja2|PyYAML|Click|Rich)"

# Check file encodings
file -i config.yaml templates/source/*.md

# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('config.yaml'))"

# Test template syntax
python -c "
from jinja2 import Template
with open('templates/source/prd-template.md') as f:
    Template(f.read())
print('Template syntax OK')
"

# Check system resources
df -h      # Disk space
free -h    # Memory (Linux)
vm_stat    # Memory (macOS)
top -p $$  # Process monitor
```

### Getting Help

If you can't resolve an issue:

1. **Check existing issues**: Search GitHub issues
2. **Collect debug information**:
   ```bash
   # System information
   python --version
   pip list
   uname -a

   # Error details
   python scripts/process_templates.py --config config.yaml --verbose 2>&1 | tee error.log
   ```

3. **Create a minimal reproduction case**:
   ```bash
   # Copy minimal working example
   cp examples/minimal-project-config.yaml test-config.yaml

   # Modify until it breaks
   # Then share the minimal failing config
   ```

4. **File a bug report** with:
   - Stable Flow version
   - Python version
   - Operating system
   - Full error traceback
   - Minimal config to reproduce
   - Expected vs actual behavior

This troubleshooting guide covers the most common issues and provides systematic approaches to diagnose and resolve problems. Start with the quick solutions, then work through the detailed sections as needed. 🚀</content>
</xai:function_call">Now let me create a comprehensive README.md file to replace the basic one currently in the repository.</content>
</xai:function_call name="write">
<parameter name="file_path">README.md

