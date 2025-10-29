produccion = [
[120, 135, 128, 140, 132, 50], # Línea 1
[110, 120, 115, 130, 125, 40], # Línea 2
[150, 145, 155, 160, 150, 65], # Línea 3
[100, 105, 98, 110, 120, 45] # Línea 4
]


'''produccion = []
for i in range(4):
    filas = input(f'Ingrese los datos de producción de la fila {i+1} separadas por comas: ')
    produccion.append(list(map(int, filas.split(','))))
print(produccion)
for filas in produccion:
    print(filas)
print('-----------------------------------------------')'''

''' Calcula:
a. El total semanal producido por cada línea (15%).
b. El promedio diario general de producción considerando todas las líneas.
(15%).
c. El día con mayor producción total en toda la planta, se debe considera la
producción diaria de cada línea no promedios (20%).
d. Qué línea presentó la mayor variabilidad, es decir, la diferencia entre su día de
mayor y menor producción (25%). '''

# a. El total semanal producido por cada línea
total_semanal = []
for i in range(4):
    # Se suman los valores de cada fila para obtener el total semanal de cada línea
    total_semanal.append(sum(produccion[i]))
print(f"Total semanal por línea: {total_semanal}")
print('-----------------------------------------------')
# b. El promedio diario general de producción considerando todas las líneas
total_diario = 0 
for i in range(4):
    total_diario += sum(produccion[i])
promedio_diario_general = total_diario / (4 * 6)
print(f"Promedio diario general: {promedio_diario_general}")
print('-----------------------------------------------')
# c. El día con mayor producción total en toda la planta
produccion_diaria = [0]*6 # sería de buscar el maximo en las columnas 
for i in range(4):
    # Recorremos las filas
    for j in range(6):
        # Recorremos las columnas
        produccion_diaria[j] += produccion[i][j] # Sumamos la producción diaria de cada línea
dia = produccion_diaria.index(max(produccion_diaria)) + 1 # El indice del día con mayor producción + 1 para que no empiece en 0
print(f"Día de mayor prodcción: Día  {dia} ( total: {max(produccion_diaria)}) ")
print('-----------------------------------------------')
# d. Qué línea presentó la mayor variabilidad, es decir, la diferencia entre su día de
# mayor y menor producción
variabilidad = []
for i in range(4):
    variabilidad.append(max(produccion[i]) - min(produccion[i]))# Diferenciamos entre el valor máximo y minimo de cada línea de embalaje
print(f"Línea con mayor variabilidad: Línea {variabilidad.index(max(variabilidad)) + 1} (diferencia de {max(variabilidad)} unidades.)")

