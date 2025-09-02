# Ejercicio 3:

def main():
    while True:
        try:
            numero = int(input("Ingrese un número par: "))
            
            if numero % 2 == 0:
                print("Ha ingresado un número par")
                break  
            else:
                print("Por favor, ingrese un número par")
        except ValueError:
            print("Ingrese un número válido")

if __name__ == "__main__":
    main()

