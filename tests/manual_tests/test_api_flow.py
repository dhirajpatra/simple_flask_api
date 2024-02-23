import requests

# The base URL for the API
BASE_URL = "http://127.0.0.1:5000"


def create_task(title, description):
    """
    Creates a task using the web API.
    """
    response = requests.post(
        f"{BASE_URL}/tasks",
        json={"title": title, "description": description},
    )
    return response


def list_tasks():
    """
    Lists all tasks using the web API.
    """
    response = requests.get(f"{BASE_URL}/tasks")
    return response


def main():
    # Creating two tasks
    print("Creating Task 1...")
    create_task("Buy groceries", "Milk, Eggs, Bread")
    print("Task 1 created.")

    print("Creating Task 2...")
    create_task("Prepare meeting", "Slides for the project update")
    print("Task 2 created.")

    # Listing all tasks
    print("Listing all tasks...")
    response = list_tasks()
    tasks = response.json()
    print("Tasks listed:")
    for task in tasks:
        print(
            f"ID: {task['id']}, Title: {task['title']}, Completed: {task['is_completed']}"
        )


if __name__ == "__main__":
    main()
