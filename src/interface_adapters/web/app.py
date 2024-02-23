from flask import Flask, request, jsonify
from entities.task import Task
from use_cases.task_management import TaskManagement
from repositories.in_memory_task_repository import InMemoryTaskRepository

app = Flask(__name__)

# Initialize the in-memory task repository
repo = InMemoryTaskRepository()

# Initialize the task management use case with the repository
task_management = TaskManagement(repo)


@app.route("/tasks", methods=["POST"])
def add_task():
    """
    Endpoint to add a new task.

    Expects a JSON payload with 'title' and 'description'.
    Returns a success message upon adding a task.
    """
    data = request.json
    # Create a Task object with data from the request
    task = Task(
        id=0,  # ID will be set by the repository
        title=data["title"],
        description=data["description"],
        is_completed=False,  # Default value for new tasks
    )
    # Use the task management use case to add the task
    task_management.add_task(task)
    return jsonify({"success": True, "message": "Task added"}), 201


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """
    Endpoint to list all tasks.

    Returns a list of tasks with their details.
    """
    tasks = task_management.list_tasks()
    # Convert the list of Task objects to a list of dictionaries
    tasks_data = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "is_completed": task.is_completed,
        }
        for task in tasks
    ]
    return jsonify(tasks_data)


@app.route("/tasks/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    """
    Endpoint to mark a task as completed.

    Task ID is provided in the URL path.
    Returns a success message upon marking a task as completed.
    """
    # Use the task management use case to mark the task as completed
    task_management.complete_task(task_id)
    return jsonify({"success": True, "message": "Task marked as completed"})


def run_web_app():
    """
    Starts the Flask web application.
    """
    app.run(debug=True)


if __name__ == "__main__":
    run_web_app()
