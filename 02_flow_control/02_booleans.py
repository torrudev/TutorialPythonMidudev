###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

import os
os.system("cls")# Limpiar terminal

# Los booleanes representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano
print("\nOperadores de comparación:")
print("5 > 3", 5 > 3)       #True
print("5 < 3", 5 < 3)       #False
print("5 == 5", 5 == 5)     #True (igualdad)
print("5 != 3", 5 != 3)     #True (desigualdad)
print("5 >= 5", 5 >= 5)     #True (mayor o igual)
print("5 <= 3", 5 <= 3)     #False (menor o igual)

# Comparación de cadena: mira el orden alfabético y discrimina entre mayúsculas o minúsculas
print("\nComparación de cadenas:")                  
print("'manzana' < 'pera':", "manzana" < "pera")    # True
print("'Hola' == 'hola':", "Hola" == "hola")        # False
print("'Hola' < 'hola':", "Hola" < "hola")          # True

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)      # True
print("True and False:", True and False)    # False
print("True or False:", True or False)      # True
print("False or False:", False or False)    # False
print("not True:", not True)                # False
print("not False:", not False)              # True

# Tablas de la verdad
print("\nTablas de la verdad:")
print("\n and:")
print("A      B     A and   B")
print("True   True ", True and True)
print("True   False", True and False)
print("False  True ", False and True)
print("False  False", False and False)

print("\n or:")
print("A      B     A or   B")
print("True   True ", True or True)
print("True   False", True or False)
print("False  True ", False or True)
print("False  False", False or False)