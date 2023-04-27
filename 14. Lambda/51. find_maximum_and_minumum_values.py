# 51. Write a python program to find the maximum and minimum values in a given list of tuple using the lambda function

lista = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

mini = min(list(map(lambda x:x[1], lista))) 
maxi = max(list(map(lambda x:x[1], lista)))

print(mini)
print(maxi)