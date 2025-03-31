import requests
import argparse # permite manejar argumentos desde la terminal
from bs4 import BeautifulSoup

###
# 04 - Scrip SEO web scraping
# Script para comprobar el SEO de una URL determinada, pensado para ejecutarse desde la terminal.
# Además tiene un argumento llamado help que nos ayuda a entender cómo usar el script.
# Uso de secuencias ANSI para cambiar el color de la salida en la terminal.
# ###

parser = argparse.ArgumentParser(description="Web scraping para comprobar el SEO de una URL determinada") # Crea un analizador de argumentos con una descripción
parser.add_argument('url', type=str, help='La URL del sitio web que quieres analizar') # Define un argumento obligatorio llamado url de tipo str con una descripción
args = parser.parse_args() # Lee los argumentos ingresados en la línea de comandos
url = args.url

headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
    }
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("La petición fue exitosa!")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Utilizar secuencias ANSI para cambiar el color de la salida en la terminal
    print(f"\033[34mRevisando la página: {url}\033[0m") # \33 es el caracter de escape que indica el inicio de una secuencia ANSI, 34 es el código para el color azul
    print("\nSEO básico:")

    titulo_pagina = soup.title.string

    if titulo_pagina:
        print(f"\033[46mEl título de la página es: {titulo_pagina}\033[0m") # no olvidar poner el 0 al final para que no afecte a los siguientes prints
        if len(titulo_pagina) < 70:
            print("\033[32m El título de la página tiene una longitud adecuada\033[0m")
        else:
            print("\033[91mEl título de la página es DEMASIADO largo\033[0m")

# Ejecutar este script desde la terminal.
# Importante activer el entorno virtual (venv) y tener instalado los paquetes necesarios.
# para activarlo ir a la carpeta del proyecto y poner: 
#   .\venv\Scripts\activate
# Luego ejecutar el script con el siguiente comando:
#   python 07_scraping/04_seo_cli.py https://midu.dev/
# Comprobar que hemos añadido mensaje help para el argumento
#   py 04_seo_cli.py --help
# Si no funciona el color en la terminal de Windows, ejecutar el siguiente comando desde el PowerShell o comprobar versiones del Sistema Operativo:
#   reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f