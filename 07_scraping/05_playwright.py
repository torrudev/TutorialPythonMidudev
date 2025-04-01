# 5.Ventajas y desventajas de hacer scraping con playwright
# Ventajas:
# - Simular usuario y navegar la pagina
# - Utilidades como screenshots, grabar videos, etc.
# - Cargar javascript
# - Funciona con SPAs (Single Page Applications)
# Neutro:
# - Más fácil saltarse los paywalls o modales
# Desventajas:
# - Más lento y costoso que beautifulsoup

import re # regular expression
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright")) # to_have_title debería tener un time out de 5 segundos

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click en el link get started.
    page.get_by_role("link", name="Get started").click()

    # Se espera que la página tenga un encabezado con el nombre de Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()