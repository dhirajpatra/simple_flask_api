# main.py
from flask import Flask, jsonify, request
from entities.task import Task

# Initialize Flask app
app = Flask(__name__)

# Initialize empty list to store tasks
tasks = []

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [task.__dict__ for task in tasks]})

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Create task object from request JSON data
    task_data = request.json
    task = Task(
        id=len(tasks) + 1,
        title=task_data['title'],
        description=task_data.get('description', ""),
        is_completed=False
    )
    # Add task to the list
    tasks.append(task)
    # Return newly created task with status code 201 (Created)
    return jsonify({'task': task.__dict__}), 201

# Endpoint to update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Find the task with the given ID
    task = next((task for task in tasks if task.id == task_id), None)
    # If task not found, return error response with status code 404 (Not Found)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    # Update task properties from request JSON data, if provided
    task_data = request.json
    task.title = task_data.get('title', task.title)
    task.description = task_data.get('description', task.description)
    task.is_completed = task_data.get('completed', task.is_completed)
    # Return updated task
    return jsonify({'task': task.__dict__})

# Entry point to run the Flask web application
if __name__ == "__main__":
    app.run(debug=True)
