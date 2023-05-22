# 106. Write a python program to count integers in a given mixed list

mix = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

result = len(list(filter(lambda x:isinstance(x,int), mix)))

print(result)