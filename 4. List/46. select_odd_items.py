# 46. Write a python program to select the odd items from a list

lista = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x:x%2!=0, lista))
print(result)