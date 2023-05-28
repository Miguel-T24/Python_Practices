# 218. Write a python program to sort one list based another lists containing the desired indexes


l1 = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
l2 = [3, 2, 6, 4, 1, 5]

d = dict(zip(l1,l2))
print(d)

d = sorted(d,key = lambda x:d[x])
print(d)