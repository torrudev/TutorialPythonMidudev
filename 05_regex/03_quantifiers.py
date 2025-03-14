###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter
# o grupos de caracteres se deben encontraren una cadena. 
###

import re

# *: Puede aparecer 0 o más veces
texto = "aaaba"
patron = "a*"
encontrado = re.findall(patron, texto)

print(encontrado)

# +: Una a más veces
texto = "dddd aaa ccc aabbbb a casa"
patron = "a+"
encontrado = re.findall(patron, texto)

print(encontrado)

# ?: Cero o una vez
texto = "aaabacb"
patron = r"a?b" # devuelve la b siempre y una única a en caso de encotrarla delante de la b
encontrado = re.findall(patron, texto)

print(encontrado)

# EJERCICIO:
# Haz opcional que aparezca el '+' delante del 34 en el siguiente texto
telefono = "+34 284189586"
patron_tel = r"\+?34 \d{9}"
encontrado_tel = re.findall(patron_tel, telefono)

print(encontrado_tel)

# {n}: Exactamente n ocurrencias
texto = "aaaaaa"
patron = r"a{2}"
coincidencias = re.findall(patron, texto)

print(coincidencias)

# {n, m}: De n a m veces
texto = "u uu uuu u"
patron = r"\w{2,3}"
coincidencias = re.findall(patron, texto)

print(coincidencias)

# EJERCICIO:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
palabras = "ala casa árbol león cinco quinto murcielago"
patron = r"\b\w{4,6}\b"
coincidencias = re.findall(patron, palabras)

print(coincidencias)

# EJERCICIO:
# Encuentra las palabras de más de 6 letras en el siguiente texto
palabras = "ala casa arbolada león cinco quinto murcielago"
patron = r"\b\w{6,}\b"
coincidencias = re.findall(patron, palabras)

print(coincidencias)