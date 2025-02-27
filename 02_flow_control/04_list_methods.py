###
# 04 - Métodos de listas
# Métodos más importantes para trabajar con listas
###

# Añadir o insertar elementos a la lista
print("\nAñadir o insertar elementos")
lista1 = [1, 2, 3, 4, 5]
lista1.append(6) # Añade un elemento al final
lista1.append('@')
print(lista1)

lista2 = ['a', 'c', 'd', 'e']
lista2.insert(1, 'b') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista2)

lista2.extend(['caminar', 'correr', 'nadar']) # Agrega elementos al final
print(lista2)

# Eliminar elementos de la lista
print("\nEliminar elementos")
lista1.remove('@') # Elimina primera aparición elemento pasado como argumento
print(lista1)

ultimo_eliminado = lista1.pop() # Elimina el último elemento de la lista y además lo devuelve
print(f"Elemento eliminado es : {ultimo_eliminado}")
print(lista1)

segundo_elemento_eliminado = lista1.pop(1) # Eliminar por indice, en este caso 2º elemento
print(f"Eliminar segundo elemento: {segundo_elemento_eliminado}")
print(lista1)

del lista1[-2] # Eliminar a lo bestia, en este caso penúltimo elemento
print(lista1)
lista3 = ['Panda', 'Koala', 'Perro', 'Gato', 'Hamster']
print(lista3)
del lista3[1:3] # del es interesante para eliminar un rango de elementos
print(lista3)

lista1.clear() # Eliminar todos los elemetos
print(lista1)

# Ordenar elementos de la lista
print("\nOrdenar modificando original")
numeros = [48, 78, 2, 73,18]
numeros.sort() # Modifica la lista y la guarda, no la devuelve
# numeros_ordenados = numeros.sort() - esto no funciona
print(numeros)

print("\nOrdenar creando una copia")
numeros = [48, 78, 2, 73,18]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
print(numeros)

print("\nOrdenar cadenas de texto")
print("todo minúsculas")
frutas = ['manzana', 'pera', 'limón', 'platano']
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)

print("mezcla minúsculas y mayúsculas")
frutas = ['Manzana', 'Pera', 'limón', 'platano']
frutas.sort(key=str.lower)
print(frutas)

print("\nCosas útiles")
animales = ['Panda', 'Koala', 'Perro', 'Gato', 'Koala', 'Hamster']
print(len(animales)) # Tamaño de la lista
print(f"Veces aparece 'Koala': {animales.count('Koala')}") # Contar apariciones elemento
print(f"Hay un panda: {'Panda' in animales}") # Comprueba si hay un elemento
print(f"Hay un panda: {'panda' in animales}")