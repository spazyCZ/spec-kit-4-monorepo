# Tasks Guide

## Purpose

The tasks document (`tasks.md`) breaks down the implementation plan into ordered, executable work items. Each task specifies what to build, where to build it, and what dependencies must be satisfied first.

## Task Structure

### Basic Task Format

```markdown
### User Story 1: [Story Title]

#### Setup & Prerequisites
- [ ] Task description (file: path/to/file.ext)
- [ ] Another task (files: path/one.ext, path/two.ext)

#### Core Implementation
- [ ] Task with dependency (requires: Task above) (file: path/file.ext)
- [ ] [P] Parallel-safe task (file: path/other.ext)

#### Testing & Validation
- [ ] Test task (file: tests/test_file.ext)
- [ ] Checkpoint: Validate story completion
```

### Task Components

**Task Description**: Clear, actionable statement of work
**File Path**: Exact location where work occurs
**Dependencies**: Prerequisites that must complete first
**Parallel Marker**: `[P]` indicates safe for parallel execution

## Task Organization Principles

### 1. Group by User Story

Tasks organized by user story for incremental delivery:

```markdown
### User Story 1: User Authentication (Priority: P1)

[Tasks for authentication]

### User Story 2: Profile Management (Priority: P2)

[Tasks for profiles]
```

**Benefits**:
- Clear progress tracking per story
- Enables delivering stories independently
- Easy to prioritize work
- Natural checkpoints after each story

### 2. Dependency Ordering

Tasks ordered so prerequisites come first:

```markdown
#### Data Layer
- [ ] Define User model (file: src/models/user.py)
- [ ] Define Session model (requires: User model) (file: src/models/session.py)

#### Service Layer
- [ ] Create auth service (requires: User, Session models) (file: src/services/auth.py)

#### API Layer
- [ ] Create login endpoint (requires: auth service) (file: src/api/auth.py)
```

**Dependency Types**:
- **Data dependencies**: Models before services before APIs
- **Contract dependencies**: Interfaces before implementations
- **Test dependencies**: Contracts before integration tests

### 3. Parallel Execution Markers

Mark tasks that can run simultaneously with `[P]`:

```markdown
#### Independent Components
- [ ] [P] Create user service (file: src/services/user.py)
- [ ] [P] Create message service (file: src/services/message.py)
- [ ] [P] Create channel service (file: src/services/channel.py)
```

**Parallel-Safe Criteria**:
- No shared file modifications
- No dependency relationships
- Different functional areas
- Independent test coverage

**Not Parallel-Safe**:
- Same file modifications
- Dependent on each other
- Shared database schema changes
- Integration that requires both

### 4. Test-Driven Development Flow

If TDD requested, tests come before implementation:

```markdown
#### Contract Tests
- [ ] Define message API contract (file: tests/contracts/message_api.yaml)
- [ ] Write contract tests (file: tests/contract/test_message_api.py)
- [ ] Verify tests FAIL (Red phase)

#### Implementation
- [ ] Implement message endpoint (file: src/api/message.py)
- [ ] Verify tests PASS (Green phase)

#### Refinement
- [ ] Refactor for clarity (files: src/api/message.py, src/services/message.py)
- [ ] Verify tests still PASS
```

### 5. Checkpoint Validations

End each user story with validation checkpoint:

```markdown
#### Checkpoint: User Story 1 Complete
- [ ] All tasks in story completed
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] API contracts validated
- [ ] Manual smoke test passed
- [ ] Story acceptance criteria met
```

## Task Derivation Process

### From Implementation Plan

