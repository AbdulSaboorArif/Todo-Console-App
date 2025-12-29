# Quickstart: Phase I Todo CLI Application

## Running the Application

From the repository root:

```bash
python -m src.todo_app.main
```

Or:

```bash
cd src/todo_app
python main.py
```

## Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `add` | Create a new task | Run `add`, then enter title and description |
| `list` | Show all tasks | Run `list` to see all tasks with status |
| `update <id>` | Modify a task | Run `update 1`, then enter new values |
| `delete <id>` | Remove a task | Run `delete 1` to remove task 1 |
| `complete <id>` | Toggle completion | Run `complete 1` to mark task 1 complete |
| `help` | Show available commands | Run `help` at any time |
| `exit` | Quit the application | Run `exit` to close |

## Usage Examples

### Adding a Task

```
$ python -m src.todo_app.main
Welcome to Todo CLI!
Commands: add, list, update, delete, complete, help, exit
> add
Enter task title: Buy groceries
Enter task description: Milk, eggs, bread
Task created with ID: 1
>
```

### Listing Tasks

```
> list
[ ] 1. Buy groceries
    Milk, eggs, bread
>
```

### Completing a Task

```
> complete 1
Task 1 marked as completed.
> list
[✓] 1. Buy groceries
    Milk, eggs, bread
>
```

### Deleting a Task

```
> delete 1
Task 1 deleted.
>
```

## Error Handling

- Invalid commands show help message
- Non-existent IDs show error message
- Empty title prompts for valid input
- Application never crashes on invalid input
