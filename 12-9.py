# num = 0
# while num <= 0:
#     num = float(input("Enter a positive integer: "))
# print(f"You entered: {num}")

# Calculadora Temu
print("Calculadora Temu")
print("-----------------")  
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

wantsToLeave = False

nums = []
options = ["Sumando", "Restando", "Multiplicando", "Diviendo"]

while wantsToLeave == False:
    print("-----------------")  
    option = int(input("Elige una opción (1-5): "))
    cant = int(input("¿Cuántos números deseas operar? (Mínimo 2): "))
    for i in range(cant):
        num = float(input(f"Ingrese el número #{i+1}: "))
        nums.append(num) # Agrego el número a la lista
    print("-----------------")
    if option == 5:
        wantsToLeave = True
        print("Saliendo de la calculadora. ¡Hasta luego!")
    elif option == 1:
        result = sum(nums)
        print(result)
    elif option == 2:
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        print(result)
    elif option == 3:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result * nums[i]
        print(result)
    elif option == 4:
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != 0:
                result = result / nums[i]
                print(result)
            else:
                print("Error: División por cero no está permitida.")
                result = None
                break
    else:
       print(options[option - 1])
    