''' 1. Ingreso de datos. Solicita al usuario los valores de PM2.5 de las 4 zonas (6 días c/u) y almacénalos en una
lista anidada (pm25).
2. Análisis básico
a. Promedio semanal por zona (lista con 4 promedios).
b. Promedio general considerando todas las mediciones.
3. Tendencia semanal por zona. Para cada zona, compara el promedio de los primeros 3 días vs. el promedio
de los últimos 3 días:
a. Si baja ≥ 1.0 µg/m³ → “Mejoró”
b. Si sube ≥ 1.0 µg/m³ → “Empeoró”
c. En otro caso → “Sin cambio”
d. Reporta una lista con la etiqueta por zona y di cuántas zonas mejoraron.
4. Análisis de estabilidad. Calcula la variabilidad (máx y mín) de cada zona. Clasifica cada zona según su
estabilidad:
a. Variabilidad ≤ 3.5 → “Estable”
b. Variabilidad > 3.5 → “Inestable”
c. Si al menos el 51% de las zonas son estables, muestra un mensaje de que no se detecta riesgo de
contaminación, caso contrario informa sobre el peligro.'''


# Datos quemados
pm25 = [
 [18.0, 20.5, 19.2, 17.8, 16.9, 17.0], # Zona 1
 [12.5, 13.0, 14.2, 15.3, 16.0, 15.7], # Zona 2
 [25.0, 24.8, 24.5, 23.2, 22.7, 22.5], # Zona 3
 [10.0, 11.5, 12.2, 13.1, 12.8, 13.3] # Zona 4
]

# Ingreso de datos por el usuario
# pm25 = []
# for i in range(4):
#     filas = input(f'Ingrese los datos de PM2.5 de la zona {i+1} separadas por comas: ')
#     pm25.append(list(map(float, filas.split(','))))
# for filas in pm25:
#     print(filas)

# a. El promedio semanal de PM2.5 para cada zona
promedio_semanal = []
print("-----------------------------------------------")
for i in range(4):
    # Se suman los valores de cada fila y se divide entre la cantidad de días (6)
    prom = sum(pm25[i]) / len(pm25[i])
    promedio_semanal.append(round(prom, 2))
print(f"Promedio semanal por zona: {promedio_semanal}")
print('-----------------------------------------------')
# b. El promedio general considerando todas las mediciones
total_general = 0
for i in range(4):
    total_general += sum(pm25[i])
    promedio_general = total_general / (4 * 6)
print(f"Promedio general: {round(promedio_general, 2)} µg/m³")
print('-----------------------------------------------')
# 2. Tendencia semanal por zona
# a. Si baja ≥ 1.0 µg/m³ → “Mejoró”
tendencias = []
for i in range(4):
    prom_primeros3 = sum(pm25[i][:3]) / 3
    prom_ultimos3 = sum(pm25[i][3:]) / 3
    # Diferencia entre los promedios
    diferencia = prom_primeros3 - prom_ultimos3
    print(f"Diferencia zona {i+1}: {diferencia}")
    # Clasificación según la diferencia
    if diferencia <= -1.0:
        # Si la diferencia es negativa mejoro
        tendencias.append("Mejoró")
    elif diferencia >= 1.0:
        # Si la diferencia es positiva empeoro
        tendencias.append("Empeoró")
    else:
        tendencias.append("Sin cambio")
print(f"Tendencias por zona: {tendencias}")
tendencias_count = []
for i in range(4):
    if tendencias[i] == "Mejoró":
        tendencias_count.append(f"Zona {i+1}: Mejoró")
print(f'Zonas que mejoraaron: {tendencias_count}')
print('-----------------------------------------------')
# 3. Análisis de estabilidad
variabilidades = []
count = 0
for i in range(4):
    # Calculo de la variabilidad por zona
    variabilidades.append(max(pm25[i]) - min(pm25[i]))
    if variabilidades[i] <= 3.5:
        print(f"Zona {i+1} es Estable")
        count += 1
    elif variabilidades[i] > 3.5:
        print(f"Zona {i+1} es Inestable")
if count >= 3:
    print("No se detecta riesgo de contaminación")
else:
    print("Peligro de contaminación detectado")
print('-----------------------------------------------')