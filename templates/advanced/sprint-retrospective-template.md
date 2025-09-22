# {{ project.name }} - Sprint {{ sprint.number }} Retrospective

## Instructions for Creating Sprint Retrospective
1. **Data Collection**: Gather quantitative and qualitative data from the sprint
2. **Team Preparation**: Ensure all team members are prepared to participate openly
3. **Format Selection**: Choose appropriate retrospective format based on team needs
4. **Facilitation**: Guide discussion to focus on improvement, not blame
5. **Action Planning**: Create specific, actionable improvement items
6. **Follow-up**: Establish process for tracking and implementing action items
7. **Documentation**: Record insights and decisions for future reference
8. **Celebration**: Acknowledge team achievements and positive developments
{% if features.cascade %}
9. **Master Index Update**: Update master-index.md with retrospective insights and process improvements
{% endif %}

## Document Information
- **Version**: {{ retrospective.version | default('1.0') }}
- **Last Updated**: {{ retrospective.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Sprint**: {{ sprint.number }} - {{ sprint.name }}
- **Retrospective Date**: {{ retrospective.date | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Facilitator**: {{ retrospective.facilitator | default('[Name]') }}

## Sprint Overview

### Sprint Summary
- **Sprint Goal**: {{ sprint.goal }}
- **Sprint Duration**: {{ sprint.start_date }} - {{ sprint.end_date }}
- **Team Members**: {{ sprint.team_members | join(', ') }}
- **Sprint Owner**: {{ sprint.owner | default('[Name]') }}

### Sprint Metrics
- **Planned Story Points**: {{ sprint.metrics.planned_points | default('[X]') }}
- **Completed Story Points**: {{ sprint.metrics.completed_points | default('[X]') }}
- **Velocity**: {{ sprint.metrics.velocity | default('[X] points/sprint') }}
- **Sprint Goal Achievement**: {{ sprint.metrics.goal_achievement | default('[X]%') }}

### Key Deliverables
{% for deliverable in sprint.deliverables %}
- [ ] {{ deliverable.name }} - {{ deliverable.status | default('[Status]') }}
  - **Description**: {{ deliverable.description }}
  - **Acceptance Criteria Met**: {{ deliverable.acceptance_criteria_met | default('[Yes/No]') }}
{% endfor %}

## Retrospective Format

### Selected Format
**{{ retrospective.format.name }}**: {{ retrospective.format.description }}

### Format Details
- **Duration**: {{ retrospective.format.duration | default('[X] minutes') }}
- **Participants**: {{ retrospective.format.participants | join(', ') }}
- **Preparation Required**: {{ retrospective.format.preparation | join(', ') }}
- **Materials Needed**: {{ retrospective.format.materials | join(', ') }}

## Data Collection

### Quantitative Data
{% for metric in retrospective.quantitative_data %}
#### {{ metric.name }}
- **Value**: {{ metric.value }}
- **Previous Sprint**: {{ metric.previous_sprint | default('[X]') }}
- **Trend**: {{ metric.trend | default('[Improving/Declining/Stable]') }}
- **Target**: {{ metric.target | default('[X]') }}
- **Analysis**: {{ metric.analysis | default('[Analysis of the data]') }}
{% endfor %}

### Qualitative Data
{% for source in retrospective.qualitative_data %}
#### {{ source.name }}
- **Method**: {{ source.method }}
- **Participants**: {{ source.participants | join(', ') }}
- **Key Insights**: {{ source.key_insights | join(', ') }}
- **Themes**: {{ source.themes | join(', ') }}
{% endfor %}

## Retrospective Discussion

### What Went Well
{% for item in retrospective.went_well %}
- **{{ item.category }}**: {{ item.description }}
  - **Impact**: {{ item.impact | default('[High/Medium/Low]') }}
  - **Contributing Factors**: {{ item.contributing_factors | join(', ') }}
  - **How to Sustain**: {{ item.how_to_sustain | default('[Actions to maintain this positive aspect]') }}
{% endfor %}

### What Could Be Improved
{% for item in retrospective.improvements %}
- **{{ item.category }}**: {{ item.description }}
  - **Impact**: {{ item.impact | default('[High/Medium/Low]') }}
  - **Root Causes**: {{ item.root_causes | join(', ') }}
  - **Proposed Solutions**: {{ item.proposed_solutions | join(', ') }}
{% endfor %}

### What We Learned
{% for learning in retrospective.learnings %}
- **{{ learning.category }}**: {{ learning.description }}
  - **Application**: {{ learning.application | default('[How to apply this learning]') }}
  - **Future Impact**: {{ learning.future_impact | default('[Expected impact on future sprints]') }}
{% endfor %}

### Team Health Check
{% for indicator in retrospective.team_health %}
#### {{ indicator.name }}
- **Rating**: {{ indicator.rating | default('[1-5 scale]') }}/5
- **Previous Sprint**: {{ indicator.previous_rating | default('[X]') }}/5
- **Comments**: {{ indicator.comments | default('[Team feedback on this indicator]') }}
- **Action Items**: {{ indicator.action_items | join(', ') }}
{% endfor %}

## Action Items

### High Priority Actions
{% for action in retrospective.high_priority_actions %}
- [ ] **{{ action.title }}**
  - **Description**: {{ action.description }}
  - **Owner**: {{ action.owner | default('[Name]') }}
  - **Due Date**: {{ action.due_date | default('[Date]') }}
  - **Success Criteria**: {{ action.success_criteria | join(', ') }}
  - **Dependencies**: {{ action.dependencies | join(', ') }}
{% endfor %}

### Medium Priority Actions
{% for action in retrospective.medium_priority_actions %}
- [ ] **{{ action.title }}**
  - **Description**: {{ action.description }}
  - **Owner**: {{ action.owner | default('[Name]') }}
  - **Due Date**: {{ action.due_date | default('[Date]') }}
  - **Success Criteria**: {{ action.success_criteria | join(', ') }}
{% endfor %}

### Low Priority Actions
{% for action in retrospective.low_priority_actions %}
- [ ] **{{ action.title }}**
  - **Description**: {{ action.description }}
  - **Owner**: {{ action.owner | default('[Name]') }}
  - **Due Date**: {{ action.due_date | default('[Date]') }}
{% endfor %}

## Process Improvements

### Immediate Changes
{% for change in retrospective.immediate_changes %}
- **{{ change.name }}**: {{ change.description }}
  - **Implementation**: {{ change.implementation | default('[How to implement this change]') }}
  - **Owner**: {{ change.owner | default('[Name]') }}
  - **Timeline**: {{ change.timeline | default('[When to implement]') }}
{% endfor %}

### Long-term Improvements
{% for improvement in retrospective.long_term_improvements %}
- **{{ improvement.name }}**: {{ improvement.description }}
  - **Implementation Plan**: {{ improvement.implementation_plan }}
  - **Expected Benefits**: {{ improvement.expected_benefits | join(', ') }}
  - **Success Metrics**: {{ improvement.success_metrics | join(', ') }}
  - **Timeline**: {{ improvement.timeline | default('[Implementation timeline]') }}
{% endfor %}

## Team Dynamics

### Communication
{% for aspect in retrospective.team_dynamics.communication %}
- **{{ aspect.name }}**: {{ aspect.rating | default('[1-5]') }}/5
  - **Strengths**: {{ aspect.strengths | join(', ') }}
  - **Areas for Improvement**: {{ aspect.improvements | join(', ') }}
  - **Action Items**: {{ aspect.action_items | join(', ') }}
{% endfor %}

### Collaboration
{% for aspect in retrospective.team_dynamics.collaboration %}
- **{{ aspect.name }}**: {{ aspect.rating | default('[1-5]') }}/5
  - **Strengths**: {{ aspect.strengths | join(', ') }}
  - **Areas for Improvement**: {{ aspect.improvements | join(', ') }}
  - **Action Items**: {{ aspect.action_items | join(', ') }}
{% endfor %}

### Conflict Resolution
{% for aspect in retrospective.team_dynamics.conflict_resolution %}
- **{{ aspect.name }}**: {{ aspect.rating | default('[1-5]') }}/5
  - **Strengths**: {{ aspect.strengths | join(', ') }}
  - **Areas for Improvement**: {{ aspect.improvements | join(', ') }}
  - **Action Items**: {{ aspect.action_items | join(', ') }}
{% endfor %}

## Technical Insights

### Code Quality
{% for insight in retrospective.technical_insights.code_quality %}
- **{{ insight.name }}**: {{ insight.description }}
  - **Impact**: {{ insight.impact | default('[High/Medium/Low]') }}
  - **Recommendations**: {{ insight.recommendations | join(', ') }}
  - **Action Items**: {{ insight.action_items | join(', ') }}
{% endfor %}

### Technical Debt
{% for item in retrospective.technical_insights.technical_debt %}
- **{{ item.name }}**: {{ item.description }}
  - **Impact**: {{ item.impact | default('[High/Medium/Low]') }}
  - **Effort to Address**: {{ item.effort | default('[High/Medium/Low]') }}
  - **Priority**: {{ item.priority | default('[High/Medium/Low]') }}
  - **Action Plan**: {{ item.action_plan | default('[Plan to address this technical debt]') }}
{% endfor %}

### Tools & Processes
{% for tool in retrospective.technical_insights.tools_processes %}
- **{{ tool.name }}**: {{ tool.description }}
  - **Effectiveness**: {{ tool.effectiveness | default('[1-5]') }}/5
  - **Issues**: {{ tool.issues | join(', ') }}
  - **Improvements**: {{ tool.improvements | join(', ') }}
{% endfor %}

## Celebrations & Recognition

### Team Achievements
{% for achievement in retrospective.celebrations.team_achievements %}
- **{{ achievement.name }}**: {{ achievement.description }}
  - **Impact**: {{ achievement.impact | default('[Description of impact]') }}
  - **Recognition**: {{ achievement.recognition | default('[How to recognize this achievement]') }}
{% endfor %}

### Individual Recognition
{% for recognition in retrospective.celebrations.individual_recognition %}
- **{{ recognition.person }}**: {{ recognition.achievement }}
  - **Contribution**: {{ recognition.contribution | default('[Description of contribution]') }}
  - **Impact**: {{ recognition.impact | default('[Impact on team/project]') }}
{% endfor %}

### Milestones Reached
{% for milestone in retrospective.celebrations.milestones %}
- **{{ milestone.name }}**: {{ milestone.description }}
  - **Date Achieved**: {{ milestone.date_achieved | default('[Date]') }}
  - **Significance**: {{ milestone.significance | default('[Why this milestone matters]') }}
{% endfor %}

## Next Sprint Preparation

### Carry-over Items
{% for item in retrospective.next_sprint.carry_over %}
- **{{ item.name }}**: {{ item.description }}
  - **Reason for Carry-over**: {{ item.reason | default('[Why this item wasn't completed]') }}
  - **Priority for Next Sprint**: {{ item.priority | default('[High/Medium/Low]') }}
  - **Action Plan**: {{ item.action_plan | default('[Plan to complete this item]') }}
{% endfor %}

### Process Adjustments
{% for adjustment in retrospective.next_sprint.process_adjustments %}
- **{{ adjustment.name }}**: {{ adjustment.description }}
  - **Implementation**: {{ adjustment.implementation | default('[How to implement this adjustment]') }}
  - **Expected Impact**: {{ adjustment.expected_impact | default('[Expected benefits]') }}
{% endfor %}

### Focus Areas
{% for focus in retrospective.next_sprint.focus_areas %}
- **{{ focus.name }}**: {{ focus.description }}
  - **Why Important**: {{ focus.importance | default('[Why this focus area is important]') }}
  - **Success Criteria**: {{ focus.success_criteria | join(', ') }}
{% endfor %}

## Follow-up Plan

### Action Item Tracking
- **Tracking Method**: {{ retrospective.follow_up.tracking_method | default('[How action items will be tracked]') }}
- **Review Frequency**: {{ retrospective.follow_up.review_frequency | default('[How often to review progress]') }}
- **Accountability**: {{ retrospective.follow_up.accountability | default('[Who is responsible for tracking]') }}

### Next Retrospective
- **Scheduled Date**: {{ retrospective.follow_up.next_retrospective_date | default('[Date]') }}
- **Format**: {{ retrospective.follow_up.next_retrospective_format | default('[Format for next retrospective]') }}
- **Preparation**: {{ retrospective.follow_up.next_retrospective_preparation | join(', ') }}

### Progress Review
{% for review in retrospective.follow_up.progress_reviews %}
- **{{ review.name }}**: {{ review.description }}
  - **Date**: {{ review.date | default('[Date]') }}
  - **Participants**: {{ review.participants | join(', ') }}
  - **Focus**: {{ review.focus | default('[What to review]') }}
{% endfor %}

## Appendices

### References
{% for reference in retrospective.references %}
- {{ reference }}
{% endfor %}

### Templates
{% for template in retrospective.templates %}
- **{{ template.name }}**: {{ template.description }}
  - **Location**: {{ template.location }}
  - **Usage**: {{ template.usage }}
{% endfor %}

### Glossary
{% for term, definition in retrospective.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

---
*This retrospective should be reviewed and action items tracked until completion. Use insights to improve future sprints.*
