# 11. Write a python program that takes two digits m (row) and n (column) as input and generates a two-dimesional array. The element value in the i-th row and h-th column of the array should be i*j


m = int(input("Enter Rows: "))
n = int(input("Enter Columns: "))
lista = []
temp = []

for i in range(m):
    for j in range(n):
        temp.append(i*j)
    lista.append(temp)
    temp = []

print(lista)