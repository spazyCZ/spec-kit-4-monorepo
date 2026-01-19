# Using the Spec-Driven Development Skill

## Installation

1. **Option 1: Direct Use with Claude Desktop**
   - Place the `spec-driven-development` folder in your Claude skills directory
   - The skill will be automatically available when Claude starts

2. **Option 2: Package as .skill file**
   - Use Anthropic's packaging tool to create a `.skill` file
   - Share the `.skill` file with your team

## Example Session

### Scenario: User wants to build a todo list API

**User**: "I have a PRD for a todo list REST API. I need help creating a complete specification and implementation plan."

**Claude (with skill loaded)**: "I'll guide you through the Spec-Driven Development workflow to transform your PRD into a complete, executable specification. Let's start with the constitution phase to establish project principles."

---

### Phase 1: Constitution

**Claude**: "Let's establish the foundational principles for your project. Based on your REST API needs, I recommend creating a constitution focused on:
- RESTful design standards
- Comprehensive testing
- Clear error handling
- API documentation

Would you like me to create a constitution with these principles?"

**User**: "Yes, please create it."

**Claude creates** `/memory/constitution.md` with articles covering:
- Article I: RESTful Design
- Article II: Test Coverage  
- Article III: Error Handling
- Article IV: Documentation Standards

---

### Phase 2: Specification

**Claude**: "Now let's create the feature specification. Please describe your todo list API requirements."

**User**: "Users should be able to create todos with a title and description, list all their todos, update existing todos, and delete todos. Each todo has a completion status."

**Claude**: "I'll create a structured specification with prioritized user stories. Let me analyze your requirements..."

**Claude creates** `specs/001-todo-api/spec.md` containing:

```markdown
# Feature Specification: Todo Management API

## User Scenarios & Testing

### User Story 1 - Create Todo (Priority: P1)
User submits new todo with title and description.

**Acceptance Scenarios**:
1. **Given** valid title/description, **When** POST /todos, **Then** 201 with created todo
2. **Given** missing title, **When** POST /todos, **Then** 400 with error
...

### User Story 2 - List Todos (Priority: P1)
User retrieves all their todos with pagination.

### User Story 3 - Update Todo (Priority: P2)
User modifies existing todo details or completion status.

### User Story 4 - Delete Todo (Priority: P2)
User removes todo from the system.

## Requirements
### Functional Requirements
- FR-001: System MUST create todo with title (1-200 chars) and optional description
- FR-002: System MUST list todos with pagination (20 per page)
...
```

---

### Phase 3: Clarification (Optional)

**Claude**: "I notice a few areas that could use clarification:

1. Should todos be user-specific or shared globally?
2. Do you need authentication for this API?
3. What's the expected load (requests per second)?

These will help me create a more accurate technical plan."

**User**: "No authentication for now, todos are shared. Expecting low load, maybe 10 requests/second."

**Claude updates spec.md** with clarifications documented in Assumptions section.

---

### Phase 4: Planning

**Claude**: "Now let's create the technical implementation plan. What technology stack would you prefer?"

**User**: "Python with FastAPI, SQLite database, pytest for testing."

**Claude**: "Perfect. I'll create a comprehensive implementation plan..."

**Claude creates multiple files**:

1. **`specs/001-todo-api/plan.md`** - High-level implementation roadmap
2. **`specs/001-todo-api/research.md`** - Technology decisions and rationale
3. **`specs/001-todo-api/data-model.md`** - Todo entity definition
4. **`specs/001-todo-api/contracts/api-spec.json`** - OpenAPI specification
5. **`specs/001-todo-api/quickstart.md`** - Validation scenarios

**Claude**: "I've generated your implementation plan. The design includes:
- Single FastAPI application (satisfies Simplicity Gate)
- SQLite for persistence (lightweight, embedded)
- Standard REST endpoints for CRUD operations
- Comprehensive test coverage (pytest + httpx)

All constitutional gates pass. Ready to proceed to task breakdown?"

---

### Phase 5: Task Breakdown

**User**: "Yes, create the tasks."

**Claude creates** `specs/001-todo-api/tasks.md`:

```markdown
# Tasks: Todo Management API

### User Story 1: Create Todo (Priority: P1)

#### Setup
- [ ] Initialize FastAPI project (files: main.py, requirements.txt)
- [ ] Configure SQLite database (file: src/database.py)
- [ ] Set up pytest (file: tests/conftest.py)

#### Data Layer
- [ ] Create Todo model (file: src/models/todo.py)
- [ ] Create database schema (file: migrations/001_todos.sql)

#### Service Layer
- [ ] Create todo service: create operation (file: src/services/todo_service.py)

#### API Layer
- [ ] POST /todos endpoint (file: src/api/todos.py)
- [ ] Error handling middleware (file: src/middleware/errors.py)

#### Testing
- [ ] Model validation tests (file: tests/unit/test_todo_model.py)
- [ ] POST /todos integration test (file: tests/integration/test_create_todo.py)

#### Checkpoint
- [ ] Can create todo via API
- [ ] Validation works
- [ ] Tests passing

[... more tasks for stories 2-4 ...]
```

**Claude**: "I've created 45 tasks organized by user story, with dependencies marked and parallel execution opportunities identified. The tasks follow a test-driven approach per your constitution."

---

### Phase 6: Implementation

**User**: "Great! Can you implement this?"

**Claude**: "I'll now execute the implementation plan. I'll work through each task in order, respecting dependencies and running tests as we go..."

**Claude executes**:
1. Project setup
2. Data models with validation
3. Service layer logic
4. API endpoints
5. Tests (unit, integration)
6. Documentation

**Final Result**: A complete, tested REST API matching all specifications.

---

## Key Benefits Demonstrated

1. **Structured Process**: Each phase builds on the previous, ensuring nothing is missed
2. **Clear Documentation**: Every decision documented with rationale
3. **Testability**: Acceptance scenarios → test cases
4. **Incremental Value**: User stories prioritized for progressive delivery
5. **Constitutional Compliance**: Architectural principles enforced throughout
6. **Comprehensive**: From high-level requirements to working code

## Validation

After the workflow completes, you can validate using the included script:

```bash
python skills/spec-driven-development/scripts/validate_workflow.py specs/001-todo-api
```

This checks:
- ✓ All required files exist
- ✓ Specification has user stories with priorities
- ✓ Requirements are testable
- ✓ Acceptance scenarios use Given-When-Then
- ✓ Clarification markers limited (≤3)

## Progressive Disclosure

The skill uses progressive disclosure effectively:

1. **Initial Load**: Only metadata and description (minimal context)
2. **Phase Guidance**: Skill body loaded when activated
3. **Deep Dives**: Reference guides loaded only when specific phase needs detailed guidance

Example: If user struggles with writing good user stories, Claude can reference `specification-guide.md` for detailed patterns and examples.

## Skill Adaptation

The skill adapts to different project types:
- Simple REST APIs (as shown above)
- Real-time systems (WebSockets, events)
- Mobile apps (iOS/Android with backend)
- Data pipelines (ETL workflows)
- CLI tools (command-line applications)

See `references/workflow-examples.md` for complete examples of each type.

## Tips for Best Results

1. **Provide Context**: More detail in initial PRD = better specification
2. **Answer Clarifications**: Don't skip the clarify phase
3. **Review Before Implementation**: Validate plan before executing tasks
4. **Use Checkpoints**: Test after each user story for incremental validation
5. **Trust the Process**: Each phase sets up the next for success
