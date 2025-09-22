# {{ project.name }} - Sprint {{ sprint.number }}: {{ sprint.name }}

## Instructions for Creating a Sprint
1. **Prerequisites**: Ensure development guide is checked and strictly adhered to
2. **Cascade Check**: If cascade=true in dev guide, update planning docs when adding new features
3. **Fill Sprint Metadata**: Complete all metadata fields with AI agents and project information
4. **Define Objectives**: Set 3-5 clear, measurable sprint objectives
5. **Plan Tasks**: Use structured format with context files, goals, and acceptance criteria
6. **Estimate Duration**: Use story points or days for realistic planning
7. **Check Dependencies**: Ensure all dependencies are identified and manageable
8. **Review Optional Sections**: Only include sections relevant to your sprint or project as specified in development guide
9. **API Integration Planning**: If integrating with external APIs, specify headers, auth, payloads, and response formats
{% if sections.sprint_template.parallel_agents %}
10. **Parallel Agent Planning**: If using multiple agents, plan coordination and parallel processing
{% endif %}
11. **Set Success Criteria**: Define clear completion criteria for each objective
{% if features.cascade %}
12. **Master Index Update**: Plan to update master-index.md during sprint execution and retrospectives
{% endif %}
{% if sections.sprint_template.agile_documents %}
13. **Agile Document Updates**: Update relevant agile methodology documents based on sprint activities:
    - **Sprint Review**: Update Scrum Master Guide, Product Owner Guide, and Kanban Metrics
    - **Retrospective**: Update Sprint Retrospective template and Scrum Master Guide
    - **Process Changes**: Update Agile Methodology Selection Guide if processes evolve
    - **Team Changes**: Update Scrum Master Guide and Product Owner Guide for role changes
{% endif %}
14. **Update Changelog**: Track progress throughout the sprint

## Sprint Metadata
- **Sprint Number**: {{ sprint.number }}
- **Sprint Name**: {{ sprint.name }}
- **Duration**: {{ sprint.start_date }} - {{ sprint.end_date }} ({{ sprint.duration }} weeks)
- **Sprint Goal**: {{ sprint.goal }}
- **Sprint Owner**: {{ sprint.owner | default('[Name]') }}
- **AI Agents**: {{ sprint.ai_agents | default('[List of AI agents and development tools]') }}
- **Sprint Capacity**: {{ sprint.capacity | default('[Total story points planned]') }}

## Sprint Overview
### Sprint Objectives
{% for objective in sprint.objectives %}
- [ ] {{ objective }}
{% endfor %}

### Success Criteria
{% for criteria in sprint.success_criteria %}
- [ ] {{ criteria }}
{% endfor %}

### Key Deliverables
{% for deliverable in sprint.deliverables %}
- [ ] {{ deliverable }}
{% endfor %}

## Planned Tasks
{% for task in sprint.tasks %}
- [ ] {{ task.description }} — {{ task.driver | default('[Driver]') }} ({{ task.duration | default('[X]d') }})
  - **Context Files**: {{ task.context_files | join(', ') | default('`[File1.md#section]`, `[File2.js]`, `[File3.md#section]`') }}
  - **Goal**: {{ task.goal | default('[Clear, specific goal for this task]') }}
  - **Acceptance Criteria**: {{ task.acceptance_criteria | default('[Specific, testable criteria]') }}
  - **Files to Modify**: {{ task.files_to_modify | join(', ') | default('`[file1.js]`, `[file2.js]`, `[file3.js]`') }}
{% for subtask in task.subtasks %}
  - [ ] {{ subtask }}
{% endfor %}

{% endfor %}

{% if sections.sprint_template.parallel_agents %}
## Parallel Agent Capabilities
### Agent Coordination
{% for agent in sprint.parallel_agents.coordination %}
#### {{ agent.name }}
- **Role**: {{ agent.role }}
- **Specialization**: {{ agent.specialization }}
- **Context Files**: {{ agent.context_files | join(', ') }}
- **Communication Protocol**: {{ agent.communication_protocol }}

