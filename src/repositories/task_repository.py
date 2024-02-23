from abc import ABC, abstractmethod
from typing import List
from entities.task import Task


class TaskRepository(ABC):
    """
    An abstract base class that defines the interface for a task repository.
    """

    @abstractmethod
    def add(self, task: Task) -> None:
        """
        Adds a new task to the repository.

        Args:
            task (Task): The task object to be added to the repository.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[Task]:
        """
        Lists all tasks in the repository.

        Returns:
            List[Task]: A list of all task objects in the repository.
        """
        pass

    @abstractmethod
    def get(self, task_id: int) -> Task:
        """
        Retrieves a task by its unique ID.

        Args:
            task_id (int): The unique identifier of the task to retrieve.

        Returns:
            Task: The task object associated with the given ID.

        Raises:
            ValueError: If no task with the given ID exists in the repository.
        """
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        """
        Updates an existing task in the repository.

        This method should replace an existing task's details with those of
        the provided task object, based on the task ID.

        Args:
            task (Task): The task object with updated details.

        Raises:
            ValueError: If no task with the given ID exists in the repository.
        """
        pass
