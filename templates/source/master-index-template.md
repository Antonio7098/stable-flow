# {{ project.name }} - Master Index

## Instructions for Creating a Master Index
1. **Document Mapping**: Create hyperlinks between all template documents
2. **Workflow Definition**: Define the sequence of document creation and updates
3. **Cross-References**: Ensure all documents reference each other appropriately
4. **Version Control**: Track document versions and update dependencies
5. **Team Onboarding**: Use this as a starting point for new team members
6. **Maintenance**: Update links and references when documents change
7. **Tool Integration**: Link to external tools (Jira, GitHub, etc.) where applicable
8. **Search Optimization**: Include keywords for easy document discovery
9. **Access Control**: Define who can edit which documents
10. **Review Cycle**: Establish regular review and update schedules

## Document Information
- **Version**: {{ master_index.version | default('1.0') }}
- **Last Updated**: {{ master_index.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Project**: {{ project.name }}

## Document Ecosystem Overview
```mermaid
graph TD
    A[PRD] --> B[Features CSV]
    A --> C[Technical Design]
    B --> D[Sprint Planning]
    B --> E[Sprint Template]
    C --> E
    C --> F[Development Guide]
    D --> E
    E --> G[ADRs]
    F --> H[Master Index]
    G --> H
{% if sections.master_index.advanced_templates %}
    H --> I[Performance Tracker]
    H --> J[Security Audit]
    H --> K[Technical Debt]
    H --> L[API Evolution]
{% endif %}
{% if sections.master_index.operations_templates %}
    H --> M[Incident Response]
    H --> N[Data Migration]
{% endif %}
{% if sections.master_index.agile_templates %}
    H --> O[Scrum Master Guide]
    H --> P[Product Owner Guide]
    H --> Q[Kanban Board Setup]
    H --> R[Agile Methodology Selection]
{% endif %}
```

## Core Documents

### 1. Product Requirements Document (PRD)
- **File**: `docs/prd.md`
- **Template**: `templates/core/prd-template.md`
- **Purpose**: Product vision, features, and user requirements
- **Dependencies**: None (starting document)
- **Updates**: When product vision or requirements change
- **Links To**: Features CSV, Technical Design
- **Tier**: All tiers
- **Owner**: {{ master_index.owners.prd | default('Product Manager') }}

### 2. Features CSV
- **File**: `docs/features.csv`
- **Template**: `templates/core/features-csv-template.csv`
- **Purpose**: Detailed feature tracking and prioritization
- **Dependencies**: PRD
- **Updates**: When features are added, modified, or reprioritized
- **Links To**: Sprint Planning, Sprint Template, Technical Design
- **Tier**: All tiers
- **Owner**: {{ master_index.owners.features | default('Product Manager') }}

### 3. Technical Design Document
- **File**: `docs/technical-design.md`
- **Template**: `templates/core/technical-design-template.md`
- **Purpose**: System architecture, technology choices, and technical specifications
- **Dependencies**: PRD
- **Updates**: When architecture or technical requirements change
- **Links To**: Development Guide, Sprint Template, ADRs
- **Tier**: All tiers
- **Owner**: {{ master_index.owners.technical_design | default('Technical Lead') }}

### 4. Development Guide
- **File**: `docs/development-guide.md`
- **Template**: `templates/core/development-guide-template.md`
- **Purpose**: Coding standards, workflow, and development practices
- **Dependencies**: Technical Design
- **Updates**: When development practices or standards change
- **Links To**: All documents (provides context for implementation)
- **Tier**: Core, Advanced
- **Owner**: {{ master_index.owners.development_guide | default('Development Team') }}

### 5. Sprint Planning Overview
- **File**: `docs/sprint-planning.md`
- **Template**: `templates/core/sprint-planning-template.md`
- **Purpose**: Multi-sprint planning, resource allocation, and milestone tracking
- **Dependencies**: Features CSV, Technical Design
- **Updates**: At sprint planning meetings or when project scope changes
- **Links To**: Individual Sprint Templates
- **Tier**: Core, Advanced
- **Owner**: {{ master_index.owners.sprint_planning | default('Scrum Master') }}

### 6. Sprint Template
- **File**: `docs/sprint-[number].md`
- **Template**: `templates/core/sprint-template.md`
- **Purpose**: Individual sprint planning, execution tracking, and retrospectives
- **Dependencies**: Sprint Planning, Features CSV
- **Updates**: Daily during sprint, at sprint review and retrospective
- **Links To**: Features CSV, Technical Design, Development Guide
- **Tier**: Core, Advanced
- **Owner**: {{ master_index.owners.sprint_template | default('Sprint Team') }}

{% if sections.master_index.adr_template %}
### 7. Architecture Decision Records (ADRs)
- **File**: `docs/adrs/`
- **Template**: `templates/advanced/adr-template.md`
- **Purpose**: Documenting architectural decisions and their rationale
- **Dependencies**: Technical Design
- **Updates**: When architectural decisions are made
- **Links To**: Technical Design, Development Guide
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.adr | default('Technical Lead') }}
{% endif %}