{% endfor %}

### Conflict Resolution Protocol
{{ sprint.parallel_agents.conflict_resolution | default('[How agents resolve conflicts]') }}

### AI Hallucination Mitigation
{{ sprint.parallel_agents.hallucination_mitigation | default('[How to prevent and detect AI hallucinations]') }}
{% endif %}

{% if sections.sprint_template.api_integration %}
## API Integration
### External APIs
{% for api in sprint.api_integration.external %}
#### {{ api.name }}
- **Endpoint**: {{ api.endpoint }}
- **Method**: {{ api.method }}
- **Headers**: {{ api.headers | default('`Content-Type: application/json`') }}
- **Authentication**: {{ api.authentication | default('[Bearer token, API key, etc.]') }}
- **Request Payload**: {{ api.request_payload | default('`{ "key": "value" }`') }}
- **Response Format**: {{ api.response_format | default('`{ "status": "success", "data": {} }`') }}
- **Error Handling**: {{ api.error_handling | default('[How to handle errors]') }}

{% endfor %}

### Internal APIs
{% for api in sprint.api_integration.internal %}
#### {{ api.name }}
- **Endpoint**: {{ api.endpoint }}
- **Method**: {{ api.method }}
- **Purpose**: {{ api.purpose }}
- **Data Format**: {{ api.data_format }}

{% endfor %}
{% endif %}

{% if sections.sprint_template.environmental_impact %}
## Environmental Impact
### Carbon Footprint Considerations
{{ sprint.environmental.carbon_footprint | default('[Considerations for reducing carbon footprint]') }}

### Energy Efficiency
{{ sprint.environmental.energy_efficiency | default('[Energy efficiency measures]') }}

### Sustainable Practices
{% for practice in sprint.environmental.sustainable_practices %}
- {{ practice }}
{% endfor %}
{% endif %}

## Definition of Done
### Code Quality
{% for criteria in sprint.definition_of_done.code_quality %}
- [ ] {{ criteria }}
{% endfor %}

### Testing
{% for criteria in sprint.definition_of_done.testing %}
- [ ] {{ criteria }}
{% endfor %}

### Documentation
{% for criteria in sprint.definition_of_done.documentation %}
- [ ] {{ criteria }}
{% endfor %}

### Deployment
{% for criteria in sprint.definition_of_done.deployment %}
- [ ] {{ criteria }}
{% endfor %}

## Sprint Velocity Calculation
### Planned Velocity
- **Story Points Planned**: {{ sprint.velocity.planned_points }}
- **Sprint Duration**: {{ sprint.velocity.duration }} days
- **Daily Velocity**: {{ sprint.velocity.daily_velocity }} points/day

### Actual Velocity
- **Story Points Completed**: {{ sprint.velocity.completed_points | default('[To be filled during sprint]') }}
- **Actual Duration**: {{ sprint.velocity.actual_duration | default('[To be filled during sprint]') }} days
- **Actual Daily Velocity**: {{ sprint.velocity.actual_daily_velocity | default('[To be calculated]') }} points/day

### Velocity Analysis
{{ sprint.velocity.analysis | default('[Analysis of velocity trends and factors]') }}

{% if sections.sprint_template.agile_documents %}
## Agile Document Maintenance

### Sprint Review Updates
During the sprint review, update the following documents:
- **Scrum Master Guide**: Record ceremony effectiveness, team dynamics, and process improvements
- **Product Owner Guide**: Update backlog management insights, stakeholder feedback, and prioritization learnings
- **Kanban Metrics**: Update flow metrics, bottleneck analysis, and performance indicators

### Retrospective Updates
During the sprint retrospective, update the following documents:
- **Sprint Retrospective Template**: Document retrospective insights and action items
- **Scrum Master Guide**: Update team coaching strategies and impediment management approaches
- **Agile Methodology Selection Guide**: Note any methodology adjustments or process changes

