# Stable Flow Examples

This directory contains example project configurations demonstrating different tiers of the Stable Flow documentation system.

## Available Examples

### Minimal Tier
- **Configuration**: `minimal-project-config.yaml`
- **Description**: Simplest possible configuration with only essential documents
- **Templates**: PRD, Technical Design, Features CSV
- **Use Case**: Solo developers, simple projects, proof of concepts

### Core Tier
- **Configuration**: `core-project-config.yaml`
- **Description**: Standard project configuration with comprehensive documentation
- **Templates**: PRD, Technical Design, Features CSV, Development Guide, Sprint Planning, Sprint Template
- **Use Case**: Small to medium teams, standard software projects

### Advanced Tier
- **Configuration**: `advanced-project-config.yaml` (coming soon)
- **Description**: Enterprise-grade configuration with all advanced features
- **Templates**: All core templates plus Master Index, ADR, and advanced trackers
- **Use Case**: Large teams, enterprise projects, complex systems

### Custom Tier
- **Configuration**: `custom-project-config.yaml` (coming soon)
- **Description**: Fully customizable configuration with granular control
- **Templates**: User-defined selection of any available templates
- **Use Case**: Specialized projects, unique requirements, experimental setups

## How to Use Examples

1. **Copy a configuration file** to your project root:
   ```bash
   cp examples/minimal-project-config.yaml project-config.yaml
   ```

2. **Customize the configuration** for your project:
   - Update project information (name, author, description)
   - Modify feature flags and sections
   - Adjust template selections

3. **Generate documentation**:
   ```bash
   python scripts/process_templates.py --config project-config.yaml
   ```

4. **Review generated documents** in the `docs/` directory

## Configuration Guide

Each configuration file contains:

- **Project Information**: Basic project metadata
- **Tier Selection**: Determines which templates are included by default
- **Feature Flags**: Enable/disable specific sections within templates
- **Template Selection**: Choose which templates to generate
- **Output Configuration**: Control how documents are generated
- **AI Agent Settings**: Configure AI-specific features

## Next Steps

After generating your initial documentation:

1. **Review and customize** the generated templates
2. **Add project-specific data** to the configuration
3. **Iterate and refine** as your project evolves
4. **Use the Master Index** to navigate between documents
5. **Update regularly** as requirements change

For more detailed information, see the main documentation in the `docs/` directory.
