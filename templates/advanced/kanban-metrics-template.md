# {{ project.name }} - Kanban Metrics Dashboard

## Instructions for Creating Kanban Metrics
1. **Metric Selection**: Choose metrics that align with team goals and business objectives
2. **Data Collection**: Establish reliable data collection methods and sources
3. **Baseline Establishment**: Set initial baselines for comparison and trend analysis
4. **Visualization Setup**: Create clear, actionable visualizations and dashboards
5. **Review Cadence**: Establish regular review cycles for metric analysis
6. **Action Planning**: Use metrics to identify improvements and track progress
7. **Stakeholder Communication**: Share relevant metrics with appropriate stakeholders
8. **Continuous Improvement**: Regularly evaluate and adjust metrics based on value
{% if features.cascade %}
9. **Master Index Update**: Update master-index.md when metrics strategy or targets change
{% endif %}

## Document Information
- **Version**: {{ kanban_metrics.version | default('1.0') }}
- **Last Updated**: {{ kanban_metrics.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Metrics Owner**: {{ kanban_metrics.metrics_owner | default('[Name]') }}

## Metrics Overview

### Purpose
{{ kanban_metrics.purpose | default('[Clear statement of why these metrics matter and what they help achieve]') }}

### Key Questions Answered
{% for question in kanban_metrics.key_questions %}
- {{ question }}
{% endfor %}

### Stakeholders
{% for stakeholder in kanban_metrics.stakeholders %}
- **{{ stakeholder.name }}**: {{ stakeholder.role }}
  - **Interests**: {{ stakeholder.interests | join(', ') }}
  - **Metrics**: {{ stakeholder.metrics | join(', ') }}
  - **Frequency**: {{ stakeholder.frequency | default('[How often they need updates]') }}
{% endfor %}

## Flow Metrics

### Lead Time
#### Definition
{{ kanban_metrics.flow_metrics.lead_time.definition | default('[Time from work item creation to completion]') }}

#### Measurement
- **Start Point**: {{ kanban_metrics.flow_metrics.lead_time.start_point | default('[When measurement begins]') }}
- **End Point**: {{ kanban_metrics.flow_metrics.lead_time.end_point | default('[When measurement ends]') }}
- **Unit**: {{ kanban_metrics.flow_metrics.lead_time.unit | default('[Days/Hours/etc.]') }}
- **Data Source**: {{ kanban_metrics.flow_metrics.lead_time.data_source | default('[Where data comes from]') }}

#### Current Performance
- **Average**: {{ kanban_metrics.flow_metrics.lead_time.current.average | default('[X] days') }}
- **Median**: {{ kanban_metrics.flow_metrics.lead_time.current.median | default('[X] days') }}
- **95th Percentile**: {{ kanban_metrics.flow_metrics.lead_time.current.percentile_95 | default('[X] days') }}
- **Target**: {{ kanban_metrics.flow_metrics.lead_time.target | default('[X] days') }}
- **Trend**: {{ kanban_metrics.flow_metrics.lead_time.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.flow_metrics.lead_time.analysis | default('[Analysis of lead time performance and factors]') }}

### Cycle Time
#### Definition
{{ kanban_metrics.flow_metrics.cycle_time.definition | default('[Time from work start to completion]') }}

#### Measurement
- **Start Point**: {{ kanban_metrics.flow_metrics.cycle_time.start_point | default('[When work actually begins]') }}
- **End Point**: {{ kanban_metrics.flow_metrics.cycle_time.end_point | default('[When work is completed]') }}
- **Unit**: {{ kanban_metrics.flow_metrics.cycle_time.unit | default('[Days/Hours/etc.]') }}
- **Data Source**: {{ kanban_metrics.flow_metrics.cycle_time.data_source | default('[Where data comes from]') }}

#### Current Performance
- **Average**: {{ kanban_metrics.flow_metrics.cycle_time.current.average | default('[X] days') }}
- **Median**: {{ kanban_metrics.flow_metrics.cycle_time.current.median | default('[X] days') }}
- **95th Percentile**: {{ kanban_metrics.flow_metrics.cycle_time.current.percentile_95 | default('[X] days') }}
- **Target**: {{ kanban_metrics.flow_metrics.cycle_time.target | default('[X] days') }}
- **Trend**: {{ kanban_metrics.flow_metrics.cycle_time.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.flow_metrics.cycle_time.analysis | default('[Analysis of cycle time performance and factors]') }}

### Throughput
#### Definition
{{ kanban_metrics.flow_metrics.throughput.definition | default('[Number of work items completed per unit of time]') }}

#### Measurement
- **Time Period**: {{ kanban_metrics.flow_metrics.throughput.time_period | default('[Weekly/Monthly/etc.]') }}
- **Unit**: {{ kanban_metrics.flow_metrics.throughput.unit | default('[Items per week]') }}
- **Data Source**: {{ kanban_metrics.flow_metrics.throughput.data_source | default('[Where data comes from]') }}

#### Current Performance
- **Current Average**: {{ kanban_metrics.flow_metrics.throughput.current.average | default('[X] items/week') }}
- **Last Period**: {{ kanban_metrics.flow_metrics.throughput.current.last_period | default('[X] items/week') }}
- **Target**: {{ kanban_metrics.flow_metrics.throughput.target | default('[X] items/week') }}
- **Trend**: {{ kanban_metrics.flow_metrics.throughput.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.flow_metrics.throughput.analysis | default('[Analysis of throughput performance and factors]') }}

## Quality Metrics

### Defect Rate
#### Definition
{{ kanban_metrics.quality_metrics.defect_rate.definition | default('[Percentage of work items with defects]') }}

#### Measurement
- **Calculation**: {{ kanban_metrics.quality_metrics.defect_rate.calculation | default('[Defects / Total Items * 100]') }}
- **Time Period**: {{ kanban_metrics.quality_metrics.defect_rate.time_period | default('[Weekly/Monthly]') }}
- **Data Source**: {{ kanban_metrics.quality_metrics.defect_rate.data_source | default('[Where defect data comes from]') }}

#### Current Performance
- **Current Rate**: {{ kanban_metrics.quality_metrics.defect_rate.current.rate | default('[X]%') }}
- **Target**: {{ kanban_metrics.quality_metrics.defect_rate.target | default('[X]%') }}
- **Trend**: {{ kanban_metrics.quality_metrics.defect_rate.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.quality_metrics.defect_rate.analysis | default('[Analysis of defect patterns and causes]') }}

### Rework Rate
#### Definition
{{ kanban_metrics.quality_metrics.rework_rate.definition | default('[Percentage of work requiring rework]') }}

#### Measurement
- **Calculation**: {{ kanban_metrics.quality_metrics.rework_rate.calculation | default('[Rework Items / Total Items * 100]') }}
- **Time Period**: {{ kanban_metrics.quality_metrics.rework_rate.time_period | default('[Weekly/Monthly]') }}
- **Data Source**: {{ kanban_metrics.quality_metrics.rework_rate.data_source | default('[Where rework data comes from]') }}

#### Current Performance
- **Current Rate**: {{ kanban_metrics.quality_metrics.rework_rate.current.rate | default('[X]%') }}
- **Target**: {{ kanban_metrics.quality_metrics.rework_rate.target | default('[X]%') }}
- **Trend**: {{ kanban_metrics.quality_metrics.rework_rate.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.quality_metrics.rework_rate.analysis | default('[Analysis of rework patterns and causes]') }}

### Customer Satisfaction
#### Definition
{{ kanban_metrics.quality_metrics.customer_satisfaction.definition | default('[Customer satisfaction with delivered work]') }}

#### Measurement
- **Method**: {{ kanban_metrics.quality_metrics.customer_satisfaction.method | default('[Survey/Rating/etc.]') }}
- **Scale**: {{ kanban_metrics.quality_metrics.customer_satisfaction.scale | default('[1-5/1-10/etc.]') }}
- **Frequency**: {{ kanban_metrics.quality_metrics.customer_satisfaction.frequency | default('[How often measured]') }}
- **Data Source**: {{ kanban_metrics.quality_metrics.customer_satisfaction.data_source | default('[Where satisfaction data comes from]') }}

#### Current Performance
- **Current Score**: {{ kanban_metrics.quality_metrics.customer_satisfaction.current.score | default('[X.X]') }}
- **Target**: {{ kanban_metrics.quality_metrics.customer_satisfaction.target | default('[X.X]') }}
- **Trend**: {{ kanban_metrics.quality_metrics.customer_satisfaction.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.quality_metrics.customer_satisfaction.analysis | default('[Analysis of customer satisfaction trends and factors]') }}

## Efficiency Metrics

### Work in Progress (WIP)
#### Definition
{{ kanban_metrics.efficiency_metrics.wip.definition | default('[Number of work items currently in progress]') }}

#### Measurement
- **Calculation**: {{ kanban_metrics.efficiency_metrics.wip.calculation | default('[Count of items in active columns]') }}
- **Frequency**: {{ kanban_metrics.efficiency_metrics.wip.frequency | default('[Daily/Weekly]') }}
- **Data Source**: {{ kanban_metrics.efficiency_metrics.wip.data_source | default('[Where WIP data comes from]') }}

#### Current Performance
- **Current WIP**: {{ kanban_metrics.efficiency_metrics.wip.current.value | default('[X] items') }}
- **WIP Limit**: {{ kanban_metrics.efficiency_metrics.wip.limit | default('[X] items') }}
- **Utilization**: {{ kanban_metrics.efficiency_metrics.wip.utilization | default('[X]%') }}
- **Trend**: {{ kanban_metrics.efficiency_metrics.wip.trend | default('[Increasing/Decreasing/Stable]') }}

#### Analysis
{{ kanban_metrics.efficiency_metrics.wip.analysis | default('[Analysis of WIP levels and efficiency]') }}

### Blocked Items
#### Definition
{{ kanban_metrics.efficiency_metrics.blocked_items.definition | default('[Number of work items currently blocked]') }}

#### Measurement
- **Calculation**: {{ kanban_metrics.efficiency_metrics.blocked_items.calculation | default('[Count of blocked items]') }}
- **Frequency**: {{ kanban_metrics.efficiency_metrics.blocked_items.frequency | default('[Daily/Weekly]') }}
- **Data Source**: {{ kanban_metrics.efficiency_metrics.blocked_items.data_source | default('[Where blocked item data comes from]') }}

#### Current Performance
- **Current Blocked**: {{ kanban_metrics.efficiency_metrics.blocked_items.current.count | default('[X] items') }}
- **Blocked Rate**: {{ kanban_metrics.efficiency_metrics.blocked_items.current.rate | default('[X]%') }}
- **Average Block Time**: {{ kanban_metrics.efficiency_metrics.blocked_items.current.avg_block_time | default('[X] days') }}
- **Trend**: {{ kanban_metrics.efficiency_metrics.blocked_items.trend | default('[Increasing/Decreasing/Stable]') }}

#### Analysis
{{ kanban_metrics.efficiency_metrics.blocked_items.analysis | default('[Analysis of blocking patterns and causes]') }}

### Flow Efficiency
#### Definition
{{ kanban_metrics.efficiency_metrics.flow_efficiency.definition | default('[Percentage of time work is actively being worked on]') }}

#### Measurement
- **Calculation**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.calculation | default('[Active Time / Total Time * 100]') }}
- **Time Period**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.time_period | default('[Weekly/Monthly]') }}
- **Data Source**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.data_source | default('[Where flow data comes from]') }}

