# Sprint Template

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
10. **Parallel Agent Planning**: If using multiple agents, plan coordination and parallel processing
11. **Set Success Criteria**: Define clear completion criteria for each objective
12. **Master Index Update**: If cascade=true in development-guide.md, plan to update master-index.md during sprint execution and retrospectives
13. **Update Changelog**: Track progress throughout the sprint

## Sprint Metadata
- **Sprint Number**: [Sprint #]
- **Sprint Name**: [Sprint Name]
- **Duration**: [Start Date] - [End Date] ([X] weeks)
- **Sprint Goal**: [High-level sprint objective]
- **Sprint Owner**: [Name]
- **AI Agents**: [List of AI agents and development tools]
- **Sprint Capacity**: [Total story points planned]

## Sprint Overview
### Sprint Objectives
- [ ] [Primary objective 1]
- [ ] [Primary objective 2]
- [ ] [Primary objective 3]

### Success Criteria
- [ ] [Success criteria 1]
- [ ] [Success criteria 2]
- [ ] [Success criteria 3]

### Key Deliverables
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

## Planned Tasks
- [ ] [Task description] — <driver> ([X]d)
  - **Context Files**: `[File1.md#section]`, `[File2.js]`, `[File3.md#section]`
  - **Goal**: [Clear, specific goal for this task]
  - **Acceptance Criteria**: [Specific, testable criteria]
  - **Files to Modify**: `[file1.js]`, `[file2.js]`, `[file3.js]`
  - [ ] [Subtask 1]
  - [ ] [Subtask 2]
  - [ ] [Subtask 3]

- [ ] [Task description] — <driver> ([X]d)
  - **Context Files**: `[File1.md#section]`, `[File2.js]`, `[File3.md#section]`
  - **Goal**: [Clear, specific goal for this task]
  - **Acceptance Criteria**: [Specific, testable criteria]
  - **Files to Modify**: `[file1.js]`, `[file2.js]`, `[file3.js]`
  - [ ] [Subtask 1]
  - [ ] [Subtask 2]
  - [ ] [Subtask 3]

- [ ] [Task description] — <driver> ([X]d)
  - **Context Files**: `[File1.md#section]`, `[File2.js]`, `[File3.md#section]`
  - **Goal**: [Clear, specific goal for this task]
  - **Acceptance Criteria**: [Specific, testable criteria]
  - **Files to Modify**: `[file1.js]`, `[file2.js]`, `[file3.js]`
  - [ ] [Subtask 1]
  - [ ] [Subtask 2]
  - [ ] [Subtask 3]

## Optional Sections

### Database Schema Changes
- [ ] [Schema change 1]
- [ ] [Schema change 2]
- [ ] [Schema change 3]

**Migration Scripts:**
- [ ] [Migration 1]
- [ ] [Migration 2]
- [ ] [Migration 3]

### API Integration
#### External API Endpoints
- [ ] [API endpoint 1] - **Method**: [GET/POST/PUT/DELETE] - **Auth**: [Type]
- [ ] [API endpoint 2] - **Method**: [GET/POST/PUT/DELETE] - **Auth**: [Type]
- [ ] [API endpoint 3] - **Method**: [GET/POST/PUT/DELETE] - **Auth**: [Type]

#### Request Headers
- [ ] **Content-Type**: [application/json/application/xml/etc]
- [ ] **Authorization**: [Bearer token/API key/Basic auth/etc]
- [ ] **Accept**: [application/json/application/xml/etc]
- [ ] **Custom Headers**: [Header name: value]

#### Request Payloads
- [ ] [Payload structure 1] - **Required fields**: [field1, field2, field3]
- [ ] [Payload structure 2] - **Required fields**: [field1, field2, field3]
- [ ] [Payload structure 3] - **Required fields**: [field1, field2, field3]

#### Response Formats
- [ ] **Success Response**: [Status code, response structure]
- [ ] **Error Response**: [Status codes, error structure]
- [ ] **Data Validation**: [Response validation rules]

#### Integration Testing
- [ ] [API test scenario 1]
- [ ] [API test scenario 2]
- [ ] [API test scenario 3]

### Parallel Agent Capabilities
#### Agent Coordination
- [ ] [Agent coordination task 1] - **Primary Agent**: [Agent Name] - **Support Agent**: [Agent Name]
- [ ] [Agent coordination task 2] - **Primary Agent**: [Agent Name] - **Support Agent**: [Agent Name]
- [ ] [Agent coordination task 3] - **Primary Agent**: [Agent Name] - **Support Agent**: [Agent Name]

#### Parallel Processing
- [ ] [Parallel task 1] - **Agents**: [Agent A, Agent B] - **Synchronization**: [Method]
- [ ] [Parallel task 2] - **Agents**: [Agent A, Agent B] - **Synchronization**: [Method]
- [ ] [Parallel task 3] - **Agents**: [Agent A, Agent B] - **Synchronization**: [Method]

#### Agent Specialization
- [ ] [Specialized task 1] - **Required Agent**: [Agent Name] - **Capability**: [Specific skill]
- [ ] [Specialized task 2] - **Required Agent**: [Agent Name] - **Capability**: [Specific skill]
- [ ] [Specialized task 3] - **Required Agent**: [Agent Name] - **Capability**: [Specific skill]

#### Agent Communication
- [ ] [Communication protocol 1] - **Between**: [Agent A ↔ Agent B]
- [ ] [Communication protocol 2] - **Between**: [Agent A ↔ Agent B]
- [ ] [Communication protocol 3] - **Between**: [Agent A ↔ Agent B]

#### Conflict Resolution Protocol
- [ ] **Priority Order**: 1) Security, 2) Performance, 3) Simplicity
- [ ] **Conflict Detection**: [How to identify conflicting outputs]
- [ ] **Resolution Process**: [Steps to resolve conflicts between agents]
- [ ] **Escalation Path**: [When to involve human oversight]

