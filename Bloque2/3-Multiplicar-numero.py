# Usa reduce para multiplicar todos los elementos de una lista.
from functools import reduce

numeros = [2, 7, 10, 13, 15, 9]

def multiplicar(num1, num2):
    return num1 * num2

producto = reduce(multiplicar, numeros)
# producto = reduce(lambda a, b: a * b, numeros)
print(producto)