# lista = [1, 2, 3, 4, 5, 6, 7]
# print(lista)
# # Añadir
# lista.append(1)
# print(lista)
# # Ordernar
# lista.sort()
# print(lista)

# #Eliminar
# lista.remove(1)
# print(lista)

# for valor in lista:
#     print(f'Valor: {valor}')

nombres = []
for n in range(5):
    nombres.append(input(f'Ingrese el nombre {n+1}: '))
print(nombres)