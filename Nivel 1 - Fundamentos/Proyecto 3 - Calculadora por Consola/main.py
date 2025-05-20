import math, sys, os

class Calculadora:
    def __init__(self):
        self.historial = []
        self.menu()
    
    def menu(self):
        while True:
            
            os.system("cls" if os.name == "nt" else "clear")
            print("\n" + "="*30)
            print("        CALCULADORA")
            print("="*30)
            print("  1. Sumar")
            print("  2. Restar")
            print("  3. Multiplicar")
            print("  4. Dividir")
            print("  5. Potencia")
            print("  6. Raíz Cuadrada")
            print("  7. Factorial")
            print("  8. Historial de Operaciones")
            print("  0. Salir")
            print("="*30)
            
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
            elif opcion == "8":
                self.imprimir_historial()
            elif opcion == "0":
                print("¡Gracias por usar la calculadora!")
                sys.exit()
            else:
                print("Opción no válida.")
                self._pausar()
    
    def sumar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 + numero2
        if resultado.is_integer():
            print(f"\nSuma: {int(resultado)}")
        else:
            print(f"\nSuma: {resultado:.2f}")
            
        self.historial.append(f"{numero1} + {numero2} = {self._formatear_resultado(resultado)}")
        
        self._pausar()
    
    def restar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 - numero2
        if resultado.is_integer():
                    print(f"\nResta: {int(resultado)}")
        else:
            print(f"\nResta: {resultado:.2f}")
        
        self.historial.append(f"{numero1} - {numero2} = {self._formatear_resultado(resultado)}")
                
        self._pausar()
    
    def multiplicar(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = numero1 * numero2
        if resultado.is_integer():
            print(f"\nMultiplicación: {int(resultado)}")
        else:
            print(f"\nMultiplicación: {resultado:.2f}")
            
        self.historial.append(f"{numero1} * {numero2} = {self._formatear_resultado(resultado)}")
        
        self._pausar()
    
    def dividir(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        try:
            resultado = numero1 / numero2
                
            if resultado.is_integer():
                print(f"\nDivisión: {int(resultado)}")
            else:
                print(f"\nDivisión: {resultado:.2f}")
            
            self.historial.append(f"{numero1} / {numero2} = {self._formatear_resultado(resultado)}")
            
        except ZeroDivisionError:
                print("\n❌ La división entre cero esta prohibida.")
        except Exception as e:
                print(f"\n⚠️ Error inesperado: {e}")
        
        self._pausar()
    
    def potencia(self):
        numero1, numero2 = self._obtener_dos_numeros()
        
        resultado = math.pow(numero1, numero2 )
        
        if resultado.is_integer():
            print(f"\nPotencia: {int(resultado)}")
        else:
            print(f"\nPotencia: {resultado:.2f}")
        
        self.historial.append(f"{numero1} ** {numero2} = {self._formatear_resultado(resultado)}")
        
        self._pausar()
    
    def raiz_cuadrada(self):
        numero = self._obtener_un_numero()
        
        try:
            resultado = math.sqrt(numero)
            
            if resultado.is_integer():
                print(f"\nRaíz cuadrada: {int(resultado)}")
            else:
                print(f"\nRaíz cuadrada: {resultado:.2f}")
            
            self.historial.append(f"√{numero} = {self._formatear_resultado(resultado)}")
            
        except ValueError:
            print("\n❌ No existe la raíz cuadrada para los negativos en los números reales.")
        
        self._pausar()
    
    def factorial(self):
        numero = self._obtener_un_numero()
        if not numero.is_integer() or numero < 0:
            print("\n❌ El factorial solo se puede calcular para enteros no negativos.")
            self._pausar()
            return
        
        try:
            resultado = math.factorial(int(numero))
            
            if resultado.is_integer():
                print(f"\nFactorial: {int(resultado)}")
            else:
                print(f"\nFactorial: {resultado:.2f}")
            
            self.historial.append(f"!{numero} = {self._formatear_resultado(resultado)}")
        except ValueError as e:
            print(f"{e}")
        
        self._pausar()
    
    def imprimir_historial(self):
        print("\n--- Historial de Operaciones ---")
        
        for i, resultado in enumerate(self.historial, 1):
            print(f"{i}. {resultado}")
        
        self._pausar()
    
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
    
    def _obtener_un_numero(self):
        while True:
            try:
                num = float(input("\nIngrese el numero: ").strip())
                return num
            except ValueError:
                print("❌ Entrada inválida. Debes ingresar números válidos.")
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")
    
    def _formatear_resultado(self, resultado):
        resultado_formateado = int(resultado) if resultado.is_integer() else f"{resultado:.2f}"
        return resultado_formateado

if __name__ == "__main__":
    # Crear una instancia de la clase, lo que inicia automáticamente el programa
    calculadora = Calculadora()