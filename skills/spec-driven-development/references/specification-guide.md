# Specification Guide

## Purpose

The specification (`spec.md`) is the translation layer between user intent and technical implementation. It describes WHAT and WHY, never HOW.

## Core Template Structure

### 1. Header
```markdown
# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`
**Created**: [DATE]
**Status**: Draft
**Input**: User description: "$ARGUMENTS"
```

### 2. User Scenarios & Testing

This is the heart of the specification. Each user story must:
- Be independently testable
- Deliver standalone value
- Have clear priority (P1, P2, P3)
- Include acceptance scenarios

#### Format:
```markdown
### User Story 1 - [Brief Title] (Priority: P1)

[Plain language description of user journey]

**Why this priority**: [Value and priority rationale]

**Independent Test**: [How to test this story alone]

**Acceptance Scenarios**:
1. **Given** [state], **When** [action], **Then** [outcome]
2. **Given** [state], **When** [action], **Then** [outcome]
```

#### Prioritization Guidelines

**P1 (Critical)**: 
- Core value proposition
- Minimum viable functionality
- Blocking for other features
- Example: User login for authenticated app

**P2 (Important)**:
- Enhances core value
- Significant user benefit
- Not blocking but highly desired
- Example: Password reset flow

**P3 (Nice-to-have)**:
- Improves experience
- Can be deferred
- Optional convenience
- Example: Remember me checkbox

### 3. Edge Cases

Document boundary conditions and error scenarios:
```markdown
### Edge Cases
- What happens when user provides invalid input?
- How does system handle concurrent operations?
- What occurs when external service unavailable?
- How are rate limits enforced?
```

### 4. Requirements

#### Functional Requirements
Must be specific, testable, and traceable to user stories.

**Format**:
```markdown
### Functional Requirements
- **FR-001**: System MUST [specific capability]
- **FR-002**: Users MUST be able to [interaction]
- **FR-003**: System MUST [data requirement]
```

**Good Examples**:
- **FR-001**: System MUST validate email addresses using RFC 5322 format
- **FR-002**: Users MUST be able to reset password within 5 minutes
- **FR-003**: System MUST encrypt passwords using bcrypt with cost factor ≥12

**Bad Examples**:
- ❌ System should handle users nicely (vague)
- ❌ Fast response time (not measurable)
- ❌ Uses React for UI (implementation detail)

#### Non-Functional Requirements
Performance, security, scalability, usability.

```markdown
### Non-Functional Requirements
- **NFR-001**: Response time MUST be <200ms for 95th percentile
- **NFR-002**: System MUST support 1000 concurrent users
- **NFR-003**: UI MUST meet WCAG 2.1 AA standards
```

### 5. Key Entities

If feature involves data, define conceptual entities (not database schema):

```markdown
### Key Entities
- **User**: Person interacting with system
  - Attributes: identifier, email, preferences
  - Behaviors: login, logout, update profile
  
- **Session**: User's active interaction period
  - Attributes: start time, expiry, device info
  - Relationships: belongs to one User
```

### 6. Success Criteria

Measurable outcomes that define "done":

```markdown
### Success Criteria
- Users can complete primary workflow in <3 minutes
- System maintains 99.9% uptime
- User satisfaction score >4.5/5
- Zero critical security vulnerabilities
- All P1 user stories fully functional
```

### 7. Assumptions

Document what you're assuming to be true:

```markdown
### Assumptions
- Users have modern web browser (Chrome 90+, Firefox 88+, Safari 14+)
- Email delivery service is reliable
- Users understand basic web navigation
- Maximum 10,000 users in first year
```

### 8. Out of Scope

Explicitly state what's NOT included:

```markdown
### Out of Scope
- Mobile native apps (web only)
- Social media authentication
- Multi-language support
- Advanced admin analytics
```

### 9. Dependencies

External factors needed for success:

```markdown
### Dependencies
- Email service (SendGrid) account and API key
- SSL certificate for domain
- Cloud hosting account (AWS/GCP/Azure)
- Third-party payment processor integration
```

## Writing Effective User Stories

### Independent Testing Principle

Each story must be demonstrable alone:

✅ **Good - Independent**:
```markdown
### User Story 1 - View Personal Dashboard (Priority: P1)

