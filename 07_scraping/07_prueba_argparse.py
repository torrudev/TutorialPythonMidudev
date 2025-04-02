import argparse
import re
from playwright.sync_api import sync_playwright

###
# 07 - Prueba web scraping con argparse y playwright
# Script para obtener la clasificacion actual de los equipos de la nba desde la terminal y resaltar los dos equipos pasado como parámetro (con secuencias ANSI).
# Para ello vamos necesitar dos argumentos, que seran el nombre de los dos equipos a analizar.
# Todos los datos se obtendran de la página: https://www.sportingnews.com/es/nba?gr=www
#
# USO:
#   python 07_scraping/07_prueba_argparse.py <equipo1> <equipo2>
# IMPORTANTE:
#   Ejecutar este script desde la terminal y activar el entorno virtual (venv) donde están instalados los paquetes.
# ###

parser = argparse.ArgumentParser(description="Obtener los datos de clasificación de 2 equipos de la nba  y compararlos") # Crea un analizador de argumentos con una descripción
parser.add_argument('equipo1', type=str, help='Primer equipo de la nba a comparar') # Define un argumento obligatorio llamado equipo1, con una descripción para el comando --help
parser.add_argument('equipo2', type=str, help='Segundo equipo de la nba a comparar') # Define un argumento obligatorio llamado equipo2, con una descripción para el comando --help
args = parser.parse_args() # Lee los argumentos ingresados en la línea de comandos

equipo1 = args.equipo1
equipo2 = args.equipo2

with sync_playwright() as p:  # Inicia Playwright
    navegador = p.chromium.launch(headless=False, slow_mo=2000)  # Abre el navegador
    pagina = navegador.new_page()  # Crea una nueva página
    pagina.goto("https://www.sportingnews.com/es/nba/clasificacion")  # Navega a una URL

    print(f"Titulo de la pagina: {pagina.title()}")

    pagina.wait_for_selector("table.sr-us-table__table") # Espera a que la tabla esté disponible en la página

    tablas = pagina.locator("table.sr-us-table__table") # Selecciona las tablas de clasificación de la NBA

    for i in range(tablas.count()): # recorre todas las tablas encontradas
        tabla = tablas.nth(i) # Selecciona la tabla en la posición i
        conferencia = tabla.locator("thead tr td:nth-child(1)").inner_text()
        print(f"\n{conferencia} conference:")

        equipos_conferencia = tabla.locator("tbody tr")
        print("\nP   Equipo                   V  D  Confe Divi  Local Visi")

        for j in range(equipos_conferencia.count()): # recorre todos los equipos de la conferencia encontradas
            equipo = equipos_conferencia.nth(j) # Selecciona el equipo en la posición j

            # datos a mostrar
            posicion = f"{j+1}º"
            nombre = equipo.locator("xpath=.//td[1]/div/div/span[5]/span").inner_text()     # Selecciona el nombre del equipo
            victorias = equipo.locator("td:nth-child(2)").inner_text()                      # Selecciona el número de victorias
            derrotas = equipo.locator("td:nth-child(3)").inner_text()                       # Selecciona el número de derrotas
            resultados_conferencia = equipo.locator("td:nth-child(6)").inner_text()         # Selecciona los resultados en la conferencia  
            resultados_division = equipo.locator("td:nth-child(7)").inner_text()            # Selecciona los resultados en la división
            local = equipo.locator("td:nth-child(8)").inner_text()                          # Selecciona resultados como local
            visitante = equipo.locator("td:nth-child(9)").inner_text()                      # Selecciona resultados como visitante

            #datos estilizados
            posicion_estilizada = posicion.ljust(3)
            nombre_estilizado = nombre.ljust(24)
            victorias_estilizadas = victorias.ljust(2)
            derrotas_estilizadas = derrotas.ljust(2)
            resultados_conferencia_estilizados = resultados_conferencia.ljust(5)
            resultados_division_estilizados = resultados_division.ljust(5)
            local_estilizado = local.ljust(5)
            visitante_estilizado = visitante.ljust(5)

            re.search(equipo1, nombre, re.IGNORECASE)
            if re.search(equipo1, nombre, re.IGNORECASE) or re.search(equipo2, nombre, re.IGNORECASE):
                print(f"\033[30;42m{posicion_estilizada} {nombre_estilizado} {victorias_estilizadas} {derrotas_estilizadas} {resultados_conferencia_estilizados} {resultados_division_estilizados} {local_estilizado} {visitante_estilizado}\033[0m") # Imprime datos del equipo con el fondo amarillo
            else:
                print(f"{posicion_estilizada} {nombre_estilizado} {victorias_estilizadas} {derrotas_estilizadas} {resultados_conferencia_estilizados} {resultados_division_estilizados} {local_estilizado} {visitante_estilizado}") # Imprime datos del equipo

    navegador.close()