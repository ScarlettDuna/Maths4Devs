# Usa filter para obtener solo los números primos de una lista.
numeros = [2, 7, 10, 13, 15, 29, 36, 41]
def esPrimo(num):
    if num == 1: False
    if num == 2 or num == 3: True
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True
primos = filter(esPrimo, numeros)
for num in primos:
    print(num)