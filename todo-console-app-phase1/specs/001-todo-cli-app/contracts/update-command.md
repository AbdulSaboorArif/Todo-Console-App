# Command Contract: update

## Purpose

Modify an existing task's title and/or description.

## Input

Command line: `update <id>`

Interactive prompts (if task exists):
1. `Enter new title (or press Enter to keep current): `
2. `Enter new description (or press Enter to keep current): `

## Output

Success:
```
Task {id} updated.
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
4. Prompt for new title (optional)
5. Prompt for new description (optional)
6. Apply updates
7. Confirm success

## Constraints

- ID must be a positive integer
- Title can be empty to keep current value
- Description can be empty to keep current value
- Only updates provided values; others remain unchanged
