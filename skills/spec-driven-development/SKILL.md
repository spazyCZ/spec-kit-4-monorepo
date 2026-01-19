---
name: spec-driven-development
description: Guide users through the complete Spec-Driven Development workflow from PRD to implementation. Use this skill when users need to create specifications, technical plans, or implement features using a structured development methodology. This skill helps transform high-level requirements into executable specifications across all phases - constitution, specification, clarification, planning, task breakdown, and implementation.
---

# Spec-Driven Development Workflow Automation

This skill automates the complete Spec-Driven Development (SDD) process, helping you transform Product Requirements Documents (PRDs) into fully executable specifications and implementation plans.

## Quick Start

When a user provides a PRD or feature description, guide them through the SDD workflow:

1. **Constitution** - Establish project principles and governance
2. **Specify** - Create structured feature specifications
3. **Clarify** - Resolve ambiguities through targeted questions
4. **Plan** - Generate technical implementation plans
5. **Tasks** - Break down into actionable task lists
6. **Implement** - Execute the implementation

## Core Workflow

### Phase 1: Establishing Foundation

#### Constitution (`/speckit.constitution`)

**Purpose**: Define project governance, principles, and architectural constraints.

**When to use**: 
- Starting a new project
- Major architectural decisions needed
- Team alignment required on principles

**Process**:
1. Read existing constitution at `/memory/constitution.md`
2. Identify gaps or needed principles from user input
3. Fill template with concrete values (no `[PLACEHOLDER]` tokens)
4. Ensure principles are testable and declarative
5. Version appropriately (MAJOR/MINOR/PATCH)
6. Propagate changes to dependent templates

**Key Requirements**:
- Each principle must have clear rationale
- Amendment process must be documented
- Compliance review expectations stated
- Version incremented per semantic versioning

**Reference**: See [references/constitution-guide.md](references/constitution-guide.md) for detailed guidance.

### Phase 2: Specification Creation

#### Specify (`/speckit.specify`)

**Purpose**: Convert natural language feature descriptions into structured specifications.

**Input**: Natural language feature description from user.

**Process**:
1. Generate concise branch name (2-4 words, action-noun format)
2. Check existing branches/specs for numbering
3. Run feature creation script with next available number
4. Parse user description for: actors, actions, data, constraints
5. Fill specification template with prioritized user stories
6. Generate functional requirements (testable, specific)
7. Define success criteria (measurable, tech-agnostic)
8. Identify key entities if data involved

**Critical Rules**:
- User stories must be independently testable
- Prioritize stories (P1, P2, P3, etc.)
- Limit to 3 `[NEEDS CLARIFICATION]` markers maximum
- Use reasonable defaults, document assumptions
- Each user story must deliver standalone value

**Template Location**: `/templates/spec-template.md`

**Reference**: See [references/specification-guide.md](references/specification-guide.md) for patterns and examples.

### Phase 3: Clarification

#### Clarify (`/speckit.clarify`)

**Purpose**: Resolve ambiguities through structured, coverage-based questioning before planning.

**When to run**: After specification creation, before planning to reduce downstream rework.

**Process**:
1. Read specification and identify ambiguous areas
2. Generate targeted questions focusing on:
   - Scope-impacting decisions
   - Security/privacy concerns
   - User experience critical paths
   - Integration requirements
3. Record answers in Clarifications section
4. Update specification with resolved information
5. Remove `[NEEDS CLARIFICATION]` markers

**Best Practice**: Run this before `/speckit.plan` to minimize plan revisions.

### Phase 4: Implementation Planning

#### Plan (`/speckit.plan`)

**Purpose**: Transform feature specifications into detailed technical implementation plans.

**Prerequisites**: 
- Completed specification (`spec.md`)
- Constitution exists (`/memory/constitution.md`)
- Clarifications resolved (or explicitly deferred)

**Process**:

1. **Setup**: Run setup script to get feature paths
2. **Load Context**: Read spec and constitution
3. **Phase 0 - Research**:
   - Identify unknowns from Technical Context
   - Generate research tasks for each unknown
   - Consolidate findings in `research.md`
   - Resolve all `NEEDS CLARIFICATION` items
