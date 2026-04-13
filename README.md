# 📝 Python Task CLI

Aplicación de consola desarrollada en Python para gestionar tareas, como parte de un roadmap de aprendizaje backend.

---

## 🚀 Funcionalidades (Semana 2)

- ✅ Añadir tareas
- ✅ Listar tareas
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Editar título de tareas
- ✅ Persistencia en archivo JSON

---

## 🧠 Qué he aprendido

- Implementación de CRUD completo en Python
- Manipulación de estructuras de datos (listas/diccionarios)
- Gestión de estado y persistencia con JSON
- Validación de inputs en CLI
- Organización modular del código
- Flujo de trabajo con Git y GitHub
- Gestión de errores con try/except
- Diseño de funciones con responsabilidades claras
- Implementación de operaciones seguras sobre listas

---

## 📂 Estructura del proyecto

python-task-cli/
│
├── src/
│ ├── main.py # Interfaz CLI
│ └── tasks.py # Lógica de negocio (CRUD)
│
├── data/
│ └── tasks.json
│
├── tests/ # (pendiente)
├── .gitignore
├── requirements.txt
└── README.md


---

## ▶️ Cómo ejecutar

```bash
python -m venv venv
venv\Scripts\activate
python src/main.py

📌 Ejemplo de uso
1. Ver tareas
2. Añadir tarea
3. Completar tarea
4. Eliminar tarea
5. Editar tarea
6. Salir

🔄 Estado del proyecto

    🟢 Semana 2 completada — CRUD funcional

📅 Próximos pasos (Semana 3)
    Refactorizar estructura del proyecto
    Separar lógica de presentación
    Introducir testing básico
    Preparar base para API (FastAPI)

👨‍💻 Autor

Proyecto de aprendizaje backend en Python