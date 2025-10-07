# Usa filter para obtener solo los números primos de una lista.
numeros = [2, 7, 10, 13, 15, 29, 36, 41]
def esPrimo(num):
    if num < 2: False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True
primos = list(filter(esPrimo, numeros))
print(primos)