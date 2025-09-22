# Stable Flow Customization Guide

This guide shows you how to customize Stable Flow templates and configurations to match your specific needs and workflows.

## Overview

Stable Flow is designed to be highly customizable while maintaining consistency and quality. You can customize:

- **Document Structure**: Enable/disable sections within templates
- **Content**: Modify generated content through configuration
- **Features**: Control advanced features and integrations
- **Workflows**: Adapt processes to your team's preferences

## Configuration Structure

### Basic Configuration Format

```yaml
# Project Information
project:
  name: "Your Project Name"
  description: "Brief project description"
  author: "Your Name or Team"
  version: "1.0.0"
  created: "2024-12-09"

# Tier Selection
tier: "minimal"  # minimal, core, advanced, custom

# Feature Flags
features:
  cascade: true  # Enable cascading updates between documents

# Section Control
sections:
  prd:
    competitive_analysis: true
    user_experience: false
  technical_design:
    security_detailed: true
    api_specification: false

# Template Selection
templates:
  core:
    prd: true
    technical_design: true
  advanced:
    security_audit: false

# AI Agent Configuration
ai_agents:
  system_prompt: "Custom AI prompt"
  parallel_processing: true
  context_window: 8000
```

## Customizing Document Sections

### PRD Customization

Control which sections appear in your Product Requirements Document:

```yaml
sections:
  prd:
    competitive_analysis: true    # Include competitor analysis
    user_experience: true         # Include wireframes and UX requirements
    data_strategy: false          # Skip data strategy (if handled elsewhere)
    competitive_moat: false       # Skip competitive advantage analysis
    monetization: true           # Include revenue model
```

#### Available PRD Sections:
- `competitive_analysis`: Competitor research and market positioning
- `user_experience`: Wireframes, user flows, A/B testing plans
- `data_strategy`: Data collection, governance, and privacy
- `competitive_moat`: Competitive advantages and defensibility
- `monetization`: Revenue streams and pricing strategy

### Technical Design Customization

```yaml
sections:
  technical_design:
    accessibility: true           # Include WCAG compliance and ARIA guidelines
    security_detailed: true       # Include threat modeling and zero-trust architecture
    api_specification: true       # Include OpenAPI specs and contract testing
    architectural_decisions: true # Include ADR framework
```

#### Available Technical Design Sections:
- `accessibility`: WCAG compliance, screen readers, keyboard navigation
- `security_detailed`: Threat modeling, attack surface analysis, zero-trust
- `api_specification`: OpenAPI specs, contract testing, API versioning
- `architectural_decisions`: ADR templates and decision tracking

### Sprint Template Customization

```yaml
sections:
  sprint_template:
    parallel_agents: true         # Include multi-agent coordination
    environmental_impact: false   # Skip environmental considerations
    api_integration: true        # Include API integration details
```

#### Available Sprint Template Sections:
- `parallel_agents`: Multi-agent coordination and conflict resolution
- `environmental_impact`: Carbon footprint and energy efficiency tracking
- `api_integration`: API endpoint documentation and testing

### Sprint Planning Customization

```yaml
sections:
  sprint_planning:
    ai_assisted_velocity: true    # Include AI velocity metrics
    ai_specific_risks: true      # Include AI-specific risk management
```

#### Available Sprint Planning Sections:
- `ai_assisted_velocity`: AI-assisted development metrics and velocity tracking
- `ai_specific_risks`: AI hallucination mitigation and context management

### Features CSV Customization

```yaml
sections:
  features_csv:
    business_metrics: true       # Include business value scores and revenue impact
    sprint_assignment: true      # Include sprint assignment columns
    risk_level: true            # Include risk level assessment
```

#### Available Features CSV Sections:
- `business_metrics`: Business value scores, revenue impact, user segments
- `sprint_assignment`: Sprint assignment tracking
- `risk_level`: Risk level assessment and mitigation

### Master Index Customization

```yaml
sections:
  master_index:
    advanced_templates: true     # Include advanced template references
    operations_templates: true   # Include operations template references
    adr_template: true          # Include ADR references
```

## Template Selection

### Core Templates

Choose which core documents to generate:

```yaml
templates:
  core:
    prd: true                    # Product Requirements Document
    technical_design: true       # Technical Design Document
    features_csv: true           # Features Tracking Spreadsheet
    development_guide: true      # Development Guidelines
    sprint_planning: true        # Multi-Sprint Planning
    sprint_template: true        # Individual Sprint Execution
    master_index: true           # Documentation Hub
```

