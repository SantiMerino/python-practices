# suma de cadenas de números al cuadrado
num = int(input("Ingrese un número entero positivo: "))
suma = 0
# 0 -> n 
# por cada número en el rango de 1 a n (incluido)
for i in range(1, num + 1):
    # se suma el cuadrado del número siguiente en el rango a la variable suma
    suma += i**2 # i**2 es igual a i*i no
print(f"La suma de los cuadrados de los números del 1 al {num} es: {suma}")
# suma de cuadrados hasta 4:  1 + 4 + 9 + 16 = 30 <----- resultado esperado.
print("--------------------------------------------------")
print("El cadete encedío exitosamente el reactor")