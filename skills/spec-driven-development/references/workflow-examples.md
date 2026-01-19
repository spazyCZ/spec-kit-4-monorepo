# Workflow Examples

This document provides complete, end-to-end examples of the Spec-Driven Development workflow for common project types.

## Example 1: Simple REST API

### User Input
"I need a REST API for managing a todo list. Users should be able to create, read, update, and delete todos. Each todo has a title, description, and completion status."

### Phase 1: Constitution

```bash
/speckit.constitution Create principles for a simple REST API: focus on clarity, standard REST patterns, comprehensive error handling, and extensive testing
```

**Output**: `/memory/constitution.md`
```markdown
# Project Constitution v1.0.0

## Article I: RESTful Design
All APIs MUST follow standard REST conventions.

## Article II: Test Coverage
All endpoints MUST have integration tests.

## Article III: Error Handling
All errors MUST return consistent JSON format.
```

### Phase 2: Specify

```bash
/speckit.specify REST API for todo list management. Users create, read, update, delete todos. Each todo has title, description, completion status.
```

**Output**: `specs/001-todo-api/spec.md`
```markdown
# Feature Specification: Todo Management API

## User Scenarios & Testing

### User Story 1 - Create Todo (Priority: P1)
User submits new todo with title and description.

**Acceptance Scenarios**:
1. **Given** valid title/description, **When** POST /todos, **Then** 201 with created todo
2. **Given** missing title, **When** POST /todos, **Then** 400 with error
3. **Given** empty title, **When** POST /todos, **Then** 400 with validation error

### User Story 2 - List Todos (Priority: P1)
User retrieves all their todos.

**Acceptance Scenarios**:
1. **Given** todos exist, **When** GET /todos, **Then** 200 with array
2. **Given** no todos, **When** GET /todos, **Then** 200 with empty array
3. **Given** many todos, **When** GET /todos, **Then** paginated results

### User Story 3 - Update Todo (Priority: P2)
User modifies existing todo.

**Acceptance Scenarios**:
1. **Given** valid todo ID, **When** PUT /todos/{id}, **Then** 200 with updated
2. **Given** invalid ID, **When** PUT /todos/{id}, **Then** 404
3. **Given** completed=true, **When** PUT /todos/{id}, **Then** status updated

### User Story 4 - Delete Todo (Priority: P2)
User removes todo.

**Acceptance Scenarios**:
1. **Given** valid ID, **When** DELETE /todos/{id}, **Then** 204
2. **Given** invalid ID, **When** DELETE /todos/{id}, **Then** 404
3. **Given** already deleted, **When** DELETE /todos/{id}, **Then** 404

## Requirements

### Functional Requirements
- **FR-001**: System MUST create todo with title (1-200 chars) and optional description
- **FR-002**: System MUST list todos with pagination (20 per page)
- **FR-003**: System MUST update todo title, description, or completion status
- **FR-004**: System MUST delete todos permanently
- **FR-005**: System MUST validate input before persistence

### Non-Functional Requirements
- **NFR-001**: API response time MUST be <100ms for 95th percentile
- **NFR-002**: API MUST handle 100 requests/second
- **NFR-003**: Error messages MUST be user-friendly and actionable

### Key Entities
- **Todo**: Task item
  - Attributes: id, title, description, completed, created_at, updated_at
  - Validation: title required 1-200 chars, description optional <1000 chars
```

### Phase 3: Clarify (Optional)

```bash
/speckit.clarify
```

AI asks: "Should todos be user-specific or global? Authentication required?"
User responds: "No authentication for now, todos are shared."

Spec updated to reflect shared todos.

### Phase 4: Plan

```bash
/speckit.plan Python FastAPI, SQLite database, pytest for testing
```

**Outputs**:

**`specs/001-todo-api/plan.md`**:
```markdown
# Implementation Plan: Todo Management API

## Summary
REST API for shared todo list using FastAPI and SQLite.

## Technical Context
- Language: Python 3.11
- Framework: FastAPI 0.104
- Database: SQLite (simple, embedded)
- Testing: pytest, httpx
- Project Type: Single service

## Constitution Check
### Simplicity Gate
- [x] Single project (backend only)
- [x] No future-proofing

### Test Coverage Gate
- [x] Integration tests for all endpoints
```

**`specs/001-todo-api/data-model.md`**:
```markdown
# Data Model: Todo API

## Entities

### Todo
**Attributes**:
- id: INTEGER PRIMARY KEY
- title: TEXT NOT NULL (1-200 chars)
- description: TEXT NULL (<1000 chars)
- completed: BOOLEAN DEFAULT FALSE
- created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
- updated_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

**Validation**:
- Title required, 1-200 characters
- Description optional, max 1000 characters
- Completed defaults to false

**Indexes**:
- PRIMARY KEY on id
- INDEX on completed for filtering
```

