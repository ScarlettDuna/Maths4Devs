# Combina map + filter para quedarte solo con los cuadrados de los números pares.

numeros_filtrar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x % 2 == 0, numeros_filtrar)

cuadrados = map(lambda x: x ** 2, numeros_pares)
for num in cuadrados:
    print(num)