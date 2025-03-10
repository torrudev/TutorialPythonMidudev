###
# 04 - dictionaries()
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados
###

# ejemplo
persona = {
    "nombre": "jesus",
    "edad": 25,
    "es_estudiante": False,
    "titulos": ["DAM","DAW"],
    "redes":{
        "twitter":"@jesust",
        "instagram":"@tjesus"
    }
}

# para acceder a los valores
print(persona["nombre"])
print(persona["titulos"][1])
print(persona["redes"]["instagram"])

# cambiar valores al acceder
persona["nombre"] = "jesusDEV"
persona["titulos"][1] = "óptica"

# eliminar completamente una propiedad
del persona["edad"]
print(persona)

# eliminar propiedad recuperando el dato eliminado
es_estudiante = persona.pop("es_estudiante") # no hace falta asignar a variable
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"nombre" : "Juan", "edad" : 36}
b = {"nombre" : "Elisa", "es_estudiante" : False}

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in persona)
print("nombre" in persona)

# obtener todas las claves
print("\nClaves:")
print(persona.keys())

# obtener todos los valores
print("\nValores:")
print(persona.values())

# obtener tanto claves como valores
print("\nItems:")
print(persona.items())

for k, v in persona.items():
    print(f"{k}: {v}")