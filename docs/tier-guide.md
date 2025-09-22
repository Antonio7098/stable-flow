# Stable Flow Tier Guide

This guide explains the different tiers available in Stable Flow and helps you choose the right tier for your project.

## Overview

Stable Flow offers four tiers of documentation complexity, designed to scale with your project's needs and team maturity:

| Tier | Complexity | Use Case | Documents | Best For |
|------|------------|----------|-----------|----------|
| **Minimal** | Low | Solo developers, simple projects | 3 core docs | Quick starts, prototypes |
| **Core** | Medium | Small to medium teams | 6 core docs | Standard development |
| **Advanced** | High | Large teams, enterprises | 11+ docs + trackers | Enterprise-grade projects |
| **Custom** | Variable | Specialized needs | User-defined | Unique requirements |

## Tier Comparison

### Minimal Tier
**For: Individual developers, proof-of-concepts, simple applications**

#### What's Included:
- ✅ Product Requirements Document (PRD)
- ✅ Technical Design Document
- ✅ Features CSV

#### When to Use:
- You're working alone or with 1-2 other developers
- The project is relatively simple (< 6 months development)
- You want lightweight documentation
- Budget and time constraints are tight

#### Generated Documents:
```
docs/
├── prd.md
├── technical-design.md
└── features.csv
```

#### Example Use Case:
> *"I'm building a simple web app for a client. I need basic requirements and architecture documentation but don't want to spend weeks on docs."*

### Core Tier
**For: Small to medium teams, standard software projects**

#### What's Included:
- ✅ All Minimal tier documents
- ✅ Development Guide (coding standards, workflow)
- ✅ Sprint Planning (multi-sprint roadmap)
- ✅ Sprint Template (individual sprint execution)

#### When to Use:
- You have 3-15 developers
- The project will take 6-18 months
- You follow agile development practices
- You need consistent coding standards and processes

#### Generated Documents:
```
docs/
├── prd.md
├── technical-design.md
├── features.csv
├── development-guide.md
├── sprint-planning.md
└── sprint-1.md (and subsequent sprints)
```

#### Example Use Case:
> *"Our startup is building an e-commerce platform. We have 8 developers and need to establish coding standards and sprint planning while maintaining development velocity."*

### Advanced Tier
**For: Large teams, enterprises, mission-critical systems**

#### What's Included:
- ✅ All Core tier documents
- ✅ Master Index (documentation hub)
- ✅ Architecture Decision Records (ADRs)
- ✅ Performance Optimization Tracker
- ✅ Security Audit & Compliance Tracker
- ✅ Technical Debt Management Tracker
- ✅ API Design & Evolution Tracker
- ✅ Incident Response Runbook
- ✅ Data Migration Plan
- ✅ Scrum Master Guide
- ✅ Product Owner Guide
- ✅ Sprint Retrospective Template
- ✅ Kanban Board Setup Guide
- ✅ Kanban Metrics Dashboard
- ✅ Agile Methodology Selection Guide
- ✅ Sprint-Kanban Hybrid Framework

#### When to Use:
- You have 15+ developers
- The project is enterprise-scale or mission-critical
- You need comprehensive quality assurance and compliance
- You require advanced tracking and monitoring capabilities

#### Generated Documents:
```
docs/
├── prd.md
├── technical-design.md
├── features.csv
├── development-guide.md
├── sprint-planning.md
├── sprint-1.md
├── master-index.md
├── adrs/
│   └── adr-001.md
├── performance-tracker.md
├── security-audit.md
├── technical-debt.md
├── api-evolution.md
├── incident-response.md
├── data-migration.md
├── scrum-master-guide.md
├── product-owner-guide.md
├── sprint-retrospective-1.md
├── kanban-board-setup.md
├── kanban-metrics.md
├── agile-methodology-selection.md
└── sprint-kanban-hybrid.md
```

#### Example Use Case:
> *"We're a Fortune 500 company building a global financial platform. We need enterprise-grade documentation, compliance tracking, and comprehensive quality assurance across our 50+ person development team."*

