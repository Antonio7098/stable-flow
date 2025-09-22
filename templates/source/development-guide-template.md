# {{ project.name }} - Development Guide

## System Prompt for AI Agent
You are an expert full-stack software engineer working on the {{ project.name }}.
Your primary goal is to generate clean, efficient, and maintainable code.
Current Date: {{ "now" | strftime("%Y-%m-%d") }} - Use this for up-to-date library recommendations.

ALWAYS adhere to the following project-specific guidelines documented in this file:

1. **Coding Standards**: Follow all rules in Section 1.
2. **Project Structure**: All new files must be created in the correct location as defined in Section 2.
3. **Git Workflow**: All commits must follow the convention in Section 3.2.
4. **Error Handling**: Use the patterns defined in Section 5.
5. **Security Guidelines**: Follow all security practices in Section 7.
6. **Performance Standards**: Apply optimization techniques from Section 6.
7. **Modern Paradigms**: Follow current best practices from Section 8.

### Ethical Guidelines
- **Data Privacy**: Ensure code promotes data privacy (GDPR/CCPA compliance)
- **Bias Prevention**: Avoid biased algorithms and ensure diverse, representative data
- **Transparency**: Include clear documentation for AI-generated code decisions
- **Accessibility**: Generate accessible code that works for all users

### Version Awareness
- **Current Libraries**: Use current date {{ "now" | strftime("%Y-%m-%d") }} for up-to-date library recommendations
- **Deprecation Avoidance**: Avoid deprecated features and suggest modern alternatives
- **Security Updates**: Prioritize security patches and current best practices

Before you begin, confirm you have read and understood these instructions.

## Instructions for Creating a Development Guide
1. **Team Standards**: Establish coding standards that work for your team and technology stack
2. **Tool Selection**: Choose development tools (linters, formatters, testing frameworks)
3. **Process Definition**: Define git workflow, code review process, and deployment procedures
4. **Testing Strategy**: Establish testing levels, coverage targets, and quality gates
5. **Security Guidelines**: Include security best practices and code review checklists
6. **Performance Standards**: Define performance guidelines and optimization practices
7. **Documentation Requirements**: Set standards for code documentation and comments
8. **Cascade Setting**: Set cascade=true if feature changes should update planning docs and Master Index
{% if features.cascade %}
9. **Master Index Update**: Update master-index.md when coding standards or processes change
{% endif %}
10. **Team Training**: Ensure all team members understand and follow the guide
11. **Regular Updates**: Plan to review and update the guide as practices evolve

