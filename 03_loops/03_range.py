###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nRange():")

nums = range(5) # IMPORTANTE: no crea una lista
lista = [0, 1, 2, 3, 4, 5]

print(type(nums))
print(nums) # Más óptimo que una lista ya que crea los números bajo demanda, no crea una lista en memoria
print(type(lista))

#secuencia del 0 al 9
for i in range(10):
    print(i)

# range(inicio, fin)
for n in range(-2, 3):
    print(n)

# range(inicio, fin, paso)
for p in range(2, 11, 2):
    print(p)

print("\nCrear lista con range():")
numeros = range(10)
lista_numeros = list(numeros)
print(lista_numeros)

print("\nHacer repetidamente algo con range():")
contador = 0
while contador < 5:
    print("Imprimir cinco veces")
    contador += 1
print("\n")

for _ in range(5): # _ se usa por convención para indicar que no quieres usar esa variable
    print("Imprimir cinco veces")