## Advanced Templates
{% if sections.master_index.advanced_templates %}

### Performance Optimization Tracker
- **File**: `docs/performance-tracker.md`
- **Template**: `templates/advanced/performance-optimization-tracker-template.md`
- **Purpose**: Track incremental performance improvements and optimizations
- **Dependencies**: Technical Design, Sprint Template
- **Updates**: After performance optimization sprints
- **Links To**: Technical Design, Sprint Template
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.performance | default('Performance Engineer') }}

### Security Audit & Compliance Tracker
- **File**: `docs/security-audit.md`
- **Template**: `templates/advanced/security-audit-compliance-tracker-template.md`
- **Purpose**: Track security audits, compliance requirements, and vulnerability management
- **Dependencies**: Technical Design, Development Guide
- **Updates**: Monthly security reviews, after incidents
- **Links To**: Technical Design, Development Guide
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.security | default('Security Officer') }}

### Technical Debt Management Tracker
- **File**: `docs/technical-debt.md`
- **Template**: `templates/advanced/technical-debt-management-tracker-template.md`
- **Purpose**: Systematically track and prioritize technical debt reduction
- **Dependencies**: All technical documents
- **Updates**: Quarterly technical debt reviews
- **Links To**: Sprint Planning, Technical Design
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.technical_debt | default('Technical Lead') }}

### API Design & Evolution Tracker
- **File**: `docs/api-evolution.md`
- **Template**: `templates/advanced/api-design-evolution-tracker-template.md`
- **Purpose**: Manage API lifecycle, versioning, and breaking changes
- **Dependencies**: Technical Design
- **Updates**: When APIs are modified or new versions released
- **Links To**: Technical Design, Sprint Template
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.api | default('API Architect') }}
{% endif %}

## Operations Templates
{% if sections.master_index.operations_templates %}

### Incident Response Runbook
- **File**: `docs/incident-response.md`
- **Template**: `templates/operations/incident-response-template.md`
- **Purpose**: Standardized incident response procedures and post-mortems
- **Dependencies**: Technical Design, Development Guide
- **Updates**: After incidents, quarterly reviews
- **Links To**: All operational documents
- **Tier**: Operations
- **Owner**: {{ master_index.owners.incident_response | default('DevOps Team') }}

### Data Migration Plan
- **File**: `docs/data-migration.md`
- **Template**: `templates/operations/data-migration-template.md`
- **Purpose**: Plan and execute data migrations safely
- **Dependencies**: Technical Design
- **Updates**: Before data migration projects
- **Links To**: Technical Design, Sprint Planning
- **Tier**: Operations
- **Owner**: {{ master_index.owners.data_migration | default('Data Engineer') }}
{% endif %}

## Agile Methodology Templates
{% if sections.master_index.agile_templates %}