### Advanced Templates

Enable specialized templates for advanced use cases:

```yaml
templates:
  advanced:
    adr: true                    # Architecture Decision Records
    performance_tracker: true    # Performance Optimization Tracking
    security_audit: true         # Security Compliance Tracking
    technical_debt: true         # Technical Debt Management
    api_evolution: true          # API Lifecycle Management
```

### Operations Templates

Include operational documentation:

```yaml
templates:
  operations:
    incident_response: true      # Incident Response Procedures
    data_migration: true         # Data Migration Planning
```

## Feature Flags

### Cascade Updates

Enable automatic cross-document updates:

```yaml
features:
  cascade: true
```

When `cascade: true`, changes to features automatically update:
- Features CSV → Sprint Planning
- Technical Design → Development Guide
- Sprint completion → Master Index

### AI Agent Configuration

Customize AI agent behavior:

```yaml
ai_agents:
  system_prompt: "You are a senior full-stack developer specializing in React, Node.js, and PostgreSQL. Always prioritize code quality, security, and performance."
  parallel_processing: true      # Allow multiple AI agents to work simultaneously
  context_window: 8000          # Maximum context window size
  temperature: 0.7             # AI creativity level (0.0-1.0)
```

## Content Customization

### Project Information

Basic project metadata that appears in all documents:

```yaml
project:
  name: "Enterprise Customer Portal"
  description: "A comprehensive customer portal for enterprise clients"
  author: "Enterprise Development Team"
  version: "2.1.0"
  created: "2024-12-09"
```

### Technical Stack Configuration

Define your technology choices:

```yaml
technical_design:
  tech_stack:
    frontend: "React 18, TypeScript, Material-UI"
    backend: "Node.js 18, Express, TypeScript"
    database: "PostgreSQL 15, Redis 7"
    infrastructure: "AWS EKS, CloudFront, Route53"
    devops: "GitHub Actions, Terraform, ArgoCD"
```

### Security Configuration

Customize security requirements:

```yaml
technical_design:
  security:
    auth_method: "OAuth 2.0 + JWT"
    authz_model: "RBAC + ABAC"
    encryption_at_rest: "AES-256"
    encryption_in_transit: "TLS 1.3"
```

### Performance Requirements

Set performance targets:

```yaml
technical_design:
  performance:
    api_response: "< 200ms P95"
    page_load: "< 2s"
    concurrent_users: "10000+"
    rps: "5000"
```

## Development Guide Customization

### Coding Standards

Define your coding conventions:

```yaml
development_guide:
  coding_standards:
    javascript:
      - "Use ESLint with Airbnb config"
      - "Use Prettier for code formatting"
      - "Use TypeScript strict mode"
    python:
      - "Follow PEP 8"
      - "Use Black for formatting"
      - "Use MyPy for type checking"
```

### Git Workflow

Customize version control processes:

```yaml
development_guide:
  git:
    branching_strategy: "GitFlow with feature branches"
    commit_convention: "Conventional commits: type(scope): description"
    pr_process:
      - "Require at least 2 approvals"
      - "Must pass all CI checks"
      - "Security review required"
```

### Testing Strategy

Define testing requirements:

```yaml
development_guide:
  testing:
    levels:
      unit:
        purpose: "Test individual functions and methods"
        tools: "Jest, Pytest"
        coverage_target: "80%"
      integration:
        purpose: "Test component interactions"
        tools: "Cypress, Postman"
        coverage_target: "60%"
      e2e:
        purpose: "Test complete user workflows"
        tools: "Playwright"
        coverage_target: "40%"
```

## Sprint Planning Customization

### Team Configuration

Set up your team structure:

```yaml
sprint_planning:
  team:
    capacity: "50 story points per sprint"
    velocity: "45 points/sprint (historical average)"
    ai_velocity: "55 points/sprint (with AI assistance)"
    velocity_multiplier: "1.22x"
    members: "Alice (Frontend), Bob (Backend), Carol (DevOps), Dave (QA)"
```

### Sprint Schedule

Define sprint timing:

```yaml
sprint_planning:
  timeline:
    start_date: "2024-12-09"
    end_date: "2025-06-09"
    duration: "6 months"
    sprint_length: "2 weeks"
    total_sprints: "12"
```

## Advanced Customizations

### Custom System Prompts

Create specialized AI prompts for your domain:

```yaml
ai_agents:
  system_prompt: |
    You are a senior developer at a fintech company. You specialize in:
    - Financial regulations and compliance (SOX, PCI-DSS)
    - High-availability distributed systems
    - Real-time transaction processing
    - Security-first development practices

    Always consider:
    - Financial data sensitivity
    - Audit trail requirements
    - Regulatory compliance
    - System availability requirements
```

### Custom Validation Rules

Add project-specific validation (future feature):

```yaml
validation:
  custom_rules:
    - name: "security_review_required"
      condition: "file_contains('authentication')"
      action: "require_security_review"
    - name: "performance_budget"
      condition: "api_endpoint_defined"
      action: "check_performance_budget"
```

## Real-World Examples

### Startup Configuration

```yaml
project:
  name: "SaaS Platform"
  author: "Startup Team"
tier: "core"
features:
  cascade: true
sections:
  prd:
    competitive_analysis: true
    user_experience: true
  technical_design:
    security_detailed: true
ai_agents:
  system_prompt: "You are a startup engineer. Prioritize speed, scalability, and user experience."
  parallel_processing: true
```

### Enterprise Configuration

```yaml
project:
  name: "Banking Platform"
  author: "Enterprise Team"
tier: "advanced"
features:
  cascade: true
sections:
  prd:
    competitive_analysis: true
    user_experience: true
    data_strategy: true
    competitive_moat: true
    monetization: true
  technical_design:
    accessibility: true
    security_detailed: true
    api_specification: true
    architectural_decisions: true
ai_agents:
  system_prompt: "You are an enterprise software architect. Always prioritize security, compliance, and scalability."
  temperature: 0.3  # Lower creativity for enterprise stability
```

### Individual Developer Configuration

```yaml
project:
  name: "Personal Project"
  author: "Solo Developer"
tier: "minimal"
features:
  cascade: false
ai_agents:
  system_prompt: "You are a solo developer. Help me build quickly and efficiently."
  parallel_processing: false
```

## Best Practices

### Configuration Management

1. **Version Control**: Keep your configuration in version control
2. **Documentation**: Comment your configuration choices
3. **Consistency**: Use consistent naming conventions
4. **Review**: Have team members review configuration changes

### Customization Strategy

1. **Start Simple**: Begin with minimal configuration
2. **Iterate**: Add features as you need them
3. **Team Consensus**: Get buy-in for configuration changes
4. **Documentation**: Document why you made certain choices

### AI Agent Optimization

1. **Domain-Specific**: Tailor prompts to your industry
2. **Team Alignment**: Ensure AI behavior matches team expectations
3. **Quality Gates**: Set up reviews for AI-generated content
4. **Feedback Loop**: Provide feedback to improve AI performance

## Troubleshooting

### Common Issues

#### Template Not Generating
**Problem**: A template you selected isn't being generated
**Solution**: Check that all required configuration sections are present

#### Section Not Appearing
**Problem**: A section you enabled doesn't appear in the document
**Solution**: Verify the section flag is set correctly in the configuration

#### AI Agent Not Following Guidelines
**Problem**: AI agents aren't following your custom prompts
**Solution**: Make prompts more specific and provide examples

#### Configuration Validation Errors
**Problem**: Your configuration fails validation
**Solution**: Check the error message and ensure all required fields are present

### Getting Help

1. **Check Examples**: Look at `examples/` for working configurations
2. **Review Templates**: Check `templates/source/` for available options
3. **Validate YAML**: Use a YAML validator for syntax errors
4. **Start Minimal**: Begin with a basic configuration and add features gradually

## Advanced Features

### Custom Template Development

You can create custom templates by:

1. Adding new Jinja2 templates to `templates/source/`
2. Updating the configuration schema
3. Adding template processing logic

### Integration Development

Extend Stable Flow with custom integrations:

1. **External Tools**: Add support for Jira, Slack, etc.
2. **CI/CD Integration**: Automate document generation
3. **Custom Validators**: Add project-specific validation rules

### Plugin Architecture

Future versions will support plugins for:
- Custom document types
- Specialized workflows
- Industry-specific templates
- Integration adapters

## Summary

Stable Flow's customization system allows you to:

- **Scale Complexity**: Start simple, add features as you grow
- **Match Workflows**: Adapt to your team's preferred processes
- **Maintain Consistency**: Ensure all documentation follows your standards
- **Leverage AI**: Customize AI behavior for your specific needs
- **Future-Proof**: Easy to extend and modify as requirements change

Remember: The best configuration is one that your team will actually use and maintain! 🚀

