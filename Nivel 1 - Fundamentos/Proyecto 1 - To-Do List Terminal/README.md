# 📝 Proyecto: To-Do List en Consola

## 📋 Descripción

Aplicación de consola desarrollada en Python para gestionar una lista de tareas, con funcionalidades completas del ciclo CRUD:

- Crear tareas
- Listar y visualizar detalles
- Editar descripciones
- Marcar como completadas
- Eliminar tareas

Las tareas se almacenan de forma persistente en un archivo `JSON`.

---

## 🚀 Tecnologías y herramientas utilizadas

- Python 3.x
- Módulos estándar: `json`, `os`, `uuid`, `sys`, `datetime`
- Formato de persistencia: JSON
- Estilo de programación: Orientado a Objetos

---

## ⚙️ Cómo ejecutar el proyecto

1. Clona el repositorio o copia los archivos en una carpeta local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el archivo principal:

```bash
python main.py
```

## 💡 Funcionalidades implementadas

- Menú interactivo por consola.  
- Generación de ID único con `uuid`.  
- Registro de fecha de creación con `datetime`.  
- Gestión persistente de datos con `json`.  
- Validación de entradas y control de errores.  
- Limpieza de pantalla multiplataforma (`cls` y `clear`).  

---

## 🛠️ Posibles mejoras futuras

- ✅ Persistencia en archivo JSON ✔️  
- 🔄 Ordenar tareas por fecha o estado  
- 🧠 Filtro por tareas completadas o pendientes  
- 🖥️ Interfaz visual usando `curses` o `tkinter`  
- 📦 Separar lógica y presentación (MVC básico)  

---

## ✅ Estado actual

- CRUD funcional completo  
- Persistencia implementada  
- Control de errores básico  
- Terminal limpio y navegable  
