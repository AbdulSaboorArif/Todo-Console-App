# Command Contract: add

## Purpose

Create a new task with title and optional description.

## Input

Interactive prompts via stdin:
1. `Enter task title: ` - Required string input
2. `Enter task description (optional): ` - Optional string input (press Enter to skip)

## Output

Success:
```
Task created with ID: {id}
```

Error:
```
Error: Title cannot be empty.
```

## Flow

1. Display prompts for title and description
2. Validate title is not empty
3. Create Task with unique ID
4. Add to repository
5. Confirm creation

## Constraints

- Title must be non-empty after stripping whitespace
- Description defaults to empty string if not provided
- ID is auto-generated (monotonically increasing)
