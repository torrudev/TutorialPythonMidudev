from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def scrape_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("La petición fue exitosa!")

        soup = BeautifulSoup(response.text, "html.parser")

        # Extraer todos los títulos <h1>
        titulos = [titulo.text for titulo in soup.find_all("h2")]
        print(titulos)

        # Extraer todos los enlaces <a>
        enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all("a")]
        # print(enlaces)

        # Extraer texto elemento main
        # texto_main = soup.find("main").text
        # print(texto_main)

        # Extraer del id "mw-content-text" el texto
        content_text = soup.find("div", {'id': 'mw-content-text'}).get_text()
        print(content_text)

scrape_url('https://es.wikipedia.org/wiki/Web_scraping')

def og_image_midu(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("La petición fue exitosa!")

        soup = BeautifulSoup(response.text, "html.parser")

        # extrar el open graph si existe
        og_image = soup.find('meta', property='og:image')
        if og_image:
            print(og_image['content'])
        else:
            print('No se encontró la imagen')

og_image_midu('https://midu.dev/')