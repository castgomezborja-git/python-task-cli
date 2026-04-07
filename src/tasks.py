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
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    return tasks

def list_tasks(tasks):
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}]')