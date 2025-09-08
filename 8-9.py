numero  = input('Ingresa un número entero mayor a 100: ')
numero = list(numero) # Cifra separada en una lista/matriz 
numero = map(int, numero) # Puntero de el valor en la memoria
numero = list(map(int, numero)) # Cifras separadas 

# suma = 0
# for i in numero:
#     suma = suma + i
# Otra forma de hacerlo más simple
suma = sum(numero) # Función de suma que aparentemente no le importa si es un array

print(numero)
print(suma) 
