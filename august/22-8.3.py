# Generador de Contraseñas de Key Institute
# Crear un programa que solicite al usuario un nombre y su color favorito, luego generar una contraseña mezclando ambos con un número aleatorio. Sugerencia: investigar cómo generar números aleatorios en Python. Conceptos explorados: input(), variables tipo string, uso de librerías.

# Ejemplo de ejecución del programa:

# Nombre: Erick

# Color favorito: azul

# -------------------------

# Contraseña sugerida: Erick_azul83
import random
 
nombre = input('Ingrese su nombre: ')
color = input('Ingrese su color favorito: ')
n = input('Ingrese la cantidad de números que desea')
print('---------------------------------------------')
number = str(random.randint(10, 100))
clave = nombre + '_' + color + number
print(f'Contraseña sugerida:  {clave} ')