#### Current Performance
- **Current Efficiency**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.current.value | default('[X]%') }}
- **Target**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.target | default('[X]%') }}
- **Trend**: {{ kanban_metrics.efficiency_metrics.flow_efficiency.trend | default('[Improving/Declining/Stable]') }}

#### Analysis
{{ kanban_metrics.efficiency_metrics.flow_efficiency.analysis | default('[Analysis of flow efficiency and improvement opportunities]') }}

## Bottleneck Analysis

### Bottleneck Identification
{% for bottleneck in kanban_metrics.bottleneck_analysis.bottlenecks %}
#### {{ bottleneck.name }}
- **Location**: {{ bottleneck.location | default('[Which column/stage]') }}
- **Severity**: {{ bottleneck.severity | default('[High/Medium/Low]') }}
- **Impact**: {{ bottleneck.impact | default('[Description of impact]') }}
- **Root Causes**: {{ bottleneck.root_causes | join(', ') }}
- **Mitigation**: {{ bottleneck.mitigation | join(', ') }}
{% endfor %}

### Bottleneck Metrics
{% for metric in kanban_metrics.bottleneck_analysis.metrics %}
#### {{ metric.name }}
- **Current Value**: {{ metric.current_value | default('[X]') }}
- **Target Value**: {{ metric.target_value | default('[X]') }}
- **Trend**: {{ metric.trend | default('[Improving/Declining/Stable]') }}
- **Action Required**: {{ metric.action_required | default('[What needs to be done]') }}
{% endfor %}

