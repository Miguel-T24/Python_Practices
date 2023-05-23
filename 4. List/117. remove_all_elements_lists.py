# 117. Write a python program to remove all elements from a given list that are rpesent in another list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

result = list(filter(lambda x:x not in list2,list1))

print(result)