# Command Contract: list

## Purpose

Display all tasks with their details and completion status.

## Input

None (no parameters required)

## Output

Success (with tasks):
```
[ ] 1. Buy groceries
    Milk, eggs, bread
[✓] 2. Finish report
    Q4 analysis document
```

Success (empty):
```
No tasks yet. Use 'add' to create one.
```

## Flow

1. Retrieve all tasks from repository
2. Check if list is empty
3. Format each task with status indicator
4. Display formatted output

## Constraints

- Show all tasks (both pending and completed)
- Display ID, title, description, and status
- Use `[✓]` for completed, `[ ]` for pending
- Each task on its own line with proper formatting
