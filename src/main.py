# main.py
from interface_adapters.web.app import run_web_app
from flask import Flask, jsonify, request
from entities.task import Task, db

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Database URI
db.init_app(app)  # Initialize db with Flask app

# Initialize the database
with app.app_context():
    db.create_all()

# Initialize empty list to store tasks
tasks = []

# Endpoint to get all tasks
# /tasks?sort=priority
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Check if sorting by priority is requested
    sort_by_priority = request.args.get('sort') == 'priority'
    
    # Retrieve tasks from the database
    if sort_by_priority:
        tasks = Task.query.order_by(Task.priority).all()  # Sort tasks by priority
    else:
        tasks = Task.query.all()

    # Serialize tasks
    serialized_tasks = [
        {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed, 'priority': task.priority} 
        for task in tasks
    ]
    return jsonify({'tasks': serialized_tasks})

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(title=data['title'], description=data.get('description', ''), completed=data.get('completed', False))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'task': {'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'completed': new_task.completed}}), 201

# Endpoint to update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        db.session.commit()
        return jsonify({'task': {'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed}})
    return jsonify({'error': 'Task not found'}), 404

# Entry point to run the Flask web application
if __name__ == "__main__":
    run_web_app()
