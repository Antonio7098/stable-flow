# {{ project.name }} - Scrum Master Guide

## Instructions for Creating Scrum Master Guide
1. **Role Definition**: Clearly define Scrum Master responsibilities and boundaries
2. **Team Context**: Understand team composition, experience level, and challenges
3. **Ceremony Facilitation**: Define how each Scrum ceremony should be conducted
4. **Impediment Management**: Establish process for identifying and resolving blockers
5. **Coaching Strategy**: Plan how to coach team members and stakeholders
6. **Metrics Setup**: Define KPIs and metrics for team health and performance
7. **Tool Integration**: Specify tools for backlog management, communication, and tracking
8. **Stakeholder Management**: Define how to work with Product Owners and management
9. **Continuous Improvement**: Establish process for regular retrospectives and improvements
{% if features.cascade %}
10. **Master Index Update**: Update master-index.md when Scrum processes or team structure changes
{% endif %}

## Document Information
- **Version**: {{ scrum_master_guide.version | default('1.0') }}
- **Last Updated**: {{ scrum_master_guide.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Scrum Master**: {{ scrum_master_guide.scrum_master | default('[Name]') }}

## Scrum Master Role Overview

### Core Responsibilities
{% for responsibility in scrum_master_guide.core_responsibilities %}
- **{{ responsibility.title }}**: {{ responsibility.description }}
  - **Key Activities**: {{ responsibility.activities | join(', ') }}
  - **Success Metrics**: {{ responsibility.metrics | join(', ') }}
{% endfor %}

### Servant Leadership Principles
{% for principle in scrum_master_guide.servant_leadership %}
- {{ principle }}
{% endfor %}

## Team Coaching Strategy

### Team Development Stages
{% for stage in scrum_master_guide.team_development_stages %}
#### {{ stage.name }}
- **Characteristics**: {{ stage.characteristics }}
- **Coaching Focus**: {{ stage.coaching_focus }}
- **Key Activities**: {{ stage.key_activities | join(', ') }}
- **Expected Duration**: {{ stage.duration }}
{% endfor %}

### Individual Coaching Plans
{% for role in scrum_master_guide.individual_coaching %}
#### {{ role.role_name }}
- **Common Challenges**: {{ role.challenges | join(', ') }}
- **Coaching Approach**: {{ role.approach }}
- **Development Areas**: {{ role.development_areas | join(', ') }}
- **Success Indicators**: {{ role.success_indicators | join(', ') }}
{% endfor %}

## Scrum Ceremonies Facilitation

### Sprint Planning
#### Preparation
{% for prep in scrum_master_guide.ceremonies.sprint_planning.preparation %}
- {{ prep }}
{% endfor %}

#### Facilitation Guidelines
- **Duration**: {{ scrum_master_guide.ceremonies.sprint_planning.duration }}
- **Participants**: {{ scrum_master_guide.ceremonies.sprint_planning.participants | join(', ') }}
- **Agenda**: {{ scrum_master_guide.ceremonies.sprint_planning.agenda | join(', ') }}
- **Facilitation Tips**: {{ scrum_master_guide.ceremonies.sprint_planning.tips | join(', ') }}

#### Common Challenges
{% for challenge in scrum_master_guide.ceremonies.sprint_planning.challenges %}
- **{{ challenge.issue }}**: {{ challenge.solution }}
{% endfor %}

### Daily Standups
#### Facilitation Guidelines
- **Duration**: {{ scrum_master_guide.ceremonies.daily_standup.duration }}
- **Time**: {{ scrum_master_guide.ceremonies.daily_standup.time }}
- **Format**: {{ scrum_master_guide.ceremonies.daily_standup.format }}
- **Questions**: {{ scrum_master_guide.ceremonies.daily_standup.questions | join(', ') }}

#### Standup Variations
{% for variation in scrum_master_guide.ceremonies.daily_standup.variations %}
- **{{ variation.name }}**: {{ variation.description }}
  - **When to Use**: {{ variation.when_to_use }}
  - **Format**: {{ variation.format }}
{% endfor %}

### Sprint Review
#### Facilitation Guidelines
- **Duration**: {{ scrum_master_guide.ceremonies.sprint_review.duration }}
- **Participants**: {{ scrum_master_guide.ceremonies.sprint_review.participants | join(', ') }}
- **Demo Preparation**: {{ scrum_master_guide.ceremonies.sprint_review.demo_prep | join(', ') }}
- **Feedback Collection**: {{ scrum_master_guide.ceremonies.sprint_review.feedback_collection }}

### Sprint Retrospective
#### Facilitation Guidelines
- **Duration**: {{ scrum_master_guide.ceremonies.sprint_retrospective.duration }}
- **Format Options**: {{ scrum_master_guide.ceremonies.sprint_retrospective.formats | join(', ') }}
- **Facilitation Techniques**: {{ scrum_master_guide.ceremonies.sprint_retrospective.techniques | join(', ') }}

#### Retrospective Formats
{% for format in scrum_master_guide.ceremonies.sprint_retrospective.format_details %}
##### {{ format.name }}
- **Description**: {{ format.description }}
- **Duration**: {{ format.duration }}
- **Steps**: {{ format.steps | join(', ') }}
- **Best For**: {{ format.best_for }}
{% endfor %}

## Impediment Management

### Impediment Identification
{% for source in scrum_master_guide.impediment_management.identification_sources %}
- **{{ source.name }}**: {{ source.description }}
  - **Detection Methods**: {{ source.detection_methods | join(', ') }}
  - **Escalation Path**: {{ source.escalation_path }}
{% endfor %}

### Impediment Resolution Process
1. **Identification**: {{ scrum_master_guide.impediment_management.process.identification }}
2. **Documentation**: {{ scrum_master_guide.impediment_management.process.documentation }}
3. **Prioritization**: {{ scrum_master_guide.impediment_management.process.prioritization }}
4. **Resolution**: {{ scrum_master_guide.impediment_management.process.resolution }}
5. **Follow-up**: {{ scrum_master_guide.impediment_management.process.follow_up }}

### Impediment Tracking
{% for tool in scrum_master_guide.impediment_management.tracking_tools %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Fields**: {{ tool.fields | join(', ') }}
  - **Workflow**: {{ tool.workflow }}
{% endfor %}

## Team Health & Metrics

### Team Health Indicators
{% for indicator in scrum_master_guide.team_health.indicators %}
- **{{ indicator.name }}**: {{ indicator.description }}
  - **Measurement**: {{ indicator.measurement }}
  - **Target**: {{ indicator.target }}
  - **Red Flags**: {{ indicator.red_flags | join(', ') }}
{% endfor %}

### Performance Metrics
{% for metric in scrum_master_guide.performance_metrics %}
#### {{ metric.name }}
- **Purpose**: {{ metric.purpose }}
- **Calculation**: {{ metric.calculation }}
- **Frequency**: {{ metric.frequency }}
- **Target**: {{ metric.target }}
- **Trend Analysis**: {{ metric.trend_analysis }}
{% endfor %}

### Velocity Tracking
- **Sprint Velocity**: {{ scrum_master_guide.velocity.sprint_velocity }}
- **Average Velocity**: {{ scrum_master_guide.velocity.average_velocity }}
- **Velocity Trend**: {{ scrum_master_guide.velocity.trend }}
- **Capacity Planning**: {{ scrum_master_guide.velocity.capacity_planning }}

## Stakeholder Management

### Product Owner Collaboration
{% for aspect in scrum_master_guide.stakeholder_management.product_owner %}
- **{{ aspect.name }}**: {{ aspect.description }}
  - **Frequency**: {{ aspect.frequency }}
  - **Participants**: {{ aspect.participants | join(', ') }}
  - **Outcomes**: {{ aspect.outcomes | join(', ') }}
{% endfor %}

### Management Engagement
{% for activity in scrum_master_guide.stakeholder_management.management %}
- **{{ activity.name }}**: {{ activity.description }}
  - **Frequency**: {{ activity.frequency }}
  - **Key Messages**: {{ activity.key_messages | join(', ') }}
  - **Success Criteria**: {{ activity.success_criteria }}
{% endfor %}

### Team Communication
{% for channel in scrum_master_guide.stakeholder_management.communication_channels %}
- **{{ channel.name }}**: {{ channel.description }}
  - **Purpose**: {{ channel.purpose }}
  - **Frequency**: {{ channel.frequency }}
  - **Participants**: {{ channel.participants | join(', ') }}
{% endfor %}

## Tool Configuration

### Backlog Management
{% for tool in scrum_master_guide.tools.backlog_management %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Configuration**: {{ tool.configuration }}
  - **Workflows**: {{ tool.workflows | join(', ') }}
  - **Integration**: {{ tool.integration }}
{% endfor %}

### Communication Tools
{% for tool in scrum_master_guide.tools.communication %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Use Cases**: {{ tool.use_cases | join(', ') }}
  - **Best Practices**: {{ tool.best_practices | join(', ') }}
{% endfor %}

### Metrics & Reporting
{% for tool in scrum_master_guide.tools.metrics_reporting %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Metrics Tracked**: {{ tool.metrics | join(', ') }}
  - **Reporting Frequency**: {{ tool.reporting_frequency }}
  - **Dashboard Configuration**: {{ tool.dashboard_config }}
{% endfor %}

## Continuous Improvement

### Retrospective Action Items
{% for action in scrum_master_guide.continuous_improvement.retrospective_actions %}
- [ ] {{ action.description }}
  - **Owner**: {{ action.owner }}
  - **Due Date**: {{ action.due_date }}
  - **Success Criteria**: {{ action.success_criteria }}
{% endfor %}

### Process Improvements
{% for improvement in scrum_master_guide.continuous_improvement.process_improvements %}
- **{{ improvement.name }}**: {{ improvement.description }}
  - **Implementation Plan**: {{ improvement.implementation_plan }}
  - **Expected Benefits**: {{ improvement.expected_benefits }}
  - **Success Metrics**: {{ improvement.success_metrics | join(', ') }}
{% endfor %}

### Learning & Development
{% for learning in scrum_master_guide.continuous_improvement.learning_development %}
- **{{ learning.name }}**: {{ learning.description }}
  - **Target Audience**: {{ learning.target_audience }}
  - **Format**: {{ learning.format }}
  - **Timeline**: {{ learning.timeline }}
{% endfor %}

## Common Challenges & Solutions

### Team Challenges
{% for challenge in scrum_master_guide.common_challenges.team %}
#### {{ challenge.name }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Prevention**: {{ challenge.prevention | join(', ') }}
{% endfor %}

### Process Challenges
{% for challenge in scrum_master_guide.common_challenges.process %}
#### {{ challenge.name }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Prevention**: {{ challenge.prevention | join(', ') }}
{% endfor %}

### Organizational Challenges
{% for challenge in scrum_master_guide.common_challenges.organizational %}
#### {{ challenge.name }}
- **Symptoms**: {{ challenge.symptoms | join(', ') }}
- **Root Causes**: {{ challenge.root_causes | join(', ') }}
- **Solutions**: {{ challenge.solutions | join(', ') }}
- **Escalation Path**: {{ challenge.escalation_path }}
{% endfor %}

## Appendices

### References
{% for reference in scrum_master_guide.references %}
- {{ reference }}
{% endfor %}

### Templates
{% for template in scrum_master_guide.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in scrum_master_guide.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This Scrum Master Guide should be reviewed and updated regularly as team dynamics and processes evolve.*
