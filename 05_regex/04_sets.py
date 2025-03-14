import re

# []: Coincide con cualquier caracter dentro de los corchetes

usuario = "rub.$ius_19+"
patron = r"^[\w.%+-]+$" 
coincidencia = re.search(patron, usuario)

if coincidencia: 
    print("El nombre de usuario es válido: ", coincidencia.group())
else: 
    print("Nombre de usuario no válido")  

# Buscar todas las vocales de un frase
frase = "Hola mundo, aereo"
patron1 = r"[aeiou]"
patron2 = r"[aeiou]+"
coincidencia1 = re.findall(patron1, frase)
coincidencia2 = re.findall(patron2, frase)
print(coincidencia1)
print(coincidencia2)

# Una Regex para encontrar las palabras man fan y ban
texto = "Este man es fan de un tal ban famoso por sus bufandas"
patron = r"\b[mfb]an\b"
coincidencia = re.findall(patron, texto)
print(coincidencia)

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
frase = "Hola mundo, aereo"
patron = r"[^aeiou, ]+"
matches = re.findall(patron, frase)
print(matches)