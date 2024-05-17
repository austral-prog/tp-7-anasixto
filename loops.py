def index_of_by_index(word, list_1, index):
    if index < 0 or index >= len(list_1):
        return -1
        
    for index in range(index, len(list_1)):
        if list_1[index] == word:
            return index
    return -1


def index_of_empty(list_1):
    for index, value in enumerate(list_1):
        if value == "":
            return index
    return -1
    


def index_of(word, list_1):
    for index, value in enumerate(list_1):
        if value == word:
            return index
    return -1


def put(word, list_1):
    for index, value in enumerate(list_1):
        if value == "":
            list_1[index] = word
            return index
    return -1


def remove(word, list):
    count = 0
    for index, value in enumerate(list_1):
        if value == word:
            list_1[index] = ""
            count += 1
    return count
