from typing import List
from entities.task import Task
from repositories.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    """
    An in-memory implementation of the TaskRepository.

    This repository is intended for testing or development purposes,
    where a persistent storage is not required. It simulates basic CRUD
    operations on tasks within an in-memory list.

    Attributes:
        tasks (List[Task]): A list to store tasks in memory.
        current_id (int): A counter for assigning unique IDs to new tasks.
    """

    def __init__(self):
        """
        Initializes the repository with an empty list for tasks and
        starts the ID counter at 1.
        """
        self.tasks = []
        self.current_id = 1

    def add(self, task: Task) -> None:
        """
        Adds a new task to the repository, automatically assigning
        a unique ID to the task.

        Args:
            task (Task): The task to be added.
        """
        task.id = self.current_id  # Assign a unique ID to the task
        self.tasks.append(task)  # Add the task to the list
        self.current_id += 1  # Increment the ID counter

    def list_all(self) -> List[Task]:
        """
        Returns a list of all tasks in the repository.

        Returns:
            List[Task]: The list of tasks.
        """
        return self.tasks

    def get(self, task_id: int) -> Task:
        """
        Retrieves a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Task: The task with the specified ID.

        Raises:
            ValueError: If no task with the given ID is found.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError("Task not found")

    def update(self, task: Task) -> None:
        """
        Updates an existing task in the repository.

        This method searches for a task by its ID and replaces it
        with the updated task provided.

        Args:
            task (Task): The task with updated information.

        Raises:
            ValueError: If no task with the given ID is found.
        """
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task  # Replace the old task with the updated task
                return
        raise ValueError("Task not found")
