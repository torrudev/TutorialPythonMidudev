import requests
import re

# 1.Ventajas y desventajas de hacer scraping con requests
# Ventajas:
# - Sencillo de implementar
# - Muy rapido
# Desventajas:
# - No puede saltarse los paywalls ni los captchas
# - No puedes navegar por la web
# - Muy manual para encontrar lo que te interesa (expresiones regulares)

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print('La petición fue exitosa!')

    html = response.text

    # expresion regular para encotrar el precio
    pattern_price = r'<span class="rc-prices-fullprice">(.*?)</span>'
    match = re.search(pattern_price, html)

    if match:
        print(f'El precio del Macbook Air es: {match.group(1)}')