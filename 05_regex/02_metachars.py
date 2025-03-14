###
# 02 - Metacaracteres
# Los metacaracteres son símbolos con significados específicos en las expresiones regulares.
###

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

texto = "Hola mundo, H0la de nuevo, H€la otra vez"
patron_punto = "H.la"

encontrado = re.findall(patron_punto, texto)

if (encontrado):
    print(encontrado)
else:
    print("No se ha encontrado el patrón.")

# Otro ejemplo

texto_2 = "casa caasa cosa cisa cesa causa"
patron_punto_2 = "c.sa"

encontrado_2 = re.findall(patron_punto_2, texto_2) # el punto solo significa un caracter, por tanto no encuentra caasa y causa

print(encontrado_2)

# Barra invertida para anular el significado especial de un símbolo

texto_3 = "Vivo en Guatemala. Tienes que venir a visitarme."
patron = r"\." # Raw String

encontrado_3 = re.findall(patron, texto_3)

print(encontrado_3)

# \d: Coincide con cualquier dígito (0-9), un solo dígito

texto_tel = "Número de teléfono: 155768173"
encontrado_digitos = re.findall(r"\d\d\d", texto_tel) # divide el número de 3 en tres
print(encontrado_digitos)

# \d{n}: Añadir cuantificador

encontrado_tel = re.findall(r"\d{9}", texto_tel) # encontrar 9 dígitos seguidos
print(encontrado_tel)

# EJERCICIO: 
# Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 685 98 16 32 apúntalo vale?"
pattern = r"\+34 \d{3} \d{2} \d{2} \d{2}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

texto_4 = "@nombre_usuario@"
patron_alfa = r"\w" # no encuentra símbolos como el @
encontrado_alfa = re.findall(patron_alfa, texto_4)
print(encontrado_alfa)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea)

texto_espacios = "Hola mundo\n¿Cómo te va la vida?\t"
patron_espacios = r"\s"
encontrado_espacios = re.findall(patron_espacios, texto_espacios)
print(encontrado_espacios)

# ^: Coincide con el principio de una cadena

texto_5 = "%423_name"
patron_principio = r"^\w" # no podrá no empezar con un caracter alfanumerico
encontrado_principio = re.search(patron_principio, texto_5)

if encontrado_principio: print("Nombre de usuario válido")
else: print("Nombre de usuario no válido")

telefono = "+34 685 98 16 32"
patron_tel = r"^\+\d{1,3} \d{3} \d{2} \d{2} \d{2}"
valido = re.search(patron_tel, telefono)

if valido: print("Número de teléfono válido")
else: print("No existe ese número")

# $: Coincide con el final de una cadena

texto_fin = "Hola mundo"
patron_fin = r"mundo$" # comprobar que termina en mundo
encontrado_fin = re.search(patron_fin, texto_fin)

if encontrado_fin: print("Acaba en mundo")
else: print("No acaba en mundo")

# EJERCICIO
# Valida que un correo sea de gmail

gmail = "tor@gmail.com"
patron_gmail = r"^\w+@gmail.com$" # + significa 1 o más veces
gmail_valido = re.search(patron_gmail, gmail)

if gmail_valido: 
    print("Gmail válido")
else: 
    print("Gmail no válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
patron_txt = r"\b\w+.txt\b"
archivos_txt = re.findall(patron_txt, files)

print(archivos_txt)

# \b: Coincide con el principio o final de una palabra

texto_palabras = "casa casada casado"
patron_palabra = r"\bcasa\b"
encontrado_palabra = re.findall(patron_palabra, texto_palabras)

print(encontrado_palabra)

# |: Coincidir con una opción u otra

texto_or = "platano, palta, aguacate, manzana, aguacate, pera, palta"
patron_or = r"palta|aguacate|p..a"
aguacate_encontrado = re.findall(patron_or, texto_or)

print(aguacate_encontrado)