**`specs/001-todo-api/contracts/api-spec.json`** (OpenAPI):
```json
{
  "paths": {
    "/todos": {
      "get": {
        "summary": "List todos",
        "parameters": [
          {"name": "page", "in": "query", "schema": {"type": "integer", "default": 1}},
          {"name": "limit", "in": "query", "schema": {"type": "integer", "default": 20}}
        ],
        "responses": {
          "200": {
            "description": "List of todos",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "items": {"type": "array", "items": {"$ref": "#/components/schemas/Todo"}},
                    "total": {"type": "integer"},
                    "page": {"type": "integer"},
                    "limit": {"type": "integer"}
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "summary": "Create todo",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {"$ref": "#/components/schemas/TodoCreate"}
            }
          }
        },
        "responses": {
          "201": {"description": "Todo created"},
          "400": {"description": "Validation error"}
        }
      }
    }
  }
}
```

### Phase 5: Tasks

```bash
/speckit.tasks
```

**Output**: `specs/001-todo-api/tasks.md`
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
- [ ] Add validation functions (file: src/models/todo.py)

#### Service Layer
- [ ] Create todo service: create operation (file: src/services/todo_service.py)
- [ ] Create todo service: validation logic (file: src/services/todo_service.py)

#### API Layer
- [ ] POST /todos endpoint (file: src/api/todos.py)
- [ ] Error handling middleware (file: src/middleware/errors.py)

#### Testing
- [ ] Model validation tests (file: tests/unit/test_todo_model.py)
- [ ] Service logic tests (file: tests/unit/test_todo_service.py)
- [ ] POST /todos integration test (file: tests/integration/test_create_todo.py)

#### Checkpoint
- [ ] Can create todo via API
- [ ] Validation works
- [ ] Tests passing

### User Story 2: List Todos (Priority: P1)

#### Service Layer
- [ ] Todo service: list with pagination (file: src/services/todo_service.py)

#### API Layer
- [ ] GET /todos endpoint (file: src/api/todos.py)

#### Testing
- [ ] List pagination tests (file: tests/integration/test_list_todos.py)
- [ ] Empty list test (file: tests/integration/test_list_todos.py)

#### Checkpoint
- [ ] Can list todos
- [ ] Pagination works
- [ ] Tests passing

### User Story 3: Update Todo (Priority: P2)

#### Service Layer
- [ ] Todo service: update operation (file: src/services/todo_service.py)

#### API Layer
- [ ] PUT /todos/{id} endpoint (file: src/api/todos.py)

#### Testing
- [ ] Update tests (file: tests/integration/test_update_todo.py)

#### Checkpoint
- [ ] Can update todos
- [ ] Tests passing

### User Story 4: Delete Todo (Priority: P2)

#### Service Layer
- [ ] Todo service: delete operation (file: src/services/todo_service.py)

#### API Layer
- [ ] DELETE /todos/{id} endpoint (file: src/api/todos.py)

#### Testing
- [ ] Delete tests (file: tests/integration/test_delete_todo.py)

#### Checkpoint
- [ ] Can delete todos
- [ ] Tests passing
```

### Phase 6: Implement

```bash
/speckit.implement
```

Executes all tasks in order, building the complete API.

---

## Example 2: Real-time Chat Application

### User Input
"Build a real-time chat application with WebSocket support. Users can create channels, send messages, see who's online, and get typing indicators."

### Phase 1: Constitution

```bash
/speckit.constitution Create principles for real-time systems: low latency (<100ms), scalability to 1000 concurrent connections, graceful degradation, comprehensive error handling
```

### Phase 2: Specify

```bash
/speckit.specify Real-time chat with WebSocket. Users create channels, send messages, see online users, typing indicators. Messages persist. Presence tracking.
```

**Key user stories**:
1. **P1**: Send/receive messages in real-time
2. **P1**: Create and join channels
3. **P2**: See who's online
4. **P3**: Show typing indicators

### Phase 3: Clarify

```bash
/speckit.clarify
```

Questions:
- Message history retention? → "Keep all messages, no deletion for now"
- Authentication required? → "Yes, JWT-based"
- Multiple channels per user? → "Yes"

### Phase 4: Plan

```bash
/speckit.plan FastAPI for REST, WebSocket for real-time, PostgreSQL for messages, Redis for presence/typing
```

**Key outputs**:
- `research.md`: Why PostgreSQL over MongoDB (relational queries), why Redis (TTL for presence)
- `data-model.md`: User, Channel, Message, ChannelMembership entities
- `contracts/websocket-events.md`: Event schemas for message.send, typing.start, presence.update
- `contracts/rest-api.json`: REST endpoints for channel/user CRUD

### Phase 5: Tasks

Tasks include:
- WebSocket connection management
- Event bus for broadcasting
- REST APIs for data management
- Real-time event handlers
- Presence tracking with TTL
- Typing indicator debouncing

### Phase 6: Implement

Builds complete real-time system with REST + WebSocket.

---

## Example 3: Mobile App with API

### User Input
"iOS app for tracking daily habits. Users create habits, check them off daily, view progress charts. Sync across devices."

### Phase 1: Constitution

```bash
/speckit.constitution iOS app principles: offline-first, Core Data for local storage, sync via REST API, SwiftUI for UI, XCTest for testing
```

### Phase 2: Specify

```bash
/speckit.specify iOS habit tracker. Create habits, daily check-offs, progress charts, device sync. Offline capable.
```

**Key user stories**:
1. **P1**: Create and manage habits
2. **P1**: Check off habits daily (offline)
3. **P1**: Sync data across devices
4. **P2**: View progress charts
5. **P3**: Habit streaks and statistics

### Phase 3: Plan

```bash
/speckit.plan iOS app: SwiftUI + Core Data + Combine. Backend: FastAPI + PostgreSQL. Sync: background fetch with conflict resolution (last-write-wins)
```

**Project structure**:
```
backend/        # FastAPI REST API
├── src/
└── tests/

