# Planning Guide

## Purpose

The implementation plan (`plan.md`) bridges specification and code. It translates WHAT (from spec) into HOW (for implementation), while respecting constitutional principles.

## Plan Structure Overview

```
specs/[###-feature]/
├── plan.md              # High-level roadmap (this guide)
├── research.md          # Technology decisions & rationale
├── data-model.md        # Entity definitions & relationships
├── contracts/           # API specifications
│   ├── api-spec.json    # REST/GraphQL contracts
│   └── events.md        # Event/message contracts
└── quickstart.md        # Key validation scenarios
```

## Phase 0: Research & Technology Selection

### Purpose
Resolve all unknowns before design. Every `NEEDS CLARIFICATION` from Technical Context must be resolved.

### Process

1. **Identify Research Tasks**:
   - Each unknown → research task
   - Each technology choice → best practices task
   - Each integration → patterns task

2. **Generate Research Questions**:
   ```markdown
   ### Research Task 1: Database Selection
   **Question**: PostgreSQL vs MongoDB for chat message storage?
   
   **Context**: 
   - Need to store 1M+ messages/day
   - Complex queries (search, filter by user/date)
   - Real-time updates required
   
   **Evaluation Criteria**:
   - Query performance
   - Real-time capabilities
   - Scaling characteristics
   - Team familiarity
   ```

3. **Consolidate Findings**:
   ```markdown
   ### Decision: PostgreSQL
   
   **Rationale**:
   - Complex relational queries needed (user, channel, message joins)
   - LISTEN/NOTIFY for real-time updates
   - JSONB for flexible message metadata
   - Team has production PostgreSQL experience
   
   **Alternatives Considered**:
   - MongoDB: Better for pure document storage, weaker for relational queries
   - Redis: Great for caching, not primary storage
   
   **Trade-offs Accepted**:
   - More complex scaling than MongoDB
   - Requires connection pooling for high concurrency
   ```

### Research Document Format

```markdown
# Implementation Research: [Feature]

## Overview
[Brief summary of research scope]

## Technology Decisions

### Decision 1: [Technology/Pattern Name]
**Question**: [What needed deciding]
**Decision**: [What was chosen]
**Rationale**: [Why chosen - bullet points]
**Alternatives Considered**: [What else evaluated]
**Trade-offs**: [What sacrificed for this choice]
**References**: [Links to docs, benchmarks, articles]

### Decision 2: [Next decision]
[... repeat pattern ...]

## Open Questions
- [ ] [Any remaining unknowns]
- [ ] [To be resolved during implementation]

## Version Compatibility
- [Library/Framework]: [Specific version] - [Why this version]
- [Another dependency]: [Version] - [Rationale]
```

### Common Research Areas

**Backend Technology**:
- Framework selection (FastAPI vs Django vs Flask)
- Database choice (relational vs document vs graph)
- Caching strategy (Redis vs Memcached vs in-memory)
- Authentication (JWT vs sessions vs OAuth)

**Frontend Technology**:
- Framework (React vs Vue vs Svelte vs vanilla)
- State management (Redux vs Context vs signals)
- Build tool (Vite vs webpack vs esbuild)
- Styling approach (CSS modules vs Tailwind vs CSS-in-JS)

**Infrastructure**:
- Hosting (AWS vs GCP vs Azure vs self-hosted)
- Container orchestration (Kubernetes vs ECS vs Cloud Run)
- CI/CD (GitHub Actions vs GitLab CI vs Jenkins)
- Monitoring (Prometheus vs Datadog vs CloudWatch)

## Phase 1: Design & Contracts

### Data Model Design

#### Purpose
Define entities, relationships, and validation rules from specification.

#### Format

```markdown
# Data Model: [Feature]

## Entity Overview
Brief description of domain model.

## Entities

### Entity 1: User
**Description**: [What this represents]

**Attributes**:
- `id`: UUID - Primary identifier
- `email`: String(255) - Unique, validated per RFC 5322
- `created_at`: Timestamp - Account creation time
- `preferences`: JSONB - User settings (nullable)

**Validation Rules**:
- Email MUST be unique
- Email MUST match RFC 5322 format
- Preferences MUST validate against schema
- Created_at MUST be immutable

**Relationships**:
- Has many: Messages
- Has many: Sessions
- Belongs to many: Channels (through memberships)

**State Transitions**:
```
[Created] -> [Active] -> [Suspended] -> [Deleted]
                |            |
                +------------+
```

**Invariants**:
- User MUST have at least one valid email
- Deleted users MUST NOT be reactivated

### Entity 2: Message
[... repeat pattern ...]

## Relationships Diagram

```
User 1--* Message
User 1--* Session
User *--* Channel (via ChannelMembership)
Message *--1 Channel
```

## Aggregates

### Aggregate: User Account
**Root**: User
**Includes**: Sessions, Preferences
**Boundary**: User data and active sessions
**Consistency**: Changes to user affect all sessions

## Database Considerations
- Indexes needed: [user.email, message.channel_id, message.created_at]
- Partitioning: Messages by date (monthly partitions)
- Constraints: Foreign keys with CASCADE on user deletion
```

