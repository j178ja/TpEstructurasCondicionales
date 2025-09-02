# ejercicio n°5

def main():
    contrasena = input("Ingrese su contraseña (8 a 14 caracteres): ")

    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

if __name__ == "__main__":
    main()

# ejercicio n°6 no me convence.