"""
Crear una función que dado un número del 1-10 imprima por pantalla todas las tablas de multiplicar del 1 al número recibido.

"""

def impresion_multiplicaciones(num):
    for n in range(1, num+1):
        print(f"\nTabla del {n}:\n")
        for m in range(1, 11):
            print(f"\t{n} x {m} = {n*m}")

numero = int(input("Introduce un número del 1 al 10: "))

impresion_multiplicaciones(numero)