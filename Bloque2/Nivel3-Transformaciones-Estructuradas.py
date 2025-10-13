from functools import reduce
# Convierte una lista de listas en una sola lista (aplana una lista anidada).
numeros = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
    [10]
]
lista_plana = reduce(lambda x, y: x + y, numeros)
print(lista_plana)
""" Para listas muy grandes
from itertools import chain
list(chain.from_iterable(numeros))
"""

# Une un diccionario de pares clave-valor en un solo string "clave=valor;".
pares = {"user": "anchan", "id": 42, "activo": True}
items = list(pares.items())
lista_pares = reduce(lambda acc, kv: acc + f"{kv[0]}={kv[1]};", items, "")
print(lista_pares)
""" Alternativa más compacta:
";".join(f"{k}={v}" for k, v in pares.items()) + ";"
"""

# Convierte una lista de tuplas (clave, valor) en un diccionario.
tuplas = [("nombre", "Anchan"), ("edad", 25), ("activo", True)]
def accumular(acc, pair):
    acc[pair[0]] = pair[1]
    return acc
dict_tuplas = reduce(accumular, tuplas, {})
print(dict_tuplas)

# Crea un string con los elementos de una lista, pero al revés (["a","b","c"] → "cba").
letras = ["a","b","c","d","e"]
string_delreves = ""
for i in letras:
    string_delreves = i + string_delreves
string_delreves2 = reduce(lambda acc, x: x + acc, letras) # opción con reduce()
print(string_delreves)

# Calcula el factorial de un número usando reduce.
n = [n for n in range(1, 6)]
print(list(n))
factorial_n = reduce(lambda acc, num: acc * num, n, 1)
print(factorial_n)

# Crea una lista de factoriales para todos los números del 1 al n (usa map o comprensión junto a reduce).
def crear_lista_factoriales(num):
    nums = [n for n in range(1, num+1)]
    lista_factoriales = []
    for i in range(len(nums)):
        lista_factoriales.append(reduce(lambda acc, f: acc * f, nums[:i+1], 1))
    return lista_factoriales
print(crear_lista_factoriales(6))