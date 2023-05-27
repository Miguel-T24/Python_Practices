# 198. Write a python program to compare two given lists and find the indices of the values present in both lists

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 5, 2, 10, 12]

result = [list1.index(x) for x in list1 if x in list2]

print(result)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 5, 7, 10, 12]

result = [list1.index(x) for x in list1 if x in list2]
print(result)