# 275. Write a python program to add all elements of a list of integers except the number at index. return the updated strinf

def add_el(l):
    return list(map(lambda x:sum(l)-x,l))

print([0, 9, 2, 4, 5, 6])
print(add_el([0, 9, 2, 4, 5, 6]))