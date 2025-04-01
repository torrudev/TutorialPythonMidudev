from playwright.sync_api import sync_playwright

url = "https://midu.dev"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, slow_mo=2000)  # Cambia a True si no quieres ver el navegador
    pagina = navegador.new_page()
    pagina.goto(url)

    primer_articulo_ancla = pagina.locator('article a').first
    primer_articulo_ancla.click()

    pagina.wait_for_load_state() # Esperar a que la página cargue completamente

    # primera_imagen = pagina.locator('main img').first
    # imagen_src = primera_imagen.get_attribute('src')
    # print(f"La imagen del primer curso es: {imagen_src}")

    contenedor_contenido_curso = pagina.locator('text="Contenido del curso"')
    hermano_contenido_curso = contenedor_contenido_curso.locator('xpath=./div/')

    navegador.close() # Importante cerrar el navegador