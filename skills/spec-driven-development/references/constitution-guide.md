# Constitution Guide

## Purpose

The constitution (`/memory/constitution.md`) is the architectural DNA of your project. It defines immutable principles that govern how specifications become code.

## Core Sections

### 1. Project Identity
- **Project Name**: Official name
- **Version**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Ratification Date**: When constitution first adopted
- **Last Amended**: Most recent update date

### 2. Principles (Articles)

Each principle should follow this pattern:

```markdown
### Article [N]: [Principle Name]

[2-3 sentence description of the principle]

**Rationale**: [Why this principle exists]

**Requirements**:
- MUST: [Non-negotiable requirement]
- MUST: [Another requirement]
- SHOULD: [Recommended but not mandatory]

**Exceptions**: [When/if violations are acceptable]
```

#### Common Principle Categories

**Development Methodology**:
- Test-Driven Development requirements
- Code review processes
- Documentation standards

**Architecture**:
- Modularity requirements (e.g., library-first)
- Service boundaries
- Data flow patterns

**Quality**:
- Performance benchmarks
- Security standards
- Observability requirements

**Technology**:
- Approved tech stack
- Framework usage patterns
- Dependency management

### 3. Governance

Define how the constitution evolves:

```markdown
## Governance

### Amendment Process
1. Propose change with rationale
2. Review by [role/team]
3. Document impact assessment
4. Update version per semantic versioning

### Version Bumping Rules
- **MAJOR**: Breaking changes to principles
- **MINOR**: New principles or expanded guidance
- **PATCH**: Clarifications, typos, non-semantic fixes

### Compliance Reviews
- Frequency: [e.g., quarterly]
- Responsibility: [e.g., tech lead]
- Action: Audit recent code against principles
```

## Semantic Versioning Guidelines

### MAJOR Version (X.0.0)
Increment when:
- Removing a principle entirely
- Reversing a principle (MUST → MUST NOT)
- Changing core architectural patterns
- Breaking backward compatibility

Example: Removing "Library-First Principle" from constitution

### MINOR Version (0.X.0)
Increment when:
- Adding new principle/article
- Materially expanding existing guidance
- Adding new requirements to existing principles
- Introducing new quality gates

Example: Adding "Article X: Security-First Development"

### PATCH Version (0.0.X)
Increment when:
- Fixing typos or grammar
- Clarifying existing wording
- Reorganizing content without semantic change
- Updating examples

Example: Clarifying what "testable" means in TDD principle

## Template Propagation

When updating constitution, check these files:

### 1. Plan Template (`/templates/plan-template.md`)
- Update "Constitution Check" section
- Add new gates for new principles
- Remove gates for deleted principles

### 2. Spec Template (`/templates/spec-template.md`)
- Update any principle-driven sections
- Add new mandatory sections if principles require them

### 3. Tasks Template (`/templates/tasks-template.md`)
- Update task categories
- Add principle-specific validation tasks

### 4. Command Files (`/templates/commands/*.md`)
- Update references to principles
- Ensure commands enforce new principles

## Example Constitution Structures

### Minimal Constitution (Startup/Prototype)
```markdown
# Project Constitution

**Version**: 1.0.0
**Ratified**: 2024-01-15

## Article I: Ship Fast, Learn Fast
Focus on rapid iteration over perfection.

## Article II: Test What Matters
Write tests for critical paths only.

## Article III: Documentation as Code
README and inline comments are sufficient.
```

### Enterprise Constitution
```markdown
# Project Constitution

**Version**: 2.3.1
**Ratified**: 2023-06-01
**Last Amended**: 2024-01-15

## Article I: Security-First Development
All code changes must pass security review.
- MUST: Use approved authentication libraries
- MUST: Encrypt data at rest and in transit
- MUST: Log all security events

## Article II: Observability Mandate
Every service must be fully observable.
- MUST: Expose metrics, traces, logs
- MUST: Define SLIs for critical paths
- MUST: Alert on SLO violations

[... additional articles ...]

## Governance
### Amendment Process
1. RFC submitted to architecture board
2. 2-week review period
3. Approval requires consensus
4. Changes effective next sprint

### Compliance Reviews
Quarterly audits by security and architecture teams.
```

