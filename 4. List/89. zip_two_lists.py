# 89. Write apython program to zip two given lists of  lists

list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]

result = list(map(lambda x,y: [*x,*y], list1,list2))

print(result)