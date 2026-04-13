from tasks import load_tasks, save_tasks, add_task, list_tasks, upd_task, del_task, complete_task

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Modificar titulo de una tarea")
        print("4. Eliminar tarea")
        print("5. Marcar tarea como completada")
        print("6. Salir\n")

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
            taskID = int(input("ID tarea a modificar: "))
            title = input("Nuevo Título: ").strip()
            if not title:
                print("❌ El título no puede estar vacío")
                continue

            try:
                success = upd_task(tasks, taskID, title)
                if success:
                    save_tasks(tasks)
                    print("✅ Tarea modificada correctamente")
                else:
                    print("❌ No se ha encontrado la tarea")

            except ValueError:
                print("❌ El ID de la tarea debe ser un número entero")

        elif option == "4":
            taskID = int(input("ID tarea a eliminar: "))

            try:
                success = del_task(tasks, taskID)
                if success:
                    save_tasks(tasks)
                    print("✅ Tarea eliminada correctamente")
                else:
                    print("❌ No se ha encontrado la tarea")

            except ValueError:
                print("❌ El ID de la tarea debe ser un número entero")
        elif option == "5":
            taskID = int(input("ID tarea completada: "))

            try:
                success = complete_task(tasks, taskID)
                if success:
                    save_tasks(tasks)
                    print("✅ Tarea completada")
                else:
                    print("❌ No se ha podido completar la tarea")

            except ValueError:
                print("❌ El ID de la tarea debe ser un número entero")
        elif option == "6":
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()