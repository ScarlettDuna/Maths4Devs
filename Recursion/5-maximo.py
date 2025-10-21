def maximo(array):
    if len(array) == 1:
        return array[0]
    else:
        max_restante = maximo(array[1:])
        return array[0] if array[0] > max_restante else max_restante
    
print(maximo([3, 8, 1, 9, 2]))  # 9

""" Version más limpia
def maximo(array):
    if len(array) == 1:
        return array[0]
    resto = maximo(array[1:])
    return array[0] if array[0] > resto else resto

"""