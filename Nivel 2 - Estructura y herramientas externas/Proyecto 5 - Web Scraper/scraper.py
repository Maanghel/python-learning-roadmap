"""Modulos necesarios para el scraper de libros."""
import time  # Para manejar esperas y temporizaciones
from urllib.parse import urljoin  # Para construir URLs absolutas
from datetime import datetime  # Para generar nombres de archivo con timestamp
import csv  # Para guardar los datos en formato CSV
from bs4 import BeautifulSoup  # Para analizar y extraer contenido HTML
import requests  # Para realizar peticiones HTTP
import schedule  # Para programar tareas automáticas

# URL base del sitio a scrapear
BASE_URL = "http://books.toscrape.com/catalogue/"

# Encabezado personalizado para simular un navegador real
HEADER = {"User-Agent": "Mozilla/5.0"}

def obtener_html(url):
    """
    Realiza una solicitud HTTP a la URL proporcionada y retorna el HTML.
    
    Parámetros:
        url (str): La URL de la página a obtener.
    
    Retorna:
        str: El contenido HTML de la página, o None si ocurre un error.
    """
    try:
        response = requests.get(url, headers=HEADER, timeout=10)  # Hace la petición HTTP
        response.raise_for_status()  # Lanza error si el estado no es 200 (OK)
        return response.text  # Devuelve el contenido HTML
    except requests.RequestException as e:
        print(f"❌ Error al obtener la página {url}: {e}")  # Muestra error
        return None  # Devuelve None si hay fallo

def parsear_pagina(html):
    """
    Extrae los datos de los libros presentes en la página HTML.
    
    Parámetros:
        html (str): Contenido HTML de una página de libros.
    
    Retorna:
        tuple: (lista de libros, botón 'next' si existe)
    """
    soup = BeautifulSoup(html, "html.parser")  # Convierte HTML a objeto navegable
    libros = soup.find_all("article", class_="product_pod")  # Encuentra todos los libros en la página
    
    datos = []
    for libro in libros:
        titulo = libro.h3.a["title"]  # Obtiene el título del libro
        precio = libro.find("p", class_="price_color").text  # Precio
        disponibilidad = libro.find("p", class_="instock availability").text.strip()  # Disponibilidad (con espacios limpiados)
        calificacion = libro.p["class"][1] if len(libro.p["class"]) > 1 else "SinCalificación"  # Calificación por clase CSS
        enlace_relativo = libro.h3.a["href"]  # Enlace relativo al libro
        enlace_completo = urljoin(BASE_URL, enlace_relativo)  # Enlace absoluto
        
        datos.append({
            "Título": titulo,
            "Precio": precio,
            "Disponibilidad": disponibilidad,
            "Calificación": calificacion,
            "Enlace": enlace_completo
        })
    
    return datos, soup.find("li", class_="next")  # Devuelve los datos y el botón "next" si existe


def ejecutar_scraper():
    """
    Ejecuta el scraping sobre todas las páginas del catálogo
    y guarda los datos en un archivo CSV.
    """
    pagina_actual = "page-1.html"  # Comienza desde la primera página
    todos_los_datos = []  # Lista para acumular todos los libros
    
    while pagina_actual:
        url = urljoin(BASE_URL, pagina_actual)  # Construye URL completa
        print(f"📄 Procesando: {url}")
        html = obtener_html(url)  # Obtiene HTML de la página actual
        if not html:
            break  # Si falla la petición, termina
        
        datos, next_btn = parsear_pagina(html)  # Extrae libros y el botón "next"
        todos_los_datos.extend(datos)  # Agrega los libros encontrados a la lista
        
        if next_btn:
            pagina_actual = next_btn.a["href"]  # Actualiza con la siguiente página
        else:
            pagina_actual = None  # Fin del catálogo
        
        time.sleep(1)  # Espera 1 segundo para evitar saturar el servidor
    
    guardar_csv(todos_los_datos)  # Guarda todos los libros en un archivo CSV

def guardar_csv(datos):
    """
    Guarda la lista de libros en un archivo CSV con nombre único por timestamp.
    
    Parámetros:
        datos (list): Lista de diccionarios con los datos de los libros.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Fecha actual para nombrar el archivo
    nombre_archivo = f"libros_{timestamp}.csv"  # Nombre del archivo con fecha
    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["Título", "Precio", "Disponibilidad", "Calificación", "Enlace"]
        writer = csv.DictWriter(archivo, fieldnames=campos)  # Prepara el escritor CSV
        writer.writeheader()  # Escribe la cabecera (nombres de columnas)
        writer.writerows(datos)  # Escribe los datos de cada libro
    
    print(f"✅ Datos guardados en '{nombre_archivo}'.")

def tarea_programada():
    """
    Función envoltorio que se ejecuta automáticamente según la programación.
    """
    print(f"🕒 Ejecutando scraper: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    ejecutar_scraper()  # Ejecuta todo el scraping

schedule.every(1).hours.do(tarea_programada)  # Programa para ejecutar scraper cada 1 hora

if __name__ == "__main__":  # Solo se ejecuta si este archivo es el principal
    print("🔁 Iniciando programa en modo automático. Presiona Ctrl+C para detener.")
    try:
        while True:
            schedule.run_pending()  # Ejecuta las tareas programadas si corresponde
            time.sleep(1)  # Espera 1 segundo antes de volver a comprobar
    except KeyboardInterrupt:
        print("\n🛑 Programa detenido por el usuario.")