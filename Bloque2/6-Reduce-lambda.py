from functools import reduce
# Ejercicio 1 — Multiplicar todos los elementos
numeros = [2, 4, 6, 8]
producto = reduce(lambda a, b: a * b, numeros)
print(producto)

# Ejercicio 2 — Sumar solo los pares
numeros = [1, 2, 3, 4, 5, 6]
suma_pares = reduce(lambda acc, x: acc + x if x % 2 == 0 else acc, numeros, 0)
print(suma_pares)

# Ejercicio 3 — Concatenar palabras
palabras = ["Python", "es", "potente", "y", "elegante"]
frase = reduce(lambda acc, w: acc + " " + w, palabras)
print(frase)

# Ejercicio 4 — Encontrar el máximo
numeros = [3, 41, 12, 9, 27]
mayor = reduce(lambda a, b: a if a > b else b, numeros)
print(mayor)

# Ejercicio 5 — Transformación + acumulación combinada
# Eleva al cuadrado cada número y acumula solo los impares:
numeros = [1, 2, 3, 4, 5, 6]
suma_impares_cuadrados = reduce(
    lambda acc, x: acc + (x**2 if x % 2 != 0 else 0),
    numeros,
    0
)
print(suma_impares_cuadrados)

