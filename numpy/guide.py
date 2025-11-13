from asyncio.windows_events import CONNECT_PIPE_MAX_DELAY
from socket import INADDR_UNSPEC_GROUP
import numpy as np
# my_list = [1, 2, 3, 4, 5]
# arr = np.array(my_list)
# print(arr)

# zeros = np.zeros(5)
# print(zeros)

# arr = np.array([1,2,3,4,5])
# slice = arr[2:4]
# print(slice)

# mask = arr > 2
# result = arr[mask]
# print(result)

# arr = np.array([1, 2, 3, 4, 5])
# indices = np.array([0, 2, 4]) 
# result = arr[indices]
# print(result)

# arr1 = np.array([1,2, 3])
# arr2 = np.array([4, 5, 6])
# concatenated = np.concatenate((arr1, arr2))
# print(concatenated)

# arr = np.array([1, 2, 3, 4, 5, 6])
# split = np.split(arr, 3)
# print(split)

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])

#Promedio por hogar
promedioHogar = np.mean(consumo, axis = 1)

#Promedio de consumo diario de todos los hogares
promedioDia = np.mean(consumo, axis = 0)

#Suma total de consuma de la semana de los 10 hogares
totalConsumo = np.sum(consumo)

print(promedioHogar)
print(promedioDia)
print(totalConsumo)

maximos = np.max(consumo, axis=1)
minimos = np.min(consumo, axis=0)
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(f'Desviación{desviacion}')

consumoTotal = np.sum(consumo, axis = 1)
hogarMayorConsumo = np.argmax(consumoTotal)
hogarEficiente = np.argmin(consumoTotal)

print(consumoTotal)
print(hogarMayorConsumo)
print(hogarEficiente)

consumoTotalHogar = np.sum(consumo, axis = 1)
print(f'Consumo total de cada hogar durante la semana: { consumoTotalHogar}')

altos = consumoTotalHogar > 100

consumoMayor100 = np.where(altos)[0]
print(f'ids de hogares con consumo mayor a 100: {consumoMayor100}')

consumoNormalizado = (consumo - consumo.min()/(consumo.max() - consumo.min()))
# Resultado
print(consumoNormalizado)

# Cuestionario.
# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumoHogar5 = consumo[4, 4]
print(f'Consumo del Hogar 5 el día 5: {consumoHogar5}')
# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
indices = np.array([7,8,9])
consumoUltimos3 = consumo[indices, 6] 
print(f'Consumo de los ultimos 3 hogares el domingo {consumoUltimos3}')
# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promConsumoFinSemana = np.mean(consumo[:, [5, 6]])
print(f'Promedio de consumo en el fin de semana: {promConsumoFinSemana}')
# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviacionDia = np.std(consumo, axis =1)
indice = np.argmax(desviacionDia)
print(f"El día con mayor desviación estandar {indice}")
# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
indicesMenores = np.argsort(consumoTotalHogar)[:3]
valoresMenores = consumoTotalHogar[indicesMenores]
print(f'Los 3 hogares con menor consumo total son: {indicesMenores} con consumos {valoresMenores}')
# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
consumoHogar3 = consumo[2, :] * 1.1
consumoTotalHogar3 = np.sum(consumoHogar3)
print(f'Nuevo consumo total semanal del Hogar 3 con aumento del 10%: {consumoHogar3}')
