# Command Contract: complete

## Purpose

Toggle the completion status of a task.

## Input

Command line: `complete <id>`

## Output

Success (pending -> completed):
```
Task {id} marked as completed.
```

Success (completed -> pending):
```
Task {id} marked as pending.
```

Error (task not found):
```
Error: Task {id} not found.
```

Error (invalid ID):
```
Error: Please provide a valid task ID.
```

## Flow

1. Parse and validate ID parameter
2. Look up task in repository
3. If not found, show error
4. Toggle task status
5. Confirm new state

## Constraints

- ID must be a positive integer
- Toggles between "pending" and "completed"
- No separate "uncomplete" command needed
