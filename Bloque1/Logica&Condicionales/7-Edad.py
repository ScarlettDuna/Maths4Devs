# Dada una edad, devuelve una categoría: niño, adolescente, adulto o jubilado.
try: 
    edad = int(input("Introduce una edad para saber a qué parte de la vida pertenece"))
    if edad < 0 or edad > 110:
        print("Número incorrecto")
    elif edad < 13:
        print("niño")
    elif edad < 20:
        print("adolescente")
    elif edad < 65:
        print("Adulto")
    else:
        print("Jubilado")
except ValueError:
    print("Has introducido un valor incorrecto")