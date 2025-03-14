###
# 01 - Expresiones regulares
# Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda. 
# Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc.
###

""" ¿Por que aprender Regex?

- Búsqueda avanzada: Encontrar patrones especísficos en textos grandes de forma rápida y precisa.
(editor de Markdown usando Regex puede ser una buena práctica)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email. teléfono... son correctos

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente.
"""

# 1º Importar módulo
import re

# 2º Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

# 3º El texto donde queremos buscar
text = "Hola mundo"

# 4º Usar la función de búsqueda del módulo 're'
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")

# group() devuelve la cadena que coincide con el patrón
print(result.group())

# start() devolver la posición inicial de la coincidencia
print(result.start())

# end() devolver la posición final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.

texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
patron = "IA"
resultado = re.search(patron,texto)
inicio = resultado.start()
final = resultado.end()

if resultado:
  print(f"He encontrado el patrón en el texto en la posición {inicio} y termina en la posición {final}")
else:
  print("No he encontrado el patrón en el texto")

### Encontrar todas las coincidencias de un patron
# .findall() devuelve una lista con todas las coincidencias

texto_2 = "Estoy aprendiendo Python, me esta encantando usar Python. Python esta por todos lados."
patron_2 = "Python"

coincidencias = re.findall(patron_2, texto_2)
print(f"{patron_2} aparece {len(coincidencias)} veces.")

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

iterador_coincidencias = re.finditer(patron_2, texto_2)

for coincidencia in iterador_coincidencias:
   print(coincidencia.group(), coincidencia.start(), coincidencia.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

patron = "midu"
match = re.findall(patron, text)
iterador = re.finditer(patron, text)

print(f"Veces que aparecer la palabra {patron}: {len(match)}")
for c in iterador:
   print(f"\t- {c.group()} inicio: {c.start()} fin: {c.end()}")

### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado. !ia Ia oh¡"
patron_minus = "ia"
encontrado = re.findall(patron_minus,texto, re.IGNORECASE)

if resultado: print(encontrado)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYThON"
patron = "python"
encontrado_indistinto = re.findall(patron, text, re.IGNORECASE)
iter = re.finditer(patron, text, re.IGNORECASE)

print(f"Veces que aparece la palabra '{patron}': {len(encontrado_indistinto)}")
for i in iter:
   print(f"\t- {i.group()} inicio: {i.start()} fin: {i.end()}")

### Remplazar el texto

# .sub() remplaza todas las coincidencias de un patrón en un texto

txto = "Hola, mundo! Hola de nuevo"
patron = "hola"
remplazo = "Adiós"

nuevo_txto = re.sub(patron, remplazo, txto, count = 0, flags = re.IGNORECASE) # count = numero de veces a remplazar, 0 significa todas. flags para evitar erro al usar IGNORECASE
print(nuevo_txto)