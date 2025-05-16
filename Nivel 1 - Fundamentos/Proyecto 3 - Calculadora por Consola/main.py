import math, decimal, sys, os

class Calculadora:
    def __init__(self):
        self.historial = []
        self.menu()
    
    def menu(self):
        while True:
            
            os.system("cls" if os.name == "nt" else "clear")
            print("""\n----- MENU -----
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Potencia
6. Raíz Cuadrada
7. Factorial
0. Salir
-----------------""")
            opcion = input("\nSeleccione una opción: ").strip()
            if opcion == "1":
                self.sumar()
            elif opcion == "2":
                self.restar()
            elif opcion == "3":
                self.multiplicar()
            elif opcion == "4":
                self.dividir()
            elif opcion == "5":
                self.potencia()
            elif opcion == "6":
                self.raiz_cuadrada()
            elif opcion == "7":
                self.factorial()
            else:
                print("Opción no válida.")
                self._pausar()
    
    def sumar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 + numero2
        if resultado.is_integer():
            print(f"\nSuma: {int(resultado)}")
        else:
            print(f"\nSuma: {resultado}")
            
        self.historial.append(f"{numero1} + {numero2} = {resultado}")
        
        self._pausar()
    
    def restar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 - numero2
        if resultado.is_integer():
                    print(f"\nResta: {int(resultado)}")
        else:
            print(f"\nResta: {resultado:.2f}")
                    
        self.historial.append(f"{numero1} - {numero2} = {resultado}")
                
        self._pausar()
    
    def multiplicar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 * numero2
        if resultado.is_integer():
            print(f"\nMultiplicación: {int(resultado)}")
        else:
            print(f"\nMultiplicación: {resultado}")
            
        self.historial.append(f"{numero1} * {numero2} = {resultado}")
        
        self._pausar()
    
    def dividir(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        try:
            resultado = numero1 / numero2
            
            print(f"\nDivisión: {resultado}")
            
            self.historial.append(f"{numero1} / {numero2} = {resultado}")
        except ZeroDivisionError:
            print("❌ La división entre cero esta prohibida.")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")
    
    def potencia(self):
        pass
    
    def raiz_cuadrada(self):
        pass
    
    def factorial(self):
        pass
    
    def _pausar(self):
        input("\nPresiona Enter para continuar...")
    
    def _obtener_dos_numeros(self):
        while True:
            try:
                num1 = float(input("\nIngrese el primer número: ").strip())
                num2 = float(input("Ingrese el segundo número: ").strip())
                return num1, num2
            except ValueError:
                print("❌ Entrada inválida. Debes ingresar números válidos.")
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")

if __name__ == "__main__":
    # Crear una instancia de la clase, lo que inicia automáticamente el programa
    calculadora = Calculadora()