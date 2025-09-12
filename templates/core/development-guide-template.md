# Development Guide Template

## System Prompt for AI Agent
You are an expert full-stack software engineer working on the [Project Name].
Your primary goal is to generate clean, efficient, and maintainable code.
Current Date: [Insert current date] - Use this for up-to-date library recommendations.

ALWAYS adhere to the following project-specific guidelines documented in this file:

1. **Coding Standards**: Follow all rules in Section 1.
2. **Project Structure**: All new files must be created in the correct location as defined in Section 2.
3. **Git Workflow**: All commits must follow the convention in Section 3.2.
4. **Error Handling**: Use the patterns defined in Section 5.
5. **Security Guidelines**: Follow all security practices in Section 7.
6. **Performance Standards**: Apply optimization techniques from Section 6.
7. **Modern Paradigms**: Follow current best practices from Section 8.

### Ethical Guidelines
- **Data Privacy**: Ensure code promotes data privacy (GDPR/CCPA compliance)
- **Bias Prevention**: Avoid biased algorithms and ensure diverse, representative data
- **Transparency**: Include clear documentation for AI-generated code decisions
- **Accessibility**: Generate accessible code that works for all users

### Version Awareness
- **Current Libraries**: Use current date [insert date] for up-to-date library recommendations
- **Deprecation Avoidance**: Avoid deprecated features and suggest modern alternatives
- **Security Updates**: Prioritize security patches and current best practices

Before you begin, confirm you have read and understood these instructions.

## Instructions for Creating a Development Guide
1. **Team Standards**: Establish coding standards that work for your team and technology stack
2. **Tool Selection**: Choose development tools (linters, formatters, testing frameworks)
3. **Process Definition**: Define git workflow, code review process, and deployment procedures
4. **Testing Strategy**: Establish testing levels, coverage targets, and quality gates
5. **Security Guidelines**: Include security best practices and code review checklists
6. **Performance Standards**: Define performance guidelines and optimization practices
7. **Documentation Requirements**: Set standards for code documentation and comments
8. **Cascade Setting**: Set cascade=true if feature changes should update planning docs and Master Index
9. **Master Index Update**: If cascade=true, update master-index.md when coding standards or processes change
10. **Team Training**: Ensure all team members understand and follow the guide
11. **Regular Updates**: Plan to review and update the guide as practices evolve

## Document Information
- **Version**: [Version Number]
- **Last Updated**: [Date]
- **Author**: [Author Name]
- **Cascade**: [true/false] - If true, changes to features require updates to planning docs and Master Index

## 1. Coding Standards
### General Principles
- [Coding principle 1]
- [Coding principle 2]
- [Coding principle 3]

### Language Standards
#### [Language Name]
```[language]
// [Code example with comments]
[code example]
```

#### [Language Name]
```[language]
// [Code example with comments]
[code example]
```

## 2. Project Structure
```
src/
├── [directory 1]/          # [Purpose]
├── [directory 2]/          # [Purpose]
├── [directory 3]/          # [Purpose]
└── [directory 4]/          # [Purpose]
```

## 3. Git Workflow
### Branching Strategy
- **[branch name]**: [Description]
- **[branch name]**: [Description]
- **[branch name]**: [Description]

### Commit Convention
```
[type]([scope]): [description]

[type]: [description]
[type]: [description]
```

### Pull Request Process
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]

## 4. Testing Guidelines
### Test Structure
```[language]
[test code example]
```

### Testing Levels
- **[Level 1]**: [Description]
- **[Level 2]**: [Description]
- **[Level 3]**: [Description]
- **Coverage Target**: [Percentage]% code coverage

## 5. Error Handling
### Error Types
```[language]
// [Error handling example]
[code example]
```

### Error Handling Pattern
```[language]
[error handling pattern example]
```

## 6. Performance Guidelines
### [Category 1] Optimization
- [Optimization tip 1]
- [Optimization tip 2]
- [Optimization tip 3]

### [Category 2] Optimization
- [Optimization tip 1]
- [Optimization tip 2]
- [Optimization tip 3]

## 7. Security Best Practices
### [Security Category 1]
```[language]
[security code example]
```

### [Security Category 2]
- [Security practice 1]
- [Security practice 2]
- [Security practice 3]

## 8. Modern Paradigms
### Serverless Architecture
- **Function Design**: [e.g., AWS Lambda patterns, cold start optimization]
- **Event-Driven**: [e.g., event sourcing, CQRS patterns]
- **Stateless Design**: [e.g., session management, state storage]

### AI/ML Integration
- **MLOps Practices**: [e.g., MLflow, model versioning, A/B testing]
- **Data Pipeline**: [e.g., ETL processes, feature stores]
- **Model Deployment**: [e.g., containerization, monitoring]

