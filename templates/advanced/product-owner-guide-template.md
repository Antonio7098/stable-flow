# {{ project.name }} - Product Owner Guide

## Instructions for Creating Product Owner Guide
1. **Product Vision**: Define clear product vision and strategic direction
2. **Stakeholder Mapping**: Identify all stakeholders and their needs
3. **Backlog Management**: Establish effective backlog grooming and prioritization processes
4. **User Story Standards**: Define consistent user story writing and acceptance criteria
5. **Release Planning**: Plan product releases and roadmap alignment
6. **Decision Framework**: Establish criteria for product decisions and trade-offs
7. **Communication Strategy**: Define how to communicate with development team and stakeholders
8. **Metrics & Success**: Define product success metrics and measurement approach
9. **Risk Management**: Identify and manage product-related risks
{% if features.cascade %}
10. **Master Index Update**: Update master-index.md when product strategy or roadmap changes
{% endif %}

## Document Information
- **Version**: {{ product_owner_guide.version | default('1.0') }}
- **Last Updated**: {{ product_owner_guide.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Product Owner**: {{ product_owner_guide.product_owner | default('[Name]') }}

## Product Owner Role Overview

### Core Responsibilities
{% for responsibility in product_owner_guide.core_responsibilities %}
- **{{ responsibility.title }}**: {{ responsibility.description }}
  - **Key Activities**: {{ responsibility.activities | join(', ') }}
  - **Success Metrics**: {{ responsibility.metrics | join(', ') }}
  - **Stakeholders**: {{ responsibility.stakeholders | join(', ') }}
{% endfor %}

### Decision Authority
{% for authority in product_owner_guide.decision_authority %}
- **{{ authority.area }}**: {{ authority.description }}
  - **Decision Criteria**: {{ authority.criteria | join(', ') }}
  - **Escalation Path**: {{ authority.escalation_path }}
{% endfor %}

## Product Vision & Strategy

### Product Vision
{{ product_owner_guide.product_vision.statement | default('[Clear, inspiring product vision statement]') }}

### Product Goals
{% for goal in product_owner_guide.product_goals %}
- **{{ goal.name }}**: {{ goal.description }}
  - **Success Metrics**: {{ goal.success_metrics | join(', ') }}
  - **Timeline**: {{ goal.timeline }}
  - **Priority**: {{ goal.priority }}
{% endfor %}

### Target Market
{% for segment in product_owner_guide.target_market %}
#### {{ segment.name }}
- **Description**: {{ segment.description }}
- **Size**: {{ segment.size }}
- **Pain Points**: {{ segment.pain_points | join(', ') }}
- **Value Proposition**: {{ segment.value_proposition }}
{% endfor %}

### Competitive Landscape
{% for competitor in product_owner_guide.competitive_landscape %}
#### {{ competitor.name }}
- **Strengths**: {{ competitor.strengths | join(', ') }}
- **Weaknesses**: {{ competitor.weaknesses | join(', ') }}
- **Market Position**: {{ competitor.market_position }}
- **Our Differentiation**: {{ competitor.our_differentiation }}
{% endfor %}

## Stakeholder Management

### Stakeholder Map
{% for stakeholder in product_owner_guide.stakeholder_map %}
#### {{ stakeholder.name }}
- **Role**: {{ stakeholder.role }}
- **Influence**: {{ stakeholder.influence | default('[High/Medium/Low]') }}
- **Interest**: {{ stakeholder.interest | default('[High/Medium/Low]') }}
- **Communication Needs**: {{ stakeholder.communication_needs | join(', ') }}
- **Key Concerns**: {{ stakeholder.key_concerns | join(', ') }}
{% endfor %}

### Communication Plan
{% for channel in product_owner_guide.communication_plan %}
#### {{ channel.name }}
- **Purpose**: {{ channel.purpose }}
- **Frequency**: {{ channel.frequency }}
- **Participants**: {{ channel.participants | join(', ') }}
- **Format**: {{ channel.format }}
- **Key Messages**: {{ channel.key_messages | join(', ') }}
{% endfor %}

### Feedback Collection
{% for method in product_owner_guide.feedback_collection %}
- **{{ method.name }}**: {{ method.description }}
  - **Frequency**: {{ method.frequency }}
  - **Participants**: {{ method.participants | join(', ') }}
  - **Process**: {{ method.process }}
  - **Integration**: {{ method.integration }}
{% endfor %}

## Backlog Management

### Backlog Structure
{% for level in product_owner_guide.backlog_structure %}
#### {{ level.name }}
- **Description**: {{ level.description }}
- **Granularity**: {{ level.granularity }}
- **Time Horizon**: {{ level.time_horizon }}
- **Examples**: {{ level.examples | join(', ') }}
{% endfor %}

### Prioritization Framework
#### {{ product_owner_guide.prioritization.framework_name }}
- **Description**: {{ product_owner_guide.prioritization.description }}
- **Criteria**: {{ product_owner_guide.prioritization.criteria | join(', ') }}
- **Scoring Method**: {{ product_owner_guide.prioritization.scoring_method }}
- **Review Frequency**: {{ product_owner_guide.prioritization.review_frequency }}

### Prioritization Matrix
{% for dimension in product_owner_guide.prioritization.matrix_dimensions %}
- **{{ dimension.name }}**: {{ dimension.description }}
  - **Weight**: {{ dimension.weight }}%
  - **Scale**: {{ dimension.scale }}
  - **Examples**: {{ dimension.examples | join(', ') }}
{% endfor %}

### Backlog Grooming Process
1. **Preparation**: {{ product_owner_guide.backlog_grooming.preparation }}
2. **Review**: {{ product_owner_guide.backlog_grooming.review }}
3. **Refinement**: {{ product_owner_guide.backlog_grooming.refinement }}
4. **Estimation**: {{ product_owner_guide.backlog_grooming.estimation }}
5. **Prioritization**: {{ product_owner_guide.backlog_grooming.prioritization }}
6. **Documentation**: {{ product_owner_guide.backlog_grooming.documentation }}

## User Story Management

### User Story Template
```
As a [user type]
I want [functionality]
So that [benefit/value]

Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

Definition of Done:
- [ ] [DoD item 1]
- [ ] [DoD item 2]
- [ ] [DoD item 3]
```

### User Story Standards
{% for standard in product_owner_guide.user_story_standards %}
- **{{ standard.name }}**: {{ standard.description }}
  - **Requirements**: {{ standard.requirements | join(', ') }}
  - **Examples**: {{ standard.examples | join(', ') }}
{% endfor %}

### Acceptance Criteria Guidelines
{% for guideline in product_owner_guide.acceptance_criteria_guidelines %}
- **{{ guideline.name }}**: {{ guideline.description }}
  - **Format**: {{ guideline.format }}
  - **Best Practices**: {{ guideline.best_practices | join(', ') }}
  - **Common Pitfalls**: {{ guideline.common_pitfalls | join(', ') }}
{% endfor %}

### Definition of Ready
{% for criterion in product_owner_guide.definition_of_ready %}
- [ ] {{ criterion }}
{% endfor %}

### Definition of Done
{% for criterion in product_owner_guide.definition_of_done %}
- [ ] {{ criterion }}
{% endfor %}

## Release Planning

### Release Strategy
- **Release Cadence**: {{ product_owner_guide.release_planning.cadence }}
- **Release Types**: {{ product_owner_guide.release_planning.types | join(', ') }}
- **Quality Gates**: {{ product_owner_guide.release_planning.quality_gates | join(', ') }}
- **Rollback Strategy**: {{ product_owner_guide.release_planning.rollback_strategy }}

### Release Roadmap
{% for release in product_owner_guide.release_roadmap %}
#### {{ release.name }}
- **Target Date**: {{ release.target_date }}
- **Key Features**: {{ release.key_features | join(', ') }}
- **Success Metrics**: {{ release.success_metrics | join(', ') }}
- **Dependencies**: {{ release.dependencies | join(', ') }}
- **Risks**: {{ release.risks | join(', ') }}
{% endfor %}

### Feature Flags Strategy
{% for flag in product_owner_guide.feature_flags %}
- **{{ flag.name }}**: {{ flag.description }}
  - **Purpose**: {{ flag.purpose }}
  - **Rollout Plan**: {{ flag.rollout_plan }}
  - **Success Criteria**: {{ flag.success_criteria }}
  - **Rollback Criteria**: {{ flag.rollback_criteria }}
{% endfor %}

## Sprint Planning & Execution

### Sprint Planning Preparation
{% for prep in product_owner_guide.sprint_planning.preparation %}
- {{ prep }}
{% endfor %}

### Sprint Goal Setting
{% for guideline in product_owner_guide.sprint_goal_guidelines %}
- **{{ guideline.name }}**: {{ guideline.description }}
  - **Criteria**: {{ guideline.criteria | join(', ') }}
  - **Examples**: {{ guideline.examples | join(', ') }}
{% endfor %}

### Sprint Review Facilitation
{% for activity in product_owner_guide.sprint_review.activities %}
- **{{ activity.name }}**: {{ activity.description }}
  - **Duration**: {{ activity.duration }}
  - **Participants**: {{ activity.participants | join(', ') }}
  - **Outcomes**: {{ activity.outcomes | join(', ') }}
{% endfor %}

## Metrics & Success Measurement

### Product Metrics
{% for metric in product_owner_guide.product_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Frequency**: {{ metric.frequency }}
- **Target**: {{ metric.target }}
- **Data Source**: {{ metric.data_source }}
{% endfor %}

### User Experience Metrics
{% for metric in product_owner_guide.ux_metrics %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Measurement Method**: {{ metric.measurement_method }}
  - **Target Value**: {{ metric.target_value }}
  - **Frequency**: {{ metric.frequency }}
{% endfor %}

### Business Impact Metrics
{% for metric in product_owner_guide.business_metrics %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Calculation**: {{ metric.calculation }}
  - **Target**: {{ metric.target }}
  - **Timeline**: {{ metric.timeline }}
{% endfor %}

## Risk Management

### Product Risks
{% for risk in product_owner_guide.product_risks %}
#### {{ risk.name }}
- **Description**: {{ risk.description }}
- **Probability**: {{ risk.probability | default('[High/Medium/Low]') }}
- **Impact**: {{ risk.impact | default('[High/Medium/Low]') }}
- **Mitigation**: {{ risk.mitigation }}
- **Owner**: {{ risk.owner }}
{% endfor %}

### Market Risks
{% for risk in product_owner_guide.market_risks %}
#### {{ risk.name }}
- **Description**: {{ risk.description }}
- **Probability**: {{ risk.probability | default('[High/Medium/Low]') }}
- **Impact**: {{ risk.impact | default('[High/Medium/Low]') }}
- **Mitigation**: {{ risk.mitigation }}
- **Monitoring**: {{ risk.monitoring }}
{% endfor %}

### Technical Risks
{% for risk in product_owner_guide.technical_risks %}
#### {{ risk.name }}
- **Description**: {{ risk.description }}
- **Probability**: {{ risk.probability | default('[High/Medium/Low]') }}
- **Impact**: {{ risk.impact | default('[High/Medium/Low]') }}
- **Mitigation**: {{ risk.mitigation }}
- **Escalation**: {{ risk.escalation }}
{% endfor %}

## Decision Making Framework

### Decision Criteria
{% for criterion in product_owner_guide.decision_criteria %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Weight**: {{ criterion.weight }}%
  - **Measurement**: {{ criterion.measurement }}
  - **Threshold**: {{ criterion.threshold }}
{% endfor %}

### Decision Process
1. **Problem Definition**: {{ product_owner_guide.decision_process.problem_definition }}
2. **Information Gathering**: {{ product_owner_guide.decision_process.information_gathering }}
3. **Option Analysis**: {{ product_owner_guide.decision_process.option_analysis }}
4. **Stakeholder Input**: {{ product_owner_guide.decision_process.stakeholder_input }}
5. **Decision**: {{ product_owner_guide.decision_process.decision }}
6. **Communication**: {{ product_owner_guide.decision_process.communication }}
7. **Implementation**: {{ product_owner_guide.decision_process.implementation }}

### Escalation Process
{% for level in product_owner_guide.escalation_process %}
#### {{ level.name }}
- **Triggers**: {{ level.triggers | join(', ') }}
- **Process**: {{ level.process }}
- **Timeline**: {{ level.timeline }}
- **Decision Authority**: {{ level.decision_authority }}
{% endfor %}

## Tools & Technology

### Backlog Management Tools
{% for tool in product_owner_guide.tools.backlog_management %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Features**: {{ tool.features | join(', ') }}
  - **Configuration**: {{ tool.configuration }}
  - **Integration**: {{ tool.integration }}
{% endfor %}

### Analytics & Metrics Tools
{% for tool in product_owner_guide.tools.analytics %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Metrics Tracked**: {{ tool.metrics | join(', ') }}
  - **Reporting**: {{ tool.reporting }}
  - **Dashboard**: {{ tool.dashboard }}
{% endfor %}

### Communication Tools
{% for tool in product_owner_guide.tools.communication %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Use Cases**: {{ tool.use_cases | join(', ') }}
  - **Best Practices**: {{ tool.best_practices | join(', ') }}
{% endfor %}

## Continuous Improvement

### Product Owner Development
{% for area in product_owner_guide.continuous_improvement.development_areas %}
- **{{ area.name }}**: {{ area.description }}
  - **Current Level**: {{ area.current_level }}
  - **Target Level**: {{ area.target_level }}
  - **Development Plan**: {{ area.development_plan }}
  - **Timeline**: {{ area.timeline }}
{% endfor %}

### Process Improvements
{% for improvement in product_owner_guide.continuous_improvement.process_improvements %}
- **{{ improvement.name }}**: {{ improvement.description }}
  - **Implementation Plan**: {{ improvement.implementation_plan }}
  - **Expected Benefits**: {{ improvement.expected_benefits }}
  - **Success Metrics**: {{ improvement.success_metrics | join(', ') }}
{% endfor %}

### Learning & Development
{% for learning in product_owner_guide.continuous_improvement.learning %}
- **{{ learning.name }}**: {{ learning.description }}
  - **Format**: {{ learning.format }}
  - **Timeline**: {{ learning.timeline }}
  - **Success Criteria**: {{ learning.success_criteria }}
{% endfor %}

## Appendices

### References
{% for reference in product_owner_guide.references %}
- {{ reference }}
{% endfor %}

### Templates
{% for template in product_owner_guide.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in product_owner_guide.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This Product Owner Guide should be reviewed and updated regularly as product strategy and market conditions evolve.*
