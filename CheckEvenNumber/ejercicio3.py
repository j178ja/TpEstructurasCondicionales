# Ejercicio 3:

def main():
    while True:
        try:
            numero = int(input("Ingrese un n�mero par: "))
            
            if numero % 2 == 0:
                print("Ha ingresado un n�mero par")
                break  
            else:
                print("Por favor, ingrese un n�mero par")
        except ValueError:
            print("Ingrese un n�mero v�lido")

if __name__ == "__main__":
    main()

