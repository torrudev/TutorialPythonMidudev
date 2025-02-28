###
# 03 - while
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

print("\nBucle while:")

# Bucle while con una simple condición
print("\nBucle while simple:")
contador = 0

while contador <= 5:
    print(contador)
    contador += 1 # Importante para evitar bucle infinito

# Bucle while con break
print("\nBucle while con break:")
contador = 0

while contador <=100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        print("El número es multiplo de 5")
        break # Rompe el bucle

print("\nBucle while con continue:")
contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue # salta esa iteración y continua el bucle

    print(contador)

print("\nBucle while con else:")
contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

print("\nBucle while con else y break:")
contador = 0

while contador < 3:
    print(contador)
    contador += 1
    break
else: # Interesante cuando quieres asegurarte que ha recorrido todos los casos
    print("El bucle ha terminado") # no se ejecuta porque se ejecuta el break

print("Con break no se ejecuta el else")

# pedirle al usuario un número que tiene que ser positivo
numero = -1

while numero < 0:
    try:
        numero = int(input("Escribe un número positivo:"))
        if numero < 0:
            print("El número debe ser positivo.")
    except: # se ejecuta si el try genera una excepción, como en este caso introducir letras o números decimales
        print("Debes introducir un número entero si no peta")

print(f"El número introducido es: {numero}")