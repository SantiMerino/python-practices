# Ingresando los valores de intensidad de señal captados durante 10 minutos consecutivos de un satelit.
# El usuario ingresa los 10 valores.
intensidades = [0]*10
for i in range(10):
    intensidades[i] = float(input(f"Ingrese la intensidad captada en el minuto {i+1}: "))
print(f"Intensidades: {intensidades}")
# Minuto y valor registrado
tiempo_intensidad = []
for i in range(10):
    tiempo_intensidad.append((i+1, intensidades[i]))
print(f"Minuto e intensidad registrada: {tiempo_intensidad}")
# Valor máximo y tiempo de intensidad
max_intensidad = []
for i in range(10):
    valor = max(intensidades)
    if intensidades[i] == valor:
        max_intensidad.append((i+1, intensidades[i]))
print('---------------------------------------------------------')
print(f"Máximo: {valor} (minuto {intensidades.index(valor)+1})")
print(f"Minuto e intensidad máxima registrada: {max_intensidad}")
min_intensidad = []
for i in range(10):
    valor = min(intensidades)
    if intensidades[i] == valor:
        min_intensidad.append((i+1, intensidades[i]))
print('---------------------------------------------------------')
print(f"Minímo: {valor} (minuto {intensidades.index(valor)+1})")
print(f"Minuto e intensidad mínima registrada: {min_intensidad}")
# Promedio de intensidad
promedio_intensidad = sum(intensidades) / len(intensidades)
print('---------------------------------------------------------')
print(f"Promedio {round(promedio_intensidad, 2)}")

# Ejercicio 2
# Anomalias de datos
anomalias = []
contador_anomalias = 0
for i in range(10):
    if intensidades[i] < 25 or intensidades[i] > 90:
        anomalias.append((i+1, intensidades[i])) # Minuto, intensidad
        contador_anomalias += 1
print('---------------------------------------------------------')
if len(anomalias) == 0:
    print("No se detectaron anomalías en los datos.")
else:
    print(f"Intensidades: {intensidades}")
    print(f"Anomalias de datos (minuto, intensidad): {anomalias}")
    print(f"Mediciones normales: {10 - contador_anomalias}")
    print(f"Anomalías detectadas: {contador_anomalias}")

# Ejercicio 3
# Normalización de datos
# x' = (x - min) / (max - min)
intensidades_norm = [0]*10
for i in range(10):
    if max(intensidades) - min(intensidades) == 0:
        intensidades_norm[i] = 0
    else:
        intensidades_norm[i] = (intensidades[i] - min(intensidades)) / (max(intensidades) - min(intensidades))
print('---------------------------------------------------------')
#Comparación de listas con comprensión de listas 
print(f"Intensidades oringiales: {intensidades}")
print(f"Intensidades normalizadas: {[round(x, 2) for x in intensidades_norm]}")

# Agregue dos funcionalidades al programa:
# 1. Existe la posibilidad que la intensidad no cambie por lo que la normalización no se podría realizar. En ese caso, el programa debe indicar que la normalización es 0
# 2. Existe la posibilidad de tener el valor máximo es distintos minutos durante la prueba de intensidad, por lo que el programa debe indicar todos los minutos en los que se obtuvo el valor máximo.