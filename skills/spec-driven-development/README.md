# Spec-Driven Development Skill

An Anthropic-compatible skill for guiding users through the complete Spec-Driven Development (SDD) workflow, from PRD to implementation.

## What This Skill Does

This skill automates and guides the process of transforming Product Requirements Documents (PRDs) into fully executable specifications through a structured, phase-based workflow:

1. **Constitution** - Establish project principles and governance
2. **Specification** - Create structured feature specifications  
3. **Clarification** - Resolve ambiguities through targeted questions
4. **Planning** - Generate technical implementation plans
5. **Tasks** - Break down into actionable task lists
6. **Implementation** - Execute the implementation

## When to Use This Skill

Use this skill when you need to:
- Transform a PRD or feature description into actionable specifications
- Create comprehensive technical implementation plans
- Break down complex features into ordered, executable tasks
- Ensure consistency across specification, design, and implementation
- Follow a structured development methodology

## Skill Structure

```
spec-driven-development/
├── SKILL.md                           # Main skill documentation
├── references/                        # Detailed guides
│   ├── constitution-guide.md         # Constitution creation & management
│   ├── specification-guide.md        # Writing effective specs
│   ├── planning-guide.md             # Implementation planning
│   ├── tasks-guide.md                # Task breakdown patterns
│   └── workflow-examples.md          # Complete workflow examples
└── scripts/                          # Helper scripts
    └── validate_workflow.py          # Validate workflow artifacts
```

## Quick Start

### Example Usage

**User provides**: "I need a REST API for managing a todo list"

**Skill guides through**:
1. `/speckit.constitution` - Establish API design principles
2. `/speckit.specify` - Create feature specification with user stories
3. `/speckit.clarify` - Resolve authentication, validation questions
4. `/speckit.plan` - Generate technical plan with tech stack
5. `/speckit.tasks` - Break down into ordered tasks
6. `/speckit.implement` - Execute implementation

**Result**: Complete, working REST API with tests, documentation, and proper architecture.

## Reference Documents

### Constitution Guide
Covers project governance, principles, and architectural constraints. Includes:
- Semantic versioning for constitutions
- Common principle categories
- Template propagation to ensure consistency
- Best practices and anti-patterns

### Specification Guide  
Details how to write effective feature specifications. Includes:
- User story structure and prioritization
- Acceptance scenario patterns (Given-When-Then)
- Handling ambiguity (3-marker rule)
- Requirement clarity and testability

### Planning Guide
Explains technical implementation planning. Includes:
- Research and technology selection
- Data model design
- API contract definition
- Constitutional compliance checking

### Tasks Guide
Shows how to break plans into executable tasks. Includes:
- Task organization by user story
- Dependency management
- Parallel execution strategies
- Common task patterns (CRUD, Auth, Real-time)

### Workflow Examples
Provides complete, end-to-end examples:
- Simple REST API
- Real-time chat application
- Mobile app with API backend
- Data processing pipeline
- CLI tool

## Scripts

### validate_workflow.py

Validates that a feature directory has the expected structure and content.

**Usage**:
```bash
python scripts/validate_workflow.py specs/001-feature-name
```

**Checks**:
- Required files exist (spec.md, plan.md, etc.)
- Specification contains user stories, requirements, acceptance scenarios
- Clarification markers limited to 3
- User stories are prioritized
- Constitution exists

## Integration with Spec Kit

This skill is designed to work with the [GitHub Spec Kit](https://github.com/github/spec-kit) repository, which provides:
- Template files for specifications, plans, and tasks
- Shell scripts for feature creation and setup
- Command definitions for AI agents
- Project structure and conventions

The skill references these templates and scripts to provide guidance throughout the workflow.

## Key Principles

### Specification as Source of Truth
Specifications drive implementation. Code serves specifications, not vice versa.

### Progressive Disclosure  
Information loaded incrementally:
1. Metadata (always in context)
2. SKILL.md (when triggered)
3. References (as needed)

### Testability First
Every requirement must be independently testable. Each user story must deliver standalone value.

### Constitutional Compliance
All technical decisions must align with project constitution. Violations must be justified.

### Minimal Clarification
Use `[NEEDS CLARIFICATION]` sparingly (max 3). Make informed assumptions with documented rationale.

## Quality Gates

### Specification Quality
- All user stories independently testable
- Requirements specific and testable
- Success criteria measurable
- Limited clarification markers
- Assumptions documented

### Plan Quality
- Constitutional gates pass or violations justified
- Technical context complete
- Research complete with rationale
- Data model covers all entities
- API contracts match requirements

### Task Quality
- Tasks ordered by dependencies
- Parallel execution marked
- Validation checkpoints per story
- File paths specified
- Test tasks included for TDD

## Common Anti-Patterns to Avoid

❌ **Premature Implementation**: Spec should focus on WHAT/WHY, not HOW  
❌ **Guessing at Ambiguities**: Use clarification markers instead  
❌ **Over-Engineering**: Constitutional gates prevent unnecessary complexity  
❌ **Skipping Clarification**: Leads to rework during planning  
❌ **Missing Test Scenarios**: Every requirement needs acceptance criteria

## License

This skill follows the Anthropic Skills standard and is provided as-is for use with Claude and other compatible AI assistants.

## Related Resources

- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Skill Creator Guide](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [Spec-Driven Development Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)