### Custom Tier
**For: Specialized requirements, unique workflows**

#### What's Included:
- ✅ Any combination of available templates
- ✅ Granular control over sections and features
- ✅ Custom feature flags and configurations
- ✅ Specialized document sets

#### When to Use:
- You have very specific documentation needs
- Standard tiers don't fit your workflow
- You want to start with a minimal set and expand gradually
- You need to exclude certain types of documentation

#### Configuration Example:
```yaml
tier: "custom"
templates:
  core:
    prd: true
    technical_design: false  # Skip if you have existing docs
    features_csv: true
    development_guide: true
  advanced:
    performance_tracker: true
    security_audit: false    # Skip if security is handled elsewhere
```

## Feature Comparison

### Core Features by Tier

| Feature | Minimal | Core | Advanced | Custom |
|---------|---------|------|----------|--------|
| **Documents Generated** | 3 | 6 | 11+ | Variable |
| **Cascade Updates** | ❌ | ✅ | ✅ | Configurable |
| **Competitive Analysis** | ❌ | ❌ | ✅ | Configurable |
| **User Experience Design** | ❌ | ✅ | ✅ | Configurable |
| **Security Specifications** | Basic | Basic | Detailed | Configurable |
| **API Documentation** | ❌ | ❌ | ✅ | Configurable |
| **Sprint Planning** | ❌ | ✅ | ✅ | Configurable |
| **Parallel AI Agents** | ❌ | ✅ | ✅ | Configurable |
| **Performance Tracking** | ❌ | ❌ | ✅ | Configurable |
| **Security Compliance** | ❌ | ❌ | ✅ | Configurable |
| **Technical Debt Tracking** | ❌ | ❌ | ✅ | Configurable |
| **Incident Response** | ❌ | ❌ | ✅ | Configurable |
| **Master Index** | ❌ | ❌ | ✅ | Configurable |

### AI Agent Features by Tier

| AI Feature | Minimal | Core | Advanced | Custom |
|------------|---------|------|----------|--------|
| **System Prompts** | ✅ | ✅ | ✅ | ✅ |
| **Parallel Processing** | ❌ | ✅ | ✅ | Configurable |
| **Context Management** | Basic | Basic | Advanced | Configurable |
| **Quality Assurance** | Basic | Basic | Comprehensive | Configurable |
| **Ethical Guidelines** | ✅ | ✅ | ✅ | ✅ |
| **Performance Monitoring** | ❌ | ❌ | ✅ | Configurable |

## Migration Between Tiers

### Upgrading Tiers

You can upgrade from a lower tier to a higher tier at any time:

```bash
# Start with minimal
python scripts/process_templates.py --config minimal-config.yaml

# Later upgrade to core
# Edit config to change tier: "minimal" → tier: "core"
# Add additional sections as needed
python scripts/process_templates.py --config core-config.yaml
```

### What Happens When You Upgrade:

1. **New Documents**: Additional documents are generated
2. **Enhanced Sections**: Existing documents get more detailed sections
3. **Cross-References**: Documents link to the newly available docs
4. **Cascade Updates**: If enabled, related documents are updated

### Best Practices for Upgrades:

- **Plan Ahead**: Know which sections you'll need before starting
- **Incremental Adoption**: Start minimal, add features as you grow
- **Team Buy-in**: Ensure your team is ready for additional documentation overhead
- **Automation**: Use cascade updates to maintain consistency

## Choosing the Right Tier

### Decision Factors

#### Team Size
- **1-2 developers**: Minimal tier
- **3-15 developers**: Core tier
- **15+ developers**: Advanced tier

#### Project Complexity
- **Simple CRUD app**: Minimal tier
- **Standard web/mobile app**: Core tier
- **Enterprise platform**: Advanced tier
- **Microservices architecture**: Advanced tier

