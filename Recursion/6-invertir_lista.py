def invertir_lista(lista):
    if len(lista) == 1:
        return lista
    else:
        lista_invertida = [lista[-1]] + invertir_lista(lista[:-1])
        return lista_invertida
    
print(invertir_lista([1,2,3,4]))