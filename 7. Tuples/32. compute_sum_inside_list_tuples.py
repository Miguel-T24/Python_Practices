# 32. Write a python program to compute the sum of all elements of each tuple stored inside a list of tuples

l1 = [(1, 2), (2, 3), (3, 4)]
l2 = [(1,2,6), (2,3,-6), (3,4), (2,2,2,2)]
def suma(lista):
    return list(map(sum, lista))

print(suma(l1))
print(suma(l2))