## Predictive Metrics

### Forecasting
#### Lead Time Prediction
- **Method**: {{ kanban_metrics.predictive_metrics.lead_time_prediction.method | default('[Statistical model used]') }}
- **Accuracy**: {{ kanban_metrics.predictive_metrics.lead_time_prediction.accuracy | default('[X]%') }}
- **Next Period Forecast**: {{ kanban_metrics.predictive_metrics.lead_time_prediction.forecast | default('[X] days') }}
- **Confidence Interval**: {{ kanban_metrics.predictive_metrics.lead_time_prediction.confidence | default('[X-Y days]') }}

#### Throughput Prediction
- **Method**: {{ kanban_metrics.predictive_metrics.throughput_prediction.method | default('[Statistical model used]') }}
- **Accuracy**: {{ kanban_metrics.predictive_metrics.throughput_prediction.accuracy | default('[X]%') }}
- **Next Period Forecast**: {{ kanban_metrics.predictive_metrics.throughput_prediction.forecast | default('[X] items]') }}
- **Confidence Interval**: {{ kanban_metrics.predictive_metrics.throughput_prediction.confidence | default('[X-Y items]') }}

### Capacity Planning
{% for capacity in kanban_metrics.predictive_metrics.capacity_planning %}
#### {{ capacity.name }}
- **Current Capacity**: {{ capacity.current | default('[X] items/week]') }}
- **Planned Capacity**: {{ capacity.planned | default('[X] items/week]') }}
- **Capacity Utilization**: {{ capacity.utilization | default('[X]%') }}
- **Recommendations**: {{ capacity.recommendations | join(', ') }}
{% endfor %}

