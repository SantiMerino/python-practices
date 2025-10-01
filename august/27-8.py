# Primer Reto: El mensaje misterioso
# Autor: Santi
# owner = "Santi"
# print("Estas intentando obtener un mensaje misterioso")
# name = input("Cual es tu nombre estudiante?: ")
# if name != owner:
#     print("Parece que me he equivocado... Seguiré buscando al dueño de esta carta...")
#     exit()
# print("Bienvenid@ a la aventura, " + name)

# Segundo Reto: 
clave = int(input("Ingrese la clave para númerica: "))
if clave >= 1000 and clave < 1010:
    print("La puerta se abre con un sonido metálico.")
else:
    print("La puerta sigue cerrada. Inténtalo de nuevo.")


# Tercer Reto:
direc = input("Ingrese la dirección en la que quieres avanzar: ").lower()
if direc == "izquierda":
    print("Has llegado a la cafe...por esperar a que te atienda, pierdes la clase")
elif direc == "centro":
    print("Has llegado a la mesa de ping-pong...por jugar, pierdes la clase")
elif direc == "derecha":
    print("Has llegado al aula CLIC a tiempo :D")

# Cuarto Reto:

