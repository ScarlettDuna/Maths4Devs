from functools import reduce 
# Implementa reduce para calcular una serie de Fibonacci de longitud n.
# 1 1 2 3 5 8 13 21 
def fibonacci(n):
    fibo_array = [1]
    for i in range(1, n):
        if i == 1:
            fibo_array.append(i)
        else:
            fibo_array.append(fibo_array[i-2] + fibo_array[i-1])
    return fibo_array
print(fibonacci(9))

def fibo(n):
    return reduce(
        lambda acc, _: (acc.append(acc[-2] + acc[-1]) or acc), range(n - 2), [1, 1])

fibonacci_array = fibo(9)
print(fibonacci_array)
# Usa reduce para generar el número binario correspondiente a una lista de bits ([1,0,1,1] → 11).
def bin2dec(array):
    dec = 0
    for i in range(len(array)):
        dec += pow(array[i] * 2, len(array) - 1 - i) 
    return dec
print(bin2dec([1,0,1,1]))

decimal = reduce(lambda acc, num: acc * 2 + num, [1,0,1,1], 0)
print(decimal)

# Calcula el producto escalar entre dos listas de números.
a = [5, 9, 7, 10]
b = [6, 2, 4, 8]
c = reduce(lambda acc, par: acc + par[0] * par[1], zip(a, b), 0)
print(c)

# Implementa una función que determine si una cadena es un palíndromo usando reduce.

# Escribe una función que calcule la varianza de una lista de números (usa reduce para la suma y la media).

# Implementa reduce para simular el merge sort más simple (solo la fase de fusión).

# Dado un texto, usa reduce para eliminar caracteres duplicados consecutivos (“aaabbc” → “abc”).

# Dado un número entero, calcula la suma de sus factoriales de dígitos (145 → 1! + 4! + 5!).

# Usa reduce para rotar los elementos de una lista n posiciones hacia la derecha.

# Implementa una función que “comprime” listas consecutivas de iguales ([1,1,2,2,3,1,1] → [[1,1],[2,2],[3],[1,1]]).