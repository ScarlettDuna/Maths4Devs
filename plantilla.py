# ===============================
# 🔁 Plantilla base para ejercicios con reduce + lambda
# ===============================

from functools import reduce

def run_exercise(description, data, operation):
    """Ejecuta una operación con reduce y muestra el resultado."""
    print(f"\n🧩 {description}")
    print(f"Datos: {data}")
    result = reduce(operation, data)
    print(f"Resultado: {result}")

# ===============================
# 💡 Aquí defines tu ejercicio
# ===============================

# Ejemplo 1: Suma de todos los números
numeros = [1, 2, 3, 4, 5]

run_exercise(
    "Suma de todos los números",
    numeros,
    lambda acc, x: acc + x
)

# Ejemplo 2: Producto de todos los números
run_exercise(
    "Producto de todos los números",
    numeros,
    lambda acc, x: acc * x
)

# Ejemplo 3: Concatenar palabras
palabras = ["Python", "es", "increíble"]
run_exercise(
    "Concatenar palabras en una frase",
    palabras,
    lambda acc, x: acc + " " + x
)

# ===============================
# ✅ Añade aquí tus propios ejercicios
# (usa una variable de datos y una lambda diferente)
# ===============================

