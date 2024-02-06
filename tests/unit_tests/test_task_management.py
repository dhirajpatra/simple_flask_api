import pytest
from entities.task import Task
from use_cases.task_management import TaskManagement
from repositories.in_memory_task_repository import InMemoryTaskRepository


@pytest.fixture
def task_management():
    repo = InMemoryTaskRepository()
    return TaskManagement(repo)


def test_add_task_creates_a_new_task(task_management):
    task = Task(id=0, title="New Task", description="Description")
    task_management.add_task(task)
    all_tasks = task_management.list_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].title == "New Task"


def test_complete_task_marks_task_as_completed(task_management):
    task = Task(id=0, title="Task", description="Desc")
    task_management.add_task(task)
    task_management.complete_task(1)  # Assuming the task ID is 1 after adding
    all_tasks = task_management.list_tasks()
    assert all_tasks[0].is_completed is True


def test_list_tasks_returns_all_tasks(task_management):
    task1 = Task(id=0, title="Task 1", description="Desc")
    task2 = Task(id=0, title="Task 2", description="Desc")
    task_management.add_task(task1)
    task_management.add_task(task2)
    all_tasks = task_management.list_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0].title == "Task 1"
    assert all_tasks[1].title == "Task 2"