## Document Information
- **Version**: {{ development_guide.version | default('1.0') }}
- **Last Updated**: {{ development_guide.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Cascade**: {{ features.cascade | default('false') }} - If true, changes to features require updates to planning docs and Master Index

## 1. Coding Standards
### Language-Specific Standards
{% for language, standards in development_guide.coding_standards.items() %}
#### {{ language | title }}
{% for rule in standards %}
- {{ rule }}
{% endfor %}

{% endfor %}

### General Principles
{% for principle in development_guide.general_principles %}
- {{ principle }}
{% endfor %}

### Code Review Checklist
{% for item in development_guide.code_review_checklist %}
- [ ] {{ item }}
{% endfor %}

## 2. Project Structure
### Directory Layout
```
{{ development_guide.project_structure | default('
project-root/
├── src/                    # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── scripts/                # Build and utility scripts
├── config/                 # Configuration files
└── README.md              # Project overview
') }}
```

### File Naming Conventions
{% for convention in development_guide.file_naming %}
- {{ convention }}
{% endfor %}

### Import Organization
{% for rule in development_guide.import_organization %}
- {{ rule }}
{% endfor %}

## 3. Git Workflow
### Branching Strategy
{{ development_guide.git.branching_strategy | default('[Describe your branching strategy]') }}

### Commit Convention
{{ development_guide.git.commit_convention | default('[Describe your commit message format]') }}

### Pull Request Process
{% for step in development_guide.git.pr_process %}
{{ loop.index }}. {{ step }}
{% endfor %}

## 4. Testing Strategy
### Testing Levels
{% for level, details in development_guide.testing.levels.items() %}
#### {{ level | title }}
- **Purpose**: {{ details.purpose }}
- **Tools**: {{ details.tools }}
- **Coverage Target**: {{ details.coverage_target }}
- **When to Run**: {{ details.when_to_run }}

{% endfor %}

### Test Organization
{{ development_guide.testing.organization | default('[How tests are organized]') }}

### Mocking Strategy
{{ development_guide.testing.mocking | default('[How mocking is handled]') }}

## 5. Error Handling
### Error Types
{% for error_type, details in development_guide.error_handling.types.items() %}
#### {{ error_type | title }}
- **When to Use**: {{ details.when_to_use }}
- **Pattern**: {{ details.pattern }}
- **Example**: {{ details.example }}

{% endfor %}

### Logging Standards
{% for standard in development_guide.error_handling.logging %}
- {{ standard }}
{% endfor %}

### Monitoring Integration
{{ development_guide.error_handling.monitoring | default('[How errors are monitored]') }}

## 6. Performance Guidelines
### Frontend Performance
{% for guideline in development_guide.performance.frontend %}
- {{ guideline }}
{% endfor %}

### Backend Performance
{% for guideline in development_guide.performance.backend %}
- {{ guideline }}
{% endfor %}

### Database Optimization
{% for guideline in development_guide.performance.database %}
- {{ guideline }}
{% endfor %}

### Caching Strategy
{{ development_guide.performance.caching | default('[Caching approach and tools]') }}

## 7. Security Guidelines
### Authentication & Authorization
{% for guideline in development_guide.security.auth %}
- {{ guideline }}
{% endfor %}

### Data Protection
{% for guideline in development_guide.security.data_protection %}
- {{ guideline }}
{% endfor %}

### Input Validation
{% for guideline in development_guide.security.input_validation %}
- {{ guideline }}
{% endfor %}

### Security Headers
{% for header in development_guide.security.headers %}
- {{ header }}
{% endfor %}

## 8. Modern Paradigms
### Current Best Practices
{% for practice in development_guide.modern_paradigms.best_practices %}
- {{ practice }}
{% endfor %}

### Agile Development Practices
{% if sections.development_guide.agile_practices %}
{% for practice in development_guide.modern_paradigms.agile_practices %}
- **{{ practice.name }}**: {{ practice.description }}
  - **Implementation**: {{ practice.implementation | default('[How to implement this practice]') }}
  - **Benefits**: {{ practice.benefits | join(', ') }}
  - **Tools**: {{ practice.tools | join(', ') }}
{% endfor %}
{% endif %}

### Design Patterns
{% for pattern, details in development_guide.modern_paradigms.design_patterns.items() %}
#### {{ pattern | title }}
- **Use Case**: {{ details.use_case }}
- **Implementation**: {{ details.implementation }}

{% endfor %}

### Architecture Principles
{% for principle in development_guide.modern_paradigms.architecture %}
- {{ principle }}
{% endfor %}

## 9. Code Review Automation
### Pre-commit Hooks
{% for hook in development_guide.automation.pre_commit_hooks %}
- {{ hook }}
{% endfor %}

### PR Automation
{% for automation in development_guide.automation.pr_automation %}
- {{ automation }}
{% endfor %}

### Automated Testing
{% for test in development_guide.automation.automated_testing %}
- {{ test }}
{% endfor %}

## 10. Performance Profiling
### Frontend Performance
{% for tool in development_guide.profiling.frontend %}
- {{ tool }}
{% endfor %}

### Backend Performance
{% for tool in development_guide.profiling.backend %}
- {{ tool }}
{% endfor %}

### Performance Monitoring
{% for monitoring in development_guide.profiling.monitoring %}
- {{ monitoring }}
{% endfor %}

## 11. Common Scripts
### Development Scripts
{% for script, details in development_guide.scripts.development.items() %}
#### {{ script | title }}
```bash
{{ details.command }}
```
**Purpose**: {{ details.purpose }}

{% endfor %}

### Build Scripts
{% for script, details in development_guide.scripts.build.items() %}
#### {{ script | title }}
```bash
{{ details.command }}
```
**Purpose**: {{ details.purpose }}

{% endfor %}

### Deployment Scripts
{% for script, details in development_guide.scripts.deployment.items() %}
#### {{ script | title }}
```bash
{{ details.command }}
```
**Purpose**: {{ details.purpose }}

{% endfor %}

## 12. Anti-Patterns / Things to Avoid
### Code Quality Anti-Patterns
{% for anti_pattern in development_guide.anti_patterns.code_quality %}
- {{ anti_pattern }}
{% endfor %}

### Security Anti-Patterns
{% for anti_pattern in development_guide.anti_patterns.security %}
- {{ anti_pattern }}
{% endfor %}

### Performance Anti-Patterns
{% for anti_pattern in development_guide.anti_patterns.performance %}
- {{ anti_pattern }}
{% endfor %}

### Architecture Anti-Patterns
{% for anti_pattern in development_guide.anti_patterns.architecture %}
- {{ anti_pattern }}
{% endfor %}

## 13. Appendices
### References
{% for reference in development_guide.references %}
- {{ reference }}
{% endfor %}

### Glossary
{% for term, definition in development_guide.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

### Tools & Resources
{% for category, tools in development_guide.tools.items() %}
#### {{ category | title }}
{% for tool in tools %}
- {{ tool }}
{% endfor %}

{% endfor %}

---
*This guide should be reviewed and updated regularly as development practices evolve.*