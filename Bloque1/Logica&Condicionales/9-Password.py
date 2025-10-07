# Crea una función que determine si una contraseña es “fuerte” (mínimo 8 caracteres, incluye mayúscula, número y símbolo).

def pass_checker(password):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    caracteres_especiales = "!@#$%^&*()_+-=[]|',.<>?/`~"

    # Boleanos de prueba
    tieneMayus = False
    tieneMinus = False
    tieneNum = False
    tieneChar = False

    for letter in password:
        if letter in mayusculas: 
            tieneMayus = True
        if letter in minusculas:
            tieneMinus = True
        if letter in numeros:
            tieneNum = True
        if letter in caracteres_especiales:
            tieneChar = True
    if tieneMayus and tieneMinus and tieneNum and tieneChar:
        return "Tu contraseña es SUPER SEGURA"
    else:
        return "Tienes que mejorar tu contaseña"
    
print(pass_checker("Anchan2025&"))


""" Corrección de ChatGPT
import string

def pass_checker(password):
    if len(password) < 8:
        return "Demasiado corta"
    tieneMayus = any(ch.isupper() for ch in password)
    tieneMinus = any(ch.islower() for ch in password)
    tieneNum = any(ch.isdigit() for ch in password)
    tieneChar = any(ch in string.punctuation for ch in password)
    return "SUPER SEGURA" if all([tieneMayus, tieneMinus, tieneNum, tieneChar]) else "Mejora tu contraseña"

"""