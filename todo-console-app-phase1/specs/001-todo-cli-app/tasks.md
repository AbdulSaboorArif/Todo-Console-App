# Tasks: Phase I Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, contracts/
**Tests**: Not explicitly requested in spec - implementation-focused tasks

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root
- Paths assume single project as defined in plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create src/todo_app/ directory per implementation plan
- [X] T002 Create src/todo_app/__init__.py package file
- [X] T003 [P] Create pyproject.toml with Python 3.13+ requirement

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task data class in src/todo_app/task.py with id, title, description, status attributes
- [X] T005 [P] Create TaskRepository class in src/todo_app/task.py with in-memory list storage
- [X] T006 [P] Implement TaskRepository.add() method with auto-incrementing ID generation
- [X] T007 [P] Implement TaskRepository.get_by_id() method for ID lookup
- [X] T008 [P] Implement TaskRepository.get_all() method to return all tasks
- [X] T009 [P] Implement TaskRepository.update() method for modifying tasks
- [X] T010 [P] Implement TaskRepository.delete() method for removing tasks
- [X] T011 [P] Implement TaskRepository.toggle_complete() method for status toggle

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) MVP

**Goal**: Users can create new tasks with title and description, receiving a unique ID

**Independent Test**: Can be fully tested by running the `add` command, entering a title and description, and verifying the task appears in the list with correct ID, title, description, and pending status.

### Implementation for User Story 1

- [X] T012 [US1] Implement add_command() function in src/todo_app/main.py per add-command.md contract
- [X] T013 [US1] Add input prompts for title and description with validation
- [X] T014 [US1] Create Task via TaskRepository.add() with auto-generated ID
- [X] T015 [US1] Display success message with task ID
- [X] T016 [US1] Handle empty title error gracefully

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Users can see all tasks with their details and completion status

**Independent Test**: Can be fully tested by running the `list` command after adding tasks and verifying all tasks display with correct ID, title, description, and status indicators.

### Implementation for User Story 2

- [X] T017 [US2] Implement list_command() function in src/todo_app/main.py per list-command.md contract
- [X] T018 [US2] Retrieve all tasks via TaskRepository.get_all()
- [X] T019 [US2] Handle empty task list with user-friendly message
- [X] T020 [US2] Format task output with [✓] for completed, [ ] for pending
- [X] T021 [US2] Display ID, title, and description for each task

**Checkpoint**: User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Task (Priority: P1)

**Goal**: Users can remove tasks they no longer need

**Independent Test**: Can be fully tested by adding a task, running `delete <id>`, and verifying the task no longer appears in the list.

### Implementation for User Story 3

- [X] T022 [US3] Implement delete_command() function in src/todo_app/main.py per delete-command.md contract
- [X] T023 [US3] Parse and validate numeric ID parameter
- [X] T024 [US3] Handle invalid ID with error message
- [X] T025 [US3] Look up task via TaskRepository.get_by_id()
- [X] T026 [US3] Handle task not found error
- [X] T027 [US3] Remove task via TaskRepository.delete()
- [X] T028 [US3] Display confirmation message

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Mark Task Complete (Priority: P2)

**Goal**: Users can toggle task completion status

**Independent Test**: Can be fully tested by adding a task, running `complete <id>`, and verifying the task status changes from pending to complete (and back when run again).

### Implementation for User Story 4

- [X] T029 [US4] Implement complete_command() function in src/todo_app/main.py per complete-command.md contract
- [X] T030 [US4] Parse and validate numeric ID parameter
- [X] T031 [US4] Handle invalid ID with error message
- [X] T032 [US4] Look up task via TaskRepository.get_by_id()
- [X] T033 [US4] Handle task not found error
- [X] T034 [US4] Toggle status via TaskRepository.toggle_complete()
- [X] T035 [US4] Display confirmation with new state (completed/pending)

**Checkpoint**: User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Update Task (Priority: P2)

**Goal**: Users can modify task title and/or description

**Independent Test**: Can be fully tested by adding a task, running `update <id>` with new values, and verifying the task details are updated.

### Implementation for User Story 5

- [X] T036 [US5] Implement update_command() function in src/todo_app/main.py per update-command.md contract
- [X] T037 [US5] Parse and validate numeric ID parameter
- [X] T038 [US5] Handle invalid ID with error message
- [X] T039 [US5] Look up task via TaskRepository.get_by_id()
- [X] T040 [US5] Handle task not found error
- [X] T041 [US5] Prompt for new title (optional, press Enter to keep current)
- [X] T042 [US5] Prompt for new description (optional, press Enter to keep current)
- [X] T043 [US5] Update task via TaskRepository.update()
- [X] T044 [US5] Display confirmation message

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Integration, CLI loop, and final polish

- [X] T045 Implement main CLI loop in src/todo_app/main.py with welcome message
- [X] T046 [P] Implement help command to display available commands
- [X] T047 [P] Implement exit command to quit the application
- [X] T048 [P] Handle invalid commands with helpful guidance
- [X] T049 [P] Run quickstart.md validation - test all commands work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion
  - User stories can proceed in parallel after Foundation
  - Or sequentially in priority order (US1 → US2 → US3 → US4 → US5)
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational - No dependencies on other stories

### Within Each User Story

- Foundational: Models (Task) before repository methods
- User Story: Repository method before command handler
- Each story complete before moving to Polish phase

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel
- Polish tasks marked [P] can run in parallel

---

## Parallel Execution Examples

```bash
# Phase 1 Setup (all parallel):
Task: "Create src/todo_app/ directory"
Task: "Create src/todo_app/__init__.py"
Task: "Create pyproject.toml"

# Phase 2 Foundational (all parallel):
Task: "Create Task data class in src/todo_app/task.py"
Task: "Create TaskRepository class in src/todo_app/task.py"
Task: "Implement TaskRepository.add() method"

# Phase 3-7 User Stories (all can run in parallel after Foundation):
Task: "Implement add_command() in src/todo_app/main.py"
Task: "Implement list_command() in src/todo_app/main.py"
Task: "Implement delete_command() in src/todo_app/main.py"
Task: "Implement complete_command() in src/todo_app/main.py"
Task: "Implement update_command() in src/todo_app/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. **STOP and VALIDATE**: Test add command works
5. Deploy/demo if ready with just Add Task

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Polish → Final delivery

### Recommended Order

Given the dependencies and priorities:
1. Setup → Foundational
2. US1 (Add) → US2 (List) → These form the basic CRUD core
3. US3 (Delete) → US4 (Complete) → US5 (Update)
4. Polish

---

## Task Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| Phase 1 | T001-T003 | Setup (3 tasks) |
| Phase 2 | T004-T011 | Foundational (8 tasks) |
| Phase 3 | T012-T016 | US1: Add Task (5 tasks) |
| Phase 4 | T017-T021 | US2: View Tasks (5 tasks) |
| Phase 5 | T022-T028 | US3: Delete Task (7 tasks) |
| Phase 6 | T029-T035 | US4: Mark Complete (7 tasks) |
| Phase 7 | T036-T044 | US5: Update Task (9 tasks) |
| Phase 8 | T045-T049 | Polish (5 tasks) |

**Total Tasks**: 49

**Parallelizable Tasks**: Marked with [P] throughout

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All user stories share the same Task and TaskRepository foundation
