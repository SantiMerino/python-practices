# # Tarea 1:
productos = [0]*5 # [0, 0, 0, 0, 0].
for i in range(5):
    productos[i] = float(input(f'Ingrese el precio del producto #{i+1}: '))
promedio = sum(productos) / len(productos)
print(f'El precio promedio de los productos es: {promedio}')

# # Tarea 2:
frase = input('Ingrese una frase: ')
vocales = 'aeiouAEIOU' # Cadena que contiene todas las vocales
contador = 0
for letra in frase:
    if letra in vocales: # Verifica si la letra es una vocal
        contador += 1
print(f'La cantidad de vocales en la frase es: {contador}')

# # Tarea 3:
frase = input('Ingrese una frase: ')
cant = len(frase) # 4
mirror = ''
# inicio : 4, fin : 0, paso : -1
for i in range(cant, 0, -1):
    # print(frase[i-1]) 
    # frase busca el caracter en la posición i-1
    print(frase[i-1]) # 
    mirror += frase[i-1]
print(mirror)  

# Tarea 4:
uno = int(input('Ingrese un número entero: '))
dos = int(input('Ingrese otro número entero: '))
if uno % 2 == 0 and dos % 2 == 0:
    if uno > dos:
        for i in range(dos, uno+1):
            print(i)
    elif dos > uno:
        for i in range(uno, dos+1):
            print(i)
else:
    print('tus números no es par')