### Scrum Master Guide
- **File**: `docs/scrum-master-guide.md`
- **Template**: `templates/advanced/scrum-master-guide-template.md`
- **Purpose**: Scrum Master role definition, ceremony facilitation, and team coaching
- **Dependencies**: Sprint Planning, Sprint Template
- **Updates**: When team processes or Scrum practices change
- **Links To**: Sprint Planning, Sprint Template, Development Guide
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.scrum_master | default('Scrum Master') }}

### Product Owner Guide
- **File**: `docs/product-owner-guide.md`
- **Template**: `templates/advanced/product-owner-guide-template.md`
- **Purpose**: Product Owner role definition, backlog management, and stakeholder engagement
- **Dependencies**: PRD, Features CSV
- **Updates**: When product strategy or stakeholder needs change
- **Links To**: PRD, Features CSV, Sprint Planning
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.product_owner | default('Product Owner') }}

### Sprint Retrospective Template
- **File**: `docs/sprint-retrospective-[number].md`
- **Template**: `templates/advanced/sprint-retrospective-template.md`
- **Purpose**: Structured sprint retrospectives with data-driven analysis
- **Dependencies**: Sprint Template
- **Updates**: At the end of each sprint
- **Links To**: Sprint Template, Sprint Planning
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.sprint_retrospective | default('Scrum Master') }}

### Kanban Board Setup Guide
- **File**: `docs/kanban-board-setup.md`
- **Template**: `templates/advanced/kanban-board-setup-template.md`
- **Purpose**: Kanban board configuration, workflow design, and team training
- **Dependencies**: Development Guide
- **Updates**: When workflow or team structure changes
- **Links To**: Development Guide, Sprint Planning
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.kanban_setup | default('Flow Master') }}

### Kanban Metrics Dashboard
- **File**: `docs/kanban-metrics.md`
- **Template**: `templates/advanced/kanban-metrics-template.md`
- **Purpose**: Flow metrics, bottleneck analysis, and performance tracking
- **Dependencies**: Kanban Board Setup
- **Updates**: Weekly metrics review and analysis
- **Links To**: Kanban Board Setup, Sprint Planning
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.kanban_metrics | default('Flow Master') }}

### Agile Methodology Selection Guide
- **File**: `docs/agile-methodology-selection.md`
- **Template**: `templates/advanced/agile-methodology-selection-guide.md`
- **Purpose**: Framework for selecting appropriate agile methodology
- **Dependencies**: None (standalone decision framework)
- **Updates**: When team or project characteristics change significantly
- **Links To**: All agile templates
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.methodology_selection | default('Agile Coach') }}

### Sprint-Kanban Hybrid Framework
- **File**: `docs/sprint-kanban-hybrid.md`
- **Template**: `templates/advanced/sprint-kanban-hybrid-template.md`
- **Purpose**: Combined Scrum and Kanban approach for flexible project management
- **Dependencies**: Scrum Master Guide, Kanban Board Setup
- **Updates**: When hybrid approach needs adjustment
- **Links To**: Scrum Master Guide, Kanban Board Setup, Sprint Planning
- **Tier**: Advanced
- **Owner**: {{ master_index.owners.hybrid_framework | default('Agile Coach') }}
{% endif %}

## Document Workflow

### Creation Sequence
1. **PRD** → Define product vision and requirements
2. **Features CSV** → Break down requirements into trackable features
3. **Technical Design** → Design system architecture and technology choices
4. **Development Guide** → Establish coding standards and practices
5. **Sprint Planning** → Plan multi-sprint roadmap and resource allocation
6. **Sprint Template** → Execute individual sprints with detailed planning
7. **ADRs** → Document architectural decisions as they are made
8. **Advanced Trackers** → Monitor and improve system quality over time

### Update Triggers
{% for trigger in master_index.update_triggers %}
- **{{ trigger.event }}**: Update {{ trigger.documents | join(', ') }}
{% endfor %}

