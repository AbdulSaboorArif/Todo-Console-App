# Command Contract: delete

## Purpose

Remove a task from the list.

## Input

Command line: `delete <id>`

## Output

Success:
```
Task {id} deleted.
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
4. Remove task from repository
5. Confirm deletion

## Constraints

- ID must be a positive integer
- Task ID is not reused after deletion
- Other tasks remain unaffected
