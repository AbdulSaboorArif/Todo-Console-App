"""Main CLI module for Todo CLI Application."""

from .task import TaskRepository


def get_valid_task_id(repository: TaskRepository, prompt: str) -> int | None:
    """Get a valid task ID from user input.

    Args:
        repository: The task repository to look up tasks in
        prompt: The prompt message to display

    Returns:
        The valid task ID, or None if input is invalid
    """
    task_id_str = input(prompt).strip()
    if not task_id_str:
        print("Error: Please provide a task ID.")
        return None

    try:
        task_id = int(task_id_str)
        if task_id <= 0:
            print("Error: Task ID must be a positive number.")
            return None
        return task_id
    except ValueError:
        print("Error: Please provide a valid task ID.")
        return None


# === User Story 1: Add Task ===

def add_command(repository: TaskRepository) -> None:
    """Add a new task with title and optional description."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return

    description = input("Enter task description (optional): ").strip()

    task = repository.add(title, description)
    print(f"Task created with ID: {task.id}")


# === User Story 2: View Tasks ===

def list_command(repository: TaskRepository) -> None:
    """Display all tasks with their details and completion status."""
    tasks = repository.get_all()

    if not tasks:
        print("No tasks yet. Use 'add' to create one.")
        return

    for task in tasks:
        status_mark = "[X]" if task.status == "completed" else "[ ]"
        print(f"{status_mark} {task.id}. {task.title}")
        if task.description:
            print(f"    {task.description}")


# === User Story 3: Delete Task ===

def delete_command(repository: TaskRepository) -> None:
    """Delete a task by ID."""
    task_id = get_valid_task_id(repository, "Enter task ID to delete: ")
    if task_id is None:
        return

    task = repository.get_by_id(task_id)
    if task is None:
        print(f"Error: Task {task_id} not found.")
        return

    repository.delete(task_id)
    print(f"Task {task_id} deleted.")


# === User Story 4: Mark Complete ===

def complete_command(repository: TaskRepository) -> None:
    """Toggle the completion status of a task."""
    task_id = get_valid_task_id(repository, "Enter task ID to complete: ")
    if task_id is None:
        return

    task = repository.get_by_id(task_id)
    if task is None:
        print(f"Error: Task {task_id} not found.")
        return

    task = repository.toggle_complete(task_id)
    if task.status == "completed":
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task {task_id} marked as pending.")


# === User Story 5: Update Task ===

def update_command(repository: TaskRepository, task_id: int | None = None) -> None:
    """Update a task's title and/or description."""
    if task_id is None:
        task_id = get_valid_task_id(repository, "Enter task ID to update: ")
        if task_id is None:
            return

    task = repository.get_by_id(task_id)
    if task is None:
        print(f"Error: Task {task_id} not found.")
        return

    new_title = input("Enter new title (or press Enter to keep current): ").strip()
    new_description = input("Enter new description (or press Enter to keep current): ").strip()

    if not new_title:
        new_title = None
    if new_description == "":
        new_description = None

    repository.update(task_id, title=new_title, description=new_description)
    print(f"Task {task_id} updated.")


# === Phase 8: Help and Exit ===

def help_command() -> None:
    """Display available commands."""
    print("Available commands:")
    print("  add         - Create a new task")
    print("  list        - Show all tasks")
    print("  update <id> - Modify a task")
    print("  delete <id> - Remove a task")
    print("  complete <id> - Toggle task completion")
    print("  help        - Show this message")
    print("  exit        - Quit the application")


def main() -> None:
    """Main entry point for the Todo CLI application."""
    repository = TaskRepository()

    print("Welcome to Todo CLI!")
    print("Commands: add, list, update, delete, complete, help, exit")

    while True:
        try:
            command_line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not command_line:
            continue

        parts = command_line.split()
        command = parts[0].lower()

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            help_command()

        elif command == "add":
            add_command(repository)

        elif command == "list":
            list_command(repository)

        elif command == "delete":
            if len(parts) < 2:
                print("Usage: delete <id>")
            else:
                try:
                    task_id = int(parts[1])
                    if task_id <= 0:
                        print("Error: Task ID must be a positive number.")
                    else:
                        task = repository.get_by_id(task_id)
                        if task is None:
                            print(f"Error: Task {task_id} not found.")
                        else:
                            repository.delete(task_id)
                            print(f"Task {task_id} deleted.")
                except ValueError:
                    print("Error: Please provide a valid task ID.")

        elif command == "complete":
            if len(parts) < 2:
                print("Usage: complete <id>")
            else:
                try:
                    task_id = int(parts[1])
                    if task_id <= 0:
                        print("Error: Task ID must be a positive number.")
                    else:
                        task = repository.get_by_id(task_id)
                        if task is None:
                            print(f"Error: Task {task_id} not found.")
                        else:
                            task = repository.toggle_complete(task_id)
                            if task.status == "completed":
                                print(f"Task {task_id} marked as completed.")
                            else:
                                print(f"Task {task_id} marked as pending.")
                except ValueError:
                    print("Error: Please provide a valid task ID.")

        elif command == "update":
            if len(parts) < 2:
                print("Usage: update <id>")
            else:
                try:
                    task_id = int(parts[1])
                    if task_id <= 0:
                        print("Error: Task ID must be a positive number.")
                    else:
                        update_command(repository, task_id)
                except ValueError:
                    print("Error: Please provide a valid task ID.")

        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")


if __name__ == "__main__":
    main()
