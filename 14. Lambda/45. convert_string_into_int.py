# 45. Write a python program to convert string elements to integers inside a given tuple using lambda

tup = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

result = tuple(map(lambda x:(int(x[0]),int(x[2])),tup))
print(result)