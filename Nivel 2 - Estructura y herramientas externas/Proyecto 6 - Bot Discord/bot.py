import discord
from datetime import datetime
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Obtiene el token de autenticación del bot desde la variable de entorno
TOKEN = os.getenv("DISCORD_TOKEN")

# Verifica que el token exista
if TOKEN is None:
    raise ValueError("❌ ERROR: No se encontró el token de Discord en las variables de entorno.")

# Configura los intents necesarios para que el bot pueda leer el contenido de los mensajes
intents = discord.Intents.default()
intents.message_content = True

# Crea una instancia del bot con el prefijo deseado
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """Evento que se ejecuta cuando el bot se ha conectado correctamente."""
    print(f"✅ Bot conectado como {bot.user}")


@bot.command()
async def ping(ctx):
    """Comando para comprobar la latencia del bot."""
    try:
        await ctx.send(f"🏓 Pong! Latencia: {round(bot.latency * 1000)}ms")
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al ejecutar el comando `ping`.")
        print(f"Error en ping: {e}")


@bot.command()
async def saludar(ctx):
    """Comando para saludar al usuario."""
    try:
        await ctx.send(f"¡Hola, {ctx.author.mention}! 👋")
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al ejecutar el comando `saludar`.")
        print(f"Error en saludar: {e}")


@bot.command()
async def usuario(ctx):
    """Comando para mostrar información del usuario que envió el mensaje."""
    try:
        user = ctx.author
        await ctx.send(f"👤 Tu nombre: {user.name}\n🆔 ID: {user.id}")
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al ejecutar el comando `usuario`.")
        print(f"Error en usuario: {e}")


@bot.command()
async def fecha(ctx):
    """Comando para mostrar la fecha y hora actual."""
    try:
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await ctx.send(f"🕒 Fecha actual: {ahora}")
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al ejecutar el comando `fecha`.")
        print(f"Error en fecha: {e}")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """Comando que muestra una lista de los comandos disponibles."""
    try:
        ayuda_texto = """
🛠️ **Comandos disponibles:**
`!ping` - Verifica que el bot esté activo.
`!fecha` - Muestra la hora actual.
`!usuario` - Muestra información sobre ti.
`!saludar` - Recibe un saludo amistoso.
"""
        await ctx.send(ayuda_texto)
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al mostrar la ayuda.")
        print(f"Error en ayuda: {e}")

@bot.event
async def on_command_error(ctx, error):
    """Maneja errores que ocurren al ejecutar comandos."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Comando no reconocido. Usa `!ayuda` para ver los comandos disponibles.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Faltan argumentos para este comando.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("💥 Ocurrió un error al ejecutar el comando.")
        print(f"Error interno: {error.original}")
    else:
        await ctx.send("❗ Ha ocurrido un error inesperado.")
        print(f"Error no manejado: {error}")

# Ejecuta el bot y maneja posibles errores de conexión
try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print("❌ ERROR: Token inválido. Verifica que esté correctamente configurado en el archivo .env.")
except Exception as e:
    print(f"❌ ERROR inesperado al iniciar el bot: {e}")
