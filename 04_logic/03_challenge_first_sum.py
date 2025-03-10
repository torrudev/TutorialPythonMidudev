"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. 
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
# 1ª Forma
def find_first_sum(nums, goal):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  
            if nums[i] + nums[j] == goal:
                return [i, j]
            
    return None

# 2ª Forma
def find_first_sum2(nums, objetivo):
    numeros_vistos = {} # diccionario para guardar el número y si índice

    for indice, valor in enumerate(nums): # recorrer lista numeros devolviendo índice y valor
        numero_necesario = objetivo - valor

        if numero_necesario in numeros_vistos: # comprobar si hay alguna clave = número necesario
            return [numeros_vistos[numero_necesario], indice]
        if not(valor in numeros_vistos):
            numeros_vistos[valor] = indice

    return None

nums = [4, 5, 5, 6, 4, 7]
goal = 12

print(f"Resultado: {find_first_sum(nums, goal)}")
print(f"Resultado: {find_first_sum2(nums,goal)}")