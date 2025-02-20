###
# 04 - variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y fuerte
###

# Esto es una variable
mi_nombre = "Jesus"
print(mi_nombre)

# Las variables se pueden reasignar
edad = 22
print(edad)

edad = 25
print(edad)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución,
# no hay que declararlo explicitamente
ejemplo = "hola"
print(type(ejemplo))

ejemplo = 24
print(type(ejemplo))

# Tipado fuerte: no realiza conversiones de tipo automáticas
# print(10 + "2")

# f-string (literal de cadena de formato)
print(f"Hola {mi_nombre}, tengo {edad} años")

# forma no recomendada de asignar variables
ciudad, provincia, comunidad = "Gotor", "Zaragoza", "Aragón"

# convenciones de nombres de variables (snake_case)
nombre_de_la_variable = "correcto"
variable = "correcto"
variable2 = "correcto"

NombreVariable = "no recomendable" #PascalCase
minombrevariable = "no recomendable"

MI_CONSTANTE = 9.81 #UPPER_CASE para constantes, 
# Aunque python como hemos visto permite modificar las,
# Con esta convención sabemos que no deberiamos cambiar la.

# 12_variable = "no funciona"
# otra variable = "no funciona"
# ultima-variable = "no funciona"

# Palabras reservadas
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']