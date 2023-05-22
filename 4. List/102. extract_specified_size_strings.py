# 102. Write a python program to extract specified size of strings from a given list of stirng values

lista = ['Python', 'list', 'exercises', 'practice', 'solution']
num = 8
print("Length of the string to extract:\n{}".format(num))
print("After extracting string:\n{}".format(list(filter(lambda x:len(x)==8,lista))))

