# Descripción
# Dadas dos listas de enteros, imprime la intersección sin duplicados, ordenada de menor a mayor.
# Entrada
# • Primera línea: n (tamaño de la lista A).
# • Segunda línea: n enteros.
# • Tercera línea: m (tamaño de la lista B).
# • Cuarta línea: m enteros.
# Salida
# • Enteros de la intersección sin duplicados, en una sola línea separados por espacio.
# • Si no hay intersección, imprime línea vacía.
def intersection_unique(a, b):
 # Escribe tu codigo aqui
 # Sugerencia
 # Convertir a sets y hacer intersección
 a_set = set(a)
 b_set = set(b)
 intersection = a_set & b_set
 return sorted(list(intersection))
 # Ordenar y devolver lista
 pass
if __name__ == "__main__":
 n = int(input("Ingresa la cantiad de elementos en la lista A: ").strip())
 a = list(map(int, input("Ingresa los elementos de la lista A: ").split()))
 m = int(input("Ingresa la cantidad de elemtnos en la lista B: ").strip())
 b = list(map(int, input("Ingresa los elementos de la lista B: ").split()))
 res = intersection_unique(a, b)
 print(" ".join(map(str, res)))