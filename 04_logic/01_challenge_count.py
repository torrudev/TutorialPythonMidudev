"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

def comprobar_balance(txt):
    txt_minus = txt.lower()

    contador_r = txt_minus.count("r")
    contador_j = txt_minus.count("j")

    print(f"contador_r: {contador_r} contador_j: {contador_j}")
    
    # if contador_r == contador_j:
    #     return True
    # else:
    #     return False
    
    return contador_r == contador_j

print(comprobar_balance("sadñasCASCAasdas"))
print(comprobar_balance("Jasdasjadsr"))
print(comprobar_balance("dasdjRRasdr"))
print(comprobar_balance("RradfasdrJ ASAJ j"))
