# Ejercicio 4
ingresos = [0]*12

for i in range(12):
    ingresos[i] = float(input(f"Ingrese el ingreso del mes {i+1}: "))
print(f"El menor ingreso en el año fue {min(ingresos)}")
print(f"El mayor ingreso en el año fue {max(ingresos)}")
# Normalización 
# x' = (x - min) / (max - min)
ingresosNorm = [0]*12
for i in range(12):
    ingresosNorm[i] = (ingresos[i] - min(ingresos)) / (max(ingresos) - min(ingresos))
print(f"Ingresos originales: {ingresos}")
print(f"Ingresos normalizados: {[round(x, 3) for x in ingresosNorm]}")


# Ejercicio 5
promNorm = sum(ingresosNorm) / len(ingresosNorm)
ingresosMayorProm = []
for i in range(12):
    if ingresosNorm[i] > promNorm:
        # (mes, ingreso normalizado)
        ingresosMayorProm.append((i+1, round(ingresosNorm[i], 3)))
print(f"Meses con ingresos normalizados mayores al promedio{ingresosMayorProm}")

# Ejercicio 6
# comp = 0
# racha = 0
# for i in range(12):
#     if i == 0 
#         comp = ingresos[i]
#     elif ingresos[i] > comp:
#         racha += 1
#         comp = ingresos[i]
#     elif ingresos[i] <= comp:
#         racha = 0
