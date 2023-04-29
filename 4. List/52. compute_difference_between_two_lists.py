# 52. Write a python program to compute the diffreence bwteen two lists

def difference_two_lists(list1,list2):
    list1 = set(list1)
    list2 = set(list2)

    return list(list1.difference(list2))

print(difference_two_lists(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))