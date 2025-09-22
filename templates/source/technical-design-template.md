# {{ project.name }} - Technical Design Document

## Instructions for Creating a Technical Design
1. **PRD Review**: Review Product Requirements Document to understand business requirements and constraints
2. **Architecture Review**: Review existing system architecture and constraints, if present
3. **Technology Selection**: Choose appropriate technologies based on development guide, requirements and team expertise
4. **Scalability Planning**: Design for current needs and future growth
5. **Security First**: Integrate security considerations from the beginning
6. **Performance Requirements**: Define and plan for performance targets
7. **Integration Points**: Map all internal and external integration requirements
8. **Data Architecture**: Design data models, storage, and processing strategies
9. **Deployment Strategy**: Plan infrastructure, CI/CD, and deployment approach
10. **Monitoring & Observability**: Design comprehensive monitoring and logging
{% if features.cascade %}
11. **Master Index Update**: Update master-index.md with any new cross-references or document changes
{% endif %}
12. **Documentation**: Ensure all technical decisions are well-documented

## Document Information
- **Version**: {{ technical_design.version | default('1.0') }}
- **Last Updated**: {{ technical_design.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Reviewers**: {{ technical_design.reviewers | default('[List of reviewers]') }}

## 1. Architecture Overview
### System Purpose
{{ technical_design.system_purpose | default('[Brief description of what the system does]') }}

### Technology Stack
- **Frontend**: {{ technical_design.tech_stack.frontend | default('[Specific framework version, e.g., React 18 with Vite, State Management: Zustand, Styling: Tailwind CSS]') }}
- **Backend**: {{ technical_design.tech_stack.backend | default('[Specific framework and version, e.g., Node.js 18, Express 4.x, TypeScript 5.x]') }}
- **Database**: {{ technical_design.tech_stack.database | default('[Specific database and version, e.g., PostgreSQL 15, Redis 7.x]') }}
- **Infrastructure**: {{ technical_design.tech_stack.infrastructure | default('[Specific cloud provider and services, e.g., AWS ECS, RDS, S3]') }}
- **DevOps**: {{ technical_design.tech_stack.devops | default('[Specific tools and versions, e.g., Docker, GitHub Actions, Terraform]') }}

### High-Level Architecture
```mermaid
{{ technical_design.architecture_diagram | default('graph TB\n    A[Component A] --> B[Component B]\n    B --> C[Component C]\n    C --> D[Component D]') }}
```

## 2. Core Components
{% for component in technical_design.components %}
### {{ component.name }}
- **Purpose**: {{ component.purpose }}
- **Key Features**: {{ component.key_features }}
- **Technologies**: {{ component.technologies }}
- **Interfaces**: {{ component.interfaces }}
- **Dependencies**: {{ component.dependencies | default('None') }}
- **Performance Requirements**: {{ component.performance | default('Standard performance requirements') }}

{% endfor %}

## 3. Data Architecture
### Data Models
{% for model in technical_design.data_models %}
#### {{ model.name }}
- **Description**: {{ model.description }}
- **Fields**: {{ model.fields }}
- **Relationships**: {{ model.relationships | default('None') }}
- **Constraints**: {{ model.constraints | default('None') }}

{% endfor %}

### Database Design
- **Primary Database**: {{ technical_design.database.primary | default('[Database type and version]') }}
- **Caching Strategy**: {{ technical_design.database.caching | default('[Redis, Memcached, etc.]') }}
- **Backup Strategy**: {{ technical_design.database.backup | default('[Backup frequency and retention]') }}
- **Migration Strategy**: {{ technical_design.database.migration | default('[How schema changes are handled]') }}

### Data Flow
```mermaid
{{ technical_design.data_flow_diagram | default('graph LR\n    A[Data Source] --> B[Processing]\n    B --> C[Storage]\n    C --> D[API]') }}
```

## 4. Security Design
### Authentication & Authorization
- **Authentication Method**: {{ technical_design.security.auth_method | default('[JWT, OAuth, etc.]') }}
- **Authorization Model**: {{ technical_design.security.authz_model | default('[RBAC, ABAC, etc.]') }}
- **Session Management**: {{ technical_design.security.session_mgmt | default('[How sessions are handled]') }}

{% if sections.technical_design.security_detailed %}
### Threat Model
#### STRIDE Analysis
{% for threat in technical_design.security.stride %}
- **{{ threat.type }}**: {{ threat.description }}
  - **Risk Level**: {{ threat.risk_level }}
  - **Mitigation**: {{ threat.mitigation }}
{% endfor %}

#### Attack Surface
- **External APIs**: {{ technical_design.security.attack_surface.external_apis | default('[List of external APIs]') if technical_design.security.attack_surface else '[List of external APIs]' }}
- **Internal Services**: {{ technical_design.security.attack_surface.internal_services | default('[List of internal services]') if technical_design.security.attack_surface else '[List of internal services]' }}
- **Data Stores**: {{ technical_design.security.attack_surface.data_stores | default('[List of data stores]') if technical_design.security.attack_surface else '[List of data stores]' }}

#### Risk Matrix
| Threat | Likelihood | Impact | Risk Level | Mitigation |
|--------|------------|--------|------------|------------|
{% for risk in technical_design.security.risk_matrix %}
| {{ risk.threat }} | {{ risk.likelihood }} | {{ risk.impact }} | {{ risk.risk_level }} | {{ risk.mitigation }} |
{% endfor %}

### Zero Trust Architecture
- **Identity Verification**: {{ technical_design.security.zero_trust.identity | default('[MFA, SSO, etc.]') if technical_design.security.zero_trust else '[MFA, SSO, etc.]' }}
- **Least Privilege Access**: {{ technical_design.security.zero_trust.least_privilege | default('[How least privilege is enforced]') if technical_design.security.zero_trust else '[How least privilege is enforced]' }}
- **Micro-segmentation**: {{ technical_design.security.zero_trust.micro_segmentation | default('[Network segmentation strategy]') if technical_design.security.zero_trust else '[Network segmentation strategy]' }}
{% endif %}

### Data Protection
- **Encryption at Rest**: {{ technical_design.security.encryption_at_rest | default('[AES-256, etc.]') }}
- **Encryption in Transit**: {{ technical_design.security.encryption_in_transit | default('[TLS 1.3, etc.]') }}
- **Key Management**: {{ technical_design.security.key_management | default('[How encryption keys are managed]') }}
- **Data Classification**: {{ technical_design.security.data_classification | default('[Public, Internal, Confidential, Restricted]') }}

{% if sections.technical_design.api_specification %}
## 5. API Specification
### OpenAPI Definition
- **API Version**: {{ technical_design.api.version | default('1.0.0') }}
- **Base URL**: {{ technical_design.api.base_url | default('https://api.example.com') }}
- **Authentication**: {{ technical_design.api.auth | default('Bearer Token') }}

### Contract Testing
- **Testing Framework**: {{ technical_design.api.contract_testing.framework | default('[Pact, etc.]') if technical_design.api.contract_testing else '[Pact, etc.]' }}
- **Consumer Contracts**: {{ technical_design.api.contract_testing.consumers | default('[List of consumers]') if technical_design.api.contract_testing else '[List of consumers]' }}
- **Provider Contracts**: {{ technical_design.api.contract_testing.providers | default('[List of providers]') if technical_design.api.contract_testing else '[List of providers]' }}

### API Endpoints
| Method | Endpoint | Description | Request Body | Response | Status Codes |
|--------|----------|-------------|--------------|----------|--------------|
{% for endpoint in technical_design.api.endpoints %}
| {{ endpoint.method }} | {{ endpoint.path }} | {{ endpoint.description }} | {{ endpoint.request_body | default('N/A') }} | {{ endpoint.response }} | {{ endpoint.status_codes }} |
{% endfor %}

### API Versioning
- **Versioning Strategy**: {{ technical_design.api.versioning.strategy | default('[URL, Header, etc.]') if technical_design.api.versioning else '[URL, Header, etc.]' }}
- **Deprecation Policy**: {{ technical_design.api.versioning.deprecation | default('[How versions are deprecated]') if technical_design.api.versioning else '[How versions are deprecated]' }}
- **Backward Compatibility**: {{ technical_design.api.versioning.compatibility | default('[Compatibility requirements]') if technical_design.api.versioning else '[Compatibility requirements]' }}
{% endif %}

{% if sections.technical_design.accessibility %}
## 6. Accessibility & Inclusivity Design
### WCAG Compliance
- **Level**: {{ technical_design.accessibility.wcag_level | default('AA') }}
- **Screen Reader Support**: {{ technical_design.accessibility.screen_reader | default('[JAWS, NVDA, VoiceOver]') }}
- **Keyboard Navigation**: {{ technical_design.accessibility.keyboard_nav | default('[Full keyboard accessibility]') }}

### ARIA Implementation
- **Landmark Roles**: {{ technical_design.accessibility.aria.landmarks | default('[main, navigation, banner, etc.]') }}
- **Live Regions**: {{ technical_design.accessibility.aria.live_regions | default('[For dynamic content updates]') }}
- **Form Labels**: {{ technical_design.accessibility.aria.form_labels | default('[Proper labeling for form elements]') }}

### Testing Strategy
- **Automated Testing**: {{ technical_design.accessibility.testing.automated | default('[axe-core, WAVE, etc.]') }}
- **Manual Testing**: {{ technical_design.accessibility.testing.manual | default('[Screen reader testing, keyboard testing]') }}
- **User Testing**: {{ technical_design.accessibility.testing.user | default('[Testing with users with disabilities]') }}
{% endif %}

## 7. Performance Requirements
### Response Time Targets
- **API Response**: {{ technical_design.performance.api_response | default('< 200ms') }}
- **Page Load**: {{ technical_design.performance.page_load | default('< 2s') }}
- **Database Queries**: {{ technical_design.performance.db_queries | default('< 100ms') }}

### Throughput Requirements
- **Concurrent Users**: {{ technical_design.performance.concurrent_users | default('1000+') }}
- **Requests per Second**: {{ technical_design.performance.rps | default('1000+') }}
- **Data Processing**: {{ technical_design.performance.data_processing | default('[Throughput requirements]') }}

### Scalability Strategy
- **Horizontal Scaling**: {{ technical_design.performance.scaling.horizontal | default('[How to scale horizontally]') }}
- **Vertical Scaling**: {{ technical_design.performance.scaling.vertical | default('[How to scale vertically]') }}
- **Caching Strategy**: {{ technical_design.performance.caching | default('[Redis, CDN, etc.]') }}

## 8. Integration Architecture
### External Integrations
{% for integration in technical_design.integrations.external %}
#### {{ integration.name }}
- **Purpose**: {{ integration.purpose }}
- **API Endpoint**: {{ integration.endpoint }}
- **Authentication**: {{ integration.auth }}
- **Data Format**: {{ integration.data_format }}
- **Error Handling**: {{ integration.error_handling }}
- **Rate Limiting**: {{ integration.rate_limiting | default('None') }}

{% endfor %}

### Internal Integrations
{% for integration in technical_design.integrations.internal %}
#### {{ integration.name }}
- **Purpose**: {{ integration.purpose }}
- **Communication Method**: {{ integration.communication }}
- **Data Format**: {{ integration.data_format }}
- **Error Handling**: {{ integration.error_handling }}

{% endfor %}

## 9. Deployment Architecture
### Infrastructure Requirements
- **Compute**: {{ technical_design.deployment.compute | default('[CPU, memory, storage requirements]') }}
- **Network**: {{ technical_design.deployment.network | default('[Bandwidth, latency requirements]') }}
- **Storage**: {{ technical_design.deployment.storage | default('[Storage type and capacity]') }}

### CI/CD Pipeline
- **Source Control**: {{ technical_design.deployment.cicd.source_control | default('[Git, GitHub, etc.]') }}
- **Build Process**: {{ technical_design.deployment.cicd.build | default('[Docker, npm, etc.]') }}
- **Testing**: {{ technical_design.deployment.cicd.testing | default('[Unit, integration, e2e tests]') }}
- **Deployment**: {{ technical_design.deployment.cicd.deployment | default('[Blue-green, rolling, etc.]') }}

### Environment Strategy
- **Development**: {{ technical_design.deployment.environments.development | default('[Local development setup]') }}
- **Staging**: {{ technical_design.deployment.environments.staging | default('[Staging environment setup]') }}
- **Production**: {{ technical_design.deployment.environments.production | default('[Production environment setup]') }}

## 10. Monitoring & Observability
### Logging Strategy
- **Log Levels**: {{ technical_design.monitoring.logging.levels | default('[DEBUG, INFO, WARN, ERROR]') }}
- **Log Aggregation**: {{ technical_design.monitoring.logging.aggregation | default('[ELK Stack, Splunk, etc.]') }}
- **Log Retention**: {{ technical_design.monitoring.logging.retention | default('[Retention period]') }}

### Metrics & Monitoring
- **Application Metrics**: {{ technical_design.monitoring.metrics.application | default('[Response time, error rate, etc.]') }}
- **Infrastructure Metrics**: {{ technical_design.monitoring.metrics.infrastructure | default('[CPU, memory, disk, network]') }}
- **Business Metrics**: {{ technical_design.monitoring.metrics.business | default('[User actions, conversions, etc.]') }}

### Alerting
- **Critical Alerts**: {{ technical_design.monitoring.alerting.critical | default('[System down, data loss, etc.]') }}
- **Warning Alerts**: {{ technical_design.monitoring.alerting.warning | default('[Performance degradation, etc.]') }}
- **Notification Channels**: {{ technical_design.monitoring.alerting.channels | default('[Email, Slack, PagerDuty, etc.]') }}

{% if sections.technical_design.architectural_decisions %}
## 11. Architectural Decisions & Future Considerations
### Key Decisions
{% for decision in technical_design.architectural_decisions %}
#### {{ decision.title }}
- **Context**: {{ decision.context }}
- **Decision**: {{ decision.decision }}
- **Rationale**: {{ decision.rationale }}
- **Consequences**: {{ decision.consequences }}
- **Status**: {{ decision.status | default('Active') }}

{% endfor %}

### Future Considerations
- **Technology Evolution**: {{ technical_design.future_considerations.technology | default('[How the system will evolve with technology changes]') }}
- **Scalability Roadmap**: {{ technical_design.future_considerations.scalability | default('[Planned scalability improvements]') }}
- **Feature Extensibility**: {{ technical_design.future_considerations.extensibility | default('[How new features will be added]') }}
{% endif %}

## 12. Key Prompts & Directives for AI
### System Prompts
- **Primary Prompt**: {{ technical_design.ai_prompts.primary | default('You are a senior software architect helping with technical design and implementation.') }}
- **Context Prompts**: {{ technical_design.ai_prompts.context | default('[Additional context for AI agents]') }}

### Prompt Iteration Guidelines
- **Version Control**: {{ technical_design.ai_prompts.version_control | default('[How prompts are versioned and updated]') }}
- **Testing Prompts**: {{ technical_design.ai_prompts.testing | default('[How prompts are tested and validated]') }}
- **Performance Monitoring**: {{ technical_design.ai_prompts.performance | default('[How prompt performance is monitored]') }}

### Ethical Considerations
- **Bias Prevention**: {{ technical_design.ai_prompts.ethics.bias | default('[How to prevent AI bias in technical decisions]') }}
- **Transparency**: {{ technical_design.ai_prompts.ethics.transparency | default('[How AI decisions are made transparent]') }}
- **Human Oversight**: {{ technical_design.ai_prompts.ethics.oversight | default('[Human oversight requirements]') }}

## 13. Appendices
### References
{% for reference in technical_design.references %}
- {{ reference }}
{% endfor %}

### Glossary
{% for term, definition in technical_design.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

### Diagrams
{% for diagram in technical_design.diagrams %}
#### {{ diagram.title }}
```mermaid
{{ diagram.content }}
```

{% endfor %}

---
*This document should be reviewed and updated regularly as the system evolves.*