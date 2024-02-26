# Software Code Challenge: Todo List Application

The Todo List Application is designed to help users manage their tasks efficiently. It allows users to keep track of their daily, weekly, or project-specific tasks in a simple yet effective manner. 
The domain revolves around task management, focusing on the creation, listing, and updating of tasks to reflect their current status and details.

## Features

This application currently supports the following features:

* **Create Tasks:** Users can add new tasks to their todo list, specifying details such as the task title and description.
* **List Tasks:** The application provides an overview of all tasks added, allowing users to see what they have planned at a glance.
* **Complete Tasks:** Users can mark tasks as completed, helping them track their progress on various activities.

These features are accessible through a RESTful API, enabling easy integration with various clients, such as web interfaces or mobile applications.


## Running the Application

To start the application, ensure you have the necessary requirements installed:

```
pip3 install -r requirements.txt
```

Then run the following command from the root directory of the project:

```
make run
```

This command starts a Flask web server, making the API accessible on http://localhost:5000.

An example usage in python of the application can be used in the `tests/manual_tests/test_api_flow.py` file. You can run this file by executing:
```
make manual_test
```


## Contributing

We are constantly looking to improve the Todo List Application and would love your contributions! We are currently seeking contributions for a new feature:

### Priority Feature

* **Task Priority:** Allow users to assign a priority (e.g., High, Medium, Low) to tasks when creating or updating them.
* **Sorting by Priority:** Enhance the task listing feature to support sorting tasks by their priority, ensuring that users can focus on the most critical tasks first.

Your contributions will help make the Todo List Application more useful for everyone!

### Development Environment

Install the development requirements:

```
pip3 install -r requirements-dev.txt
```

You can run unit tests by executing:

```
make unit_test
```