#### Entity Design Best Practices

**DO**:
- ✅ Define clear validation rules
- ✅ Specify relationships explicitly
- ✅ Document state transitions
- ✅ List invariants that must hold
- ✅ Consider query patterns for indexes

**DON'T**:
- ❌ Include SQL schema (that's implementation)
- ❌ Specify column types beyond semantics
- ❌ Design for specific ORM
- ❌ Over-normalize prematurely

### API Contract Design

#### Purpose
Define precise interface contracts between components.

#### REST API Format

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Chat API",
    "version": "1.0.0"
  },
  "paths": {
    "/messages": {
      "post": {
        "summary": "Send message",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MessageCreate"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Message created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Message"
                }
              }
            }
          },
          "400": {
            "description": "Invalid input",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "MessageCreate": {
        "type": "object",
        "required": ["channel_id", "content"],
        "properties": {
          "channel_id": {
            "type": "string",
            "format": "uuid"
          },
          "content": {
            "type": "string",
            "minLength": 1,
            "maxLength": 10000
          }
        }
      },
      "Message": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "channel_id": {
            "type": "string",
            "format": "uuid"
          },
          "user_id": {
            "type": "string",
            "format": "uuid"
          },
          "content": {
            "type": "string"
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "Error": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string"
          },
          "details": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```

#### WebSocket/Event Contracts

For real-time systems, document event schemas:

```markdown
# WebSocket Events: Chat

## Client → Server Events

### `message.send`
Send message to channel.

**Payload**:
```json
{
  "type": "message.send",
  "data": {
    "channel_id": "uuid",
    "content": "string"
  }
}
```

**Response**: `message.created` or `error`

### `typing.start`
Indicate user is typing.

**Payload**:
```json
{
  "type": "typing.start",
  "data": {
    "channel_id": "uuid"
  }
}
```

**Response**: None (broadcast to channel)

## Server → Client Events

### `message.created`
New message received.

**Payload**:
```json
{
  "type": "message.created",
  "data": {
    "id": "uuid",
    "channel_id": "uuid",
    "user_id": "uuid",
    "username": "string",
    "content": "string",
    "created_at": "ISO8601"
  }
}
```

### `typing.indicator`
Someone is typing.

**Payload**:
```json
{
  "type": "typing.indicator",
  "data": {
    "channel_id": "uuid",
    "user_id": "uuid",
    "username": "string"
  }
}
```

### `error`
Operation failed.

**Payload**:
```json
{
  "type": "error",
  "data": {
    "code": "string",
    "message": "string",
    "request_id": "uuid"
  }
}
```

## Connection Lifecycle

1. **Connect**: Client initiates WebSocket connection
2. **Authenticate**: Client sends `auth` event with token
3. **Subscribe**: Client subscribes to channels
4. **Exchange**: Bidirectional events
5. **Disconnect**: Connection closed (graceful or timeout)

## Error Handling

- Invalid event type: `error` event with code `INVALID_EVENT`
- Unauthorized action: `error` event with code `UNAUTHORIZED`
- Rate limit exceeded: `error` event with code `RATE_LIMIT`
- Server error: `error` event with code `INTERNAL_ERROR`
```

### Quickstart Scenarios

#### Purpose
Key validation scenarios for smoke testing after implementation.

#### Format

```markdown
# Quickstart Validation: [Feature]

## Prerequisites
- [ ] Environment variables configured
- [ ] Database initialized
- [ ] Services running

## Scenario 1: Happy Path
**Goal**: Verify core functionality works end-to-end

**Steps**:
1. Create user: `POST /users {"email": "test@example.com"}`
2. Authenticate: `POST /auth/login` → receive token
3. Create channel: `POST /channels {"name": "general"}`
4. Send message: `POST /messages {"channel_id": "...", "content": "Hello"}`
5. List messages: `GET /channels/{id}/messages`

**Expected**:
- All requests return 200/201
- Message appears in list
- Timestamps are recent

## Scenario 2: Error Handling
**Goal**: Verify errors handled gracefully

**Steps**:
1. Send message without auth: `POST /messages` (no token)
2. Send invalid message: `POST /messages {"content": ""}`
3. Access non-existent channel: `GET /channels/invalid-uuid/messages`

**Expected**:
- 401 Unauthorized for step 1
- 400 Bad Request for step 2
- 404 Not Found for step 3

## Scenario 3: Real-time Updates
**Goal**: Verify WebSocket events work

**Steps**:
1. Open WebSocket connection (Client A)
2. Open WebSocket connection (Client B)
3. Both join same channel
4. Client A sends message
5. Verify Client B receives message event

**Expected**:
- Both connections established
- Event delivered <1 second
- Payload matches contract

## Performance Baseline
- Message send: <50ms p95
- Message list (100 items): <100ms p95
- WebSocket event delivery: <100ms p95
```

## Constitution Check Integration

### Purpose
Validate design against constitutional principles before implementation.

### Gate Format

From constitution, generate gates:

```markdown
## Constitution Check

### Pre-Implementation Gates

#### Simplicity Gate (Article VII)
- [ ] Using ≤3 projects/services?
  - Current: 2 projects (backend, frontend)
  - Justification: Web application pattern
  
- [ ] No future-proofing?
  - [ ] Not adding "might need later" features
  - [ ] Implementing current requirements only

#### Anti-Abstraction Gate (Article VIII)
- [ ] Using framework features directly?
  - [ ] Not wrapping database ORM
  - [ ] Not abstracting HTTP framework
  
- [ ] Single model representation?
  - [ ] Not separate domain/DB models
  - [ ] Using framework models directly

#### Integration-First Gate (Article IX)
- [ ] API contracts defined?
  - [x] OpenAPI spec complete
  - [x] Event schemas documented
  
- [ ] Contract tests planned?
  - [ ] REST endpoint tests
  - [ ] WebSocket event tests

### Complexity Tracking

> Fill ONLY if gates have violations requiring justification

**Violation 1**: Using 4 projects (backend, frontend, worker, websocket-server)

**Justification**: 
- WebSocket server separated for scaling independence
- Worker needed for async tasks (email, notifications)
- Cannot combine due to different scaling characteristics

**Mitigation**:
- Start with 2 projects
- Add worker/websocket only if load testing proves necessary
- Document decision point: >1000 concurrent WebSocket connections
```

## Plan Template Filling Workflow

1. **Load Context**:
   - Read feature specification
   - Read project constitution
   - Load plan template

2. **Technical Context**:
   - Fill known values
   - Mark unknowns as `NEEDS CLARIFICATION`
   
3. **Phase 0 - Research**:
   - For each unknown → research task
   - Gather information via web search
   - Document decisions with rationale
   - Output: `research.md`

4. **Constitution Check**:
   - Generate gates from constitution
   - Evaluate each gate
   - Document any violations with justification

5. **Phase 1 - Design**:
   - Extract entities from spec → `data-model.md`
   - Generate API contracts → `/contracts/`
   - Create validation scenarios → `quickstart.md`

6. **Update Agent Context**:
   - Run agent-specific update script
   - Add new technology to agent knowledge
   - Preserve manual additions

7. **Review & Validate**:
   - All `NEEDS CLARIFICATION` resolved?
   - All constitutional gates pass or justified?
   - All artifacts generated?

## Common Patterns

### Microservice Plan
```markdown
## Project Structure

### Services
1. **API Gateway** (`services/gateway/`)
   - Route requests
   - Authentication
   - Rate limiting

2. **User Service** (`services/users/`)
   - User CRUD
   - Authentication
   - Profile management

3. **Message Service** (`services/messages/`)
   - Message CRUD
   - Real-time delivery
   - History

### Communication
- Synchronous: REST between gateway and services
- Asynchronous: Events via message queue (RabbitMQ)
```

### Monolith Plan
```markdown
## Project Structure

### Single Application (`src/`)
```
src/
├── models/      # Data models
├── services/    # Business logic
├── api/         # HTTP endpoints
├── cli/         # Command-line interface
└── lib/         # Shared utilities
```

### Modules
- **Users**: Authentication, profiles
- **Messages**: CRUD, real-time
- **Channels**: Management, memberships
```

### Mobile App Plan
```markdown
## Project Structure

### Backend (`api/`)
Standard REST API

### iOS (`ios/`)
```
ios/
├── Features/
│   ├── Auth/
│   ├── Chat/
│   └── Profile/
├── Common/
│   ├── Network/
│   ├── Storage/
│   └── UI/
└── Tests/
```

### Architecture
- MVVM pattern
- Combine for reactive programming
- SwiftUI for UI
- Core Data for local storage
```

## Quality Checklist

Before marking plan complete:

### Research Complete
- [ ] All `NEEDS CLARIFICATION` resolved
- [ ] Technology choices documented with rationale
- [ ] Alternatives considered and evaluated
- [ ] Version compatibility confirmed

### Design Complete
- [ ] Data model covers all entities from spec
- [ ] Entity relationships defined
- [ ] Validation rules specified
- [ ] API contracts match requirements

### Constitutional Compliance
- [ ] All gates evaluated
- [ ] Violations justified (if any)
- [ ] Complexity tracking filled (if violations)

### Documentation Quality
- [ ] Plan readable (high-level)
- [ ] Details in separate files
- [ ] No implementation code in plan.md
- [ ] All artifacts referenced from plan

### Quickstart Valid
- [ ] Scenarios cover core functionality
- [ ] Error cases included
- [ ] Performance baselines stated
- [ ] Prerequisites listed
