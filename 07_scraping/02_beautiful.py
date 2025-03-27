from bs4 import BeautifulSoup
import requests

# 1.Ventajas y desventajas de hacer scraping con beautifulsoup
# Ventajas:
# - Extremadamente sencillo de implementar
# - Rápido
# - Fácil encontrar elementos, atributos y filtrar
# Desventajas:
# - No puede saltarse los paywalls ni los captchas
# - No puedes navegar por la web

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa!")

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # tittle_tag = soup.find("title")
    # print(tittle_tag.text)
    tittle_tag = soup.title

    if tittle_tag:
        print(f"El título de la página es: {tittle_tag.text}") # título de la página
        print(f"Etiqueta padre: {tittle_tag.parent.name}") # etiqueta padre del título

# Encontra el precio usando beautifulsoup
# price_span = soup.find("span", class_="rc-prices-fullprice")
# if price_span:
#     print(f"El precio del Macbook Air es: {price_span.text}")

# Encontrar todos los precios
prices_span = soup.find_all("span", class_="rc-prices-fullprice") # span realmente es opcional
if prices_span:
    print("Precios encontrados:")
    for price in prices_span:
        print(f"    -{price.text}")

# Encontrar características y precios de cada producto
productos = soup.find_all("div", class_="rc-productselection-item")

if productos:
    print("\nProductos encontrados:") 
    for producto in productos: # recorrer html cada producto
        caracteristicas = producto.find(class_="list-title").text
        precio = producto.find(class_="rc-prices-fullprice").text
        print(f"{caracteristicas}")

        otras_caracteristicas = producto.find(class_="rc-productbundle-specs")
        list_li = otras_caracteristicas.find_all("li")
        if list_li:
            print("Otras características:")
            for l in list_li:
                print(f"    -{l.text}")
       
        print(f"Precio: {precio}")