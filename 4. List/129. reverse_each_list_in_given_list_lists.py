# 129. Write a python program to reverse eachb list in a given lists of lists

lista  = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Original:\n{}".format(lista))

# way 1
result = list(map(lambda x:x[::-1],lista))
print(result)

# Way 2
result = [x[::-1] for x in lista]
print(result)