### Cascade Updates
{% if features.cascade %}
When `cascade=true` in the Development Guide:
- **Feature changes** → Update Features CSV, PRD, and Technical Design
- **Technical changes** → Update Technical Design and Development Guide
- **Sprint completion** → Update Sprint Planning and Master Index
- **ADR creation** → Update Technical Design and Master Index
{% endif %}

## Automated Validation

### Document Health Checks
{% for check in master_index.validation.health_checks %}
- **{{ check.name }}**: {{ check.description }}
  - **Frequency**: {{ check.frequency }}
  - **Owner**: {{ check.owner }}
{% endfor %}

### CI/CD Integration
```yaml
# Example GitHub Actions workflow
name: Document Validation
on:
  push:
    paths:
      - 'docs/**'
      - 'templates/**'
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Validate document links
      run: |
        # Check for broken internal links
        find docs -name "*.md" -exec grep -l "\[.*\](\.\." {} \;
    - name: Check document completeness
      run: |
        # Validate required sections exist
        python scripts/validate_docs.py
```

### Link Validation
{% for validator in master_index.validation.link_validators %}
- **{{ validator.name }}**: {{ validator.description }}
  - **Coverage**: {{ validator.coverage }}
  - **False Positives**: {{ validator.false_positives | default('Low') }}
{% endfor %}

## Change Management

### RFC Process
{% for step in master_index.change_management.rfc_process %}
{{ loop.index }}. {{ step }}
{% endfor %}

### Version Control Integration
- **Branch Strategy**: {{ master_index.change_management.branch_strategy | default('GitFlow with feature branches') }}
- **Commit Convention**: {{ master_index.change_management.commit_convention | default('Conventional commits') }}
- **PR Reviews**: {{ master_index.change_management.pr_reviews | default('Required for all document changes') }}

## Monitoring & Metrics

### Document Engagement
{% for metric in master_index.monitoring.engagement %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Target**: {{ metric.target }}
  - **Measurement**: {{ metric.measurement }}
{% endfor %}

### Quality Metrics
{% for metric in master_index.monitoring.quality %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Target**: {{ metric.target }}
  - **Current**: {{ metric.current | default('TBD') }}
{% endfor %}

### Team Adoption
{% for metric in master_index.monitoring.adoption %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Target**: {{ metric.target }}
  - **Measurement**: {{ metric.measurement }}
{% endfor %}

## Team Resources

### Training Materials
{% for resource in master_index.resources.training %}
- **{{ resource.title }}**: {{ resource.description }}
  - **Audience**: {{ resource.audience }}
  - **Format**: {{ resource.format }}
  - **Location**: {{ resource.location }}
{% endfor %}

### Support Channels
{% for channel in master_index.resources.support %}
- **{{ channel.name }}**: {{ channel.description }}
  - **Purpose**: {{ channel.purpose }}
  - **Response Time**: {{ channel.response_time }}
{% endfor %}

### Templates & Tools
{% for tool in master_index.resources.tools %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Purpose**: {{ tool.purpose }}
  - **Training Required**: {{ tool.training_required | default('No') }}
{% endfor %}

## Appendices

### Document Templates Reference
| Template | Location | Tier | Description |
|----------|----------|------|-------------|
{% for template in master_index.templates_reference %}
| {{ template.name }} | `{{ template.location }}` | {{ template.tier }} | {{ template.description }} |
{% endfor %}

### External Tool Integration
{% for tool in master_index.external_tools %}
#### {{ tool.name }}
- **Purpose**: {{ tool.purpose }}
- **Integration Point**: {{ tool.integration_point }}
- **Data Sync**: {{ tool.data_sync }}
- **Access**: {{ tool.access }}
{% endfor %}

### Glossary
{% for term, definition in master_index.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

### Changelog
{% for change in master_index.changelog %}
- **{{ change.date }}**: {{ change.description }}
  - **Author**: {{ change.author }}
  - **Impact**: {{ change.impact }}
{% endfor %}

---
*This Master Index should be updated whenever documents are added, removed, or significantly changed. It serves as the central navigation hub for the entire documentation ecosystem.*