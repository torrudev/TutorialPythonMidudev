###
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre = "Pepe"
ciudad = "Benalmadena"

print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"{a} es de tipo: {type(a)}")
print(f"{b} es de tipo: {type(b)}")
print(f"{c} es de tipo: {type(c)}")
print(f"{d} es de tipo: {type(d)}")
print(f"{e} es de tipo: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
print(f"Transformando {cadena} a tipo int...")
numero_entero = int(cadena)
print(f"Transformando {numero_entero} a tipo float...")
numero_decimal = float(numero_entero)
print(f"Resultado final: {numero_decimal}")

num = 3.99
print(f"Pasar {num} a entero: {int(num)}")# Se trunca

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

mi_nombre = "Rocio"
edad = 25
altura = 1.72

print(f"Hola! Me llamo {mi_nombre} y tengo {edad} años, mido {altura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.1415) / 2)
print("Valor de PI (aproximado):", 3.1415)
print("PI redondeado:", round(3.1415))
print("División entera de PI redondeado entre 2:", resultado)