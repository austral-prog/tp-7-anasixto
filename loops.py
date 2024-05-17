def index_of_by_index(word, list_1, index):
    for index, value in enumerate(list_1):
        if value == word:
            return index
    return -1


def index_of_empty(target, list_1, start_index):
    # Aseguramos que el indice de inicio este dentro del rango valido
    if start_index < 0 or start_index >= len(list_1):
        return -1
    # Recorremos la lista desde el indice de inicio hasta el final
    for index in range(start_index, len(list_1)):
        if list_1[index] == target:
            return index
    return -1
    


def index_of(word, list_1):
    # Recorremos la lista con un bulce
    for index, value in enumerate(list_1):
        # Si encontramos un elemento vacio, retornamos el indice
        if index == "":
            return index
    # Si no encontramos ningun elemento vacio, retornamos -1
    return -1


def put(word, list_1):
    for index, value in enumerate(list_1):
        if value == "":
            list_1 = word
            return index
    return -1


def remove(word, list):
    count = 0
    for index, value in enumerate(list_1):
        if value == word:
            list_1[index] = ""
    return -1
