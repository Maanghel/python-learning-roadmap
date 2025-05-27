# 🤖 Proyecto: Discord Bot - M-bot

## 📋 Descripción

Un bot básico para Discord construido con Python y `discord.py`. Ofrece comandos simples para interactuar con los usuarios y obtener información del servidor, ideal como base para bots más complejos.

---

## 🚀 Tecnologías y herramientas utilizadas

- Python 3.x
- Módulos estándar: `os`, `datetime`
- Módulos externos: `discord`, `dotenv`
- Estilo de programación: modular
- Permiso de "Message Content Intent" habilitado en el portal de desarrolladores de Discord

---

## ⚙️ Cómo ejecutar el proyecto

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` con tu token:
   ```bash
    DISCORD_TOKEN=tu_token_aqui
   ```
4. Ejecuta el bot:
   ```bash
   python bot.py
   ```

## 💡 Funcionalidades implementadas

- `!ping` – Verifica la latencia del bot.
- `!fecha` – Muestra la fecha y hora actual.
- `!usuario` – Muestra información del usuario que ejecuta el comando.
- `!saludar` – Envía un saludo personalizado.
- `!ayuda` – Lista los comandos disponibles.
- Manejador de errores para comandos no reconocidos o fallidos.

---

## 🛠️ Posibles mejoras futuras

- 🔧 **Sistema de moderación**: comandos para expulsar, silenciar o banear usuarios.
- 🎮 **Mini juegos**: trivia, adivinanzas o piedra-papel-tijera para entretenimiento.
- 🎭 **Roles automáticos**: asignación de roles según reacciones o comandos.
- 📈 **Logs y estadísticas**: seguimiento de actividad en el servidor.
- 🧠 **IA o respuestas automáticas**: integración con ChatGPT o similares.
- 🌐 **Comandos personalizados por servidor**: configuración dinámica.

---

## ✅ Estado actual

✅ **Finalizado** – El bot está completamente funcional con comandos básicos implementados.  
🧪 Fase de pruebas superada satisfactoriamente.  
🧰 Listo para ser usado o extendido con nuevas funcionalidades.
