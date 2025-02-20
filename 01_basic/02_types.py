###
# 02 - types()
# Tipos de datos en python:
# int, float, complex, str, bool, NoneType, list, tuple, dict, set, range...
###

print("int:")
print(10, type(10))
print(0, type(0))
print(-2, type(-2))

print("float:")
print(3.14, type(3.14))
print(-2.07, type(-2.07))
print(1e4, type(1e4))

print("complex:")
print(1 + 2j, type(1 + 2j))

print("str:")
print("cadena", type("cadena"))
print("", type(""))
print("123", type("123"))
print("""multilinea""", type("""multilinea"""))

print("bool:")
print(True, type(True))
print(False, type(False))
print(1 < 2, type(1 < 2))

print("NoneType:")
print(None, type(None))