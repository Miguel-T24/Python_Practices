# 26. Write a python program to find a list with maximum and minimun length using lambda

lista = [[13, 15, 17],[0],[5, 7], [9, 11], [1, 3]]
print("Original {}".format(lista))
result = sorted(lista)
print("Minimum:",(len(result[0]),result[0]))
print("Maximum:",(len(result[-1]),result[-1]))


# With lambda
len_list = len(min(lista))
min_list = min(lista, key=lambda i:len(i))
print("Minimum:",(len_list,min_list))
len_list = len(max(lista))
max_list = max(lista, key=lambda i:len(i))
print("Maximum:",(len_list,max_list))
