# Ingresar las 10 notas
# nota1 = float(input('Ingresa la nota #1: '))
# nota2 = float(input('Ingresa la nota #2: '))
# nota3 = float(input('Ingresa la nota #3: '))
# nota4 = float(input('Ingresa la nota #4: '))
# nota5 = float(input('Ingresa la nota #5: '))
# nota6 = float(input('Ingresa la nota #6: '))
# nota7 = float(input('Ingresa la nota #7: '))
# nota8 = float(input('Ingresa la nota #8: '))
# nota9 = float(input('Ingresa la nota #9: '))
# nota10 = float(input('Ingresa la nota #10: '))

# prom = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8+ nota9 + nota10)/10
# if prom >= 6:
#     print(f'Has sido APROBADO con {prom} en tu nota global')
# else:
#     print(f'Has sido REPROBADO con {prom} en tu nota global')

# Introducción al bucle for
suma = 0
cant = int(input('Ingrese la cantidad de notas que desea ingresar: '))
for i in range(cant): # El rango inicia desde el primer valor hasta n-1 del valor final del rango
    nota = float(input(f'Ingresa la nota {i+1} de {cant}: '))
    suma += nota

promedio = suma/cant
print(f'Has aprobado con un promedio de {promedio:.2f}')
