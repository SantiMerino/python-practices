import math
# Ejercicio 1
v_inicial = float(input("Ingresa la velocidad inicial (m/s): "))
angulo = float(input("Ingrese el angulo de lanzamiento (grados): "))
radian = math.radians(angulo)

Xcomp = lambda: round(v_inicial*math.cos(radian), 2)
Ycomp = lambda:  round(v_inicial*math.sin(radian), 2)
Tvuelo = lambda ycomp: round((2*ycomp)/9.8, 2) 

print(f'Velocidad inicial (m/s): {v_inicial}')
print(f'Angulo de lanzamiento: {angulo}')
print('----- Resultados ------')
print(f'Velocidad horizontal: {Xcomp()} m/s')
print(f'Velocidad vertical: {Ycomp()} m/s')
print(f'Tiempo de vuelo: {Tvuelo(Ycomp())}')

# Angulos
angulos = [15, 30, 45, 60, 75]
# Radianes
rads = list(map(lambda ang: math.radians(ang), angulos))
# Prints
print(f'Angulos en grados: {angulos}')
print(f'Angulos en radianes: {rads}')
# Formula de distancia angular 
R = list(map(lambda angulo: round(((math.pow(30, 2))/9.81)*math.sin(2*angulo),2), rads))
print(f'Distancias calculadas: {R}')
destacados = list(filter(lambda r: r > 70, R))
print(f'Lanzamientos destacados (>70 m): {destacados}')