ios/           # iOS app
├── HabitTracker/
│   ├── Models/
│   ├── Views/
│   ├── ViewModels/
│   ├── Services/
│   └── Persistence/
└── HabitTrackerTests/
```

### Phase 4: Tasks

**Backend tasks**:
- User authentication
- Habit CRUD API
- Check-off tracking API
- Sync endpoint with timestamps

**iOS tasks**:
- Core Data models
- Local CRUD operations
- SwiftUI views
- Sync service with conflict resolution
- Background fetch
- Charts with Swift Charts

---

## Example 4: Data Processing Pipeline

### User Input
"Build a pipeline that processes CSV files, validates data, enriches it with external API calls, and exports to database and S3."

### Phase 1: Constitution

```bash
/speckit.constitution Data pipeline principles: idempotency, error recovery, monitoring, schema validation, backpressure handling
```

### Phase 2: Specify

```bash
/speckit.specify Data pipeline: ingest CSV, validate schema, enrich via API, load to PostgreSQL and S3. Handle errors gracefully, provide progress tracking.
```

**Key user stories**:
1. **P1**: Ingest CSV files and validate
2. **P1**: Enrich data via external API
3. **P1**: Load to PostgreSQL
4. **P2**: Export to S3 for archival
5. **P2**: Error handling and retry
6. **P3**: Progress tracking and alerts

### Phase 3: Plan

```bash
/speckit.plan Python with Pandas for CSV, asyncio for API calls, SQLAlchemy for database, boto3 for S3. Prefect for orchestration and monitoring.
```

**Architecture**:
- Task 1: Extract (read CSV, validate)
- Task 2: Transform (API enrichment, data cleaning)
- Task 3: Load (database insert, S3 upload)
- Error handling: Dead letter queue, retry with exponential backoff

### Phase 4: Tasks

Tasks organized by pipeline stage:
- Extract: File reading, schema validation, error collection
- Transform: API integration, rate limiting, caching
- Load: Batch inserts, transaction management, S3 upload
- Orchestration: Prefect flows, error handling, monitoring

---

## Example 5: CLI Tool

### User Input
"Command-line tool for managing project specifications. Commands to init project, create spec, generate plan, show status."

### Phase 1: Constitution

```bash
/speckit.constitution CLI tool principles: intuitive commands, helpful error messages, progress indicators, color-coded output, comprehensive help
```

### Phase 2: Specify

```bash
/speckit.specify CLI tool for spec management. Commands: init (new project), specify (create spec), plan (generate plan), status (show info). Rich terminal output.
```

**Key user stories**:
1. **P1**: Initialize new project structure
2. **P1**: Create specification from description
3. **P1**: Generate implementation plan
4. **P2**: Show project status
5. **P3**: Validate specs and plans

### Phase 3: Plan

```bash
/speckit.plan Python with Typer for CLI, Rich for terminal formatting, Pydantic for validation. Package with setuptools for pip install.
```

**Commands**:
```bash
speckit init <project>
speckit spec create "Feature description"
speckit plan generate --tech "FastAPI + PostgreSQL"
speckit status
speckit validate
```

### Phase 4: Tasks

- CLI framework setup (Typer)
- Command handlers
- File operations (templates, directories)
- Rich formatting (tables, progress)
- Input validation (Pydantic)
- Help text and documentation
- Package configuration (setup.py, pyproject.toml)

---

## Common Patterns Across Examples

### All Projects Follow Same Workflow

1. **Constitution**: Establish principles
2. **Specify**: Define user stories
3. **Clarify**: Resolve ambiguities
4. **Plan**: Choose tech stack, design architecture
5. **Tasks**: Break down into executable steps
6. **Implement**: Build the system

### Specification Focus

- Always user-centric (user stories, acceptance criteria)
- Technology-agnostic (WHAT, not HOW)
- Testable (clear success criteria)
- Prioritized (P1/P2/P3 for incremental delivery)

### Planning Consistency

- Constitution compliance checks
- Research documents technology decisions
- Data models define entities
- Contracts specify interfaces
- Quickstart provides validation scenarios

### Task Organization

- Grouped by user story
- Ordered by dependencies
- Parallel execution marked
- Checkpoints per story
- File paths specified

### Quality Throughout

- Tests at every level (unit, integration, E2E)
- Error handling explicit
- Performance requirements stated
- Security considerations included
- Documentation generated alongside code
