###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

"""
Definición de una función:

def nombre_ de_la_funcion(parametro1, parametro2, ...):
    #docstring
    #cuerpo de la función
    return valor_de_retorno #opcinal
"""

# Ejemplo de función
def saludar():
    print("¡Hola!")

saludar()
print("")

# Ejemplo de función con parámetros
# El parametro es el valor que la función espera recibir
def saludar_a(nombre):
    print(f"¡Hola {nombre}!")

saludar_a("Midudev") # Midudev sería el argumento, que es el valor que la función recibe
print("")

# Función con más de un parámetro
def sumar(a, b):
    suma = a + b
    return suma

res = sumar(4, 3)
print(res)
print("")

# Documentar las funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve el resultado""" # esta linea aparece en la descripcion de la función
    return a-b

print(restar(3, 4))
print("")

# Función con parámetro por defecto
def cuadrado(a, b = 2):
    return a ** b

print(cuadrado(4))
print(cuadrado(4, 3))
print("")

# Argumentos por clave
def describir_persona(nombre, edad, ciudad):
    print(f"Soy {nombre}, tengo {edad} y vivo en {ciudad}")

# Los parámetros son posicionales
describir_persona("Jesus", 24, "Tamarite")
describir_persona(32, "Magnolia", "Alfajarin")

# Argumentos por clave
describir_persona(ciudad="Madrid", nombre="Isabel", edad="21")
print("")

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7))
print("")

# Argumentos clave_valor variables (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Juan", trabajo="Peletero")
print("")
mostrar_informacion_de(nombre="Maria", licenciada=True, hobbies=["Escalar", "Esquiar", "Programar"])