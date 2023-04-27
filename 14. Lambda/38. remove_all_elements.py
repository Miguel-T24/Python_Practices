# 38. Write a python program to remove all elements from given list present in another list using lambda

list1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =  [2, 4, 6, 8]

print(list(filter(lambda x: x not in list2,list1)))