#### AI Hallucination Mitigation
- [ ] **Validation Process**: [Validate AI-generated code with unit tests before commit]
- [ ] **Fact Checking**: [Verify AI claims against documentation]
- [ ] **Code Review**: [Human review of AI-generated code]
- [ ] **Rollback Plan**: [How to revert if AI generates incorrect code]

### Test Areas
#### Unit Tests
- [ ] [Test area 1]
- [ ] [Test area 2]
- [ ] [Test area 3]

#### Integration Tests
- [ ] [Test area 1]
- [ ] [Test area 2]
- [ ] [Test area 3]

#### End-to-End Tests
- [ ] [Test scenario 1]
- [ ] [Test scenario 2]
- [ ] [Test scenario 3]

#### Performance Tests
- [ ] [Performance test 1]
- [ ] [Performance test 2]
- [ ] [Performance test 3]

### Monitoring Areas
#### Application Monitoring
- [ ] [Monitoring setup 1]
- [ ] [Monitoring setup 2]
- [ ] [Monitoring setup 3]

#### Infrastructure Monitoring
- [ ] [Infrastructure monitoring 1]
- [ ] [Infrastructure monitoring 2]
- [ ] [Infrastructure monitoring 3]

#### Business Metrics
- [ ] [Business metric 1]
- [ ] [Business metric 2]
- [ ] [Business metric 3]

### Documentation Changes
#### Technical Documentation
- [ ] [Doc update 1]
- [ ] [Doc update 2]
- [ ] [Doc update 3]

#### User Documentation
- [ ] [User doc update 1]
- [ ] [User doc update 2]
- [ ] [User doc update 3]

#### API Documentation
- [ ] [API doc update 1]
- [ ] [API doc update 2]
- [ ] [API doc update 3]

### Algorithmic Details
#### Core Algorithms
- [ ] [Algorithm implementation 1]
- [ ] [Algorithm implementation 2]
- [ ] [Algorithm implementation 3]

#### Performance Optimizations
- [ ] [Optimization 1]
- [ ] [Optimization 2]
- [ ] [Optimization 3]

#### Data Processing
- [ ] [Data processing 1]
- [ ] [Data processing 2]
- [ ] [Data processing 3]

### Environmental Impact
#### Carbon Footprint Estimation
- [ ] [Feature carbon impact 1] - **Estimation Method**: [e.g., Green Software Foundation metrics]
- [ ] [Feature carbon impact 2] - **Estimation Method**: [e.g., Green Software Foundation metrics]
- [ ] [Feature carbon impact 3] - **Estimation Method**: [e.g., Green Software Foundation metrics]

