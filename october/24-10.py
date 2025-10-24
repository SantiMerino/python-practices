N = int(input("ingresa la magnitud de la matriz: "))
M = []
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
print('-----------------------------------------------')

if N == len(diagonal_principal):
    print("La matriz es cuadrada")
else:
    print("La matriz no es cuadrada")
    
