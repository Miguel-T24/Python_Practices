# 37. Write a python program to sort a list of list by given index of the inner list using lambda

def sorted_by_index(lista,index):
    return sorted(lista,key=lambda x:x[index])

list1 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print("Original List: {}\nSorted List by index 0: {}".format(list1, sorted_by_index(list1,0)))

print("\nOriginal List: {}\nSorted List by index 2: {}".format(list1, sorted_by_index(list1,2)))