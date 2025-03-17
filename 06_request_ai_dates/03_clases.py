# 1.Introducción a las clases en Python.
# Las clases son plantillas para crear objetos. Un objeto es una 
# instancia de una clase 
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos).

class Coche:
    # atributo de clase (lo comparten todas las instancias)
    ruedas = 4

    # método especial que es el que construye el objeto
    # se llama automáticamente este método cuando creas la instancia
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó!")

mi_coche = Coche("Ford", "Fiesta", "Granate")
mi_coche.arrancar()
print(mi_coche.ruedas)
print(mi_coche.color)

coche_paco = Coche("Seat", "Ibiza", "Blanco")
coche_paco.arrancar()
print(coche_paco.ruedas)
print(coche_paco.color)

# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública