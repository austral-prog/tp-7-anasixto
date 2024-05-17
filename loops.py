def index_of_by_index(word, my_list, index):
    i=index
    while i < len(my_list):
        if my_list[i]==word:
            return i
        i+=1
    return -1


def index_of_empty(my_list):
    i=0
    while i < len(my_list):
        if my_list[i] == "":
            return i
        i += 1
    return -1


def index_of(word, my_list):
    i=0
    while i < len(my_list):
        if my_list[i]==word:
            return i 
        i+=1
    return -1


def put(word, my_list):
    i=0
    while i < len(my_list):
        if my_list[i]=="":
            my_list[i]= word
            return i
        i+=1
    return -1


def remove(word, my_list):
    i=0
    count=0
    while i < len(my_list):
        if my_list[i]==word:
            my_list[i]=""
            count+=1
        i+=1
    return count
