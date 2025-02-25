###
# 03 - listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

# Creación listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzanas", "peras", "plátanos"]
lista3 = [1, "hola", 2.17, True]

lista_vacia = []
lista_de_listas = [[2, 4], [6, 8], ["accede a este elemento", 7]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

# Acceso elementos por índice
print("\nAcceso elementos por índice")
print(lista2[0])    # 1ª posición, manzanas
print(lista2[1])    # 2ª posición, peras
print(lista2[-1])   # última posición, plátanos
print(lista2[-2])   # 2ª desde el final, peras

print(lista_de_listas[2][0]) # tercer elemento 1ª lista, primero de esa nueva lista

# Slicing de listas
lista = [1, 2, 3, 4, 5]

# [desde : hasta]
print(lista[1:4])   # [2, 3, 4]
print(lista[:3])    # [1, 2, 3]
print(lista[3:])    # [4, 5]
print(lista[:])     # para hacer copias

# [desde : hasta : paso] por defecto [inicio:final:1]
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista4[::2])  # devolver índices pares
print(lista4[::-1]) # devolver índices inversos

# Modificar una lista
print("\nModificar una lista")
lista4[0] = 22
print(lista4)

# Añadir elementos a una lista
print("\nAñadir elementos")
lista = [1, 2, 3, 4, 5]

# forma larga y menos eficiente
lista = lista + [6, 7]
print(lista)

# forma corta y más eficiente
lista += [8, 9]
print(lista)

# recuperar longitud lista
print(f"Longitud de la lista: {len(lista)}")