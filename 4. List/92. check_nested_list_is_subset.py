# 92. Write a python program to check if a nested listed is a subset of another nested list

list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]

result = any(list(map(lambda x:x in list1,list2)))
print(result)

list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
list2 = [[[3, 4], [5, 6]]]

result = any(list(map(lambda x:x in list1,list2)))
print(result)

list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
list2 = [[[3, 4], [5, 6]]]
result = any(list(map(lambda x:x in list1,list2)))
print(result)
