###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

import os
os.system("cls")# Limpiar terminal

print("\nSentencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

edad = 14
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

print("\nSentencia condicional con else")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia condicional con elif")
nota = 7
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("No estas cualificado")

print("\nCondiciones multiples")
edad = 17
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Que alguien llame a la policía")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en Curazao")
else:
    print("Que alguien llame a la policía curazoleña")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("A trabajar entonces")

print("\nAnidar condicionales")
edad = 20
tiene_dinero = False
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa que hay que ahorrar")
else:
    print("No tienes edad para entrar a la discoteca")

# Forma simplificada
# Evitar anidaciones innecesarias
if edad < 18:
    print("No tienes edad para entrar a la discoteca")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quedate en casa que hay que ahorrar")