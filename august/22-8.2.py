
# Ticket de Cine
# Crear un programa para pedir al usuario su nombre, la película que quiere ver, el número de boletos y el precio por boleto. Posteriormente, el programa va a calcular el total y mostrar una factura con todos los datos. Conceptos explorados: input(), operaciones aritméticas, print() con formato.

# Ejemplo de salida del programa:

# Factura de cine:

# -------------------------

# Cliente: Erick Varela

# Película: Oppenheimer

# Boletos: 2

# Total a pagar: $12.00

nombre = input('Ingrese su nombre: ')
pelicula = input('Ingrese la película que desea ver: ')
boletos = int(input('Ingrese el número de boletos: '))
preciob = float(input('Ingrese el precio por boleto: '))
total = boletos * preciob
print('--------------------------------')
print('Factura de cine:')
print('-------------------------')
print(f'Cliente: {nombre}')
print(f'Película: {pelicula}')
print(f'Boletos: {boletos}')
print(f'Total a pagar: ${total:.2f}')
