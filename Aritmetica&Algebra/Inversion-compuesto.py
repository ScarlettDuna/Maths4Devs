# Escribe una función que calcule el valor final de una inversión con interés compuesto.
# Parametros: valor inicial, tasa de interés anual (en porcentaje), número de años.
def inversion_compuesta(V_inicial, interes_anual, anios):
    V_final = V_inicial
    for i in range(anios):
        V_final *= (1 + (interes_anual/100))
    return V_final

print(inversion_compuesta(500, 2.5, 3))