# Escribe una función que calcule la suma de los dígitos de un número entero.
def suma_digitos(num):
    total = 0
    while (num > 0):
        total += (num % 10)
        num //= 10
    return total

print("La suma de los digitos es", suma_digitos(123456))