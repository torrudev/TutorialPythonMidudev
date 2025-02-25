###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEjercicio 1:")
num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))

if num1 < num2:
    print(f"{num2} es mayor que {num1}")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1} es igual que {num2}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEjercicio 2:")
numero1 = int(input("Introduce un número:"))
numero2 = int(input("Introduce otro número:"))
operacion = input("Introduce una operación (+, -, *, /)")

if operacion == "+":
    res = numero1 + numero2
elif operacion =="-":
    res = numero1 - numero2
elif operacion =="*":
    res = numero1 * numero2
elif operacion =="/":
    if numero2 == 0:
        print("Error: no se puede dividir por cero")
    else:
        res = numero1 / numero2
else:
    res = "No se reconoce la operación"

if 'res' in locals():# Comprueba si la variable resultado existe.
    print(f"El resultado es {res}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio 3:")
anio = int(input("Introduce un año:"))
if anio % 400==0 or (anio % 4==0 and anio % 100!=0):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4:")
edad = int(input("Introduce una edad:"))

if edad >= 65:
    print(f"Tiene {edad} años por tanto es un adulto mayor")
elif edad >= 18:
    print(f"Tiene {edad} años por tanto es un adulto")
elif edad >= 13:
    print(f"Tiene {edad} años por tanto es un adolescente")
elif edad >= 3:
    print(f"Tiene {edad} años por tanto es un niño")
elif edad >= 0:
    print(f"Tiene {edad} años por tanto es un bebe")
else:
    print("Edad no valida")