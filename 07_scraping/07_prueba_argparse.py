import requests
import argparse
from bs4 import BeautifulSoup

###
# 07 - Prueba web scraping con argparse
# Script para obtener los resultados actuales de dos equipos de la nba desde la terminal y hacer una comparación.
# Para ello vamos necesitar dos argumentos, que seran el nombre de los dos equipos a analizar.
# ###

parser = argparse.ArgumentParser(description="Obtener los datos de clasificación de 2 equipos de la nba  y compararlos") # Crea un analizador de argumentos con una descripción
parser.add_argument('equipo1', type=str, help='Primer equipo de la nba a comparar') # Define un argumento obligatorio llamado equipo1, con una descripción para el comando --help
parser.add_argument('equipo2', type=str, help='Segundo equipo de la nba a comparar') # Define un argumento obligatorio llamado equipo2, con una descripción para el comando --help
args = parser.parse_args() # Lee los argumentos ingresados en la línea de comandos

equipo1 = args.equipo1
equipo2 = args.equipo2

url = "https://www.sportingnews.com/es/nba/clasificacion"
response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa!")
    soup = BeautifulSoup(response.text, 'html.parser')

else:
    print(f"Error en la petición, código de estado: {response.status_code }")