# 91. Write a python program to convert a given heterogeneous list of scalars into a string

lista  = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

result = ",".join(list(map(str,lista)))
print(result)