## Dashboard Configuration

### Visualizations
{% for visualization in kanban_metrics.dashboard.visualizations %}
#### {{ visualization.name }}
- **Type**: {{ visualization.type | default('[Chart/Graph type]') }}
- **Data Source**: {{ visualization.data_source | default('[Where data comes from]') }}
- **Update Frequency**: {{ visualization.update_frequency | default('[How often updated]') }}
- **Purpose**: {{ visualization.purpose | default('[What this visualization shows]') }}
{% endfor %}

### Dashboard Layout
{% for section in kanban_metrics.dashboard.layout %}
#### {{ section.name }}
- **Position**: {{ section.position | default('[Where on dashboard]') }}
- **Metrics**: {{ section.metrics | join(', ') }}
- **Audience**: {{ section.audience | join(', ') }}
- **Update Frequency**: {{ section.update_frequency | default('[How often updated]') }}
{% endfor %}

### Alerts & Notifications
{% for alert in kanban_metrics.dashboard.alerts %}
#### {{ alert.name }}
- **Trigger**: {{ alert.trigger | default('[What triggers this alert]') }}
- **Threshold**: {{ alert.threshold | default('[Alert threshold value]') }}
- **Recipients**: {{ alert.recipients | join(', ') }}
- **Action**: {{ alert.action | default('[What happens when triggered]') }}
{% endfor %}

