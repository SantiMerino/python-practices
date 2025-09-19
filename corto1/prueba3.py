# promedio de impares e impares

nums = [0]*10
pares = []
impares = []
for i in range(len(nums)):
    nums[i] = int(input(f"Ingrese el número entero {i+1}: "))
    # Si el número es divisible entre 2 es par, si no es impar
    if nums[i] % 2 == 0:
        # Agregamos a la lista de pares
        pares.append(nums[i])
    else:
        # Agregamos a la lista de impares
        impares.append(nums[i])
# Promedio de pares
if len(pares) > 0:
    # Sumamos los pares y dividimos por su longitud
    promedio_pares = sum(pares) / len(pares)
print(f"El promedio de los números pares es: {promedio_pares}")

# Repetimos con los números impares
if len(impares) > 0:
    promedio_impares = sum(impares) / len(impares)
print(f"El promedio de los pares es: {promedio_impares}")
print("-----------------------------------------------------------")
print("El cadete supero las tres pruebas, La Crónica Galáctica se abre lentamente.")
print("El cadete es digno de ser un verdadero programadaor estelar!!!!!!!")

# Datos prueba: 1 al 10
# Se espera 2, 4, 6, 8 y 10 como pares
# Total de 30/5 = 6

# Se espera 1, 3, 5, 7 y 9 como impares
# Total de 25/5 = 5