### Edge Computing
- **Edge Functions**: [e.g., Cloudflare Workers, Vercel Edge]
- **CDN Integration**: [e.g., edge caching, geographic distribution]
- **Offline-First**: [e.g., service workers, local storage]

### Microservices & Containers
- **Container Patterns**: [e.g., Docker best practices, Kubernetes]
- **Service Mesh**: [e.g., Istio, Linkerd for service communication]
- **API Gateway**: [e.g., routing, rate limiting, authentication]

### Low-Code/No-Code Integration
- **Workflow Automation**: [e.g., Zapier, Microsoft Power Automate]
- **Visual Development**: [e.g., drag-and-drop interfaces]
- **API-First Design**: [e.g., headless CMS, composable architecture]

## 9. Anti-Patterns / Things to Avoid
### Code Quality Anti-Patterns
- **NEVER** [Anti-pattern 1]
- **NEVER** [Anti-pattern 2]
- **NEVER** [Anti-pattern 3]
- **NEVER** [Anti-pattern 4]
- **NEVER** [Anti-pattern 5]

### Security Anti-Patterns
- **NEVER** [Security anti-pattern 1]
- **NEVER** [Security anti-pattern 2]
- **NEVER** [Security anti-pattern 3]
- **NEVER** [Security anti-pattern 4]
- **NEVER** [Security anti-pattern 5]

### Performance Anti-Patterns
- **NEVER** [Performance anti-pattern 1]
- **NEVER** [Performance anti-pattern 2]
- **NEVER** [Performance anti-pattern 3]
- **NEVER** [Performance anti-pattern 4]
- **NEVER** [Performance anti-pattern 5]

### Architecture Anti-Patterns
- **NEVER** [Architecture anti-pattern 1]
- **NEVER** [Architecture anti-pattern 2]
- **NEVER** [Architecture anti-pattern 3]
- **NEVER** [Architecture anti-pattern 4]
- **NEVER** [Architecture anti-pattern 5]

## 10. Common Scripts
### Package Management
```bash
# Install dependencies
[package-manager] install

# Add new dependency
[package-manager] add [package-name]

# Update dependencies
[package-manager] update
```

### Development
```bash
# Start development server
[dev-command]

# Build for production
[build-command]

# Run tests
[test-command]
```

### Code Quality
```bash
# Lint code
[lint-command]

# Format code
[format-command]

# Type checking
[type-check-command]
```

### Database
```bash
# Run migrations
[migrate-command]

# Create migration
[migrate-create-command] [name]

# Seed database
[seed-command]
```

### Deployment
```bash
# Deploy to staging
[deploy-staging-command]

# Deploy to production
[deploy-prod-command]

# Build container
[container-build-command]

# Run container
[container-run-command]
```

### Utilities
```bash
# Generate documentation
[docs-command]

# Clean build artifacts
[clean-command]

# Check for security vulnerabilities
[security-check-command]
```

## 11. Code Review Automation
### Pre-commit Hooks
- **Linting**: [ESLint, Pylint, RuboCop configuration]
- **Formatting**: [Prettier, Black, gofmt setup]
- **Security**: [Gitleaks, Semgrep, Snyk integration]
- **Complexity**: [Cyclomatic complexity checks, cognitive complexity limits]

### PR Automation
- **Required Checks**: [List of GitHub Actions/CI checks that must pass]
- **Auto-assignment**: [CODEOWNERS file configuration]
- **Merge Rules**: [Branch protection settings, required reviewers]

### Automated Testing
- **Unit Tests**: [Minimum coverage requirements, test patterns]
- **Integration Tests**: [API testing, database testing]
- **E2E Tests**: [Critical user journey automation]

## 12. Performance Profiling
### Frontend Performance
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1
- **Bundle Analysis**: [Webpack Bundle Analyzer, Rollup analyzer]
- **Runtime Profiling**: [Chrome DevTools Performance, React Profiler]
- **Lighthouse Scores**: [Performance, Accessibility, Best Practices, SEO]

### Backend Performance
- **APM Tools**: [DataDog, New Relic, AppDynamics configuration]
- **Database Profiling**: [Query analysis, index usage, slow query monitoring]
- **Load Testing**: [k6, JMeter thresholds and scenarios]
- **Memory Profiling**: [Heap dumps, memory leak detection]

### Performance Monitoring
- **Real User Monitoring (RUM)**: [User experience metrics]
- **Synthetic Monitoring**: [Uptime checks, performance tests]
- **Alert Thresholds**: [Performance degradation alerts]

## 13. Code Review Checklist
### Before Submitting
- [ ] [Checklist item 1]
- [ ] [Checklist item 2]
- [ ] [Checklist item 3]
- [ ] [Checklist item 4]

### Review Criteria
- [ ] [Review criteria 1]
- [ ] [Review criteria 2]
- [ ] [Review criteria 3]
- [ ] [Review criteria 4]
- [ ] [Review criteria 5]
