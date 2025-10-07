# Dada una edad, devuelve una categoría: niño, adolescente, adulto o jubilado.
try: 
    edad = int(input("Introduce una edad para saber a qué parte de la vida pertenece"))
    if edad >= 0 and edad < 13:
        print("niño")
    elif edad > 12 and edad <= 19:
        print("adolescente")
    elif edad > 18 and edad < 65:
        print("Adulto")
    elif edad > 64 and edad <= 110:
        print("Jubilado")
    else:
        print("Número incorrecto")
except ValueError:
    print("Has introducido un valor incorrecto")