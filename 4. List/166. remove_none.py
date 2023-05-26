# 166. Write a python program to remove the none valye from a given list

lista = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

result = list(filter(lambda x:x!=None,lista))

print(result)