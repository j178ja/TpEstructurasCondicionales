# ejercicio 9

def main():
    try:
        magnitud = float(input("Ingrese la magnitud del terremoto: "))
    except ValueError:
        print("Valor no v�lido")
        return

    if magnitud < 3:
        clasificacion = "Muy leve (imperceptible)"
    elif 3 <= magnitud < 4:
        clasificacion = "Leve (ligeramente perceptible)"
    elif 4 <= magnitud < 5:
        clasificacion = "Moderado (sentido por personas, pero generalmente no causa da�os)"
    elif 5 <= magnitud < 6:
        clasificacion = "Fuerte (puede causar da�os en estructuras d�biles)"
    elif 6 <= magnitud < 7:
        clasificacion = "Muy Fuerte (puede causar da�os significativos)"
    else:
        clasificacion = "Extremo (puede causar graves da�os a gran escala)"

    print(f"Clasificaci�n: {clasificacion}")

if __name__ == "__main__":
    main()

