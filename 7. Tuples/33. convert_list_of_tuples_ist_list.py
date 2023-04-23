# 33. Write a python program to convert a given list of tuples to a lists of lists

def list_t_list_l(lista):
    return list(map(list,lista))

l1 = [(1, 2), (2, 3), (3, 4)]
print("Original: {}".format(l1))
print("List of List: {}".format(list_t_list_l(l1)))