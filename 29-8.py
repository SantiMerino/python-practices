# Hechizos Mágicos
# Crea un programa que solicite al usuario ingresar varios valores y verifique si cumplen con ciertas condiciones.
# Si todas las condiciones se cumplen, el programa debe imprimir "¡Felicidades! Todos los hechizos fueron efectivos."
# Si alguna condición no se cumple, debe imprimir "Algún hechizo falló. Inténtalo de nuevo."

# ! Código anterior comentado
# rango = int(input("Ingrese un número entre 299 y 450: "))
# hechizo1 = 299 > rango < 450  #Flag 1
# par = int(input("Ingrese un número par: "))
# hechizo3 = par % 2 == 0 #Flag 2
# multiplo = int(input("Ingrese un número múltiplo de 7: "))
# hechizo2 = multiplo % 7 == 0 #Flag 3
# minus = input("Ingrese una cadena de texto en minúsculas (estudiante, doer, next-one): ").lower()
# hechizo4 = minus in {'estudiante', 'doer', 'next-one'} #Flag 4
# key = input("Ingrese una cadena que incluya 'key': ")
# hechizo5 = 'key' in key #Flag 5
# if hechizo1 and hechizo2 and hechizo3 and hechizo4 and hechizo5:
#     print("¡Felicidades! Todos los hechizos fueron efectivos.")
# else:
#     print("Algún hechizo falló. Inténtalo de nuevo.")

def rango():
    rango = int(input("Ingrese un número entre 299 y 450: "))
    if 299 < rango < 450:
        print('El hechizo fue efectivo. Sigue así')
        return True
    else:
        print('El hechizo falló. Inténtalo de nuevo.')
        return False

def par():
    par = int(input("Ingrese un número par: "))
    if par % 2 == 0:
        print("El hechizo fue efectivo. Sigue así")
        return True
    else:
        print("El hechizo falló. Inténtalo de nuevo.")
        return False

def multiplo():
    multiplo = int(input("Ingrese un número múltiplo de 7: "))
    if multiplo % 7 == 0:
        print("El hechizo fue efectivo. Sigue así")
        return True
    else:
        print("El hechizo falló. Inténtalo de nuevo.")
        return False

def minus():
    minus = input("Ingrese una cadena de texto en minúsculas (estudiante, doer, next-one): ").lower()
    if minus in {'estudiante', 'doer', 'next-one'}:
        print("El hechizo fue efectivo. Sigue así")
        return True
    else:
        print("El hechizo falló. Inténtalo de nuevo.")
        return False

def key():
    key = input("Ingrese una cadena que incluya 'key': ")
    if 'key' in key:
        print("El hechizo fue efectivo. Sigue así")
        return True
    else:
        print("El hechizo falló. Inténtalo de nuevo.")
        return False

hechizo1 = False
hechizo2 = False
hechizo3 = False
hechizo4 = False
hechizo5 = False

while not hechizo1:
    hechizo1 = rango()
while not hechizo2:
    hechizo2 = par()
while not hechizo3:
    hechizo3 = multiplo()
while not hechizo4:
    hechizo4 = minus()
while not hechizo5:
    hechizo5 = key()

print("¡Felicidades! Todos los hechizos fueron efectivos. Venciste al jefe final.")

# ! Lo siento Erick me tarde haciendo esta solución, pero aquí está. :D