#### Regulatory Requirements
- **No special requirements**: Any tier
- **Basic security**: Core tier minimum
- **Enterprise compliance (SOC2, HIPAA)**: Advanced tier required

#### Timeline
- **< 3 months**: Minimal tier
- **3-12 months**: Core tier
- **12+ months**: Advanced tier

#### Budget
- **Limited budget/time**: Minimal tier
- **Standard project budget**: Core tier
- **Enterprise budget**: Advanced tier

### Assessment Questions

Ask yourself:

1. **How many developers will work on this project?**
   - 1-2: Minimal
   - 3-15: Core
   - 15+: Advanced

2. **Do you need sprint planning and agile processes?**
   - Yes: Core or Advanced
   - No: Minimal

3. **Are there security or compliance requirements?**
   - Enterprise-grade: Advanced
   - Basic: Core
   - None: Minimal

4. **Will this project last more than 6 months?**
   - Yes: Consider Core or Advanced
   - No: Minimal might suffice

5. **Do you need comprehensive quality tracking?**
   - Yes: Advanced
   - No: Core or Minimal

## Configuration Examples

### Minimal Tier Configuration
```yaml
project:
  name: "My Project"
  author: "Developer Name"
tier: "minimal"
features:
  cascade: false
```

### Core Tier Configuration
```yaml
project:
  name: "My Project"
  author: "Team Lead"
tier: "core"
features:
  cascade: true
sections:
  prd:
    competitive_analysis: true
  technical_design:
    security_detailed: true
```

### Advanced Tier Configuration
```yaml
project:
  name: "Enterprise Platform"
  author: "Enterprise Team"
tier: "advanced"
features:
  cascade: true
sections:
  # All advanced sections enabled
  prd:
    competitive_analysis: true
    user_experience: true
    data_strategy: true
  technical_design:
    accessibility: true
    security_detailed: true
    api_specification: true
  # ... all sections enabled
```

## Cost-Benefit Analysis

### Minimal Tier Benefits
- ✅ **Fast setup**: Generate docs in minutes
- ✅ **Low overhead**: Minimal maintenance required
- ✅ **Flexible**: Easy to modify and extend
- ✅ **Cost-effective**: Less time spent on documentation

### Core Tier Benefits
- ✅ **Standardized processes**: Consistent development practices
- ✅ **Team coordination**: Sprint planning and task management
- ✅ **Quality assurance**: Coding standards and review processes
- ✅ **Scalable**: Grows with your team

### Advanced Tier Benefits
- ✅ **Enterprise-ready**: Comprehensive compliance and security
- ✅ **Quality tracking**: Performance, security, and technical debt monitoring
- ✅ **Risk management**: Incident response and audit capabilities
- ✅ **Long-term maintenance**: Sustainable development practices

## Getting Started

### Quick Start by Tier

#### Minimal Tier
```bash
# Copy example config
cp examples/minimal-project-config.yaml project-config.yaml

# Edit project details
# Generate documentation
python scripts/process_templates.py --config project-config.yaml
```

#### Core Tier
```bash
# Copy example config
cp examples/core-project-config.yaml project-config.yaml

# Edit project details and enable desired sections
# Generate documentation
python scripts/process_templates.py --config project-config.yaml
```

#### Advanced Tier
```bash
# Copy example config
cp examples/advanced-project-config.yaml project-config.yaml

# Customize extensively for enterprise needs
# Generate comprehensive documentation
python scripts/process_templates.py --config project-config.yaml
```

## Support and Resources

### Getting Help
- **Documentation**: Check this guide and `docs/getting-started.md`
- **Examples**: Review `examples/` directory for configuration samples
- **Templates**: Examine `templates/` directory for available documents

### Best Practices
- **Start Small**: Begin with Minimal tier and upgrade as needed
- **Iterate**: Regularly review and update your documentation
- **Customize**: Adapt the generated docs to your specific needs
- **Automate**: Use cascade updates to maintain consistency

Remember: The best tier is the one that fits your current needs while allowing room to grow. You can always upgrade later! 🚀

