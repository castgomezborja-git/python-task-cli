from tasks import load_tasks, save_tasks

def main():
    print("📝 Gestor de tareas iniciado")

    tasks = load_tasks()
    print(f"Tienes {len(tasks)} tareas")

if __name__ == "__main__":
    main()