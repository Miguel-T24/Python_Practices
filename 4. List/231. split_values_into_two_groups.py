# 231. Write a python program to split values into two gruops, based on the result of the given filter lists

def two_groups(l1,l2):
    return [[l1[x] for x in range(len(l1)) if l2[x] == True], [l1[x] for x in range(len(l1)) if l2[x] == False]]
l1 = ['red', 'green', 'blue', 'pink']
l2 = [True, True, False, True]
print(two_groups(l1,l2))