## Data Collection & Management

### Data Sources
{% for source in kanban_metrics.data_management.sources %}
#### {{ source.name }}
- **Type**: {{ source.type | default('[Manual/Automated/API/etc.]') }}
- **Frequency**: {{ source.frequency | default('[How often data is collected]') }}
- **Owner**: {{ source.owner | default('[Who is responsible]') }}
- **Quality Checks**: {{ source.quality_checks | join(', ') }}
{% endfor %}

### Data Quality
{% for quality in kanban_metrics.data_management.quality %}
- **{{ quality.name }}**: {{ quality.description }}
  - **Check Frequency**: {{ quality.check_frequency | default('[How often checked]') }}
  - **Owner**: {{ quality.owner | default('[Who is responsible]') }}
  - **Process**: {{ quality.process | default('[How quality is ensured]') }}
{% endfor %}

### Data Retention
- **Retention Period**: {{ kanban_metrics.data_management.retention.period | default('[How long data is kept]') }}
- **Archive Policy**: {{ kanban_metrics.data_management.retention.archive_policy | default('[How data is archived]') }}
- **Deletion Policy**: {{ kanban_metrics.data_management.retention.deletion_policy | default('[When data is deleted]') }}

## Reporting & Communication

### Report Types
{% for report in kanban_metrics.reporting.report_types %}
#### {{ report.name }}
- **Purpose**: {{ report.purpose | default('[What this report is for]') }}
- **Audience**: {{ report.audience | join(', ') }}
- **Frequency**: {{ report.frequency | default('[How often generated]') }}
- **Format**: {{ report.format | default('[PDF/Excel/Dashboard/etc.]') }}
- **Content**: {{ report.content | join(', ') }}
{% endfor %}

### Communication Schedule
{% for communication in kanban_metrics.reporting.communication_schedule %}
- **{{ communication.name }}**: {{ communication.description }}
  - **Frequency**: {{ communication.frequency | default('[How often]') }}
  - **Participants**: {{ communication.participants | join(', ') }}
  - **Format**: {{ communication.format | default('[Meeting/Email/Report/etc.]') }}
  - **Content**: {{ communication.content | join(', ') }}
{% endfor %}

## Continuous Improvement

### Metric Review Process
{% for step in kanban_metrics.continuous_improvement.metric_review %}
{{ loop.index }}. {{ step }}
{% endfor %}

### Improvement Actions
{% for action in kanban_metrics.continuous_improvement.improvement_actions %}
- [ ] **{{ action.title }}**
  - **Description**: {{ action.description }}
  - **Owner**: {{ action.owner | default('[Name]') }}
  - **Due Date**: {{ action.due_date | default('[Date]') }}
  - **Success Criteria**: {{ action.success_criteria | join(', ') }}
{% endfor %}

### Metric Evolution
{% for evolution in kanban_metrics.continuous_improvement.metric_evolution %}
#### {{ evolution.name }}
- **Current State**: {{ evolution.current_state | default('[Current metric configuration]') }}
- **Planned Changes**: {{ evolution.planned_changes | join(', ') }}
- **Expected Benefits**: {{ evolution.expected_benefits | join(', ') }}
- **Implementation Timeline**: {{ evolution.timeline | default('[When changes will be implemented]') }}
{% endfor %}

## Appendices

### References
{% for reference in kanban_metrics.references %}
- {{ reference }}
{% endfor %}

### Tools & Resources
{% for tool in kanban_metrics.tools %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Purpose**: {{ tool.purpose | default('[What this tool is used for]') }}
  - **Configuration**: {{ tool.configuration | default('[Key configuration details]') }}
  - **Integration**: {{ tool.integration | default('[How it integrates with other tools]') }}
{% endfor %}

### Glossary
{% for term, definition in kanban_metrics.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This Kanban metrics dashboard should be reviewed and updated regularly to ensure it continues to provide valuable insights for team improvement.*
