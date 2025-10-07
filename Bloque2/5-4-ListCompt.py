# Haz lo mismo que el punto 4 usando comprensión de listas.
numeros_filtrar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros_filtrar if num % 2 == 0]
cuadrados = [num ** 2 for num in numeros_pares]
print(cuadrados)