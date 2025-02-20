###
# 03 - casting tipos
# Transformar un tipo de valor a otro
###

print("Conversión de tipos:")
print(type("100"))
print(type(int("100")))

print(2 + int("80"))
print(str(2) + "80")

print(type(float("3.14")))
# pierde la parte decimal sin redondear
print(int(3.98))

# Solo 0 será false
print(bool(3))
print(bool(0))
print(bool(-1))

# False cuando la cadena no tiene contenido
print(bool(""))
print(bool(" "))
print(bool("False"))

# No se puede transformar cualquier cosa por ejemplo:
# print(int("Hola"))