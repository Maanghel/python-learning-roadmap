import sys, os

class ConversorUnidades():
    def __init__(self):
        # Longitud: valores en metros
        self.conversiones_longitud = {
            "milimetro": 0.001,
            "centimetro": 0.01,
            "decimetro": 0.1,
            "metro": 1,
            "kilometro": 1000,
            "pulgada": 0.0254,
            "pie": 0.3048,
            "yarda": 0.9144,
            "milla": 1609.344,
            "milla nautica": 1852
        }
        
        # Peso/Masa: valores en kilogramos
        self.conversiones_peso = {
            "miligramo": 0.000001,
            "gramo": 0.001,
            "kilogramo": 1,
            "tonelada": 1000,
            "onza": 0.0283495,
            "libra": 0.453592,
            "stone": 6.35029,
            "ton. larga": 1016.0469088,
            "ton. corta": 907.18474      
        }
        
        # Tiempo: valores en segundos
        self.conversiones_tiempo = {
            "milisegundo": 0.001,
            "segundo": 1,
            "minuto": 60,
            "hora": 3600,
            "dia": 86400,
            "semana": 604800,
            "mes": 2629800,
            "año": 31557600 
        }
        
        # Temperatura: valores en Celsius
        # Nota: La conversión de temperatura no es lineal, se maneja por separado
        self.conversiones_temperatura = ["celsius", "fahrenheit"]
        
        # Agrupación de conversiones
        self.categorias = {
            "longitud": self.conversiones_longitud,
            "peso": self.conversiones_peso,
            "tiempo": self.conversiones_tiempo
        }
        
        self.menu()

    # Método principal para mostrar el menú
    def menu(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n===== CONVERSOR DE UNIDADES =====")
            print("Seleccione el tipo de conversión:")
            print("  1. Longitud")
            print("  2. Peso / Masa")
            print("  3. Tiempo")
            print("  4. Temperatura")
            print("  0. Salir")
            print("=" * 34)
            self.opcion = input("\nIngrese una opción (0-4): ").strip()
            if self.opcion in ["1", "2", "3"]:
                self.convertir_unidades()
            elif self.opcion == "4":
                self.convertir_temperatura_ui()
            elif self.opcion == "0":
                print("\n¡Gracias por usar el conversor de unidades!")
                sys.exit()
            else:
                print("\nOpción no válida. Por favor, intente de nuevo.")
                self._pausar()

    # Método para convertir unidades de longitud, peso o tiempo
    def convertir_unidades(self):
        categoria = {
            "1": "longitud",
            "2": "peso",
            "3": "tiempo"
        }.get(self.opcion)
        
        self._imprimir_unidades(categoria)
        
        while True:
            de = input("\nConvertir de: ").strip().lower()
            if de not in self.categorias[categoria]:
                print("\nUnidad de origen no válida. Intente de nuevo.")
                continue
            
            a = input("Convertir a: ").strip().lower()
            if a not in self.categorias[categoria]:
                print("\nUnidad de destino no válida. Intente de nuevo.")
                continue
                
            break
        
        while True:
            try:
                valor = float(input("Valor a convertir: "))
                unidad_origen = self.categorias[categoria].get(de) # Valor de la unidad de origen
                unidad_destino = self.categorias[categoria].get(a) # Valor de la unidad de destino
                
                resultado = valor * (unidad_origen / unidad_destino) # Conversión
                print(f"\nResultado: {valor} {de} = {resultado:.4f} {a}")
            except ValueError:
                print("\nEntrada no válida.")
            
            break
        
        self._pausar()

    # Método para convertir temperatura entre Celsius y Fahrenheit
    def convertir_temperatura(self, valor, de, a):
        if de == "celsius" and a == "fahrenheit":
            return (valor * 9/5) + 32
        elif de == "fahrenheit" and a == "celsius":
            return (valor - 32) * 5/9
        elif de == a:
            return valor
        else:
            raise ValueError("Conversión de temperatura no válida.")

    # Método para la interfaz de usuario de conversión de temperatura
    def convertir_temperatura_ui(self):
        print("\nUnidades disponibles para temperatura: ")
        for id, unidad in enumerate(self.conversiones_temperatura, 1):
            print(f"{id}. {unidad}")
        
        while True:
            de = input("\nConvertir de: ").strip().lower()
            if de not in self.conversiones_temperatura:
                print("\nUnidad de origen no válida. Intente de nuevo.")
                continue
            a = input("Convertir a: ").strip().lower()
            if a not in self.conversiones_temperatura:
                print("\nUnidad de destino no válida. Intente de nuevo.")
                continue
            
            break
        
        while True:
            try:
                valor = float(input("\nValor a convertir: "))
                resultado = self.convertir_temperatura(valor, de, a)
                print(f"\nResultado: {valor} {de} = {resultado:.2f} {a}")
                break
            except ValueError:
                print(f"\nIngrese una temperatura valida.")
            
        self._pausar()

    # Método para imprimir las unidades disponibles en una categoría
    def _imprimir_unidades(self, categoria):
        unidades = list(self.categorias[categoria].keys()) # Obtener las unidades de la categoría
        print(f"\nUnidades disponibles para {categoria.capitalize()}:")
        for i, unidad in enumerate(unidades, 1):
            print(f"  {i}. {unidad.capitalize()}")
        print()

    # Método para pausar la ejecución y esperar la entrada del usuario
    def _pausar(self):
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ConversorUnidades()