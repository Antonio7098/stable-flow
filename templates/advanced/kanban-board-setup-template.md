# {{ project.name }} - Kanban Board Setup Guide

## Instructions for Creating Kanban Board Setup
1. **Workflow Analysis**: Map current work processes and identify stages
2. **Column Design**: Define columns that represent actual work states
3. **WIP Limits**: Set appropriate work-in-progress limits for each column
4. **Card Types**: Define different types of work items and their properties
5. **Policies**: Establish clear policies for each column and transition
6. **Swimlanes**: Organize work by priority, team, or work type
7. **Metrics Setup**: Configure tracking for flow metrics and bottlenecks
8. **Tool Configuration**: Set up physical or digital board with proper settings
9. **Team Training**: Ensure team understands board usage and policies
{% if features.cascade %}
10. **Master Index Update**: Update master-index.md when board structure or policies change
{% endif %}

## Document Information
- **Version**: {{ kanban_setup.version | default('1.0') }}
- **Last Updated**: {{ kanban_setup.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Board Owner**: {{ kanban_setup.board_owner | default('[Name]') }}

## Board Overview

### Board Purpose
{{ kanban_setup.board_purpose | default('[Clear statement of what this board manages and why]') }}

### Team Information
- **Team Name**: {{ kanban_setup.team.name | default('[Team Name]') }}
- **Team Size**: {{ kanban_setup.team.size | default('[X] members') }}
- **Team Roles**: {{ kanban_setup.team.roles | join(', ') }}
- **Work Types**: {{ kanban_setup.team.work_types | join(', ') }}

### Board Scope
- **Included Work**: {{ kanban_setup.scope.included | join(', ') }}
- **Excluded Work**: {{ kanban_setup.scope.excluded | join(', ') }}
- **Boundaries**: {{ kanban_setup.scope.boundaries | join(', ') }}

## Workflow Design

### Current State Analysis
{% for stage in kanban_setup.workflow.current_state %}
#### {{ stage.name }}
- **Description**: {{ stage.description }}
- **Typical Duration**: {{ stage.duration | default('[X] days') }}
- **Key Activities**: {{ stage.activities | join(', ') }}
- **Pain Points**: {{ stage.pain_points | join(', ') }}
- **Dependencies**: {{ stage.dependencies | join(', ') }}
{% endfor %}

### Target Workflow
{% for stage in kanban_setup.workflow.target_state %}
#### {{ stage.name }}
- **Description**: {{ stage.description }}
- **Purpose**: {{ stage.purpose }}
- **Entry Criteria**: {{ stage.entry_criteria | join(', ') }}
- **Exit Criteria**: {{ stage.exit_criteria | join(', ') }}
- **Key Activities**: {{ stage.activities | join(', ') }}
{% endfor %}

### Workflow Mapping
```
[Backlog] → [Analysis] → [Development] → [Testing] → [Review] → [Done]
```

## Column Configuration

### Column Definitions
{% for column in kanban_setup.columns %}
#### {{ column.name }}
- **Purpose**: {{ column.purpose }}
- **Description**: {{ column.description }}
- **Entry Criteria**: {{ column.entry_criteria | join(', ') }}
- **Exit Criteria**: {{ column.exit_criteria | join(', ') }}
- **WIP Limit**: {{ column.wip_limit | default('[X]') }}
- **Color**: {{ column.color | default('[Color]') }}
- **Icon**: {{ column.icon | default('[Icon]') }}
{% endfor %}

### WIP Limits Strategy
{% for limit in kanban_setup.wip_limits %}
#### {{ limit.column }}
- **Current Limit**: {{ limit.current_limit }}
- **Rationale**: {{ limit.rationale }}
- **Adjustment Criteria**: {{ limit.adjustment_criteria | join(', ') }}
- **Monitoring**: {{ limit.monitoring | default('[How to monitor this limit]') }}
{% endfor %}

### Column Policies
{% for policy in kanban_setup.column_policies %}
#### {{ policy.column }}
- **Pull Policy**: {{ policy.pull_policy }}
- **Push Policy**: {{ policy.push_policy }}
- **Blocking Rules**: {{ policy.blocking_rules | join(', ') }}
- **Escalation**: {{ policy.escalation | default('[When and how to escalate]') }}
{% endfor %}

## Card Types & Properties

### Card Types
{% for type in kanban_setup.card_types %}
#### {{ type.name }}
- **Description**: {{ type.description }}
- **Color**: {{ type.color | default('[Color]') }}
- **Icon**: {{ type.icon | default('[Icon]') }}
- **Properties**: {{ type.properties | join(', ') }}
- **Size Guidelines**: {{ type.size_guidelines | default('[Guidelines for sizing this type]') }}
{% endfor %}

### Card Properties
{% for property in kanban_setup.card_properties %}
#### {{ property.name }}
- **Type**: {{ property.type | default('[Text/Number/Date/List/etc.]') }}
- **Required**: {{ property.required | default('[Yes/No]') }}
- **Options**: {{ property.options | join(', ') | default('[N/A for non-list types]') }}
- **Description**: {{ property.description }}
{% endfor %}

### Card Templates
{% for template in kanban_setup.card_templates %}
#### {{ template.name }}
- **Use Case**: {{ template.use_case }}
- **Properties**: {{ template.properties | join(', ') }}
- **Example**: {{ template.example | default('[Example card content]') }}
{% endfor %}

## Swimlanes & Organization

### Swimlane Strategy
- **Organization Method**: {{ kanban_setup.swimlanes.organization_method | default('[Priority/Team/Work Type/etc.]') }}
- **Rationale**: {{ kanban_setup.swimlanes.rationale }}
- **Benefits**: {{ kanban_setup.swimlanes.benefits | join(', ') }}

### Swimlane Definitions
{% for lane in kanban_setup.swimlanes.definitions %}
#### {{ lane.name }}
- **Purpose**: {{ lane.purpose }}
- **Criteria**: {{ lane.criteria | join(', ') }}
- **Color**: {{ lane.color | default('[Color]') }}
- **Priority**: {{ lane.priority | default('[High/Medium/Low]') }}
{% endfor %}

### Cross-Swimlane Rules
{% for rule in kanban_setup.swimlanes.cross_lane_rules %}
- **{{ rule.name }}**: {{ rule.description }}
  - **Conditions**: {{ rule.conditions | join(', ') }}
  - **Actions**: {{ rule.actions | join(', ') }}
{% endfor %}

## Metrics & Tracking

### Flow Metrics
{% for metric in kanban_setup.flow_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Calculation**: {{ metric.calculation }}
- **Target**: {{ metric.target | default('[Target value]') }}
- **Frequency**: {{ metric.frequency | default('[How often to measure]') }}
- **Tools**: {{ metric.tools | join(', ') }}
{% endfor %}

### Bottleneck Detection
{% for indicator in kanban_setup.bottleneck_indicators %}
- **{{ indicator.name }}**: {{ indicator.description }}
  - **Warning Signs**: {{ indicator.warning_signs | join(', ') }}
  - **Response Actions**: {{ indicator.response_actions | join(', ') }}
  - **Prevention**: {{ indicator.prevention | join(', ') }}
{% endfor %}

### Performance Indicators
{% for indicator in kanban_setup.performance_indicators %}
#### {{ indicator.name }}
- **Description**: {{ indicator.description }}
- **Measurement**: {{ indicator.measurement }}
- **Frequency**: {{ indicator.frequency }}
- **Target**: {{ indicator.target }}
- **Trend Analysis**: {{ indicator.trend_analysis | default('[How to analyze trends]') }}
{% endfor %}

## Board Policies

### General Policies
{% for policy in kanban_setup.general_policies %}
- **{{ policy.name }}**: {{ policy.description }}
  - **Rules**: {{ policy.rules | join(', ') }}
  - **Exceptions**: {{ policy.exceptions | join(', ') }}
  - **Enforcement**: {{ policy.enforcement | default('[How this policy is enforced]') }}
{% endfor %}

### Work Item Policies
{% for policy in kanban_setup.work_item_policies %}
- **{{ policy.name }}**: {{ policy.description }}
  - **Creation Rules**: {{ policy.creation_rules | join(', ') }}
  - **Size Limits**: {{ policy.size_limits | default('[Size guidelines]') }}
  - **Review Requirements**: {{ policy.review_requirements | join(', ') }}
{% endfor %}

### Transition Policies
{% for transition in kanban_setup.transition_policies %}
#### {{ transition.from_column }} → {{ transition.to_column }}
- **Conditions**: {{ transition.conditions | join(', ') }}
- **Requirements**: {{ transition.requirements | join(', ') }}
- **Approval**: {{ transition.approval | default('[Who needs to approve]') }}
- **Documentation**: {{ transition.documentation | join(', ') }}
{% endfor %}

## Tool Configuration

### Physical Board Setup
{% if kanban_setup.tool_type == 'physical' %}
#### Board Materials
- **Board Type**: {{ kanban_setup.physical_board.board_type | default('[Whiteboard/Magnetic Board/etc.]') }}
- **Size**: {{ kanban_setup.physical_board.size | default('[Dimensions]') }}
- **Location**: {{ kanban_setup.physical_board.location | default('[Where the board is located]') }}

#### Card Materials
- **Card Type**: {{ kanban_setup.physical_board.card_type | default('[Sticky Notes/Index Cards/etc.]') }}
- **Colors**: {{ kanban_setup.physical_board.card_colors | join(', ') }}
- **Size**: {{ kanban_setup.physical_board.card_size | default('[Card dimensions]') }}

#### Accessories
- **Markers**: {{ kanban_setup.physical_board.markers | join(', ') }}
- **Magnets**: {{ kanban_setup.physical_board.magnets | default('[If using magnetic board]') }}
- **Timers**: {{ kanban_setup.physical_board.timers | default('[For time-boxed activities]') }}
{% endif %}

### Digital Board Setup
{% if kanban_setup.tool_type == 'digital' %}
#### Tool Selection
- **Tool**: {{ kanban_setup.digital_board.tool | default('[Jira/Trello/Azure DevOps/etc.]') }}
- **Version**: {{ kanban_setup.digital_board.version | default('[Tool version]') }}
- **Configuration**: {{ kanban_setup.digital_board.configuration | default('[Key configuration settings]') }}

#### Board Settings
- **Columns**: {{ kanban_setup.digital_board.columns | join(', ') }}
- **Swimlanes**: {{ kanban_setup.digital_board.swimlanes | join(', ') }}
- **Filters**: {{ kanban_setup.digital_board.filters | join(', ') }}
- **Views**: {{ kanban_setup.digital_board.views | join(', ') }}

#### Integration
- **Source Control**: {{ kanban_setup.digital_board.source_control | default('[Git integration]') }}
- **CI/CD**: {{ kanban_setup.digital_board.cicd | default('[Build pipeline integration]') }}
- **Communication**: {{ kanban_setup.digital_board.communication | default('[Slack/Teams integration]') }}
{% endif %}

## Team Training

### Training Plan
{% for session in kanban_setup.training.sessions %}
#### {{ session.name }}
- **Duration**: {{ session.duration | default('[X] hours') }}
- **Participants**: {{ session.participants | join(', ') }}
- **Content**: {{ session.content | join(', ') }}
- **Format**: {{ session.format | default('[In-person/Remote/Blended]') }}
- **Materials**: {{ session.materials | join(', ') }}
{% endfor %}

### Role-Specific Training
{% for role in kanban_setup.training.role_specific %}
#### {{ role.role }}
- **Key Concepts**: {{ role.key_concepts | join(', ') }}
- **Responsibilities**: {{ role.responsibilities | join(', ') }}
- **Tools Usage**: {{ role.tools_usage | join(', ') }}
- **Best Practices**: {{ role.best_practices | join(', ') }}
{% endfor %}

### Ongoing Support
{% for support in kanban_setup.training.ongoing_support %}
- **{{ support.name }}**: {{ support.description }}
  - **Frequency**: {{ support.frequency | default('[How often]') }}
  - **Format**: {{ support.format | default('[Format of support]') }}
  - **Contact**: {{ support.contact | default('[Who to contact]') }}
{% endfor %}

## Implementation Plan

### Phase 1: Preparation
{% for task in kanban_setup.implementation.phase1 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
{% endfor %}

### Phase 2: Setup
{% for task in kanban_setup.implementation.phase2 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
{% endfor %}

### Phase 3: Launch
{% for task in kanban_setup.implementation.phase3 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
{% endfor %}

### Phase 4: Optimization
{% for task in kanban_setup.implementation.phase4 %}
- [ ] {{ task.description }}
  - **Owner**: {{ task.owner | default('[Name]') }}
  - **Due Date**: {{ task.due_date | default('[Date]') }}
  - **Dependencies**: {{ task.dependencies | join(', ') }}
{% endfor %}

## Success Criteria

### Short-term Success (1-2 weeks)
{% for criterion in kanban_setup.success_criteria.short_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target }}
{% endfor %}

### Medium-term Success (1-2 months)
{% for criterion in kanban_setup.success_criteria.medium_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target }}
{% endfor %}

### Long-term Success (3+ months)
{% for criterion in kanban_setup.success_criteria.long_term %}
- **{{ criterion.name }}**: {{ criterion.description }}
  - **Measurement**: {{ criterion.measurement }}
  - **Target**: {{ criterion.target }}
{% endfor %}

## Troubleshooting

### Common Issues
{% for issue in kanban_setup.troubleshooting.common_issues %}
#### {{ issue.name }}
- **Symptoms**: {{ issue.symptoms | join(', ') }}
- **Causes**: {{ issue.causes | join(', ') }}
- **Solutions**: {{ issue.solutions | join(', ') }}
- **Prevention**: {{ issue.prevention | join(', ') }}
{% endfor %}

### Board Maintenance
{% for maintenance in kanban_setup.troubleshooting.board_maintenance %}
- **{{ maintenance.name }}**: {{ maintenance.description }}
  - **Frequency**: {{ maintenance.frequency | default('[How often]') }}
  - **Process**: {{ maintenance.process }}
  - **Owner**: {{ maintenance.owner | default('[Who is responsible]') }}
{% endfor %}

## Appendices

### References
{% for reference in kanban_setup.references %}
- {{ reference }}
{% endfor %}

### Templates
{% for template in kanban_setup.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in kanban_setup.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This Kanban board setup should be reviewed and updated regularly as team processes and needs evolve.*
