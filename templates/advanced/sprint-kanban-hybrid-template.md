# {{ project.name }} - Sprint-Kanban Hybrid Framework

## Instructions for Creating Sprint-Kanban Hybrid Framework
1. **Framework Design**: Define how Scrum and Kanban elements will be combined
2. **Sprint Structure**: Establish time-boxed sprint cycles with Kanban flow principles
3. **Board Configuration**: Set up hybrid board that supports both sprint and flow work
4. **Ceremony Adaptation**: Modify Scrum ceremonies to work with Kanban principles
5. **Metrics Integration**: Combine Scrum and Kanban metrics for comprehensive tracking
6. **Team Training**: Ensure team understands hybrid approach and responsibilities
7. **Process Documentation**: Document hybrid processes and decision points
8. **Continuous Improvement**: Establish regular review cycles for framework optimization
{% if features.cascade %}
9. **Master Index Update**: Update master-index.md when hybrid framework or processes change
{% endif %}

## Document Information
- **Version**: {{ hybrid_framework.version | default('1.0') }}
- **Last Updated**: {{ hybrid_framework.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Framework Owner**: {{ hybrid_framework.framework_owner | default('[Name]') }}

## Hybrid Framework Overview

### Framework Purpose
{{ hybrid_framework.purpose | default('[Clear statement of why this hybrid approach is being used and what it aims to achieve]') }}

### Core Principles
{% for principle in hybrid_framework.core_principles %}
- **{{ principle.name }}**: {{ principle.description }}
  - **Scrum Element**: {{ principle.scrum_element | default('[How this relates to Scrum]') }}
  - **Kanban Element**: {{ principle.kanban_element | default('[How this relates to Kanban]') }}
{% endfor %}

### Framework Benefits
{% for benefit in hybrid_framework.benefits %}
- **{{ benefit.name }}**: {{ benefit.description }}
  - **Scrum Contribution**: {{ benefit.scrum_contribution | default('[How Scrum contributes to this benefit]') }}
  - **Kanban Contribution**: {{ benefit.kanban_contribution | default('[How Kanban contributes to this benefit]') }}
{% endfor %}

## Sprint Structure

### Sprint Cycle
- **Sprint Length**: {{ hybrid_framework.sprint_structure.length | default('[X] weeks') }}
- **Sprint Goal**: {{ hybrid_framework.sprint_structure.goal_approach | default('[How sprint goals are set and managed]') }}
- **Planning Approach**: {{ hybrid_framework.sprint_structure.planning_approach | default('[How sprint planning works in hybrid]') }}
- **Review Process**: {{ hybrid_framework.sprint_structure.review_process | default('[How sprint reviews are conducted]') }}

### Sprint Planning
#### Preparation
{% for prep in hybrid_framework.sprint_planning.preparation %}
- {{ prep }}
{% endfor %}

#### Planning Process
{% for step in hybrid_framework.sprint_planning.process %}
{{ loop.index }}. {{ step }}
{% endfor %}

#### Kanban Integration
{% for integration in hybrid_framework.sprint_planning.kanban_integration %}
- **{{ integration.name }}**: {{ integration.description }}
  - **Process**: {{ integration.process }}
  - **Benefits**: {{ integration.benefits | join(', ') }}
{% endfor %}

### Sprint Execution
#### Daily Flow
{% for activity in hybrid_framework.sprint_execution.daily_flow %}
- **{{ activity.name }}**: {{ activity.description }}
  - **Time**: {{ activity.time | default('[When this happens]') }}
  - **Participants**: {{ activity.participants | join(', ') }}
  - **Purpose**: {{ activity.purpose }}
{% endfor %}

#### Work Management
{% for aspect in hybrid_framework.sprint_execution.work_management %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Process**: {{ aspect.process }}
  - **Rules**: {{ aspect.rules | join(', ') }}
{% endfor %}

### Sprint Review
#### Review Structure
{% for element in hybrid_framework.sprint_review.structure %}
- **{{ element.name }}**: {{ element.description }}
  - **Duration**: {{ element.duration | default('[X] minutes') }}
  - **Participants**: {{ element.participants | join(', ') }}
  - **Purpose**: {{ element.purpose }}
{% endfor %}

#### Kanban Metrics Integration
{% for metric in hybrid_framework.sprint_review.kanban_metrics %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Measurement**: {{ metric.measurement }}
  - **Discussion Points**: {{ metric.discussion_points | join(', ') }}
{% endfor %}

## Board Configuration

### Hybrid Board Design
#### Board Layout
```
[Backlog] → [Sprint Backlog] → [In Progress] → [Review] → [Done]
     ↓           ↓              ↓           ↓        ↓
[Flow Work] → [Sprint Work] → [Active] → [Testing] → [Complete]
```

#### Column Definitions
{% for column in hybrid_framework.board_configuration.columns %}
##### {{ column.name }}
- **Purpose**: {{ column.purpose }}
- **Sprint Work**: {{ column.sprint_work | default('[How sprint work flows through this column]') }}
- **Flow Work**: {{ column.flow_work | default('[How flow work moves through this column]') }}
- **WIP Limit**: {{ column.wip_limit | default('[X] items') }}
- **Entry Criteria**: {{ column.entry_criteria | join(', ') }}
- **Exit Criteria**: {{ column.exit_criteria | join(', ') }}
{% endfor %}

### Work Item Types
{% for type in hybrid_framework.board_configuration.work_item_types %}
#### {{ type.name }}
- **Description**: {{ type.description }}
- **Sprint Treatment**: {{ type.sprint_treatment | default('[How this type is handled in sprints]') }}
- **Flow Treatment**: {{ type.flow_treatment | default('[How this type is handled in flow]') }}
- **Color**: {{ type.color | default('[Color coding]') }}
- **Properties**: {{ type.properties | join(', ') }}
{% endfor %}

### Swimlanes
{% for lane in hybrid_framework.board_configuration.swimlanes %}
#### {{ lane.name }}
- **Purpose**: {{ lane.purpose }}
- **Criteria**: {{ lane.criteria | join(', ') }}
- **Sprint Work**: {{ lane.sprint_work | default('[How sprint work is organized]') }}
- **Flow Work**: {{ lane.flow_work | default('[How flow work is organized]') }}
{% endfor %}

## Ceremony Adaptation

### Daily Standup
#### Traditional Elements
{% for element in hybrid_framework.ceremonies.daily_standup.traditional_elements %}
- **{{ element.name }}**: {{ element.description }}
  - **Purpose**: {{ element.purpose }}
  - **Questions**: {{ element.questions | join(', ') }}
{% endfor %}

#### Kanban Integration
{% for integration in hybrid_framework.ceremonies.daily_standup.kanban_integration %}
- **{{ integration.name }}**: {{ integration.description }}
  - **Process**: {{ integration.process }}
  - **Benefits**: {{ integration.benefits | join(', ') }}
{% endfor %}

#### Flow Focus
{% for focus in hybrid_framework.ceremonies.daily_standup.flow_focus %}
- **{{ focus.name }}**: {{ focus.description }}
  - **Discussion Points**: {{ focus.discussion_points | join(', ') }}
  - **Actions**: {{ focus.actions | join(', ') }}
{% endfor %}

### Sprint Planning
#### Sprint Goal Setting
{% for aspect in hybrid_framework.ceremonies.sprint_planning.goal_setting %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Process**: {{ aspect.process }}
  - **Considerations**: {{ aspect.considerations | join(', ') }}
{% endfor %}

#### Work Selection
{% for method in hybrid_framework.ceremonies.sprint_planning.work_selection %}
- **{{ method.name }}**: {{ method.description }}
  - **Criteria**: {{ method.criteria | join(', ') }}
  - **Process**: {{ method.process }}
{% endfor %}

#### Capacity Planning
{% for aspect in hybrid_framework.ceremonies.sprint_planning.capacity_planning %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Calculation**: {{ aspect.calculation }}
  - **Considerations**: {{ aspect.considerations | join(', ') }}
{% endfor %}

### Sprint Review
#### Demo Structure
{% for element in hybrid_framework.ceremonies.sprint_review.demo_structure %}
- **{{ element.name }}**: {{ element.description }}
  - **Duration**: {{ element.duration | default('[X] minutes') }}
  - **Content**: {{ element.content | join(', ') }}
{% endfor %}

#### Flow Work Presentation
{% for aspect in hybrid_framework.ceremonies.sprint_review.flow_work_presentation %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Process**: {{ aspect.process }}
  - **Benefits**: {{ aspect.benefits | join(', ') }}
{% endfor %}

### Retrospective
#### Sprint Retrospective
{% for element in hybrid_framework.ceremonies.retrospective.sprint_retrospective %}
- **{{ element.name }}**: {{ element.description }}
  - **Process**: {{ element.process }}
  - **Focus**: {{ element.focus | join(', ') }}
{% endfor %}

#### Flow Retrospective
{% for element in hybrid_framework.ceremonies.retrospective.flow_retrospective %}
- **{{ element.name }}**: {{ element.description }}
  - **Process**: {{ element.process }}
  - **Focus**: {{ element.focus | join(', ') }}
{% endfor %}

#### Hybrid Insights
{% for insight in hybrid_framework.ceremonies.retrospective.hybrid_insights %}
- **{{ insight.name }}**: {{ insight.description }}
  - **Discussion Points**: {{ insight.discussion_points | join(', ') }}
  - **Actions**: {{ insight.actions | join(', ') }}
{% endfor %}

## Metrics Integration

### Sprint Metrics
{% for metric in hybrid_framework.metrics.sprint_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Integration**: {{ metric.integration | default('[How this integrates with Kanban metrics]') }}
{% endfor %}

### Kanban Metrics
{% for metric in hybrid_framework.metrics.kanban_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Integration**: {{ metric.integration | default('[How this integrates with Sprint metrics]') }}
{% endfor %}

### Hybrid Metrics
{% for metric in hybrid_framework.metrics.hybrid_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Measurement**: {{ metric.measurement }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often measured]') }}
- **Benefits**: {{ metric.benefits | join(', ') }}
{% endfor %}

### Dashboard Configuration
{% for dashboard in hybrid_framework.metrics.dashboard_configuration %}
#### {{ dashboard.name }}
- **Purpose**: {{ dashboard.purpose }}
- **Metrics**: {{ dashboard.metrics | join(', ') }}
- **Audience**: {{ dashboard.audience | join(', ') }}
- **Update Frequency**: {{ dashboard.update_frequency | default('[How often updated]') }}
{% endfor %}

## Role Definitions

### Scrum Master / Flow Master
{% for responsibility in hybrid_framework.roles.scrum_master_flow_master %}
- **{{ responsibility.name }}**: {{ responsibility.description }}
  - **Sprint Focus**: {{ responsibility.sprint_focus | default('[How this applies to sprint work]') }}
  - **Flow Focus**: {{ responsibility.flow_focus | default('[How this applies to flow work]') }}
{% endfor %}

### Product Owner
{% for responsibility in hybrid_framework.roles.product_owner %}
- **{{ responsibility.name }}**: {{ responsibility.description }}
  - **Sprint Work**: {{ responsibility.sprint_work | default('[How this applies to sprint work]') }}
  - **Flow Work**: {{ responsibility.flow_work | default('[How this applies to flow work]') }}
{% endfor %}

### Development Team
{% for responsibility in hybrid_framework.roles.development_team %}
- **{{ responsibility.name }}**: {{ responsibility.description }}
  - **Sprint Work**: {{ responsibility.sprint_work | default('[How this applies to sprint work]') }}
  - **Flow Work**: {{ responsibility.flow_work | default('[How this applies to flow work]') }}
{% endfor %}

## Process Guidelines

### Work Item Classification
{% for classification in hybrid_framework.process_guidelines.work_item_classification %}
#### {{ classification.name }}
- **Criteria**: {{ classification.criteria | join(', ') }}
- **Sprint Treatment**: {{ classification.sprint_treatment | default('[How this type is handled in sprints]') }}
- **Flow Treatment**: {{ classification.flow_treatment | default('[How this type is handled in flow]') }}
- **Examples**: {{ classification.examples | join(', ') }}
{% endfor %}

### Priority Management
{% for aspect in hybrid_framework.process_guidelines.priority_management %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Sprint Work**: {{ aspect.sprint_work | default('[How priorities are managed for sprint work]') }}
  - **Flow Work**: {{ aspect.flow_work | default('[How priorities are managed for flow work]') }}
  - **Conflicts**: {{ aspect.conflicts | default('[How to handle priority conflicts]') }}
{% endfor %}

### WIP Management
{% for aspect in hybrid_framework.process_guidelines.wip_management %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Sprint Work**: {{ aspect.sprint_work | default('[How WIP is managed for sprint work]') }}
  - **Flow Work**: {{ aspect.flow_work | default('[How WIP is managed for flow work]') }}
  - **Overall Limits**: {{ aspect.overall_limits | default('[Overall WIP limits and management]') }}
{% endfor %}

## Implementation Plan

### Phase 1: Foundation
{% for task in hybrid_framework.implementation.phase1 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
  - **Success Criteria**: {{ task.success_criteria | join(', ') }}
{% endfor %}

### Phase 2: Board Setup
{% for task in hybrid_framework.implementation.phase2 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
  - **Success Criteria**: {{ task.success_criteria | join(', ') }}
{% endfor %}

### Phase 3: Team Training
{% for task in hybrid_framework.implementation.phase3 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
  - **Success Criteria**: {{ task.success_criteria | join(', ') }}
{% endfor %}

### Phase 4: Full Implementation
{% for task in hybrid_framework.implementation.phase4 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
  - **Success Criteria**: {{ task.success_criteria | join(', ') }}
{% endfor %}

## Success Criteria

### Short-term Success (1-2 sprints)
{% for criterion in hybrid_framework.success_criteria.short_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target | default('[Target value]') }}
  - **Timeline**: {{ criterion.timeline | default('[When to achieve]') }}
{% endfor %}

### Medium-term Success (3-6 sprints)
{% for criterion in hybrid_framework.success_criteria.medium_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target | default('[Target value]') }}
  - **Timeline**: {{ criterion.timeline | default('[When to achieve]') }}
{% endfor %}

### Long-term Success (6+ sprints)
{% for criterion in hybrid_framework.success_criteria.long_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target | default('[Target value]') }}
  - **Timeline**: {{ criterion.timeline | default('[When to achieve]') }}
{% endfor %}

## Common Challenges & Solutions

### Framework Challenges
{% for challenge in hybrid_framework.common_challenges.framework_challenges %}
#### {{ challenge.name }}
- **Description**: {{ challenge.description }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Prevention**: {{ challenge.prevention | join(', ') }}
{% endfor %}

### Team Challenges
{% for challenge in hybrid_framework.common_challenges.team_challenges %}
#### {{ challenge.name }}
- **Description**: {{ challenge.description }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Prevention**: {{ challenge.prevention | join(', ') }}
{% endfor %}

### Process Challenges
{% for challenge in hybrid_framework.common_challenges.process_challenges %}
#### {{ challenge.name }}
- **Description**: {{ challenge.description }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Prevention**: {{ challenge.prevention | join(', ') }}
{% endfor %}

## Continuous Improvement

### Framework Evolution
{% for evolution in hybrid_framework.continuous_improvement.framework_evolution %}
- **{{ evolution.name }}**: {{ evolution.description }}
  - **Current State**: {{ evolution.current_state | default('[Current framework state]') }}
  - **Planned Changes**: {{ evolution.planned_changes | join(', ') }}
  - **Expected Benefits**: {{ evolution.expected_benefits | join(', ') }}
  - **Implementation Timeline**: {{ evolution.timeline | default('[When changes will be implemented]') }}
{% endfor %}

### Process Improvements
{% for improvement in hybrid_framework.continuous_improvement.process_improvements %}
- **{{ improvement.name }}**: {{ improvement.description }}
  - **Implementation Plan**: {{ improvement.implementation_plan }}
  - **Expected Benefits**: {{ improvement.expected_benefits | join(', ') }}
  - **Success Metrics**: {{ improvement.success_metrics | join(', ') }}
{% endfor %}

### Team Development
{% for development in hybrid_framework.continuous_improvement.team_development %}
- **{{ development.name }}**: {{ development.description }}
  - **Target Audience**: {{ development.target_audience | join(', ') }}
  - **Format**: {{ development.format | default('[Training format]') }}
  - **Timeline**: {{ development.timeline | default('[When this will happen]') }}
{% endfor %}

## Appendices

### References
{% for reference in hybrid_framework.references %}
- {{ reference }}
{% endfor %}

### Tools & Resources
{% for tool in hybrid_framework.tools %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Purpose**: {{ tool.purpose | default('[What this tool is used for]') }}
  - **Configuration**: {{ tool.configuration | default('[Key configuration details]') }}
  - **Integration**: {{ tool.integration | default('[How it integrates with other tools]') }}
{% endfor %}

### Templates
{% for template in hybrid_framework.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in hybrid_framework.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This Sprint-Kanban hybrid framework should be reviewed and updated regularly as team dynamics and project requirements evolve.*
