# 130. Write a python  program to count the same pair in three given lists

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [2, 2, 3, 1, 2, 6, 7, 9]
list3 = [2, 1, 3, 1, 2, 6, 7, 9]

result = [[list1[x],list2[x],list3[x]] for x in range(len(list1))]
print(result)
result = len(list(filter(lambda x:len(set(x)) == 1,result)))

print(result)