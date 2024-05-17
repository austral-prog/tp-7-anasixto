def enumerate_list(list_1):
    # list_2 es para guardar todos los elementos que no sean vacios y su numero (ej.: 0. Black, 1. White, etc.)
    list_2 = []
    # current_index es para recorrer la list_1, va recorriendo cada uno de sus elementos, y para ir al siguiente elemento le tenemos que aumentar su valor en 1
    current_index = 0
    # number es para mantener la cuenta de la cantidad de elementos NO vacios de la list_1, y despues ese numero lo usamos cuando escribimos el numero en la list_2. Solo aumentamos su valor cuando el elemento no es vacio!
    number = 0
    while current_index < len(list_1):
        if list_1[current_index] != "":
            list_2 += f"{number}. {list_1[current_index]}"
            number += 1
        current_index += 1
    return list_2


def enumerate_backwards(list):
    # list_2 es para guardar todos los elementos que no sean vacios y su numero (ej.: 0. Black, 1. White, etc.)
    list_2 = []
    # current_index es para recorrer la list_1, va recorriendo cada uno de sus elementos, y para ir al siguiente elemento le tenemos que aumentar su valor en 1
    current_index = 0
    # number es para mantener la cuenta de la cantidad de elementos NO vacios de la list_1, y despues ese numero lo usamos cuando escribimos el numero en la list_2. Solo aumentamos su valor cuando el elemento no es vacio!
    number = 0
    while current_index < len(list_1):
        if list_1[current_index] != "":
            list_2 += f""{number}. {list_1[current_index][::-1]}""
            number += 1
        current_index += 1
    return list_2
