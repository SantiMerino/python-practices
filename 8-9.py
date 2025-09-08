numero  = input('Ingresa un número entero mayor a 100: ')
    # suma = 0
    # for i in numero:
    #     suma = suma + i
    # Otra forma de hacerlo más simple
while len(numero) > 1: # La condición es 1 porque si len es igual a 1 ya no es divisible 
    numero = list(numero) # Cifra separada en una lista/matriz 
    numero = map(int, numero) # Puntero de el valor en la memoria
    numero = list(map(int, numero)) # Cifras separadas 
    suma = sum(numero) # Función de suma que aparentemente no le importa si es un array
    print(suma) 
    numero = str(suma) # Convertimos la suma a cadena y se repite hasta cumplir la condición