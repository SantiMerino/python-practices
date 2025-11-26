# Test de programación.
# Estás ayudando a un equipo a validar contraseñas creadas por usuarios. Una contraseña se considera válida si cumple todas estas reglas:

# 1.    Tiene al menos 8 caracteres.
# 2.    Contiene al menos un dígito (0–9).
# 3.    No contiene espacios en blanco (' ').

# Tu tarea: Dado un conjunto de contraseñas, debes contar cuántas de ellas son válidas.
# Entrada: La entrada se proporciona desde stdin con el siguiente formato:
# •    La primera línea contiene un entero n — el número de contraseñas.
# •    Las siguientes n líneas contienen, cada una, una contraseña (cadena de texto).
# Salida: Imprime un solo entero:
# •    El número de contraseñas válidas.

# Contraseñas válidas:
# •    segura123 → longitud ≥ 8, tiene dígitos, sin espacios.
# •    12345678 → longitud 8, tiene dígitos, sin espacios.
# •    Clave2025 → longitud ≥ 8, tiene dígitos, sin espacios.
# No válidas:
# •    abc123 → longitud < 8.
# •    pass word1 → contiene un espacio.


def count_valid_passwords(passwords):
    valid_count = 0
    for pwd in passwords:
        # Completa la lógica aquí
        pass
    return valid_count


if __name__ == "__main__":
    n = int(input().strip())
    passwords = [input().rstrip("\n") for _ in range(n)]
    print(count_valid_passwords(passwords))
    
#     Tienes un listado de movimientos de inventario. Cada línea indica un producto y una cantidad (positiva o negativa). Tu objetivo es calcular el stock total por producto.

# Tu tarea: Dado un conjunto de movimientos:

# Sumar las cantidades por cada producto.
# Mostrar el resultado ordenado alfabéticamente por nombre de producto.
# Si algún producto termina con cantidad total 0, también debe mostrarse (no se filtra).
# Entrada

# La entrada se proporciona desde stdin con el siguiente formato:
# La primera línea contiene un entero n — el número de movimientos.
# Las siguientes n líneas contienen, cada una:
# Un nombre de producto (cadena sin espacios)
# Un entero q (puede ser negativo)
# Separados por un espacio.
# Salida: Debes imprimir una línea por cada producto, en este formato:

# Producto total
# Ordenados por producto en orden lexicográfico (a–z).

# Explicación
# mouse: 5 - 2 + 4 = 7
# teclado: 3
# monitor: 2 + 1 = 3

# Ordenados alfabéticamente: monitor, mouse, teclado.

# Esqueleto de función sugerido


def aggregate_inventory(movements):
    totals = {}
    for product, qty in movements:
        # Completa la lógica aquí
        pass

    # Construir una lista ordenada de tuplas (producto, total)
    result = []
    for product in sorted(totals.keys()):
        result.append((product, totals[product]))
    return result


if __name__ == "__main__":
    n = int(input().strip())
    movements = []
    for _ in range(n):
        line = input().split()
        product = line[0]
        qty = int(line[1])
        movements.append((product, qty))

    aggregated = aggregate_inventory(movements)
    for product, total in aggregated:
        print(product, total)