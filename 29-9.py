# Ejercicio 1
cant = int(input("Ingrese la cantidad de productos a registrar: "))
productos = []
cantidad = []
ingresos = []
nombres = []

for i in range(cant):
    nombre = input(f"Producto {i+1} - Ingrese el nombre del producto: ")
    nombres.append(nombre)
    producto = float(input(f"Producto {i+1} - Ingrese el precio del producto: "))
    productos.append(producto)
    cantprod = int(input(f"Producto {i+1} - Ingrese la cantidad del producto: "))
    cantidad.append(cantprod)
    # Ingresos = precio * cantidad
    ingresos.append(producto * cantprod)
print("------------------")
productos = sorted(productos, reverse=True)
print(f"Lista ordenada de productos: {productos} de mayor a menor")
print("------------------")
print(f"Lista de ingresos: {ingresos}")
print(f"El total de ingresos es: {sum(ingresos)}")

# Ejercicio 2
destacados = []
for i in range(cant):
    if ingresos[i] > 10000:
        destacados.append(ingresos[i])
print(f"Productos destacados (mayores a 10,000): {destacados}")

# Ejercicio 3
max_precio = max(productos)
indice_max = productos.index(max_precio)
print(f"El producto con mayor ingreso es: {nombres[indice_max]} con un precio de {max_precio}")