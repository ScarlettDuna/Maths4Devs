def aplanar_lista(lista):
    if not lista:
        return lista
    else:
        cabeza = lista[0]
        cola = lista[1:]
        print("cabeza: ", cabeza)
        print("cola: ", cola)
        if isinstance(cabeza, list):
            return aplanar_lista(cabeza) + aplanar_lista(cola)
        else:
            return [cabeza] + aplanar_lista(cola)

print(aplanar_lista([1, [2, [3, 4], 5]])) 