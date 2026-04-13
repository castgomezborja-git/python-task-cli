import json
import os

FILE_PATH = os.path.join("data", "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title):
    new_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return tasks

def list_tasks(tasks):
    if not tasks:
        print("No hay tareas aún 📭")
        return

    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}]')

def update_task_title(tasks, taskID, title):
    for task in tasks:
        if task["id"] == taskID:
            task["title"] = title
            return True
    return False

def delete_task(tasks, taskID):
    initial_len = len(tasks)
    tasks[:] = [task for task in tasks if task["id"] != taskID]
    return len(tasks) < initial_len

def complete_task(tasks, taskID):
    for task in tasks:
        if task["id"] == taskID:
            task["completed"] = True
            return True
    return False