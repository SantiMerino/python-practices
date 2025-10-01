# # Actividad 1:
notas = [0]*8
for i in range(len(notas)):
    notas[i] = float(input(f"Ingresa la nota del estudiante {i+1}: "))

print("------------------")
print(f"Nota estudiante 1: {notas[0]}")
print(f"Nota estudiante 8: {notas[7]}")
print(f"Nota estudiante 3: {notas[2]}")

# # # Actividad 2:
active = True
while active:
    print("------------------")
    print("1. Agregar nota")
    print("2. Insertar nota en segunda posición")
    print("3. Eliminar la primera calificación")
    print("4. Mostrar la lista y SALIR")
    print("------------------")

    opcion = int(input("Ingresa una opción válida: "))
    match opcion:
        case 1:
            new = input("Ingresa la nota a agregar: ")
            notas.append(new)
        case 2:
            segunda = input("Ingresa la segunda nota: ")
            notas[1] = segunda
        case 3:
            del notas[0]
        case 4:
            print(notas)
            active = False

# # Actividad 3: 
contador = 0 #contador global
for i in range(len(notas)):
    if notas[i] >= 6 :
        contador += 1
print(f"Han aprobado {contador} estudiantes || Contador con for")

# contador = 0 #contador global
index = 0
contador = 0 # Reiniciamos el contador
while index < len(notas):
    if(notas[index] >= 6):
        contador += 1
    index +=1
print(f"Han aprobado {contador} estudiantes || Contador con while")

# # Actividad 4:
search= float(input("Ingrese la nota a buscar: "))
if search in notas:
    print(f"La nota {search} se encuentra en la lista")
else:
    print(f"La nota {search} no se encuentra en la lista")

# Actividad 5:
notas = sorted(notas)
print(f"Lista ordenada de notas: {notas} de menor a mayor")
notas = sorted(notas, reverse=True) # Reverse = True para ordenar de mayor a menor
print(f"Lista ordenada de notas: {notas} de mayor a menor")