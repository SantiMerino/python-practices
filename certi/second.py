
# Descripción
# Dada una lista de nombres en texto libre, normaliza cada nombre con el formato Título (primera letra de
# cada palabra en mayúscula y el resto en minúscula), eliminando espacios extra.
# Entrada
# • Primera línea: entero n.
# • Siguientes n líneas: cada una un nombre (puede tener espacios múltiples).
# Salida
# • n líneas: cada nombre normalizado

def normalize_name(name):
    # Title es la función  que convierte la primera letra de cada palabra en mayúscula y el resto en minúscula
    # Strip es la función que eliminar los espacios extra
    return name.title().strip()


if __name__ == "__main__":
 n = int(input("Ingrese la cantidad de nombres: ").strip())
 for _ in range(n):
  name = input(f"Ingrese el nombre {_ + 1}: ").rstrip("\n")
  print(normalize_name(name))