4. **Phase 1 - Design**:
   - Extract entities → `data-model.md`
   - Generate API contracts → `/contracts/` directory
   - Create quickstart validation scenarios
   - Update agent-specific context files
5. **Constitution Check**:
   - Validate against constitutional principles
   - Document any justified violations
   - Re-check after design phase

**Outputs**:
- `plan.md` - High-level implementation roadmap
- `research.md` - Technology decisions and rationale
- `data-model.md` - Entity definitions and relationships
- `contracts/` - API specifications (OpenAPI/GraphQL)
- `quickstart.md` - Key validation scenarios

**Key Rules**:
- All paths must be absolute
- Error on gate failures or unresolved clarifications
- Keep plan.md readable (detailed specs go in separate files)
- Every technical choice needs documented rationale

**Reference**: See [references/planning-guide.md](references/planning-guide.md) for patterns.

### Phase 5: Task Breakdown

#### Tasks (`/speckit.tasks`)

**Purpose**: Convert implementation plans into ordered, executable task lists.

**Prerequisites**:
- Completed plan (`plan.md`)
- Optional: `data-model.md`, `contracts/`, `research.md`

**Process**:
1. Parse plan.md and supporting documents
2. Derive tasks from:
   - API contracts → endpoint implementation tasks
   - Entities → model creation tasks
   - Requirements → feature implementation tasks
3. Order tasks by dependencies (models → services → endpoints)
4. Mark parallel tasks with `[P]`
5. Group tasks by user story for incremental delivery
6. Include test tasks if TDD requested
7. Add checkpoint validations per user story

**Output**: `tasks.md` with structured task breakdown.

**Task Format**:
```
### User Story 1: [Title]
- [ ] Task description (file: path/to/file.ext)
- [ ] [P] Parallel task (file: path/to/other.ext)
- [ ] Checkpoint: Validate story completion
```

**Reference**: See [references/tasks-guide.md](references/tasks-guide.md) for task organization patterns.

### Phase 6: Implementation

#### Implement (`/speckit.implement`)

**Purpose**: Execute the task breakdown to build the feature.

**Prerequisites**:
- Constitution, spec, plan, and tasks all complete

**Process**:
1. Validate all prerequisites exist
2. Parse task breakdown from `tasks.md`
3. Execute tasks in order, respecting:
   - Dependencies (prerequisites before dependents)
   - Parallel markers (safe to run simultaneously)
   - TDD approach (tests before implementation)
4. Provide progress updates
5. Handle and report errors

**Important**: Agent will execute local CLI commands (dotnet, npm, etc.) - ensure required tools are installed.

## Script Integration

The skill relies on helper scripts in the spec-kit repository:

### Bash Scripts
- `scripts/bash/create-new-feature.sh` - Initialize feature branch and directories
- `scripts/bash/setup-plan.sh` - Set up planning environment
- `scripts/bash/update-agent-context.sh` - Update agent-specific context

### PowerShell Scripts
- `scripts/powershell/create-new-feature.ps1` - Windows equivalent for feature creation
- `scripts/powershell/setup-plan.ps1` - Windows planning setup
- `scripts/powershell/update-agent-context.ps1` - Windows agent context update

**Usage Pattern**:
```bash
# Bash example
scripts/bash/create-new-feature.sh --json --number 5 --short-name "user-auth" "Add user authentication"

# PowerShell example
scripts/powershell/create-new-feature.ps1 -Json -Number 5 -ShortName "user-auth" "Add user authentication"
```

## Progressive Workflow Example

**User starts with**: "I need a real-time chat system with message history"

**Step 1 - Constitution** (if needed):
```
/speckit.constitution Create principles for real-time systems: low latency, scalability, data consistency
```
Output: `/memory/constitution.md` with real-time principles

**Step 2 - Specify**:
```
/speckit.specify Real-time chat system with WebSocket messaging, persistent history, user presence indicators, and typing notifications
```
Output: `specs/001-chat-system/spec.md` with user stories, requirements, and entities

