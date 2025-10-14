from functools import reduce
# Invierte una cadena (sin usar slicing).
super_string = "Supercalifragilisticexpialidocious"
super_array = []
for letter in super_string:
    super_array.append(letter)
print(super_array)
string_delreves2 = reduce(lambda acc, x: x + acc, super_array)
print(string_delreves2)

# Calcula la media ponderada de una lista de notas y pesos.
numeros = [3, 7, 2, 9, 12, 5, 8, 15, 4, 10]
media = reduce(lambda acc, num: acc + num/len(numeros), numeros, 0)
print(media)
notas = [3, 7, 2, 9]
pesos = [1, 2, 3, 4]
media_ponderada = reduce(lambda acc, par: acc + par[0]*par[1], zip(notas, pesos), 0) / sum(pesos)
print("La media ponderada es: ", media_ponderada)

# Implementa all() usando reduce (devuelve True si todos los elementos son verdaderos).
valores = [True, True, False, True]
todos_verdaderos = reduce(lambda acc, x: acc and x, valores)
print(todos_verdaderos)

# Implementa any() usando reduce (devuelve True si alguno es verdadero).
alguno_verdadero = reduce(lambda acc, x: acc or x, valores)
print(alguno_verdadero) 

# Calcula la suma de los dígitos de un número sin convertirlo en string.
figures = 123456789
suma_digitos = 0
while figures > 0:
    suma_digitos += (figures % 10)
    figures //= 10
print(suma_digitos)
suma_digitos2 = reduce(lambda acc, x: acc + x, [int(d) for d in str(num)], 0) # con reduce

# Dada una lista de palabras, agrúpalas por su longitud en un diccionario.
# ["hola","sol","nube","sí"] → {4:["hola","nube"],3:["sol"],2:["sí"]}
palabras = ["hola","sol","nube","si", "nunca", "amaneces"]
def acumulador(acc, palabra):
    longitud = len(palabra)
    if longitud not in acc: acc[longitud] = [palabra]
    else: acc[longitud].append(palabra)
    return acc
palabras_tamano = reduce(acumulador, palabras, {})
print(palabras_tamano)

# Cuenta la frecuencia de letras en una palabra y devuélvela como diccionario.
def acumulador_letras(acc, letra):
    if letra not in acc: acc[letra] = 1
    else: acc[letra] += 1
    return acc
letras_superstring = reduce(acumulador_letras, super_array, {})
print(letras_superstring)

# Fusiona varios diccionarios en uno solo, sumando los valores de las claves repetidas.
lista_dicts = [
    {"a": 2, "b": 3, "c": 1},
    {"a": 5, "c": 4, "d": 2},
    {"b": 7, "d": 3, "e": 6}
]
def acumulador_diccionarios(acc, dic): 
    for key, value in dic.items():
        acc[key] = acc.get(key, 0) + value
    return acc
suma_dicts = reduce(acumulador_diccionarios, lista_dicts, {})

# Simula la multiplicación de matrices 2×2 usando reduce y comprensión de listas.
"""
matriz_a = [[a, b], [c, d]]
matriz_b = [[e, f], [g, h]]
matriz_c = [
    [matriz_a[0][0] * matriz_b[0][0] + matriz_a[0][1] * matriz_b[1][0],
     matriz_a[0][0] * matriz_b[0][1] + matriz_a[0][1] * matriz_b[1][1]],

    [matriz_a[1][0] * matriz_b[0][0] + matriz_a[1][1] * matriz_b[1][0],
     matriz_a[1][0] * matriz_b[0][1] + matriz_a[1][1] * matriz_b[1][1]]
]
"""
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

B_T = list(zip(*B))  # esto convierte columnas en filas para poder recorrerlas fácilmente

C = [
    [reduce(lambda acc, par: acc + par[0]*par[1], zip(filaA, colB), 0)
        for colB in B_T]
    for filaA in A
]

print(C)
