# 🔐 Generador de Contraseñas Seguras

## 📋 Descripción

Aplicación de escritorio simple e intuitiva que genera contraseñas seguras y aleatorias según los criterios seleccionados por el usuario. Utiliza una interfaz gráfica con `Tkinter` para facilitar la configuración, generación y copiado de contraseñas al portapapeles.

---

## 🚀 Tecnologías y herramientas utilizadas

- Python 3.x  
- Módulos estándar: `random`, `string`, `tkinter`, `ttk`  
- Módulo externo: `pyperclip` para copiado automático  
- Estilo de programación: Orientado a Objetos  

---

## ⚙️ Cómo ejecutar el proyecto

1. Asegúrate de tener Python 3 instalado.
2. Instala el módulo externo `pyperclip` si no lo tienes:

```bash
pip install pyperclip
```

3. Ejecuta el archivo principal:

```bash
python main.py
```

## 💡 Funcionalidades implementadas

- Interfaz gráfica intuitiva con Tkinter.
- Permite definir la longitud de la contraseña generada.
- Opciones para incluir:
  - ✅ Letras mayúsculas
  - ✅ Números
  - ✅ Símbolos
- Validación del valor de longitud mínimo.
- Generación instantánea de la contraseña con un clic.
- Campo de salida con contraseña en solo lectura.
- Botón para copiar directamente al portapapeles.
- Mensajes emergentes para alertas, errores o confirmaciones.

---

## 🛠️ Posibles mejoras futuras

- 🎨 Mejora de estilo visual con temas o librerías como `ttkthemes`.
- 🔁 Regenerar contraseña sin cerrar la aplicación.
- 💾 Guardar contraseñas generadas en archivo cifrado.
- 🔐 Requisitos más estrictos por parte del usuario (al menos una mayúscula, un número, etc.).
- 🌐 Versión web con Flask o Streamlit.

---

## ✅ Estado actual

- Aplicación funcional, estable y fácil de usar.
- Interfaz dividida de forma clara en configuración y resultados.
- Buen manejo de errores y validaciones.
- Código modular y mantenible con POO.