User logs in and sees their personalized dashboard with recent activity.

**Independent Test**: Create test user, log in, verify dashboard displays.
```

❌ **Bad - Dependent**:
```markdown
### User Story 2 - Edit Dashboard Widgets (Priority: P1)

User can customize dashboard layout.

**Independent Test**: [Can't test without Story 1 implemented]
```

### Acceptance Scenario Best Practices

Use Given-When-Then format for clarity:

✅ **Good**:
```markdown
**Given** user is logged out
**When** user clicks "Forgot Password" and enters valid email
**Then** system sends reset link and displays confirmation
```

❌ **Bad**:
```markdown
User can reset password if they forgot it.
```

### Priority Assignment Strategy

Think incremental delivery:

**Sprint 1 (P1 only)**: 
- Core authentication
- Basic dashboard view
Result: Minimal but functional product

**Sprint 2 (P1 + P2)**:
- Add profile editing
- Add password reset
Result: Complete standard user experience

**Sprint 3 (P1 + P2 + P3)**:
- Add social login
- Add advanced preferences
Result: Enhanced, polished product

## Handling Ambiguity

### The 3-Marker Rule

Maximum 3 `[NEEDS CLARIFICATION]` markers per specification.

**When to use**:
- Significant scope impact
- Security/privacy implications
- Multiple reasonable interpretations
- No reasonable default exists

**When NOT to use**:
- Minor UI details
- Standard patterns exist
- Impact is minimal
- Reasonable default available

### Making Informed Assumptions

Instead of marking everything unclear:

❌ **Over-marking**:
```markdown
- **FR-001**: Users authenticate via [NEEDS CLARIFICATION: email/SSO/OAuth?]
- **FR-002**: Password length [NEEDS CLARIFICATION: min/max?]
- **FR-003**: Session timeout [NEEDS CLARIFICATION: duration?]
```

✅ **Informed assumptions**:
```markdown
- **FR-001**: Users authenticate via email/password (standard pattern)
- **FR-002**: Password length 8-128 characters (NIST guidelines)
- **FR-003**: Session timeout 30 minutes (industry standard)

### Assumptions
- Standard web authentication is sufficient
- NIST password guidelines apply
- No regulatory requirements for extended sessions
```

### Prioritizing Clarifications

If you must use 3 markers, prioritize by impact:

**Priority 1 - Scope/Architecture**:
```markdown
System must handle [NEEDS CLARIFICATION: 100 or 100,000 users?]
```
Impact: Completely different architectures

**Priority 2 - Security/Privacy**:
```markdown
Store user data in [NEEDS CLARIFICATION: EU/US/global regions?]
```
Impact: Legal compliance, architecture

**Priority 3 - User Experience**:
```markdown
Display notifications as [NEEDS CLARIFICATION: modal/toast/banner?]
```
Impact: Moderate - affects UX polish

## Common Patterns

### Authentication Feature
```markdown
### User Story 1 - Basic Login (Priority: P1)
User provides email/password and accesses protected areas.

**Acceptance Scenarios**:
1. **Given** valid credentials, **When** submitted, **Then** redirect to dashboard
2. **Given** invalid credentials, **When** submitted, **Then** show error, don't reveal which failed
3. **Given** too many failed attempts, **When** threshold exceeded, **Then** temporary lockout

### User Story 2 - Password Reset (Priority: P2)
User receives email to reset forgotten password.

**Acceptance Scenarios**:
1. **Given** registered email, **When** reset requested, **Then** send link valid 1 hour
2. **Given** reset link, **When** clicked, **Then** show password form
3. **Given** new password, **When** submitted, **Then** update and invalidate old sessions

### Edge Cases
- Account locked after 5 failed attempts, unlocks after 15 minutes
- Reset links expire after 1 hour
- Concurrent sessions: last login wins
```

### CRUD Feature
```markdown
### User Story 1 - Create Item (Priority: P1)
User submits form to create new item in system.

**Acceptance Scenarios**:
1. **Given** valid data, **When** submitted, **Then** create item and show success
2. **Given** duplicate name, **When** submitted, **Then** reject with error
3. **Given** invalid format, **When** submitted, **Then** show validation errors

### User Story 2 - List Items (Priority: P1)
User views paginated list of their items.

**Acceptance Scenarios**:
1. **Given** items exist, **When** page loads, **Then** show 20 per page
2. **Given** many items, **When** next clicked, **Then** load next page
3. **Given** no items, **When** page loads, **Then** show empty state

[... Update and Delete stories ...]
```

### Real-time Feature
```markdown
### User Story 1 - Receive Live Updates (Priority: P1)
User sees changes from other users without refreshing.

**Acceptance Scenarios**:
1. **Given** user viewing list, **When** other user adds item, **Then** update appears <1 second
2. **Given** connection drops, **When** reconnects, **Then** sync missed updates
3. **Given** multiple users, **When** concurrent edits, **Then** last write wins with notification

### Edge Cases
- WebSocket connection loss: retry with exponential backoff
- Network partition: queue updates, sync on reconnect
- Conflict resolution: timestamp-based, notify user of conflicts
```

## Quality Checklist

Before considering spec complete:

### Completeness
- [ ] All user stories have acceptance scenarios
- [ ] Edge cases identified
- [ ] Functional requirements cover all stories
- [ ] Non-functional requirements stated
- [ ] Success criteria measurable

### Clarity
- [ ] No more than 3 `[NEEDS CLARIFICATION]` markers
- [ ] Assumptions documented
- [ ] Out of scope explicitly stated
- [ ] Dependencies identified

### Testability
- [ ] Each user story independently testable
- [ ] Each requirement specific and verifiable
- [ ] Success criteria measurable
- [ ] Acceptance scenarios use Given-When-Then

### Priority
- [ ] Stories prioritized (P1, P2, P3)
- [ ] P1 forms minimum viable product
- [ ] Each priority level adds value incrementally
- [ ] Rationale for priorities documented

## Anti-Patterns

### ❌ Implementation Leakage
```markdown
Users authenticate using JWT tokens stored in localStorage.
```
This is HOW, not WHAT. Should be:
```markdown
Users remain authenticated across browser sessions.
```

### ❌ Dependent Stories
```markdown
### Story 1: Setup Database (Priority: P1)
### Story 2: Create User Table (Priority: P1)
### Story 3: Add Login Endpoint (Priority: P1)
```
These are implementation tasks, not user stories. Should be:
```markdown
### Story 1: User Login (Priority: P1)
User authenticates and accesses protected features.
```

### ❌ Vague Requirements
```markdown
- **FR-001**: System should be fast
- **FR-002**: UI must look good
```
Not measurable. Should be:
```markdown
- **FR-001**: System MUST respond <200ms for 95th percentile
- **FR-002**: UI MUST pass WCAG 2.1 AA contrast requirements
```

### ❌ No Edge Cases
Missing error scenarios leads to brittle implementations.

Always consider:
- Invalid input
- Concurrent operations
- External service failures
- Resource exhaustion
- Security attacks

## Template Filling Workflow

1. **Read user input carefully**
2. **Extract key concepts**: actors, actions, data, constraints
3. **Draft user stories**: focus on user value, prioritize
4. **Write acceptance scenarios**: Given-When-Then format
5. **Identify edge cases**: errors, boundaries, conflicts
6. **Define functional requirements**: map to stories
7. **Add non-functional requirements**: performance, security
8. **List entities**: if data involved
9. **Set success criteria**: measurable outcomes
10. **Document assumptions**: what you're taking as given
11. **Mark out of scope**: what's explicitly not included
12. **Identify dependencies**: external factors
13. **Review for clarity**: max 3 clarification markers
14. **Validate testability**: each story independently testable

## Review Checklist

Use this before marking spec complete:

```markdown
### Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain OR marked as deferred
- [ ] Requirements are specific and testable
- [ ] Success criteria are measurable
- [ ] All user stories have acceptance scenarios

### User Story Quality
- [ ] Each story is independently testable
- [ ] Each story delivers standalone value
- [ ] Stories prioritized (P1, P2, P3)
- [ ] P1 stories form minimal viable product

### Clarity
- [ ] No implementation details (no tech stack)
- [ ] Assumptions documented
- [ ] Dependencies identified
- [ ] Out of scope explicitly stated

### Coverage
- [ ] Edge cases identified
- [ ] Error scenarios covered
- [ ] Security considerations addressed
- [ ] Performance expectations stated
```
