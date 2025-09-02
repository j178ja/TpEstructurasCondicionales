
# ejercicio 10


def main():
    hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
    mes = input("Ingrese el mes (1-12): ").strip()
    dia = input("Ingrese el d�a (1-31): ").strip()

    # Convertir mes y d�a a enteros
    try:
        mes = int(mes)
        dia = int(dia)
    except ValueError:
        print("Mes o d�a no v�lido")
        return

    if hemisferio not in ("N", "S"):
        print("Hemisferio no v�lido")
        return

    # Definir estaci�n seg�n hemisferio
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia < 20)) or (mes == 3 and dia < 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 20) or (mes == 6 and dia < 21) or (mes in [4,5]):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes == 9 and dia < 23) or (mes in [7,8]):
            estacion = "Verano"
        else:
            estacion = "Oto�o"
    else:  # Hemisferio Sur
        if (mes == 6 and dia >= 21) or (mes == 9 and dia < 23) or (mes in [7,8]):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 23) or (mes == 12 and dia < 21) or (mes in [10,11]):
            estacion = "Primavera"
        elif (mes == 12 and dia >= 21) or (mes == 3 and dia < 20) or (mes in [1,2]):
            estacion = "Verano"
        else:
            estacion = "Oto�o"

    print(f"Estaci�n: {estacion}")

if __name__ == "__main__":
    main()

