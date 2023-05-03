# 66. Write a python program to find the list in a list of lists whose sum of elements is highest

lista = [ [1,2,3], [4,5,6], [10,11,12], [7,8,9]]

maxi = 0
max_el = []

for i in lista:
    suma = sum(i)
    maxi = (maxi,suma)[suma>maxi]
    max_el = (max_el,i)[suma==maxi]

print(max_el)