1. **Read plan.md**: Understand overall approach
2. **Read data-model.md**: Extract entity tasks
3. **Read contracts/**: Extract API/event tasks
4. **Read research.md**: Identify setup/config tasks

### From Specification

1. **User Stories**: Each becomes task group
2. **Functional Requirements**: Each becomes implementation task
3. **Acceptance Scenarios**: Each becomes test task

### Task Generation Rules

**Rule 1: One Task Per File** (mostly)
```markdown
✅ Good:
- [ ] Create User model (file: src/models/user.py)
- [ ] Create auth service (file: src/services/auth.py)

❌ Bad:
- [ ] Create all models (files: lots of files)
```

**Rule 2: Specify Exact Paths**
```markdown
✅ Good:
- [ ] Implement login endpoint (file: src/api/v1/auth.py)

❌ Bad:
- [ ] Implement login endpoint (somewhere in the API)
```

**Rule 3: Make Tasks Testable**
```markdown
✅ Good:
- [ ] User can create account with email (file: src/api/users.py)

❌ Bad:
- [ ] Work on user stuff
```

**Rule 4: Include Prerequisites**
```markdown
✅ Good:
- [ ] Auth service (requires: User model, Session model)

❌ Bad:
- [ ] Auth service (figure out dependencies yourself)
```

## Task Categories

### Setup Tasks
Initial project configuration:

```markdown
#### Project Setup
- [ ] Initialize project structure (files: setup.py, pyproject.toml, etc.)
- [ ] Configure development environment (file: .env.example)
- [ ] Set up database migrations (file: migrations/initial.sql)
- [ ] Configure logging (file: src/config/logging.py)
- [ ] Configure testing framework (file: pytest.ini, tests/conftest.py)
```

### Data Layer Tasks
Models and database:

```markdown
#### Data Models
- [ ] Create User model with validation (file: src/models/user.py)
- [ ] Create Message model (requires: User) (file: src/models/message.py)
- [ ] Create Channel model (file: src/models/channel.py)
- [ ] Create ChannelMembership association (requires: User, Channel) (file: src/models/membership.py)

#### Database Schema
- [ ] Create users table migration (file: migrations/001_users.sql)
- [ ] Create messages table migration (file: migrations/002_messages.sql)
- [ ] Add indexes for performance (file: migrations/003_indexes.sql)
```

### Service Layer Tasks
Business logic:

```markdown
#### Business Logic
- [ ] User service: registration (file: src/services/user_service.py)
- [ ] User service: authentication (file: src/services/user_service.py)
- [ ] Message service: send message (file: src/services/message_service.py)
- [ ] Message service: message history (file: src/services/message_service.py)
- [ ] Channel service: create/manage (file: src/services/channel_service.py)
```

### API Layer Tasks
Endpoints and interfaces:

```markdown
#### REST API Endpoints
- [ ] POST /auth/register (file: src/api/auth.py)
- [ ] POST /auth/login (file: src/api/auth.py)
- [ ] GET /channels (file: src/api/channels.py)
- [ ] POST /channels (file: src/api/channels.py)
- [ ] POST /messages (file: src/api/messages.py)
- [ ] GET /channels/{id}/messages (file: src/api/messages.py)

#### WebSocket Handlers
- [ ] Connection handler (file: src/websocket/connection.py)
- [ ] Message event handler (file: src/websocket/handlers/message.py)
- [ ] Typing event handler (file: src/websocket/handlers/typing.py)
```

### Testing Tasks

```markdown
#### Contract Tests
- [ ] Auth API contract tests (file: tests/contract/test_auth_api.py)
- [ ] Message API contract tests (file: tests/contract/test_message_api.py)
- [ ] WebSocket event contract tests (file: tests/contract/test_ws_events.py)

#### Integration Tests
- [ ] User registration flow (file: tests/integration/test_user_flow.py)
- [ ] Message sending flow (file: tests/integration/test_messaging.py)
- [ ] Real-time event delivery (file: tests/integration/test_realtime.py)

#### Unit Tests
- [ ] User model validation (file: tests/unit/models/test_user.py)
- [ ] Auth service logic (file: tests/unit/services/test_auth.py)
- [ ] Message service logic (file: tests/unit/services/test_message.py)

#### End-to-End Tests
- [ ] Complete user journey (file: tests/e2e/test_chat_journey.py)
- [ ] Error handling scenarios (file: tests/e2e/test_error_handling.py)
```

## Common Task Patterns

### CRUD Feature Tasks

```markdown
### User Story: Resource Management

#### Data Layer
- [ ] Create Resource model (file: src/models/resource.py)
- [ ] Add database migration (file: migrations/001_resources.sql)

#### Service Layer
- [ ] Service: Create resource (file: src/services/resource_service.py)
- [ ] Service: Read resource (file: src/services/resource_service.py)
- [ ] Service: Update resource (file: src/services/resource_service.py)
- [ ] Service: Delete resource (file: src/services/resource_service.py)
- [ ] Service: List resources with pagination (file: src/services/resource_service.py)

#### API Layer
- [ ] POST /resources (file: src/api/resources.py)
- [ ] GET /resources/{id} (file: src/api/resources.py)
- [ ] PUT /resources/{id} (file: src/api/resources.py)
- [ ] DELETE /resources/{id} (file: src/api/resources.py)
- [ ] GET /resources (file: src/api/resources.py)

#### Testing
- [ ] Model validation tests (file: tests/unit/models/test_resource.py)
- [ ] Service logic tests (file: tests/unit/services/test_resource_service.py)
- [ ] API endpoint tests (file: tests/integration/test_resource_api.py)
- [ ] E2E CRUD flow test (file: tests/e2e/test_resource_flow.py)

#### Checkpoint
- [ ] All CRUD operations functional
- [ ] Tests passing
- [ ] API matches OpenAPI spec
```

### Authentication Feature Tasks

```markdown
### User Story: User Authentication

#### Setup
- [ ] Configure JWT library (file: src/config/auth.py)
- [ ] Set up password hashing (file: src/security/password.py)

#### Data Layer
- [ ] User model with password field (file: src/models/user.py)
- [ ] Session model (file: src/models/session.py)
- [ ] Database migrations (file: migrations/001_auth.sql)

#### Service Layer
- [ ] Registration service (file: src/services/auth_service.py)
- [ ] Login service (file: src/services/auth_service.py)
- [ ] Token generation/validation (file: src/services/token_service.py)
- [ ] Password reset service (file: src/services/auth_service.py)

#### API Layer
- [ ] POST /auth/register (file: src/api/auth.py)
- [ ] POST /auth/login (file: src/api/auth.py)
- [ ] POST /auth/logout (file: src/api/auth.py)
- [ ] POST /auth/refresh (file: src/api/auth.py)
- [ ] POST /auth/password-reset-request (file: src/api/auth.py)
- [ ] POST /auth/password-reset-confirm (file: src/api/auth.py)

#### Middleware
- [ ] Authentication middleware (file: src/middleware/auth.py)
- [ ] Rate limiting (file: src/middleware/rate_limit.py)

#### Testing
- [ ] Password hashing tests (file: tests/unit/security/test_password.py)
- [ ] Token service tests (file: tests/unit/services/test_token_service.py)
- [ ] Auth flow integration tests (file: tests/integration/test_auth_flow.py)
- [ ] Security tests (brute force, timing) (file: tests/security/test_auth_security.py)

#### Checkpoint
- [ ] Users can register
- [ ] Users can log in
- [ ] Tokens work for protected endpoints
- [ ] Password reset functional
```

### Real-time Feature Tasks

```markdown
### User Story: Real-time Updates

#### Infrastructure
- [ ] WebSocket server setup (file: src/websocket/server.py)
- [ ] Connection manager (file: src/websocket/connection_manager.py)
- [ ] Event bus (file: src/events/event_bus.py)

#### Event Handlers
- [ ] Connection lifecycle handler (file: src/websocket/handlers/connection.py)
- [ ] Message event handler (file: src/websocket/handlers/message.py)
- [ ] Presence event handler (file: src/websocket/handlers/presence.py)
- [ ] Typing indicator handler (file: src/websocket/handlers/typing.py)

#### Integration
- [ ] REST API → WebSocket bridge (file: src/services/notification_service.py)
- [ ] Database → Event bus bridge (file: src/events/db_listener.py)

#### Testing
- [ ] WebSocket connection tests (file: tests/integration/test_websocket.py)
- [ ] Event delivery tests (file: tests/integration/test_events.py)
- [ ] Concurrency tests (file: tests/load/test_concurrent_connections.py)
- [ ] Reconnection tests (file: tests/integration/test_reconnection.py)

#### Checkpoint
- [ ] WebSocket connections stable
- [ ] Events delivered <1 second
- [ ] Handles reconnections gracefully
- [ ] Supports 100+ concurrent connections
```

## Parallel Execution Strategies

### Safe Parallelization

**Pattern 1: Independent Features**
```markdown
- [ ] [P] User authentication (files: src/auth/*)
- [ ] [P] Channel management (files: src/channels/*)
- [ ] [P] Message system (files: src/messages/*)
```
Safe because: Different directories, no shared code

**Pattern 2: Independent Layers (Same Feature)**
```markdown
#### After models complete:
- [ ] [P] User service (file: src/services/user_service.py)
- [ ] [P] User API tests (file: tests/integration/test_user_api.py)
- [ ] [P] User API docs (file: docs/api/users.md)
```
Safe because: Different file types, no conflicts

**Pattern 3: Independent Components**
```markdown
- [ ] [P] Frontend component: UserList (file: src/components/UserList.tsx)
- [ ] [P] Frontend component: MessageThread (file: src/components/MessageThread.tsx)
- [ ] [P] Frontend component: ChannelSidebar (file: src/components/ChannelSidebar.tsx)
```
Safe because: Isolated React components

### Unsafe Parallelization

❌ **Anti-pattern 1: Same File**
```markdown
- [ ] [P] Add user endpoint (file: src/api/users.py)
- [ ] [P] Add login endpoint (file: src/api/users.py)
```
Conflict: Both modify same file

❌ **Anti-pattern 2: Dependency Chain**
```markdown
- [ ] [P] Create User model (file: src/models/user.py)
- [ ] [P] Create auth service (requires: User model) (file: src/services/auth.py)
```
Conflict: Auth service depends on User model

❌ **Anti-pattern 3: Shared Schema**
```markdown
- [ ] [P] Add users table (file: migrations/001_schema.sql)
- [ ] [P] Add messages table (file: migrations/001_schema.sql)
```
Conflict: Both modify same migration file

## Task Estimation Guidance

While not required, consider complexity markers:

```markdown
- [ ] Simple task: Setup logging (file: src/config/logging.py) [~30min]
- [ ] Medium task: Auth service (file: src/services/auth_service.py) [~2hrs]
- [ ] Complex task: WebSocket connection manager (file: src/websocket/manager.py) [~4hrs]
```

**Estimation Factors**:
- Familiarity with technology
- Complexity of logic
- Number of integration points
- Testing requirements

## Task Completion Criteria

Each task should have implicit completion criteria:

```markdown
- [ ] Create User model (file: src/models/user.py)
```

**Implicit criteria**:
- File created at specified path
- Model matches data-model.md specification
- Validation rules implemented
- Unit tests pass
- Linting passes
- Code reviewed (if process requires)

## Quality Checklist

Before marking tasks.md complete:

### Organization
- [ ] Tasks grouped by user story
- [ ] Tasks ordered by dependencies
- [ ] Parallel opportunities marked
- [ ] Checkpoints after each story

### Clarity
- [ ] Each task has file path
- [ ] Dependencies specified
- [ ] Task descriptions actionable
- [ ] No ambiguous tasks

### Completeness
- [ ] All entities from data-model covered
- [ ] All endpoints from contracts covered
- [ ] All user stories covered
- [ ] Testing tasks included

### Feasibility
- [ ] No circular dependencies
- [ ] No impossible parallelization
- [ ] Reasonable task granularity
- [ ] Clear completion criteria

## Anti-Patterns

### ❌ Too Granular
```markdown
- [ ] Import library (file: src/main.py)
- [ ] Define class (file: src/main.py)
- [ ] Add method (file: src/main.py)
- [ ] Add another method (file: src/main.py)
```
Better: Combine into logical units

### ❌ Too Vague
```markdown
- [ ] Implement backend
- [ ] Build frontend
- [ ] Add tests
```
Better: Break down into specific, actionable tasks

### ❌ Missing Dependencies
```markdown
- [ ] Create API endpoint
- [ ] Create service
- [ ] Create model
```
Better: Order with dependencies noted

### ❌ No File Paths
```markdown
- [ ] Implement user authentication
```
Better: Specify exactly where work occurs

### ❌ No Checkpoints
```markdown
[500 tasks with no validation points]
```
Better: Add checkpoints every 10-20 tasks or per user story
