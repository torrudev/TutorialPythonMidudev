"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, 
la suma de todos los números pares en la lista).
"""

def es_par(n):
    return n % 2 == 0

def suma_huevos_carnivoros(lista) -> int: # para indicar que devuelve un entero en la documentación
    """
    Esta función recibe un lista de numeros enteros y suma los números pares. Devuelve la suma de todos los pares.
    """
    total = 0

    for c in lista:
        if es_par(c):
            total += c

    return total

huevos = [2, 4, 3, 1, 2, 6, 8, 7]
print(suma_huevos_carnivoros(huevos))
huevos2 = [3, 4, 7, 5, 8]
print(suma_huevos_carnivoros(huevos2))