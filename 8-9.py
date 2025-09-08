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

active = True
while active:
    print('1. Opción 1')
    print('2. Opción 2')
    print('3. Opción 3')
    print('4. Salir')
    opcion = int(input('Ingrese opción: '))
    def switch_temu(opcion):
        match opcion:
            case 1:
                print('Eligio la opción 1')
            case 2: 
                print('Eleigio la opción 2')
            case 3: 
                print('Eleigio la opción 2')
            case 4: 
                print('El usuario eligio salir')
                active = False