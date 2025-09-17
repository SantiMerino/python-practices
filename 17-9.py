# Crear un programa que simule el juego piedra, papel o tijera.
# El usuario debe ingresar su elección y la computadora debe generar una elección aleatoria.
import random
choices = ["piedra", "papel", "tijera"]
active = True
userCount = 0
computerCount = 0

while active:
    print("Ingrese [salir] para terminar el juego.")
    print("-----------------")
    userChoice = input("Elige piedra, papel o tijera: ").lower()
    if userChoice == "salir":
        active = False
        print("-----------------")
        if userCount > computerCount:
            print(f"Ganaste el juego! {userCount} a {computerCount}")
        elif userCount < computerCount:
            print(f"Perdiste el juego! {computerCount} a {userCount}")
        print("Saliendo del juego. ¡Hasta luego!")
    else:
        computerChoice = random.choice(choices)
        print(f"La computadora eligió: {computerChoice}")
        if userChoice == computerChoice:
            print("Empate!")
        elif (userChoice == "piedra" and computerChoice == "tijera") or (userChoice == "papel" and computerChoice == "piedra") or (userChoice == "tijera" and computerChoice == "papel"):
            userCount += 1
            print(f" {userChoice.upper()} le gana a {computerChoice.upper()} ¡Ganaste!")
            print("-----------------")
            print(f"Llevas {userCount} victorias y la computadora {computerCount} victorias.") 
        else:
            computerCount += 1
            print(f"{computerChoice.upper()} le gana a  {userChoice.upper()}  ¡Perdiste!")
            print("-----------------")
            print(f"Llevas {userCount} victorias y la computadora {computerCount} victorias.")
