# {{ project.name }} - Sprint Planning Overview

## Instructions for Creating Sprint Planning
1. **Project Scope**: Define project timeline, sprint length, and total number of sprints
2. **Team Capacity**: Calculate team velocity and sprint capacity based on historical data
3. **Sprint Sequencing**: Plan sprint order based on dependencies and priorities
4. **Milestone Mapping**: Align sprints with project phases and major milestones
5. **Dependency Management**: Identify and track cross-sprint and external dependencies
6. **Risk Planning**: Assess project-level risks and their impact on sprint planning
7. **Resource Allocation**: Ensure team members are properly allocated across sprints
8. **Buffer Planning**: Include buffer time for unknowns and scope changes
9. **Review Cycles**: Plan regular sprint planning review and adjustment cycles
{% if features.cascade %}
10. **Master Index Update**: Update master-index.md when sprint strategy or resource allocation changes
{% endif %}
{% if sections.sprint_planning.agile_documents %}
11. **Agile Document Integration**: Ensure sprint planning aligns with agile methodology documents:
    - **Scrum Master Guide**: Reference ceremony planning and team coaching strategies
    - **Product Owner Guide**: Align with backlog management and stakeholder engagement plans
    - **Kanban Board Setup**: Consider flow work and WIP limits in sprint planning
    - **Agile Methodology Selection**: Ensure chosen methodology supports planned sprint structure
{% endif %}
12. **Metrics Setup**: Establish tracking mechanisms for velocity and quality metrics

## Document Information
- **Version**: {{ sprint_planning.version | default('1.0') }}
- **Last Updated**: {{ sprint_planning.last_updated | default('{{ "now" | strftime("%Y-%m-%d") }}') }}
- **Author**: {{ project.author | default('{{ project.name }} Team') }}
- **Project**: {{ project.name }}

## Sprint Overview
### Project Timeline
- **Project Start**: {{ sprint_planning.timeline.start_date | default('[Date]') }}
- **Project End**: {{ sprint_planning.timeline.end_date | default('[Date]') }}
- **Total Duration**: {{ sprint_planning.timeline.duration | default('[X] weeks') }}
- **Sprint Length**: {{ sprint_planning.timeline.sprint_length | default('[X] weeks') }}
- **Total Sprints**: {{ sprint_planning.timeline.total_sprints | default('[X] sprints') }}

### Team Information
- **Sprint Capacity**: {{ sprint_planning.team.capacity | default('[X] story points per sprint') }}
- **Team Velocity**: {{ sprint_planning.team.velocity | default('[X] points/sprint (average)') }}
{% if sections.sprint_planning.ai_assisted_velocity %}
- **AI-Assisted Velocity**: {{ sprint_planning.team.ai_velocity | default('[X] points/sprint (with AI tools)') }}
- **Velocity Multiplier**: {{ sprint_planning.team.velocity_multiplier | default('[X]x (AI-assisted vs manual)') }}
{% endif %}
- **Team Members**: {{ sprint_planning.team.members | default('[List of team members]') }}

## Sprint Schedule
{% for sprint in sprint_planning.sprints %}
### Sprint {{ sprint.number }}: {{ sprint.name }}
- **Duration**: {{ sprint.start_date }} - {{ sprint.end_date }}
- **Sprint Goal**: {{ sprint.goal }}
- **Planned Points**: {{ sprint.planned_points }}
- **Status**: [ ] Not Started | [ ] In Progress | [ ] Completed | [ ] Blocked
- **Key Features**: {{ sprint.key_features | join(', ') }}
{% if sprint.dependencies %}
- **Dependencies**: {{ sprint.dependencies | join(', ') }}
{% endif %}
{% if sprint.risks %}
- **Risks**: {{ sprint.risks | join(', ') }}
{% endif %}

{% endfor %}

## Milestone Mapping
{% for milestone in sprint_planning.milestones %}
### {{ milestone.name }}
- **Target Date**: {{ milestone.target_date }}
- **Sprint**: {{ milestone.sprint }}
- **Description**: {{ milestone.description }}
- **Success Criteria**: {{ milestone.success_criteria }}
- **Status**: [ ] Not Started | [ ] In Progress | [ ] Completed | [ ] Blocked

{% endfor %}

## Dependencies & Risks
### Cross-Sprint Dependencies
{% for dependency in sprint_planning.dependencies.cross_sprint %}
- **{{ dependency.name }}**: {{ dependency.description }}
  - **Blocking Sprint**: {{ dependency.blocking_sprint }}
  - **Blocked Sprint**: {{ dependency.blocked_sprint }}
  - **Mitigation**: {{ dependency.mitigation }}

{% endfor %}

### External Dependencies
{% for dependency in sprint_planning.dependencies.external %}
- **{{ dependency.name }}**: {{ dependency.description }}
  - **Owner**: {{ dependency.owner }}
  - **Timeline**: {{ dependency.timeline }}
  - **Risk Level**: {{ dependency.risk_level | default('[High/Medium/Low]') }}

{% endfor %}

