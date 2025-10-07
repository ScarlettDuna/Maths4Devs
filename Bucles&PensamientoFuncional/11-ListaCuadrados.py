# Genera una lista con los cuadrados de los números del 1 al 20 sin usar for explícito.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = [num ** 2 for num in numeros]
print(cuadrados)