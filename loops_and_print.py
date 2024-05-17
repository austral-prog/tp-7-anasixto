def enumerate_list(my_list):
    new_list=[]
    current_index= 0
    number=0 
    while current_index < len(my_list):
        if my_list[current_index]!= "": 
            new_list.append(f"{number}. {my_list[current_index]}")
            number+=1
        current_index+=1
    return new_list


def enumerate_backwards(my_list):
    new_list=[]
    current_index= 0
    number=0 
    while current_index < len(my_list):
        if my_list[current_index]!= "": 
            new_list.append(f"{number}. {my_list[current_index][::-1]}")
            number+=1
        current_index+=1
    return new_list
