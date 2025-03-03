###
# 03 - for
# Permite ejecutar un bloque de código repetidamente mientras itera un iterable o lista
###

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas: #recorre la lista
    print(fruta)

# Iterar sobre cualquier cosa iterable
cadena = "midudev"
for caracter in cadena:
    print(caracter)

# enumerate()
for indice, fruta in enumerate(frutas): # enumerate devuelve primero el indice y segundo el valor
    print(f"La fruta {fruta} se encuentra en el índice: {indice}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras: # recorre las letras
    for numero in numeros: # para cada letra recorre todos los números
        print(f"{letra}{numero}")

# break
print("\nBreak:")

animales = ["perro", "gato", "loro", "canario", "pez", "caballo", "cocodrilo"]
for indice, animal in enumerate(animales):
    print(animal)
    if animal == "canario":
        print(f"El {animal} esta escondido en el indice: {indice}")
        break # Terminar bucle, por tanto no printa el resto de animales

# continue
print("\nContinue:")

animales = ["perro", "gato", "loro", "canario", "pez", "caballo", "cocodrilo"]
for animal in animales:
    if animal == "canario":
        continue # Saltar a la siguiente iteración, por tanto no printa el canario
    print(animal)

# continue en una sola linea, también funciona con el break
for animal in animales:
    if animal == "canario":continue
    print(animal)

# Comprensión de listas (list comprehension)
print("\nList comprehension:")
animales_mayus = [a.upper() for a in animales]
print(animales_mayus)

# Muestra los números pares de una lista
lista_numeros = [1, 2, 3, 4, 8, 2, 3, 7]
pares = [n for n in lista_numeros if n % 2 == 0]
print(pares)