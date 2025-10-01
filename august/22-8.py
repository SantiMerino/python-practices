# Calculadora de Calificaciones
# Pedir al usuario 3 notas parciales, calcular el promedio y mostrar al usuario el promedio de sus notas. Conceptos explorados: variables numéricas, operaciones aritméticas.

# Ejemplo de ejecución del programa:

# Ingresa tus 3 notas:

# > 7

# > 8

# > 6

# -------------------------

# Promedio: 7.0

print('Ingresa tus 3 notas: ')
# Matriz de nota (no copien esto)
notas = []
for i in range(3):
    nota = float(input())
    notas.append(nota)
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
print('--------------------------------')
#Calculo del promedio
# promedio = int(n1 + n2 + n3)/3

promedio = sum(notas) / len(notas)  # Calcula el promedio de las notas
print(f'Promedio: {promedio:.1f}')  # Muestra el promedio con un decimal