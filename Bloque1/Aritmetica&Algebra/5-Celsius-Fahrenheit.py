# Convierte grados Celsius a Fahrenheit y viceversa.
def cel_2_fahr(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return round(fahrenheit, 1)

def fahr_2_cel(fahrenheit):
    celsius = (fahrenheit / 1.8) - 32
    return round(celsius, 1)

print(cel_2_fahr(30))
print(fahr_2_cel(100))