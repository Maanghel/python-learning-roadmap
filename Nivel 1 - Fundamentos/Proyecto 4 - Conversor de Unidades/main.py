import sys, os

class ConversorUnidades():
    def __init__(self):
        self.conversiones_longitud = {
            "metro": 1,
            "kilometro": 1000,
            "centimetro": 0.01,
            "milimetro": 0.001,
            "milla": 1609.34,
            "yarda": 0.9144,
            "pie": 0.3048,
            "pulgada": 0.0254
        }
        
        self.conversiones_peso = {
            "kilogramo": 1,
            "ton. métrica": 1000,
            "onza": 0.029,
            "libra": 0.4536,
            "long ton": 1016.05,
            "short ton": 907.185
        }
        
        self.conversiones_tiempo = {
            "hora": 1,
            "minuto": 60,
            "segundo": 3600,
            "dia": 0.0417,
            "año": 0.000114
        }
        
        self.categorias = {
            "longitud": self.conversiones_longitud,
            "peso": self.conversiones_peso,
            "tiempo": self.conversiones_tiempo
        }
        
        self.menu()
    
    def menu(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("""\n----- MENU -----
1. Longitud
2. Peso
3. Tiempo
4. Temperatura
0. Salir
-----------------""")
            self.opcion = input("\nSeleccione el tipo de unidad: ").strip()
            if self.opcion in ["1", "2", "3"]:
                self.conversion_unidades()
            elif self.opcion == "4":
                self.convertir_temperatura_ui()
            elif self.opcion == "0":
                print("Saliendo del conversor de unidades.")
                sys.exit()
            else:
                print("Opción no válida.")
                self._pausar()
    
    def conversion_unidades(self):
        categoria = {
            "1": "longitud",
            "2": "peso",
            "3": "tiempo"
        }.get(self.opcion)
        
        self._imprimir_unidades(categoria)
        
        unidad_origen = input("\nUnidad de origen: ").strip().lower()
        unidad_destino = input("Unidad de destino: ").strip().lower()
        
        try:
            valor = float(input("Valor a convertir: "))
            factor_origen = self.categorias[categoria].get(unidad_origen)
            factor_destino = self.categorias[categoria].get(unidad_destino)
            
            if factor_origen and factor_destino:
                resultado = valor * (factor_origen / factor_destino)
                print(f"\nResultado: {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
            else:
                print("\nUna o ambas unidades no son válidas.")
        except ValueError:
            print("\nEntrada no válida.")
        self._pausar()
        
    def convertir_temperatura(self, valor, de, a):
        if de == "celsius" and a == "fahrenheit":
            return (valor * 9/5) + 32
        elif de == "fahrenheit" and a == "celsius":
            return (valor - 32) * 5/9
        elif de == a:
            return valor
        else:
            raise ValueError("Conversión de temperatura no válida.")
        
    def convertir_temperatura_ui(self):
        print("\nUnidades disponibles: celsius, fahrenheit")
        de = input("Convertir de: ").strip().lower()
        
        try:
            valor = float(input("Valor a convertir: "))
            resultado = self.convertir_temperatura(valor, de, a)
            print(f"\nResultado: {valor} {de} = {resultado:.2f} {a}")
        except ValueError as e:
            print(f"\nError: {e}")
        self._pausar()
        
    def _imprimir_unidades(self, categoria):
        print(f"\nUnidades disponibles para {categoria}:")
        for id, unidad in enumerate(self.categorias[categoria], 1):
            print(f"{id}. {unidad}")
            
    def _pausar(self):
        input("\nPresiona Enter para continuar...a")
    
if __name__ == "__main__":
    ConversorUnidades()