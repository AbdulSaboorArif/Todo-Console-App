<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0 (initial creation)
Modified principles: N/A (new constitution)
Added sections: Core Principles, Technical Constraints, Behavior Rules, Governance
Removed sections: N/A
Templates requiring updates: ✅ All templates align with constitution
  - .specify/templates/plan-template.md: No changes needed (Constitution Check section exists)
  - .specify/templates/spec-template.md: No changes needed (user stories format aligns)
  - .specify/templates/tasks-template.md: No changes needed (task organization aligns)
  - .specify/templates/phr-template.prompt.md: No changes needed (PHR format aligns)
Follow-up TODOs: None
-->

# Todo CLI Constitution

## Core Principles

### I. Spec-Driven Development
Every feature MUST be generated through the spec-driven development workflow. No manual code is permitted outside the artifacts produced by the SDD workflow (spec.md, plan.md, tasks.md, and their implementations).

**Rationale**: Ensures consistent architecture, traceable requirements, and quality gates across all development.

### II. CLI-First Interface
The application MUST be CLI-based with clear, user-friendly commands. Text in/out protocol: stdin/args → stdout, errors → stderr.

**Rationale**: Simplicity and portability without UI framework dependencies.

### III. In-Memory Storage
Tasks MUST be stored in memory only. No external database or persistent storage is required for this phase.

**Rationale**: Simplifies the architecture and aligns with the MVP scope.

### IV. Unique Task Identification
Each task MUST have a unique ID assigned upon creation. IDs are immutable and never reused.

**Rationale**: Enables reliable task referencing across CLI operations.

### V. Graceful Error Handling
All errors MUST be handled gracefully with clear, user-friendly messages. Invalid inputs and edge cases MUST be anticipated and handled appropriately.

**Rationale**: Ensures a positive user experience and prevents unexpected crashes.

## Technical Constraints

**Language**: Python 3.13+

**Architecture**: Clean architecture with separation of concerns (models, services, CLI)

**Dependencies**: No external database, no UI framework

## Behavior Rules

- Commands MUST be intuitive and well-documented
- Each operation MUST provide feedback (success or informative error)
- Task IDs MUST be generated uniquely and monotonically
- Invalid inputs MUST result in helpful error messages, not crashes

## Governance

This constitution supersedes all other development practices for the Todo CLI project.

**Amendment Process**:
- Amendments require documentation of the change
- Versioning follows semantic versioning (MAJOR for principle changes, MINOR for additions, PATCH for clarifications)
- All PRs/reviews MUST verify compliance with constitution principles

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