#### Energy Efficiency Optimizations
- [ ] [Optimization 1] - **Impact**: [e.g., lazy loading in frontend]
- [ ] [Optimization 2] - **Impact**: [e.g., efficient database queries]
- [ ] [Optimization 3] - **Impact**: [e.g., CDN usage for static assets]

#### Sustainability Metrics
- [ ] **Energy Consumption**: [Target reduction percentage]
- [ ] **Resource Utilization**: [CPU/memory efficiency targets]
- [ ] **Green Hosting**: [Use of renewable energy sources]

## Risk Management

### Identified Risks
- [ ] **Risk 1**: [Description] - **Mitigation**: [Strategy]
- [ ] **Risk 2**: [Description] - **Mitigation**: [Strategy]
- [ ] **Risk 3**: [Description] - **Mitigation**: [Strategy]

### Dependencies
- [ ] [External dependency 1]
- [ ] [External dependency 2]
- [ ] [External dependency 3]

### Blockers
- [ ] [Blocker 1] - **Owner**: [Name] - **ETA**: [Date]
- [ ] [Blocker 2] - **Owner**: [Name] - **ETA**: [Date]
- [ ] [Blocker 3] - **Owner**: [Name] - **ETA**: [Date]

## Changelog

### Sprint Start
- [Date]: Sprint [X] started
- [Date]: Sprint planning completed
- [Date]: Tasks assigned to team members

### Daily Updates
- [Date]: [Update description]
- [Date]: [Update description]
- [Date]: [Update description]

### Sprint End
- [Date]: Sprint [X] completed
- [Date]: Sprint review conducted
- [Date]: Sprint retrospective completed
- [Date]: Next sprint planning initiated

### Key Decisions
- [Date]: [Decision made and rationale]
- [Date]: [Decision made and rationale]
- [Date]: [Decision made and rationale]

### Prompt & Iteration Log
- [Date] - Task [Task-ID]: Initial prompt failed to [issue]. Iteration 2: Added specific instruction '[instruction]'. Iteration 3: Succeeded.
- [Date] - Task [Task-ID]: Initial prompt failed to [issue]. Iteration 2: Added context file '[file]'. Iteration 3: Succeeded.
- [Date] - Task [Task-ID]: Initial prompt failed to [issue]. Iteration 2: Refined acceptance criteria. Iteration 3: Succeeded.

### Master Index Updates (if cascade=true)
- [Date] - [Change Type]: [Description of change] - [Files Updated]
- [Date] - [Change Type]: [Description of change] - [Files Updated]
- [Date] - [Change Type]: [Description of change] - [Files Updated]

### Lessons Learned
- [Date]: [Lesson learned 1]
- [Date]: [Lesson learned 2]
- [Date]: [Lesson learned 3]

## Definition of Done
### Code Complete
- [ ] Feature code written and peer reviewed
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] No critical security vulnerabilities
- [ ] Performance requirements met
- [ ] Accessibility requirements met
- [ ] Code follows development guide standards

### Sprint Velocity Calculation
- **Previous Sprint Velocity**: [X] points
- **Team Capacity**: [% of full capacity]
- **Adjusted Velocity**: [Previous × Capacity%]
- **Confidence Level**: [High/Medium/Low]
- **Velocity Trend**: [Increasing/Stable/Decreasing]

## Retrospective Structure
### Data-Driven Analysis
- **Cycle Time**: [Average days from start to done]
- **Defect Escape Rate**: [Bugs found post-sprint]
- **Automation Coverage**: [% of tests automated]
- **Code Quality Metrics**: [Technical debt, complexity scores]

### Action Items
- **Keep Doing**: [What worked well]
- **Start Doing**: [New improvements]
- **Stop Doing**: [What didn't work]
- **Experiments**: [Things to try next sprint]

## Sprint Metrics

### Planned vs Actual
- **Planned Story Points**: [X]
- **Completed Story Points**: [X]
- **Velocity**: [X] points/sprint
- **Burndown**: [Chart or description]

### Quality Metrics
- **Bug Count**: [X]
- **Test Coverage**: [X]%
- **Code Review Completion**: [X]%
- **Deployment Success Rate**: [X]%