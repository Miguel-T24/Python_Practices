# 5. Write a python program to count the number of strings from a given list of strings. the string length is 2 or more and the first and last characaters are the same.

lista = ['abc' , 'xyz', 'aba' , '1221']
result = []

result = list(filter( lambda x : x[0] == x[-1] , lista))

print(result)