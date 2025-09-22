# Getting Started with Stable Flow

Welcome to Stable Flow! This guide will help you get up and running with the AI-optimized documentation system.

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd stable-flow

# Set up Python environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Choose Your Tier

Stable Flow offers four tiers of documentation complexity:

- **Minimal**: Essential documents only (PRD, Technical Design, Features)
- **Core**: Standard project documentation (adds Development Guide, Sprint Planning)
- **Advanced**: Enterprise-grade documentation (adds Master Index, ADR, Trackers)
- **Custom**: Fully customizable with granular control

### 3. Initialize Your Project

```bash
# Copy an example configuration
cp examples/minimal-project-config.yaml project-config.yaml

# Customize the configuration for your project
# Edit project-config.yaml with your project details

# Generate documentation
python scripts/process_templates.py --config project-config.yaml
```

### 4. Review Generated Documents

Your documentation will be generated in the `docs/` directory. Start with:

1. **PRD** - Product Requirements Document
2. **Technical Design** - System architecture and technical specifications
3. **Features CSV** - Feature matrix and requirements
4. **Master Index** - Navigation hub (if using Core+ tier)

### Generate into an external project

You can run Stable Flow from its own repository but generate documentation into another project.

Recommended layouts:

```text
your-project/
├── docs/                    # output target for generated docs
├── your-project-config.yaml # Stable Flow config for this project
├── src/
└── README.md
```

Vendored tool layout:

```text
your-project/
├── tools/
│   └── stable-flow/         # submodule or vendored copy
├── docs/
└── your-project-config.yaml
```

Generate from Windows PowerShell:

```powershell
# From the stable-flow repo
cd C:\\ANTONIO\\Coding\\stable-flow
.\\venv\\Scripts\\Activate.ps1

python .\\scripts\\process_templates.py `
  --config C:\\path\\to\\your-project\\your-project-config.yaml `
  --output C:\\path\\to\\your-project\\docs
```

Generate from Unix/macOS:

```bash
cd /path/to/stable-flow
source venv/bin/activate

python scripts/process_templates.py \
  --config /path/to/your-project/your-project-config.yaml \
  --output /path/to/your-project/docs
```

Alternatively, install the CLI once and run from anywhere:

```bash
# From stable-flow
pip install -e .

# From your project root
stable-flow generate \
  --config ./your-project-config.yaml \
  --output ./docs
```

## Configuration Basics

### Project Information

```yaml
project:
  name: "Your Project Name"
  description: "Brief project description"
  author: "Your Name"
  version: "1.0.0"
  created: "2024-12-09"
```

### Tier Selection

```yaml
tier: "minimal"  # or "core", "advanced", "custom"
```

### Feature Flags

Control which sections appear in your documents:

```yaml
sections:
  prd:
    competitive_analysis: true
    user_experience: true
    data_strategy: false
```

### Template Selection

Choose which documents to generate:

```yaml
templates:
  core:
    prd: true
    technical_design: true
    features_csv: true
    development_guide: false
```

## Common Workflows

### Starting a New Project

1. **Choose your tier** based on project complexity
2. **Copy the appropriate example** configuration
3. **Customize project information** and feature flags
4. **Generate initial documentation**
5. **Fill in project-specific details**
6. **Iterate and refine** as requirements evolve

### Updating Existing Documentation

1. **Modify your configuration** file
2. **Re-run the generation** process
3. **Review changes** in generated documents
4. **Customize as needed** for your specific project

### Adding New Features

1. **Update the Features CSV** with new requirements
2. **Modify technical design** if architecture changes
3. **Update PRD** if scope or goals change
4. **Regenerate documentation** to reflect changes

## AI Agent Integration

Stable Flow is designed to work seamlessly with AI coding assistants:

### System Prompts

Configure AI agents with project-specific context:

```yaml
ai_agents:
  system_prompt: "You are an AI coding assistant for [Project Name]..."
  parallel_processing: true
  context_window: 8000
```

### Parallel Processing

Enable multiple AI agents to work on different aspects simultaneously:

```yaml
sprint_template:
  parallel_agents: true
  agents:
    - name: "Frontend Agent"
      focus: "UI/UX development"
    - name: "Backend Agent"
      focus: "API and database"
```

## Best Practices

### Documentation Maintenance

- **Update regularly** as requirements change
- **Use the Master Index** for navigation
- **Keep configurations** in version control
- **Review generated docs** before committing

### AI Agent Usage

- **Provide clear context** in system prompts
- **Use structured data** (YAML, CSV) for better AI comprehension
- **Enable parallel processing** for complex projects
- **Monitor and adjust** AI agent performance

### Project Evolution

- **Start minimal** and upgrade tiers as needed
- **Use feature flags** to control complexity
- **Customize templates** for project-specific needs
- **Maintain consistency** across all documents

## Testing (Optional for Contributors)

If you plan to contribute to Stable Flow or modify the internals, set up the development environment and run tests:

```bash
# Install development (testing) dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest -q
```

If you're only using Stable Flow to generate documentation, you do not need the tests or dev dependencies.

### Removing test files (optional)

You can remove the test files from your local clone if you don't need them:

```bash
git rm -r --cached tests || true
git rm --cached pytest.ini || true
rimraf tests 2> NUL || rm -rf tests
del /f /q pytest.ini 2> NUL || rm -f pytest.ini
```

Note: Tests are excluded from package distributions via `MANIFEST.in`.

## Troubleshooting

### Common Issues

**Template not found errors:**
- Check that template files exist in `templates/source/`
- Verify template names in configuration

**Missing data errors:**
- Ensure all required fields are defined in configuration
- Check YAML syntax and indentation

**Generation failures:**
- Verify Python environment is activated
- Check that all dependencies are installed
- Review error messages for specific issues

### Getting Help

- **Check examples** in the `examples/` directory
- **Review configuration** templates in `templates/config/`
- **Read documentation** in the `docs/` directory
- **Examine generated output** for reference

## Next Steps

Once you're comfortable with the basics:

1. **Explore advanced features** in the Core and Advanced tiers
2. **Customize templates** for your specific needs
3. **Integrate with your development workflow**
4. **Contribute improvements** back to the project

Happy documenting! 🚀
