from functools import reduce
from math import prod
# Suma todos los elementos de una lista de números.
listaNumeros = [2, 4, 6, 8, 10, 9, 7]
sumaReduce = reduce(lambda acc, num: acc + num, listaNumeros)
suma = sum(listaNumeros)

print(f"Usando reduce me da: {sumaReduce} y usando suma: {suma}")

# Calcula el producto de todos los números de una lista.
productoReduce = reduce(lambda acc, num: acc * num, listaNumeros)
producto = prod(listaNumeros)
print("El producto usando reduce es: ", producto)

# Concatena todas las palabras de una lista en una sola cadena separada por comas.
palabras = ["código", "python", "lógica", "función", "lista", "cadena", "variable", "bucle"]
palabras_concatenadas = reduce(lambda acc, palabra: acc + " " + palabra, palabras)
# reduce(lambda acc, palabra: acc + ", " + palabra, palabras[1:], palabras[0]) - para evitar el espacio inicial.
print(palabras_concatenadas)

# Encuentra el número máximo en una lista sin usar max().
maximo = reduce(lambda a, b: a if a > b else b, listaNumeros)
print("El número más grande es ", maximo)

# Encuentra el número mínimo en una lista sin usar min().
minimo = reduce(lambda a, b: a if a < b else b, listaNumeros)
print("El número más pequeño es ", minimo)

# Calcula la suma acumulada de una lista (resultado final: un solo número).
acumuladas = reduce(
    lambda acc, x: acc + [acc[-1] + x],
    listaNumeros[1:],
    [listaNumeros[0]]
)
print(acumuladas)

# Calcula la resta acumulada de todos los elementos (de izquierda a derecha).
resta_acumulada = reduce(lambda acc, x: acc - x, listaNumeros)
print(resta_acumulada)

# Convierte una lista de strings en una lista con todos los caracteres concatenados (por ejemplo, ["ab","cd","ef"] → "abcdef").
letras = ["a", "b", "c", "d", "e", "f"]
letrasConcatenadas = reduce(lambda acc, let: acc + let, letras)
print(letrasConcatenadas)