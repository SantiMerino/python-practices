# Letras y números entre 1 y 5 
nums = "12345"
cadena = input("Ingrese una cadena cuántica: ")
# lista para contar las apariciones de la cadena en cada número
apariciones = [0]*len(nums)
# condicionales
if nums[0] in cadena:
    # si el la cadena nums en la posición "n" esta en la cadena, se cuenta cuántas veces aparece
    apariciones[0] = cadena.count(nums[0])
if nums[1] in cadena:
    apariciones[1] = cadena.count(nums[1])
if nums[2] in cadena:
    apariciones[2] = cadena.count(nums[2])
if nums[3] in cadena:
    apariciones[3] = cadena.count(nums[3])
if nums[4] in cadena:
    apariciones[4] = cadena.count(nums[4])
# prints
print("Resultados:")
print(f"El número 1 aparece {apariciones[0]} veces.")
print(f"El número 2 aparece {apariciones[1]} veces.")
print(f"El número 3 aparece {apariciones[2]} veces.")
print(f"El número 4 aparece {apariciones[3]} veces.")
print(f"El número 5 aparece {apariciones[4]} veces.")
print("--------------------------------------------------")
print("El firewall se abrío... el cadete logro el objetivo")