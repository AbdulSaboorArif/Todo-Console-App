"""Task and TaskRepository for Todo CLI Application."""


class Task:
    """Represents a todo task with unique ID, title, description, and status."""

    def __init__(self, id: int, title: str, description: str = "", status: str = "pending"):
        """Initialize a Task.

        Args:
            id: Unique identifier for the task
            title: Short description of the task (required)
            description: Detailed information about the task (optional)
            status: Current state - "pending" or "completed" (default: "pending")
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if status not in ("pending", "completed"):
            raise ValueError("Status must be 'pending' or 'completed'")

        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title!r}, status={self.status!r})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (self.id == other.id and
                self.title == other.title and
                self.description == other.description and
                self.status == other.status)


class TaskRepository:
    """In-memory repository for managing tasks."""

    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add(self, title: str, description: str = "") -> Task:
        """Create and add a new task with auto-generated ID.

        Args:
            title: Short description of the task (required)
            description: Detailed information about the task (optional)

        Returns:
            The newly created Task
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Retrieve a task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The Task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            List of all tasks (ordered by insertion)
        """
        return list(self._tasks)

    def update(self, task_id: int, title: str | None = None, description: str | None = None) -> Task | None:
        """Update an existing task's title and/or description.

        Args:
            task_id: The unique identifier of the task
            title: New title (optional, keeps current if None)
            description: New description (optional, keeps current if None)

        Returns:
            The updated Task if found, None otherwise
        """
        task = self.get_by_id(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return task

    def delete(self, task_id: int) -> bool:
        """Remove a task by its ID.

        Args:
            task_id: The unique identifier of the task

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def toggle_complete(self, task_id: int) -> Task | None:
        """Toggle the completion status of a task.

        Args:
            task_id: The unique identifier of the task

        Returns:
            The updated Task if found, None otherwise
        """
        task = self.get_by_id(task_id)
        if task is None:
            return None

        task.status = "completed" if task.status == "pending" else "pending"
        return task

    def count(self) -> int:
        """Return the total number of tasks."""
        return len(self._tasks)
