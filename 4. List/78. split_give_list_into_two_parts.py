# 78. wrote a python program to split a given lists into two parts where the length of the first part of the list given

def split_two_parts(lista,index):
    return [lista[:index],lista[index:]]

print(split_two_parts([1, 1, 2, 3, 4, 4, 5, 1],3))
        