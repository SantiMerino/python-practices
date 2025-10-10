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
max_intensidad = max(intensidades)
print('---------------------------------------------------------')
print(f"Máximo: {max_intensidad} (minuto {intensidades.index(max_intensidad)+1})")
min_intensidad = min(intensidades)
print('---------------------------------------------------------')
print(f"Minímo: {min_intensidad} (minuto {intensidades.index(min_intensidad)+1})")
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
    intensidades_norm[i] = (intensidades[i] - min(intensidades)) / (max(intensidades) - min(intensidades))
print('---------------------------------------------------------')
#Comparación de listas con comprensión de listas 
print(f"Intensidades oringiales: {intensidades}")
print(f"Intensidades normalizadas: {[round(x, 2) for x in intensidades_norm]}")

