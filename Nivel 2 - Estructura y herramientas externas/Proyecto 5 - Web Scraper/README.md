# 📝 Proyecto: Web Scraper

## 📋 Descripción

Este proyecto es un scraper automatizado que extrae información de libros desde el sitio [Books to Scrape](http://books.toscrape.com/), ideal para prácticas de scraping y automatización de tareas con Python.

Las tareas se almacenan de forma persistente en un archivo `JSON`.

---

## 🚀 Tecnologías y herramientas utilizadas

- Python 3.x
- Módulos estándar: `time`, `urljoin`, `datetime`, `csv`
- Módulos externos: `bs4`, `requests`, `schedule`
- Formato de persistencia: csv
- Estilo de programación: modular

---

## ⚙️ Cómo ejecutar el proyecto

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el scraper manualmente:
   ```bash
   python scraper.py
   ```
    o deja que corra de forma automatica:
   ```bash
    python scraper.py
    ```

## 💡 Funcionalidades implementadas

- Navegación automática por todas las páginas del catálogo.
- Extracción de título, precio, disponibilidad, calificación y enlace del libro.
- Generación de archivo `.csv` con los resultados.
- Agendado automático del scraper para que se ejecute cada hora.
- Manejador de errores y fallos en la red.
- Nombres únicos por archivo usando `timestamp`.
- Estructura clara y mantenible con funciones bien definidas.

---

## 🛠️ Posibles mejoras futuras

- Implementar un sistema de logs en archivo.
- Subida automática a Google Sheets o base de datos.
- Interfaz gráfica o visualización con Streamlit.
- Guardado en otros formatos como JSON o Excel.

---

## ✅ Estado actual

- ✔️ Funcionalidad principal completada y probada.
- ✔️ Automatización con `schedule` integrada y operativa.
- ✔️ Buen manejo de errores y estructura de código modular.
- ✔️ Proyecto en fase **estable y finalizada**
