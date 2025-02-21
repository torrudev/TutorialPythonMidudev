###
# 05 - input()
# Entrada de usuario - Versión simplificada
# Permite obtener datos del usuario a través de la consola
###

nombre = input("Hola, ¿cómo te llamas?\n")

print(f"Hola {nombre}, encantado de conocerte")

edad = input("¿Cuántos años tienes?\n")# Siempre va a ser una cadena lo que introduce el usuario
print(type(edad))
print(f"Dentro de 10 años tendras {int(edad) + 10} años")

pais, ciudad = input("¿En que país y ciudad vives?\n").split()
print(f"Resides en {pais}, {ciudad}")