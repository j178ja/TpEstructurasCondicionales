# ejercicion�7 y 8

def main():
    frase = input("Ingrese una frase o palabra: ").strip()  # Quita espacios al inicio y fin
    
    if frase and frase[-1].lower() in "aeiou":  # Verifica �ltima letra
        frase += "!"
    
    print(frase)




    print("Opciones:")
    print("1 - May�sculas")
    print("2 - Min�sculas")
    print("3 - Primera letra may�scula")
    
    opcion = input("Seleccione una opci�n (1, 2 o 3): ").strip()
    
    if opcion == "1":
        resultado = frase.upper()
    elif opcion == "2":
        resultado = frase.lower()
    elif opcion == "3":
        resultado = frase.title()
    else:
        resultado = "Opci�n no v�lida"
    
    print(resultado)

if __name__ == "__main__":
    main()
