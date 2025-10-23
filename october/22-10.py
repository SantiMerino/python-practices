N = int(input("ingresa la magnitud de la matriz: "))
M = []

# for i in range(int(N)):
#     # pedir al usuario que ingrese una fila de la matriz
#     fila = input(f'Fila {i+1}: ')
#     # separar los elementos de la fila por comas
#     fila = fila.split(',')
#     # convertir cada elemento de la lista en entero con la función map
#     fila = map(int, fila)
#     # convertir el map a lista
#     fila = list(fila)
#     M.append(fila)
# print(M)

# ! forma tuneada de imprimir la matriz
for i in range(int(N)):
    fila = list(map(int, input(f'Fila {i+1}: ').split(',')))
    M.append(fila)
print(M)

for fila in M:
    print(fila)

# * Imprimir la diagonal principal
diagonal_principal = []
for i in range(int(N)):
    diagonal_principal.append(M[i][i])
print("Diagonal principal:", diagonal_principal)

# * Imprimir la diagonal secundaria
diagonal_secundaria = []
for i in range(int(N)):
    diagonal_secundaria.append(M[i][N-i-1]) # N-i-1 para obtener el índice correcto de la diagonal secundaria
print("Diagonal secundaria:", diagonal_secundaria)