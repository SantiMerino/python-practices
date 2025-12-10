# Descripción
# Valida contraseñas según estas reglas:
# • Mínimo 8 caracteres.
# • Contiene al menos un dígito (0–9).
# • No contiene espacios (' ').
# Entrada
# • Primera línea: entero n que representa una cantidad de contraseñas a ingresar.
# • Siguientes n líneas: cada una, una contraseña (cadena de texto).
# Salida
# • Un solo entero: número de contraseñas válidas

def count_valid_passwords(passwords):
 valid_count = 0
 for pwd in passwords:
    if len(pwd) >= 8:
        if any(char.isdigit() for char in pwd):
            if ' ' not in pwd:
                valid_count += 1
            else:
                print("La contraseña contiene espacios")
        else:
            print("La contraseña no contiene dígitos")
    else:
        print("La contraseña no tiene al menos 8 caracteres")
 pass
 return valid_count
if __name__ == "__main__":
 n = int(input("Ingrese la cantidad de contraseñas: ").strip())
 passwords = [input(f"Ingrese la contraseña {_ + 1}: ").rstrip("\n") for _ in range(n)]
 print("La cantidad de contraseñas válidas es: ", count_valid_passwords(passwords))

