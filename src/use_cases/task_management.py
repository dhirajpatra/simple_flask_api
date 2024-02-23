from typing import List
from entities.task import Task
from repositories.task_repository import TaskRepository


class TaskManagement:
    """
    A use case class that encapsulates the logic for managing tasks.

    Attributes:
        repo (TaskRepository): The repository interface for task data access.
    """

    def __init__(self, repo: TaskRepository):
        """
        Initializes the TaskManagement with a specific implementation of
        TaskRepository.

        Args:
            repo (TaskRepository): An instance of a class that implements
            the TaskRepository interface, providing data access operations.
        """
        self.repo = repo

    def add_task(self, task: Task) -> None:
        """
        Adds a new task to the repository.

        Args:
            task (Task): The task object to be added.
        """
        self.repo.add(task)

    def list_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the repository.

        Returns:
            List[Task]: A list of all tasks.
        """
        return self.repo.list_all()

    def complete_task(self, task_id: int) -> None:
        """
        Marks a specified task as completed.

        This method retrieves a task by its ID, marks it as completed,
        and updates the task in the repository.

        Args:
            task_id (int): The ID of the task to be marked as completed.

        Raises:
            ValueError: If no task with the given ID exists in the repository.
        """
        task = self.repo.get(task_id)
        task.is_completed = True
        self.repo.update(task)
