def cel_2_fahr(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return round(fahrenheit, 1)

celsius_temperaturas = [0.0, 10.5, 22.0, 35.5, -5.0, 15.0]
fahrenheit_temperaturas = list(map(cel_2_fahr, celsius_temperaturas))

print(fahrenheit_temperaturas)