# 22. Write a python program that sums the length of a list of names after removing those that start with lowercase letters. use lambda function

lista = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

result = list(filter(lambda x:x[0].isupper(), lista))
result = len("".join(result))

print(result)