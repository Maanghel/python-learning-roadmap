import random

# Función principal que gestiona la ejecución del juego
def jugar():
    opciones = ["piedra", "papel", "tijera"]
    conteo = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
    
    print("🎮 Bienvenido al juego de Piedra, Papel o Tijera 🎮")
    
    # Solicita al usuario el número de rondas que quiere jugar
    while True:
        try:
            # Intenta convertir la entrada en un número entero
            rondas = int(input("\nIngrese la cantidad de rondas que desea jugar: "))
            if rondas <= 0:
                print("⚠️ Debe ingresar un número positivo.")
                continue
            break
        except ValueError:
            # Si la entrada no es un número válido, muestra un error
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")
    
    # Llama a la función para jugar las rondas y pasar el conteo
    jugar_rondas(rondas, opciones, conteo)
    # Muestra las estadísticas finales después de las rondas
    mostrar_estadisticas(conteo)

# Función para jugar las rondas del juego
def jugar_rondas(rondas, opciones, conteo):
    # Variable para llevar el seguimiento de la ronda actual
    ronda_actual = 0
    
    # Bucle que se ejecuta por el número de rondas
    while ronda_actual < rondas:
        print(f"\n--- Ronda {ronda_actual + 1} de {rondas} ---")
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower().strip()
        
        if jugador == "salir":
            print("👋 Gracias por jugar.")
            break
        
        # Si la opción del jugador no es válida, muestra un mensaje y pide otra elección
        if jugador not in opciones:
            print("⚠️ Elección inválida. Intenta de nuevo.")
            continue
        
        # La computadora elige aleatoriamente entre piedra, papel o tijera
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        if jugador == computadora:
            print("🤝 ¡Empataron esta ronda!")
            conteo["empatadas"] += 1
        elif (jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
            print("✅ ¡Ganaste esta ronda!")
            conteo["ganadas"] += 1
        else:
            print("❌ ¡Perdiste esta ronda!")
            conteo["perdidas"] += 1
        
        ronda_actual += 1

# Función para mostrar las estadísticas finales del juego
def mostrar_estadisticas(estadisticas):
    # Imprime las estadísticas finales
    print("\n📊 --- Estadísticas Finales ---")
    print(f"Victorias del jugador: {estadisticas['ganadas']}")
    print(f"Victorias de la computadora: {estadisticas['perdidas']}")
    print(f"Empates: {estadisticas['empatadas']}")
    
    # Determina quién ganó en base al conteo de victorias
    if estadisticas["ganadas"] > estadisticas["perdidas"]:
        print("\n🏆 El ganador es el Jugador!!")
    elif estadisticas["perdidas"] > estadisticas["ganadas"]:
        print("\n🤖 El ganador es la Computadora!!")
    else:
        print("\n😐 ¡Es un empate entre el Jugador y la Computadora!")


if __name__ == "__main__":
    jugar()