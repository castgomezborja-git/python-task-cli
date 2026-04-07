from tasks import load_tasks, save_tasks, add_task, list_tasks

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Salir\n")

        option = input("Elige opción: ")

        if option == "1":
            list_tasks(tasks)

        elif option == "2":
            title = input("Título: ").strip()

            if not title:
                print("❌ El título no puede estar vacío")
                continue

            tasks = add_task(tasks, title)
            save_tasks(tasks)
            print("✅ Tarea añadida correctamente")

        elif option == "3":
            break

if __name__ == "__main__":
    main()