# 107. Write a python program to remove a specified column from a given nested list

def remove_col(lista,col):
    result = []
    temp = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(j!=col):
                temp.append(lista[i][j])
        result.append(temp)
        temp = []
    return result

lista = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original:\n{}".format(lista))
print("After Remove\n{}".format(remove_col(lista,1)))

lista = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Original:\n{}".format(lista))
print("After Remove\n{}".format(remove_col(lista,2)))