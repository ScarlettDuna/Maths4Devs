# Suma solo los números pares de una lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumaPares = 0
for num in numeros:
    if num % 2 == 0:
        sumaPares += num
print(sumaPares)

# suma_pares = sum(n for n in numeros if n % 2 == 0)