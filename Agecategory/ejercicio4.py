#Ejercicio 4

# Pedir la edad al usuario
edad = int(input("Ingrese su edad: "))

# Evaluar categor�a
if edad < 12:
    print("Ni�o/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

