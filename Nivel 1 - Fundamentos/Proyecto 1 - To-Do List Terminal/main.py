import json, os, uuid, sys
from datetime import datetime

# Definición de la clase principal para la aplicación de lista de tareas
class To_Do_List():
    def __init__(self):
        # Lista donde se almacenarán las tareas
        self.tareas: dict = []
        # Cargar tareas desde el archivo JSON (si existe)
        self.cargar_tareas()
        # Iniciar el menú principal
        self.menu()

    def menu(self):
        # Menú de opciones principal, se ejecuta en un bucle infinito
        while True:
            # Limpia la consola dependiendo del sistema operativo
            os.system("cls" if os.name == "nt" else "clear")
            print("""\n----- MENU -----
1. Agregar tarea
2. Mostrar tareas
3. Completar tarea
4. Modificar tarea
5. Eliminar tarea
0. Salir
-----------------""")
            opcion = input("\nSeleccione una opción: ")
            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.mostrar_tareas()
            elif opcion == "3":
                self.completar_tarea()
            elif opcion == "4":
                self.modificar_tarea()
            elif opcion == "5":
                self.eliminar_tarea()
            elif opcion == "0":
                print("Saliendo de To-Do List.")
                sys.exit()
            else:
                print("Opción no válida.")
                self._pausar()
    
    def cargar_tareas(self):
        # Cargar tareas desde el archivo 'tareas.json'
        try:
            with open("tareas.json", "r") as archivo:
                self.tareas = json.load(archivo)
        # Si el archivo no existe, se inicializa una lista vacía
        except FileNotFoundError:
            print("Error: El archivo 'tareas.json' no se encuentra.")
            self.tareas = []
        # Si el archivo tiene un formato JSON inválido
        except json.JSONDecodeError:
            print("Error: Formato JSON invalido en 'tareas.json'.")
            self.tareas = []
    
    def guardar_tareas(self):
        # Guarda las tareas actuales en el archivo JSON
        try:
            with open("tareas.json", "w") as archivo:
                json.dump(self.tareas, archivo, indent= 4)
        except Exception as e:
            print(f"❌ Error al guardar las tareas: {e}")
    
    def agregar_tarea(self):
        # Solicita la descripción de la nueva tarea
        descripcion = input("\nAgrege la descripción de la tarea: ").strip()
        
        if not descripcion:
            print("⚠️ Descripción vacía. No se agregó ninguna tarea.")
        else:
            # Crea una nueva tarea con un ID único y la fecha actual
            nueva_tarea = {
                "id": str(uuid.uuid4()),
                "descripcion": descripcion,
                "completado": False,
                "fecha": datetime.now().isoformat()}
            self.tareas.append(nueva_tarea)
            self.guardar_tareas()
            print("✅ La tarea se agregó correctamente.")
        
        self._pausar()
    
    def modificar_tarea(self):
        # Solicita el ID de la tarea a modificar
        tarea_modificar = input("Ingrese el ID de la tarea a editar: ").strip()
        
        if not tarea_modificar:
            print("⚠️ No se ingresó ningún ID.")
        else:
            for tarea in self.tareas:
                if tarea.get("id") == tarea_modificar:
                    # Muestra la descripción actual y solicita una nueva
                    print(f"Descripción actual: {tarea['descripcion']}")
                    nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
                    if nueva_descripcion:
                        tarea["descripcion"] = nueva_descripcion
                        self.guardar_tareas()
                        print(f"✅ Tarea con ID {tarea_modificar} actualizada exitosamente.")
                    else:
                        print("⚠️ Descripción vacía. No se realizaron cambios.")
                    break
            else:
                # Si no se encuentra la tarea con el ID proporcionado
                print(f"❌ No se encontró ninguna tarea con el ID: {tarea_modificar}")
            
        self._pausar()
        
    
    def mostrar_tareas(self):
        # Limpia la pantalla antes de mostrar las tareas
        os.system("cls" if os.name == "nt" else "clear")
        if self.tareas:
            # Recorre todas las tareas y las imprime
            for tarea in self.tareas:
                id_tarea = tarea.get("id")
                descripcion = tarea.get("descripcion")
                completado = tarea.get("completado")
                fecha = tarea.get("fecha")
                
                try:
                    # Convierte la fecha ISO a un formato legible
                    fecha_dt = datetime.fromisoformat(fecha)
                    fecha_legible = fecha_dt.strftime("%d/%m/%Y %H:%M")
                except ValueError:
                    fecha_legible = fecha  # Si falla, se usa tal cual
                
                print("-" * 30)
                print(f"ID: {id_tarea}")
                print(f"Descripción: {descripcion}")
                print(f"Estado: {'✅ Completada' if completado else '❌ Pendiente'}")
                print(f"Fecha: {fecha_legible}")
            print("-" * 30)
        else:
            print("No hay tareas para mostrar.")
        
        self._pausar()
    
    def completar_tarea(self):
        # Solicita el ID de la tarea a completar
        tarea_completar = input("Ingrese el Id de la tarea a completar: ").strip()
        
        if not tarea_completar:
            print("⚠️ No se ingresó ningún ID.")
        else:
            for tarea in self.tareas:
                if tarea_completar == tarea.get("id"):
                    tarea["completado"] = True
                    print(f"✅ Tarea con ID {tarea_completar} marcada como completada.")
                    self.guardar_tareas()
                    break
            else:
                print(f"❌ No se encontró ninguna tarea con el ID: {tarea_completar}")
            
        self._pausar()
    
    def eliminar_tarea(self):
        # Solicita el ID de la tarea a eliminar
        tarea_eliminar = input("Ingrese el Id de la tarea a eliminar: ").strip()
        
        if not tarea_eliminar:
                print("⚠️ No se ingresó ningún ID.")
        else:
            for indice, tarea in enumerate(self.tareas):
                if tarea.get("id") == tarea_eliminar:
                    del self.tareas[indice]
                    print(f"✅ Tarea con ID {tarea_eliminar} eliminada.")
                    self.guardar_tareas()
                    break
            else:
                print(f"❌ No se encontró ninguna tarea con el ID: {tarea_eliminar}")
        
        self._pausar()
    
    def _pausar(self):
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    # Crear una instancia de la clase, lo que inicia automáticamente el programa
    todo = To_Do_List()