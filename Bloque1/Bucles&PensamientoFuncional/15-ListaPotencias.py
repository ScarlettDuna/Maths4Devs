potencias = []
num = 2
potencia = 0
contador = 1
while potencia < 1000:
    potencia= pow(num, contador)
    contador += 1
    potencias.append(potencia)
print(potencias)