# 28. Write a python program to sort gicen list of list by length and value using lambda

list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

list1 = sorted(list1,key=lambda x:x[0])
print(list1)