### Project-Level Risks
{% for risk in sprint_planning.risks.project_level %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Probability**: {{ risk.probability }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
  - **Owner**: {{ risk.owner }}

{% endfor %}

{% if sections.sprint_planning.ai_specific_risks %}
## AI-Specific Risks
### AI-Assisted Development Risks
{% if sprint_planning.ai_risks and sprint_planning.ai_risks.development %}
{% for risk in sprint_planning.ai_risks.development %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
{% endfor %}
{% else %}
- **Context Loss**: AI may lose context between sessions
  - **Impact**: Inconsistent implementation
  - **Mitigation**: Regular code reviews and documentation updates
- **Outdated Knowledge**: AI may reference deprecated practices
  - **Impact**: Technical debt and maintenance issues
  - **Mitigation**: Human oversight and current date awareness
{% endif %}

### AI Context Management
{% if sprint_planning.ai_risks and sprint_planning.ai_risks.context %}
{% for risk in sprint_planning.ai_risks.context %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
{% endfor %}
{% else %}
- **Session Continuity**: Maintaining context across development sessions
  - **Impact**: Potential rework if context is lost
  - **Mitigation**: Comprehensive documentation and regular checkpoints
- **Multi-Agent Coordination**: Managing multiple AI agents working simultaneously
  - **Impact**: Conflicts and duplicated work
  - **Mitigation**: Clear communication protocols and task assignment
{% endif %}

### AI Quality Assurance
{% if sprint_planning.ai_risks and sprint_planning.ai_risks.quality %}
{% for risk in sprint_planning.ai_risks.quality %}
- **{{ risk.name }}**: {{ risk.description }}
  - **Impact**: {{ risk.impact }}
  - **Mitigation**: {{ risk.mitigation }}
{% endfor %}
{% else %}
- **Hallucinations**: AI generating incorrect or fabricated information
  - **Impact**: Implementation of incorrect solutions
  - **Mitigation**: Human code review and testing
- **Security Oversights**: AI missing security vulnerabilities
  - **Impact**: Security breaches and compliance issues
  - **Mitigation**: Security-focused code reviews and automated scanning
{% endif %}
{% endif %}

## Resource Allocation
### Team Member Allocation
{% for member in sprint_planning.resources.team_members %}
#### {{ member.name }}
- **Role**: {{ member.role }}
- **Availability**: {{ member.availability }}%
- **Sprint Assignments**: {{ member.sprint_assignments | join(', ') }}
- **Specializations**: {{ member.specializations | join(', ') }}

{% endfor %}

### External Resources
{% for resource in sprint_planning.resources.external %}
- **{{ resource.name }}**: {{ resource.description }}
  - **Provider**: {{ resource.provider }}
  - **Cost**: {{ resource.cost }}
  - **Timeline**: {{ resource.timeline }}

{% endfor %}

## Buffer Planning
### Buffer Allocation
- **Sprint Buffer**: {{ sprint_planning.buffer.sprint_buffer | default('[X]% per sprint') }}
- **Project Buffer**: {{ sprint_planning.buffer.project_buffer | default('[X]% total') }}
- **Scope Change Buffer**: {{ sprint_planning.buffer.scope_change | default('[X]% for scope changes') }}

### Buffer Usage Guidelines
{% for guideline in sprint_planning.buffer.guidelines %}
- {{ guideline }}
{% endfor %}

## Review Cycles
### Sprint Planning Reviews
{% for review in sprint_planning.reviews.sprint_planning %}
- **{{ review.name }}**: {{ review.description }}
  - **Frequency**: {{ review.frequency }}
  - **Participants**: {{ review.participants | join(', ') }}
  - **Outcomes**: {{ review.outcomes }}

{% endfor %}

### Velocity Reviews
{% for review in sprint_planning.reviews.velocity %}
- **{{ review.name }}**: {{ review.description }}
  - **Frequency**: {{ review.frequency }}
  - **Participants**: {{ review.participants | join(', ') }}
  - **Metrics**: {{ review.metrics | join(', ') }}

{% endfor %}

## Metrics & Tracking
### Velocity Metrics
- **Historical Velocity**: {{ sprint_planning.metrics.velocity.historical | default('[X] points/sprint') }}
- **Current Velocity**: {{ sprint_planning.metrics.velocity.current | default('[X] points/sprint') }}
- **Velocity Trend**: {{ sprint_planning.metrics.velocity.trend | default('[Increasing/Decreasing/Stable]') }}

### Quality Metrics
{% for metric in sprint_planning.metrics.quality %}
- **{{ metric.name }}**: {{ metric.current_value }} (Target: {{ metric.target_value }})
{% endfor %}

### Progress Tracking
{% for metric in sprint_planning.metrics.progress %}
- **{{ metric.name }}**: {{ metric.description }}
  - **Current**: {{ metric.current_value }}
  - **Target**: {{ metric.target_value }}
  - **Status**: {{ metric.status }}

{% endfor %}

## Appendices
### References
{% for reference in sprint_planning.references %}
- {{ reference }}
{% endfor %}

### Glossary
{% for term, definition in sprint_planning.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

### Templates
- **Sprint Template**: [Link to individual sprint template]
- **Retrospective Template**: [Link to retrospective template]
- **Daily Standup Template**: [Link to standup template]

---
*This sprint planning document should be reviewed and updated regularly as the project progresses.*