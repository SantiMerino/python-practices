# Solicitar al usuario las ventas mensuales del año 2024 de las 5 sucursales de la empresa K
# Cada lista representa las 12 ventas mensuales de cada sucursal

# ventas quemadas para pruebas
ventas = [
[1200, 1350, 1100, 1500, 980, 1150, 1250, 1300, 1500, 1600, 1550, 1700],
[980, 1150, 1250, 1300, 1200, 1350, 1100, 1500, 1200, 1350, 1100, 1500],
[1500, 1600, 1550, 1700, 1200, 1350, 1100, 1500, 1500, 1600, 1550, 1700],
[1200, 1350, 1100, 1500, 980, 1150, 1250, 1300, 1500, 1600, 1550, 1700],
[1200, 1350, 1100, 1500, 980, 1150, 1250, 1300, 1500, 1600, 1550, 1700]]




# Matriz de ventas mensuales de 5 sucursales
# ventas = []
# for i in range(5):
#     filas = input(f'Ingrese las ventas mensuales de la sucursal {i+1} separadas por comas: ')
#     ventas.append(list(map(int, filas.split(','))))
#     total_anual.append(sum(ventas[i]))
# print(ventas)


total_anual = []
for i in range(5):
    # ! Sumamos las ventas mensuales de cada sucursal para obtener el total anual v_sucursal = enero + febrero + ... + diciembre
    total_anual.append(sum(ventas[i]))
print(f"Total anual entre sucursales: {total_anual}" )
print('-----------------------------------------------')
# * El mes con mayores ventas en total entre las 5 sucursales
ventas_mensuales = [0]*12
# ! Se recorre la fila y la columna de la matriz para sumar las ventas mensuales 
for filas in range(5):
    for columnas in range(12):
        # ! Sumando las ventas mensuales de cada sucursal enero = v_sucursal1 + v_sucursal2 + ... + v_sucursal5
        ventas_mensuales[columnas] += ventas[filas][columnas]
mes_mayor_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1
print(f"El mes con mayores ventas en total entre las 5 sucursales es el mes {mes_mayor_ventas} con {max(ventas_mensuales)} ventas.")
print('-----------------------------------------------')
print(f"La sucursal con mayor rendimiento es la sucursal {total_anual.index(max(total_anual))+1} con {max(total_anual)} ventas anuales.")