class Task:
    """
    Represents a task in a todo list application.

    Attributes:
        id (int): A unique identifier for the task.
        title (str): The title of the task.
        description (str): A detailed description of the task.
        is_completed (bool): A flag indicating whether the task has been completed. Defaults to False.

    Example:
        >>> task = Task(1, "Buy groceries", "Milk, Eggs, Bread", False)
        >>> print(task.title)
        Buy groceries
    """

    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        is_completed: bool = False,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed
