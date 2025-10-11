from functools import reduce
# Suma solo los números pares de una lista.
numeros = [3, 7, 2, 9, 12, 5, 8, 15, 4, 10]
suma_pares = reduce(lambda acc, num: acc + (num if num % 2 == 0 else 0), numeros, 0)
# otra opción - reduce(lambda acc, num: acc + num, filter(lambda x: x % 2 == 0, numeros), 0)
print(suma_pares)

# Multiplica solo los números impares.
multiplicacion_impares = reduce(lambda acc, num: acc * (num if num % 2 != 0 else 1), numeros, 1)
print(multiplicacion_impares)

# Suma los números positivos y negativos por separado, devolviendo un diccionario:
# {"positivos": suma_pos, "negativos": suma_neg}
numeros2 = [3, -7, 2, -9, 12, -5, 8, -15, 4, -10]
def acumular(acc, num):
    if num >= 0:
        acc["positivos"] += num
    else:
        acc["negativos"] += num
    return acc
suma_positivos_negativos = reduce(acumular, numeros2, {"positivos": 0, "negativos": 0})
print(suma_positivos_negativos)

# Cuenta cuántos números son mayores que 10.
mayores_10 = reduce(lambda acc, num: acc + (1 if num > 10 else 0), numeros, 0)
print(f"En la lista{numeros} hay {mayores_10} números mayores de 10")

# Cuenta cuántos nombres de una lista empiezan con vocal.
nombres = ["Ana", "Bruno", "Camila", "Diego", "Elena", "Fernando", "Gaby", "Héctor", "Isabel", "Jorge"]
def empVocal(acc, nombre):
    vocales = ["a", "e", "i", "o", "u"]
    if nombre[0].lower() in vocales:
        acc += 1
    return acc
empiezan_vocal = reduce(empVocal, nombres, 0)
print(f"En la lista {nombres} hay {empiezan_vocal} nombres que empiezan por vocal")

# Suma los cuadrados de los números impares.
suma_cuadrados = reduce(lambda acc, num: acc + (num ** 2 if num % 2 != 0 else 0), numeros, 0)
print(suma_cuadrados)

# Calcula el promedio (media aritmética) de una lista de números.
# (Pista: necesitarás usar tu propio contador dentro del acumulador, por ejemplo una tupla (suma, cantidad))
media = reduce(lambda acc, num: acc + num/len(numeros), numeros, 0)
media2 = sum(numeros) / len(numeros)
print(f"La media usando reduce {media}, la media 'tradicional' {media2}")
""" Opción más explícita:
suma_y_conteo = reduce(lambda acc, num: (acc[0] + num, acc[1] + 1), numeros, (0, 0))
media = suma_y_conteo[0] / suma_y_conteo[1]

"""