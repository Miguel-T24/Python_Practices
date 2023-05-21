# 88. Write a python program to read a square matrix from the console and print the sum of the matrix primary diagonal. Accept the size oft he squae matrix and elements for each column separated with space (for every row) as input from the user

matrix = []
diagonal = []

size = int(input(" Input the size of the matrix: "))
for i in range(size):
    row = input("Enter numbers: ")
    row = list(map(int,row.split(" ")))
    matrix.append(row)

temp = 0
for i in range(size):
    for j in range(size):
        if(j == temp):
            diagonal.append(matrix[i][j])
    temp+=1
print(diagonal)
print(sum(diagonal))