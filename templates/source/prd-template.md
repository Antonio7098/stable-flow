# {{ project.name }} - Product Requirements Document

## Instructions for Creating a PRD
1. **Stakeholder Alignment**: Ensure all stakeholders are identified and consulted
2. **User Research**: Conduct user research and define clear user personas
3. **Market Analysis**: Research competitors and market opportunities
4. **Feature Prioritization**: Use MoSCoW method (Must/Should/Could/Won't) for feature prioritization
5. **Clear Requirements**: Write specific, measurable, achievable requirements
6. **Success Metrics**: Define quantifiable success criteria and KPIs
7. **Timeline Planning**: Create realistic timeline with buffer for unknowns
8. **Risk Assessment**: Identify and plan mitigation for key risks
9. **Dependencies**: Map all internal and external dependencies
{% if features.cascade %}
10. **Master Index Update**: Update master-index.md with any new cross-references or document changes
{% endif %}
11. **Review Process**: Plan regular review cycles with stakeholders

## Document Information
- **Version**: {{ prd.version | default('1.0') }}
- **Last Updated**: {{ prd.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Stakeholders**: {{ prd.stakeholders | default('[List of stakeholders]') }}

## 1. Product Overview
### Vision
{{ prd.vision | default('[Clear statement of what the product aims to achieve]') }}

### Goals & Success Metrics
- **Primary Goal**: {{ prd.primary_goal | default('[Main objective]') }}
- **Success Metrics**: {{ prd.success_metrics | default('[How success is measured]') }}
- **Target Users**: {{ prd.target_users | default('[Primary user personas]') }}

{% if sections.prd.competitive_analysis %}
### Competitive Analysis
#### Competitors
{% for competitor in prd.competitors %}
- **{{ competitor.name }}**: **Strengths**: {{ competitor.strengths }} - **Weaknesses**: {{ competitor.weaknesses }} - **Market Position**: {{ competitor.market_position }}
{% endfor %}

#### Market Opportunities
{% for opportunity in prd.market_opportunities %}
- **{{ opportunity.name }}**: {{ opportunity.description }} - **Our Advantage**: {{ opportunity.advantage }}
{% endfor %}

#### Persona Details
{% for persona in prd.personas %}
- **{{ persona.name }}**: **Demographics**: {{ persona.demographics }} - **Pain Points**: {{ persona.pain_points }} - **Journey Map**: {{ persona.journey_map }}
{% endfor %}
{% endif %}

## 2. Core Features
### Feature Matrix
| Feature | Priority | Status | Description | Acceptance Criteria |
|---------|----------|--------|-------------|-------------------|
{% for feature in prd.features %}
| {{ feature.name }} | {{ feature.priority }} | {{ feature.status }} | {{ feature.description }} | {{ feature.acceptance_criteria }} |
{% endfor %}

### MVP Planning
#### MVP Features
{% for mvp_feature in prd.mvp_features %}
- **{{ mvp_feature.name }}**: {{ mvp_feature.description }}
  - **User Story**: {{ mvp_feature.user_story }}
  - **Acceptance Criteria**: {{ mvp_feature.acceptance_criteria }}
  - **Dependencies**: {{ mvp_feature.dependencies }}
{% endfor %}

#### Post-MVP Features
{% for post_mvp_feature in prd.post_mvp_features %}
- **{{ post_mvp_feature.name }}**: {{ post_mvp_feature.description }}
  - **Target Release**: {{ post_mvp_feature.target_release }}
  - **Dependencies**: {{ post_mvp_feature.dependencies }}
{% endfor %}

{% if sections.prd.user_experience %}
## 3. User Experience Requirements
### Wireframes & Prototypes
- **Low-fidelity Wireframes**: {{ prd.wireframes.low_fidelity | default('[Link to wireframes]') if prd.wireframes else '[Link to wireframes]' }}
- **High-fidelity Prototypes**: {{ prd.wireframes.high_fidelity | default('[Link to prototypes]') if prd.wireframes else '[Link to prototypes]' }}
- **User Flow Diagrams**: {{ prd.wireframes.user_flows | default('[Link to flow diagrams]') if prd.wireframes else '[Link to flow diagrams]' }}

### A/B Testing Plan
{% for test in prd.ab_tests %}
- **Test {{ loop.index }}**: {{ test.name }}
  - **Hypothesis**: {{ test.hypothesis }}
  - **Success Metrics**: {{ test.success_metrics }}
  - **Duration**: {{ test.duration }}
{% endfor %}

### Internationalization
- **Supported Languages**: {{ prd.i18n.supported_languages | default('[List of languages]') if prd.i18n else '[List of languages]' }}
- **RTL Support**: {{ prd.i18n.rtl_support | default('[Yes/No]') if prd.i18n else '[Yes/No]' }}
- **Cultural Considerations**: {{ prd.i18n.cultural_considerations | default('[List of considerations]') if prd.i18n else '[List of considerations]' }}
{% endif %}

{% if sections.prd.data_strategy %}
## 4. Data Strategy
### Data Collection
- **Data Sources**: {{ prd.data.sources | default('[List of data sources]') }}
- **Collection Methods**: {{ prd.data.collection_methods | default('[How data is collected]') }}
- **Privacy Compliance**: {{ prd.data.privacy_compliance | default('[GDPR, CCPA, etc.]') }}

### Data Governance
- **Data Quality Standards**: {{ prd.data.quality_standards | default('[Standards for data quality]') }}
- **Retention Policies**: {{ prd.data.retention_policies | default('[How long data is kept]') }}
- **Access Controls**: {{ prd.data.access_controls | default('[Who can access what data]') }}
{% endif %}

{% if sections.prd.competitive_moat %}
## 5. Competitive Moat
### Defensibility
- **Technical Barriers**: {{ prd.moat.technical_barriers | default('[What makes it hard to replicate]') }}
- **Network Effects**: {{ prd.moat.network_effects | default('[How value increases with users]') }}
- **Switching Costs**: {{ prd.moat.switching_costs | default('[Cost to switch to competitor]') }}

### Competitive Advantages
{% for advantage in prd.competitive_advantages %}
- **{{ advantage.name }}**: {{ advantage.description }}
  - **Sustainability**: {{ advantage.sustainability }}
  - **Replicability**: {{ advantage.replicability }}
{% endfor %}
{% endif %}

{% if sections.prd.monetization %}
## 6. Monetization Model
### Revenue Streams
{% for stream in prd.revenue_streams %}
- **{{ stream.name }}**: {{ stream.description }}
  - **Pricing Model**: {{ stream.pricing_model }}
  - **Target Revenue**: {{ stream.target_revenue }}
  - **Timeline**: {{ stream.timeline }}
{% endfor %}

### Pricing Strategy
- **Pricing Tiers**: {{ prd.pricing.tiers | default('[List of pricing tiers]') }}
- **Competitive Positioning**: {{ prd.pricing.competitive_positioning | default('[How we compare to competitors]') }}
- **Value Proposition**: {{ prd.pricing.value_proposition | default('[Why customers will pay]') }}
{% endif %}

## 7. Technical Requirements
### Performance Requirements
- **Response Time**: {{ prd.technical.performance.response_time | default('[Target response times]') }}
- **Throughput**: {{ prd.technical.performance.throughput | default('[Requests per second]') }}
- **Availability**: {{ prd.technical.performance.availability | default('[Uptime requirements]') }}

### Security Requirements
- **Authentication**: {{ prd.technical.security.authentication | default('[Auth requirements]') }}
- **Data Protection**: {{ prd.technical.security.data_protection | default('[Data security requirements]') }}
- **Compliance**: {{ prd.technical.security.compliance | default('[Regulatory compliance]') }}

### Integration Requirements
{% for integration in prd.technical.integrations %}
- **{{ integration.name }}**: {{ integration.description }}
  - **API Requirements**: {{ integration.api_requirements }}
  - **Data Format**: {{ integration.data_format }}
{% endfor %}

## 8. Timeline & Milestones
### Development Phases
{% for phase in prd.timeline.phases %}
- **{{ phase.name }}**: {{ phase.description }}
  - **Duration**: {{ phase.duration }}
  - **Deliverables**: {{ phase.deliverables }}
  - **Dependencies**: {{ phase.dependencies }}
{% endfor %}

### Key Milestones
{% for milestone in prd.timeline.milestones %}
- **{{ milestone.date }}**: {{ milestone.name }}
  - **Description**: {{ milestone.description }}
  - **Success Criteria**: {{ milestone.success_criteria }}
{% endfor %}

## 9. Risk Assessment
### Technical Risks
{% for risk in prd.risks.technical %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Probability**: {{ risk.probability }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
{% endfor %}

### Business Risks
{% for risk in prd.risks.business %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Probability**: {{ risk.probability }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
{% endfor %}

## 10. Success Metrics & KPIs
### Primary KPIs
{% for kpi in prd.kpis.primary %}
- **{{ kpi.name }}**: {{ kpi.description }}
  - **Target**: {{ kpi.target }}
  - **Measurement**: {{ kpi.measurement }}
  - **Timeline**: {{ kpi.timeline }}
{% endfor %}

### Secondary KPIs
{% for kpi in prd.kpis.secondary %}
- **{{ kpi.name }}**: {{ kpi.description }}
  - **Target**: {{ kpi.target }}
  - **Measurement**: {{ kpi.measurement }}
{% endfor %}

## 11. Dependencies & Assumptions
### External Dependencies
{% for dependency in prd.dependencies.external %}
- **{{ dependency.name }}**: {{ dependency.description }}
  - **Owner**: {{ dependency.owner }}
  - **Timeline**: {{ dependency.timeline }}
  - **Risk Level**: {{ dependency.risk_level }}
{% endfor %}

### Internal Dependencies
{% for dependency in prd.dependencies.internal %}
- **{{ dependency.name }}**: {{ dependency.description }}
  - **Owner**: {{ dependency.owner }}
  - **Timeline**: {{ dependency.timeline }}
{% endfor %}

### Key Assumptions
{% for assumption in prd.assumptions %}
- **{{ assumption.name }}**: {{ assumption.description }}
  - **Validation Method**: {{ assumption.validation_method }}
  - **Risk if Wrong**: {{ assumption.risk_if_wrong }}
{% endfor %}

## 12. Appendices
### References
{% for reference in prd.references %}
- {{ reference }}
{% endfor %}

### Glossary
{% for term, definition in prd.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This document should be reviewed and updated regularly as the product evolves.*