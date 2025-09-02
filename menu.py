

import subprocess

def ejecutar_ejercicio(script_path, *args):
    comando = ["python", script_path] + list(args)
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(resultado.stdout)

def menu():
    while True:
        print("Seleccione un ejercicio:")
        print("1. Mayor - menor de edad")
        print("2. Aprobado - Desaprobado")
        print("3. Par - Impar")
        print("4. Categoria edad")
        print("5. Contrasena")
        print("6. Media -Mediana - Modal")
        print("7. Frase")
        print("8. Convertir Texto")
        print("9. Terremoto")
        print("10. Hemisferio")
        print("0. Salir")
        opcion = input("> ")

        if opcion == "1":
            edad = input("Ingrese su edad: ")
            ejecutar_ejercicio("AgeVerification/ejercicio1.py", edad)
        elif opcion == "2":
            nota = input("Ingrese su calificacion: ")
            ejecutar_ejercicio("GradeChecker/ejercicio2.py",nota)
        elif opcion == "3":
            ejecutar_ejercicio("CheckEvenNumber/ejercicio3.py")
        elif opcion == "4":
            ejecutar_ejercicio("AgeCategory/ejercicio4.py")
        elif opcion == "5":
            ejecutar_ejercicio("PasswordVerifier/ejercicio5_6.py")
        elif opcion == "6":
            ejecutar_ejercicio("PasswordVerifier/ejercicio5_6.py")
        elif opcion == "7":
            ejecutar_ejercicio("Strings/ejercicio7_8.py")
        elif opcion == "8":
            ejecutar_ejercicio("Strings/ejercicio7_8.py")
        elif opcion == "9":
            ejecutar_ejercicio("EartquakeRanking/ejercicio9.py")
        elif opcion == "10":
            ejecutar_ejercicio("TimeOfTheYear/ejercicio10.py")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()