**Step 3 - Clarify**:
```
/speckit.clarify
```
AI asks: "Should message history be per-user or per-channel? What's the retention policy?" etc.
User responds, spec updated.

**Step 4 - Plan**:
```
/speckit.plan WebSocket for real-time, PostgreSQL for history, Redis for presence
```
Output: Multiple files in `specs/001-chat-system/`:
- `plan.md` - Implementation roadmap
- `research.md` - WebSocket library comparison
- `data-model.md` - Message, User, Channel entities
- `contracts/api-spec.json` - REST API definition
- `contracts/websocket-events.md` - Real-time event contracts

**Step 5 - Tasks**:
```
/speckit.tasks
```
Output: `specs/001-chat-system/tasks.md` with ordered task list

**Step 6 - Implement**:
```
/speckit.implement
```
Executes all tasks, builds the feature

## Key Principles

### Specification as Source of Truth
Specifications drive implementation. Code serves specifications, not vice versa.

### Progressive Disclosure
Load information incrementally:
1. Metadata always in context
2. SKILL.md when triggered
3. References as needed

### Testability First
Every requirement must be independently testable. Each user story must deliver standalone value.

### Constitutional Compliance
All technical decisions must align with project constitution. Document justified violations.

### Minimal Clarification Markers
Use `[NEEDS CLARIFICATION]` sparingly (max 3). Make informed assumptions with documented rationale.

## Common Patterns

### Starting Fresh Project
1. `/speckit.constitution` - Define principles
2. `/speckit.specify` - First feature
3. Continue workflow

### Adding Feature to Existing Project
1. Review existing constitution
2. `/speckit.specify` - New feature
3. Continue workflow

### Refining Existing Spec
1. Edit `spec.md` directly
2. Re-run `/speckit.plan` if needed
3. Continue from updated state

## Error Handling

**Missing Prerequisites**: 
- Error message indicates which file/step missing
- Guide user to complete prerequisite step

**Ambiguous Requirements**:
- Use `[NEEDS CLARIFICATION]` markers
- Run `/speckit.clarify` to resolve

**Constitution Violations**:
- Document rationale in Complexity Tracking section
- Require explicit justification before proceeding

## Template Locations

All templates are in the spec-kit repository:
- `/templates/spec-template.md` - Feature specification
- `/templates/plan-template.md` - Implementation plan
- `/templates/tasks-template.md` - Task breakdown
- `/templates/commands/*.md` - Command definitions

## Quality Gates

### Specification Quality
- [ ] All user stories independently testable
- [ ] Requirements are specific and testable
- [ ] Success criteria are measurable
- [ ] No more than 3 `[NEEDS CLARIFICATION]` markers
- [ ] Assumptions documented

### Plan Quality
- [ ] All constitutional gates pass or violations justified
- [ ] Technical context complete (no unresolved NEEDS CLARIFICATION)
- [ ] Research complete with rationale for all decisions
- [ ] Data model covers all entities
- [ ] API contracts match requirements

### Task Quality
- [ ] Tasks ordered by dependencies
- [ ] Parallel execution opportunities marked
- [ ] Each user story has validation checkpoint
- [ ] File paths specified for all tasks
- [ ] Test tasks included if TDD requested

## Anti-Patterns to Avoid

❌ **Premature Implementation Details**: Spec should focus on WHAT/WHY, not HOW
❌ **Guessing at Ambiguities**: Use clarification markers instead
❌ **Over-Engineering**: Constitution gates prevent unnecessary complexity
❌ **Skipping Clarification**: Leads to rework during planning
❌ **Missing Test Scenarios**: Every requirement needs acceptance criteria

## Getting Help

For detailed guidance on specific phases:
- Constitution: [references/constitution-guide.md](references/constitution-guide.md)
- Specification: [references/specification-guide.md](references/specification-guide.md)
- Planning: [references/planning-guide.md](references/planning-guide.md)
- Tasks: [references/tasks-guide.md](references/tasks-guide.md)

For workflow patterns and examples:
- [references/workflow-examples.md](references/workflow-examples.md)
