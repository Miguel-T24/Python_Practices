# 144. Write a python proram to extract every first or specified element form a given two-dimensional list

lista = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
extract = 0

result = list(map(lambda x:x[0],lista))
print("First Elements: \n{}".format(result))
result = list(map(lambda x:x[1],lista))
print("Second Elements: \n{}".format(result))
result = list(map(lambda x:x[2],lista))
print("Third Elements: \n{}".format(result))