## Common Principles to Consider

### Development Process
- **Test-Driven Development**: Write tests before code
- **Code Review**: All changes need approval
- **Continuous Integration**: All tests must pass
- **Documentation**: Update docs with code changes

### Architecture
- **Library-First**: Features start as libraries
- **CLI Interface**: All libraries expose CLI
- **Microservices**: Service boundaries by domain
- **Event-Driven**: Async communication via events

### Quality
- **Performance**: Response time SLAs
- **Security**: OWASP Top 10 protection
- **Accessibility**: WCAG 2.1 AA compliance
- **Reliability**: 99.9% uptime requirement

### Technology
- **Language Standard**: Python 3.11+, Go 1.20+
- **Framework Preference**: Use standard library first
- **Database**: PostgreSQL for relational data
- **Container**: Docker for all services

## Updating Workflow

### Step-by-Step Process

1. **Identify Need**:
   - New project requirement
   - Lesson learned from incident
   - Team agreement on pattern
   - Compliance requirement

2. **Draft Change**:
   - Write new/updated article
   - Document rationale clearly
   - Identify affected templates
   - Determine version bump type

3. **Review Impact**:
   - Which existing code violates new principle?
   - Which templates need updates?
   - What migration path for violations?
   - Timeline for compliance?

4. **Update Templates**:
   - Plan template gates
   - Spec template sections
   - Task template categories
   - Command enforcement logic

5. **Document Change**:
   - Version bump with date
   - Amendment log entry
   - Migration guide if needed
   - Communication plan

6. **Validate Consistency**:
   - All templates updated
   - No orphaned references
   - Version matches change type
   - Dates in ISO format

## Best Practices

### DO:
✅ Keep principles declarative and testable
✅ Provide clear rationale for each principle
✅ Use MUST/SHOULD/MAY precisely
✅ Document when exceptions acceptable
✅ Keep amendment process simple
✅ Review and update quarterly

### DON'T:
❌ Use vague language ("try to", "generally")
❌ Create principles without rationale
❌ Skip version bumping
❌ Leave template inconsistencies
❌ Add principles for one-off cases
❌ Make principles overly prescriptive

## Sync Impact Report Format

When updating constitution, prepend this report as HTML comment:

```html
<!--
Constitution Update Report
Version: 1.2.0 → 1.3.0 (MINOR)
Date: 2024-01-15

Changes:
- Added: Article VI - Observability Mandate
- Modified: Article II - Test-First (expanded to include contract tests)

Template Updates:
✅ /templates/plan-template.md - Added observability gate
✅ /templates/tasks-template.md - Added monitoring setup tasks
⚠️  /templates/commands/implement.md - Manual review needed

Follow-up TODOs:
- [ ] Update existing projects to add observability
- [ ] Create observability quick-start guide
-->
```

## Validation Checklist

Before finalizing constitution update:

- [ ] No unexplained `[PLACEHOLDER]` tokens remain
- [ ] Version number matches change type
- [ ] Ratification/amendment dates in ISO format (YYYY-MM-DD)
- [ ] Each principle has clear rationale
- [ ] MUST vs SHOULD vs MAY used correctly
- [ ] Exception conditions documented
- [ ] Templates updated consistently
- [ ] Sync Impact Report prepended
- [ ] Amendment log entry added
- [ ] No trailing whitespace
- [ ] Markdown formatting valid

## Common Mistakes

### Mistake 1: Vague Principles
❌ "Code should be clean"
✅ "Code MUST pass linting with zero warnings (Article III: Code Quality)"

### Mistake 2: Missing Rationale
❌ "All functions must be pure"
✅ "All functions must be pure (Rationale: Enables parallelization and testing)"

### Mistake 3: Inconsistent Versioning
❌ Adding new principle as PATCH
✅ Adding new principle as MINOR

### Mistake 4: Orphaned Templates
❌ Update constitution, forget plan template
✅ Update constitution and all referenced templates

### Mistake 5: No Governance
❌ Constitution with no amendment process
✅ Constitution with clear governance section
