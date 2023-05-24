# 142. Write a python program to sum a specific column of a list in a given list of lists

lista  = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
col = 0

result = sum(list(map(lambda x:x[col],lista)))
print(result)

# second way
result = sum([x[col] for x in lista])
print(result)