# {{ project.name }} - Agile Methodology Selection Guide

## Instructions for Creating Agile Methodology Selection Guide
1. **Team Assessment**: Evaluate team size, experience, and working style
2. **Project Analysis**: Understand project characteristics, constraints, and requirements
3. **Stakeholder Needs**: Identify stakeholder expectations and communication requirements
4. **Methodology Comparison**: Compare different agile methodologies against project needs
5. **Decision Framework**: Establish criteria and process for methodology selection
6. **Implementation Planning**: Plan transition strategy and change management
7. **Success Metrics**: Define how methodology success will be measured
8. **Review Process**: Establish regular review cycles for methodology effectiveness
{% if features.cascade %}
9. **Master Index Update**: Update master-index.md when methodology selection or strategy changes
{% endif %}

## Document Information
- **Version**: {{ methodology_selection.version | default('1.0') }}
- **Last Updated**: {{ methodology_selection.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Decision Maker**: {{ methodology_selection.decision_maker | default('[Name]') }}

## Selection Overview

### Purpose
{{ methodology_selection.purpose | default('[Clear statement of why methodology selection matters and what it aims to achieve]') }}

### Decision Criteria
{% for criterion in methodology_selection.decision_criteria %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Weight**: {{ criterion.weight }}%
  - **Measurement**: {{ criterion.measurement }}
  - **Threshold**: {{ criterion.threshold }}
{% endfor %}

### Selection Process
{% for step in methodology_selection.selection_process %}
{{ loop.index }}. {{ step }}
{% endfor %}

## Team Assessment

### Team Characteristics
{% for characteristic in methodology_selection.team_assessment.characteristics %}
#### {{ characteristic.name }}
- **Current State**: {{ characteristic.current_state | default('[Description of current state]') }}
- **Ideal State**: {{ characteristic.ideal_state | default('[Description of ideal state]') }}
- **Gap Analysis**: {{ characteristic.gap_analysis | default('[Analysis of gaps]') }}
- **Impact on Methodology**: {{ characteristic.methodology_impact | default('[How this affects methodology choice]') }}
{% endfor %}

### Team Size Analysis
- **Current Team Size**: {{ methodology_selection.team_assessment.team_size.current | default('[X] members') }}
- **Optimal Team Size**: {{ methodology_selection.team_assessment.team_size.optimal | default('[X] members') }}
- **Growth Plans**: {{ methodology_selection.team_assessment.team_size.growth_plans | default('[Planned team growth]') }}
- **Methodology Implications**: {{ methodology_selection.team_assessment.team_size.methodology_implications | default('[How team size affects methodology choice]') }}

### Experience Level
{% for level in methodology_selection.team_assessment.experience_levels %}
#### {{ level.role }}
- **Agile Experience**: {{ level.agile_experience | default('[Beginner/Intermediate/Advanced]') }}
- **Methodology Experience**: {{ level.methodology_experience | join(', ') }}
- **Training Needs**: {{ level.training_needs | join(', ') }}
- **Support Requirements**: {{ level.support_requirements | join(', ') }}
{% endfor %}

### Working Style Preferences
{% for preference in methodology_selection.team_assessment.working_style %}
- **{{ preference.name }}**: {{ preference.description }}
  - **Team Preference**: {{ preference.team_preference | default('[High/Medium/Low]') }}
  - **Methodology Alignment**: {{ preference.methodology_alignment | join(', ') }}
{% endfor %}

## Project Analysis

### Project Characteristics
{% for characteristic in methodology_selection.project_analysis.characteristics %}
#### {{ characteristic.name }}
- **Description**: {{ characteristic.description }}
- **Current State**: {{ characteristic.current_state | default('[Current project state]') }}
- **Expected Evolution**: {{ characteristic.expected_evolution | default('[How this will change]') }}
- **Methodology Impact**: {{ characteristic.methodology_impact | default('[How this affects methodology choice]') }}
{% endfor %}

### Project Constraints
{% for constraint in methodology_selection.project_analysis.constraints %}
- **{{ constraint.name }}**: {{ constraint.description }}
  - **Impact Level**: {{ constraint.impact_level | default('[High/Medium/Low]') }}
  - **Flexibility**: {{ constraint.flexibility | default('[High/Medium/Low]') }}
  - **Methodology Considerations**: {{ constraint.methodology_considerations | join(', ') }}
{% endfor %}

### Project Timeline
- **Project Duration**: {{ methodology_selection.project_analysis.timeline.duration | default('[X] months') }}
- **Key Milestones**: {{ methodology_selection.project_analysis.timeline.milestones | join(', ') }}
- **Delivery Cadence**: {{ methodology_selection.project_analysis.timeline.delivery_cadence | default('[How often deliverables are needed]') }}
- **Methodology Alignment**: {{ methodology_selection.project_analysis.timeline.methodology_alignment | default('[How timeline affects methodology choice]') }}

### Stakeholder Requirements
{% for stakeholder in methodology_selection.project_analysis.stakeholders %}
#### {{ stakeholder.name }}
- **Role**: {{ stakeholder.role }}
- **Communication Needs**: {{ stakeholder.communication_needs | join(', ') }}
- **Visibility Requirements**: {{ stakeholder.visibility_requirements | join(', ') }}
- **Methodology Preferences**: {{ stakeholder.methodology_preferences | join(', ') }}
{% endfor %}

## Methodology Comparison

### Scrum
#### Overview
{{ methodology_selection.methodology_comparison.scrum.overview | default('[Brief description of Scrum methodology]') }}

#### Key Characteristics
{% for characteristic in methodology_selection.methodology_comparison.scrum.characteristics %}
- **{{ characteristic.name }}**: {{ characteristic.description }}
{% endfor %}

#### Strengths
{% for strength in methodology_selection.methodology_comparison.scrum.strengths %}
- {{ strength }}
{% endfor %}

#### Weaknesses
{% for weakness in methodology_selection.methodology_comparison.scrum.weaknesses %}
- {{ weakness }}
{% endfor %}

#### Best For
{% for scenario in methodology_selection.methodology_comparison.scrum.best_for %}
- {{ scenario }}
{% endfor %}

#### Team Fit Score
- **Overall**: {{ methodology_selection.methodology_comparison.scrum.team_fit_score | default('[X]/10') }}
- **Strengths**: {{ methodology_selection.methodology_comparison.scrum.team_strengths | join(', ') }}
- **Concerns**: {{ methodology_selection.methodology_comparison.scrum.team_concerns | join(', ') }}

### Kanban
#### Overview
{{ methodology_selection.methodology_comparison.kanban.overview | default('[Brief description of Kanban methodology]') }}

#### Key Characteristics
{% for characteristic in methodology_selection.methodology_comparison.kanban.characteristics %}
- **{{ characteristic.name }}**: {{ characteristic.description }}
{% endfor %}

#### Strengths
{% for strength in methodology_selection.methodology_comparison.kanban.strengths %}
- {{ strength }}
{% endfor %}

#### Weaknesses
{% for weakness in methodology_selection.methodology_comparison.kanban.weaknesses %}
- {{ weakness }}
{% endfor %}

#### Best For
{% for scenario in methodology_selection.methodology_comparison.kanban.best_for %}
- {{ scenario }}
{% endfor %}

#### Team Fit Score
- **Overall**: {{ methodology_selection.methodology_comparison.kanban.team_fit_score | default('[X]/10') }}
- **Strengths**: {{ methodology_selection.methodology_comparison.kanban.team_strengths | join(', ') }}
- **Concerns**: {{ methodology_selection.methodology_comparison.kanban.team_concerns | join(', ') }}

### Hybrid Approaches
#### Scrum-Kanban Hybrid
{{ methodology_selection.methodology_comparison.hybrid.scrum_kanban.overview | default('[Description of Scrum-Kanban hybrid approach]') }}

##### Key Characteristics
{% for characteristic in methodology_selection.methodology_comparison.hybrid.scrum_kanban.characteristics %}
- **{{ characteristic.name }}**: {{ characteristic.description }}
{% endfor %}

##### Best For
{% for scenario in methodology_selection.methodology_comparison.hybrid.scrum_kanban.best_for %}
- {{ scenario }}
{% endfor %}

##### Team Fit Score
- **Overall**: {{ methodology_selection.methodology_comparison.hybrid.scrum_kanban.team_fit_score | default('[X]/10') }}

#### Custom Hybrid
{{ methodology_selection.methodology_comparison.hybrid.custom.overview | default('[Description of custom hybrid approach]') }}

##### Key Characteristics
{% for characteristic in methodology_selection.methodology_comparison.hybrid.custom.characteristics %}
- **{{ characteristic.name }}**: {{ characteristic.description }}
{% endfor %}

##### Best For
{% for scenario in methodology_selection.methodology_comparison.hybrid.custom.best_for %}
- {{ scenario }}
{% endfor %}

##### Team Fit Score
- **Overall**: {{ methodology_selection.methodology_comparison.hybrid.custom.team_fit_score | default('[X]/10') }}

## Decision Matrix

### Scoring Criteria
{% for criterion in methodology_selection.decision_matrix.criteria %}
#### {{ criterion.name }}
- **Weight**: {{ criterion.weight }}%
- **Description**: {{ criterion.description }}
- **Scoring Scale**: {{ criterion.scoring_scale | default('[1-5 scale]') }}
- **Measurement Method**: {{ criterion.measurement_method }}
{% endfor %}

### Methodology Scores
{% for methodology in methodology_selection.decision_matrix.scores %}
#### {{ methodology.name }}
{% for criterion in methodology.criteria_scores %}
- **{{ criterion.name }}**: {{ criterion.score }}/{{ criterion.max_score }} ({{ criterion.weighted_score }})
{% endfor %}
- **Total Weighted Score**: {{ methodology.total_score }}
- **Rank**: {{ methodology.rank }}
{% endfor %}

### Decision Rationale
{{ methodology_selection.decision_matrix.rationale | default('[Explanation of why the selected methodology was chosen]') }}

## Implementation Planning

### Transition Strategy
{% for phase in methodology_selection.implementation.transition_strategy %}
#### Phase {{ phase.number }}: {{ phase.name }}
- **Duration**: {{ phase.duration | default('[X] weeks') }}
- **Objectives**: {{ phase.objectives | join(', ') }}
- **Key Activities**: {{ phase.key_activities | join(', ') }}
- **Success Criteria**: {{ phase.success_criteria | join(', ') }}
- **Risks**: {{ phase.risks | join(', ') }}
- **Mitigation**: {{ phase.mitigation | join(', ') }}
{% endfor %}

### Change Management
{% for aspect in methodology_selection.implementation.change_management %}
#### {{ aspect.name }}
- **Description**: {{ aspect.description }}
- **Owner**: {{ aspect.owner | default('[Name]') }}
- **Timeline**: {{ aspect.timeline | default('[When this will be done]') }}
- **Success Criteria**: {{ aspect.success_criteria | join(', ') }}
{% endfor %}

### Training Plan
{% for training in methodology_selection.implementation.training_plan %}
#### {{ training.name }}
- **Audience**: {{ training.audience | join(', ') }}
- **Duration**: {{ training.duration | default('[X] hours') }}
- **Format**: {{ training.format | default('[In-person/Online/Blended]') }}
- **Content**: {{ training.content | join(', ') }}
- **Timeline**: {{ training.timeline | default('[When training will occur]') }}
{% endfor %}

### Support Structure
{% for support in methodology_selection.implementation.support_structure %}
- **{{ support.name }}**: {{ support.description }}
  - **Provider**: {{ support.provider | default('[Who provides this support]') }}
  - **Availability**: {{ support.availability | default('[When support is available]') }}
  - **Contact**: {{ support.contact | default('[How to access support]') }}
{% endfor %}

## Success Metrics

### Methodology Effectiveness
{% for metric in methodology_selection.success_metrics.methodology_effectiveness %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Owner**: {{ metric.owner | default('[Who is responsible]') }}
{% endfor %}

### Team Performance
{% for metric in methodology_selection.success_metrics.team_performance %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Owner**: {{ metric.owner | default('[Who is responsible]') }}
{% endfor %}

### Project Outcomes
{% for metric in methodology_selection.success_metrics.project_outcomes %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Owner**: {{ metric.owner | default('[Who is responsible]') }}
{% endfor %}

## Risk Management

### Implementation Risks
{% for risk in methodology_selection.risk_management.implementation_risks %}
#### {{ risk.name }}
- **Description**: {{ risk.description }}
- **Probability**: {{ risk.probability | default('[High/Medium/Low]') }}
- **Impact**: {{ risk.impact | default('[High/Medium/Low]') }}
- **Mitigation**: {{ risk.mitigation | join(', ') }}
- **Owner**: {{ risk.owner | default('[Name]') }}
{% endfor %}

### Methodology Risks
{% for risk in methodology_selection.risk_management.methodology_risks %}
#### {{ risk.name }}
- **Description**: {{ risk.description }}
- **Probability**: {{ risk.probability | default('[High/Medium/Low]') }}
- **Impact**: {{ risk.impact | default('[High/Medium/Low]') }}
- **Mitigation**: {{ risk.mitigation | join(', ') }}
- **Owner**: {{ risk.owner | default('[Name]') }}
{% endfor %}

### Contingency Plans
{% for plan in methodology_selection.risk_management.contingency_plans %}
#### {{ plan.name }}
- **Trigger**: {{ plan.trigger | default('[What triggers this plan]') }}
- **Response**: {{ plan.response | default('[What to do when triggered]') }}
- **Owner**: {{ plan.owner | default('[Name]') }}
- **Timeline**: {{ plan.timeline | default('[How quickly to respond]') }}
{% endfor %}

## Review & Adaptation

### Review Schedule
{% for review in methodology_selection.review_adaptation.review_schedule %}
- **{{ review.name }}**: {{ review.description }}
  - **Frequency**: {{ review.frequency | default('[How often]') }}
  - **Participants**: {{ review.participants | join(', ') }}
  - **Focus Areas**: {{ review.focus_areas | join(', ') }}
  - **Outcomes**: {{ review.outcomes | join(', ') }}
{% endfor %}

### Adaptation Process
{% for step in methodology_selection.review_adaptation.adaptation_process %}
{{ loop.index }}. {{ step }}
{% endfor %}

### Continuous Improvement
{% for improvement in methodology_selection.review_adaptation.continuous_improvement %}
- **{{ improvement.name }}**: {{ improvement.description }}
  - **Implementation**: {{ improvement.implementation | default('[How to implement]') }}
  - **Timeline**: {{ improvement.timeline | default('[When to implement]') }}
  - **Success Criteria**: {{ improvement.success_criteria | join(', ') }}
{% endfor %}

## Appendices

### References
{% for reference in methodology_selection.references %}
- {{ reference }}
{% endfor %}

### Tools & Resources
{% for tool in methodology_selection.tools %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Purpose**: {{ tool.purpose | default('[What this tool is used for]') }}
  - **Usage**: {{ tool.usage | default('[How to use this tool]') }}
  - **Integration**: {{ tool.integration | default('[How it integrates with other tools]') }}
{% endfor %}

### Templates
{% for template in methodology_selection.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in methodology_selection.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This methodology selection guide should be reviewed and updated regularly as team dynamics and project requirements evolve.*