### Process Evolution Tracking
Monitor and document:
- **Team Dynamics**: Changes in team composition, roles, or working relationships
- **Process Effectiveness**: What's working well and what needs adjustment
- **Tool Usage**: Effectiveness of agile tools and metrics
- **Stakeholder Engagement**: Changes in stakeholder needs or communication patterns

### Document Update Checklist
- [ ] Scrum Master Guide updated with ceremony insights
- [ ] Product Owner Guide updated with backlog management learnings
- [ ] Kanban Metrics updated with flow data
- [ ] Sprint Retrospective template updated with process improvements
- [ ] Agile Methodology Selection Guide updated if processes change
- [ ] Master Index updated with new document references
{% endif %}

## Sprint Retrospective Structure
### Data-Driven Analysis
{% for metric in sprint.retrospective.metrics %}
- **{{ metric.name }}**: {{ metric.value }}
  - **Target**: {{ metric.target }}
  - **Variance**: {{ metric.variance }}

{% endfor %}

### What Went Well
{% for item in sprint.retrospective.went_well %}
- {{ item }}
{% endfor %}

### What Could Be Improved
{% for item in sprint.retrospective.improvements %}
- {{ item }}
{% endfor %}

### Action Items
{% for action in sprint.retrospective.action_items %}
- [ ] {{ action.description }}
  - **Owner**: {{ action.owner }}
  - **Due Date**: {{ action.due_date }}

{% endfor %}

## Changelog
### Sprint Planning
- **Date**: {{ sprint.changelog.planning.date | default('[Date]') }}
- **Changes**: {{ sprint.changelog.planning.changes | default('[Initial sprint planning]') }}

### Daily Updates
{% for update in sprint.changelog.daily_updates %}
- **{{ update.date }}**: {{ update.changes }}
{% endfor %}

### Sprint Review
- **Date**: {{ sprint.changelog.review.date | default('[Date]') }}
- **Changes**: {{ sprint.changelog.review.changes | default('[Sprint review outcomes]') }}

### Master Index Updates (if cascade=true)
{% if features.cascade %}
- **Date**: {{ sprint.changelog.master_index.date | default('[Date]') }}
- **Changes**: {{ sprint.changelog.master_index.changes | default('[Updates to master index]') }}
{% endif %}

### Agile Document Updates
{% if sections.sprint_template.agile_documents %}
- **Date**: {{ sprint.changelog.agile_documents.date | default('[Date]') }}
- **Scrum Master Guide**: {{ sprint.changelog.agile_documents.scrum_master_guide | default('[Updates to Scrum Master Guide based on sprint learnings]') }}
- **Product Owner Guide**: {{ sprint.changelog.agile_documents.product_owner_guide | default('[Updates to Product Owner Guide based on sprint outcomes]') }}
- **Kanban Metrics**: {{ sprint.changelog.agile_documents.kanban_metrics | default('[Updates to Kanban Metrics based on flow data]') }}
- **Sprint Retrospective**: {{ sprint.changelog.agile_documents.sprint_retrospective | default('[Updates to Sprint Retrospective template based on process improvements]') }}
- **Process Evolution**: {{ sprint.changelog.agile_documents.process_evolution | default('[Updates to Agile Methodology Selection Guide if processes change]') }}
{% endif %}

### Prompt & Iteration Log
{% for iteration in sprint.changelog.prompt_iterations %}
- **{{ iteration.date }}**: {{ iteration.prompt_version }}
  - **Changes**: {{ iteration.changes }}
  - **Results**: {{ iteration.results }}

{% endfor %}

## Appendices
### References
{% for reference in sprint.references %}
- {{ reference }}
{% endfor %}

### Glossary
{% for term, definition in sprint.glossary.items() %}
- **{{ term }}**: {{ definition }}
{% endfor %}

### Templates
- **Daily Standup**: [Link to standup template]
- **Sprint Review**: [Link to review template]
- **Retrospective**: [Link to retrospective template]

---
*This sprint document should be updated daily and reviewed at the end of the sprint.*