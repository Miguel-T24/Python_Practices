# 108. Write a python program to extract a specified column form a given nested list

def extract_column(lista,col):
    result = []
    for i in lista:
        for j in range(len(i)):
            if(j==col):
                result.append(i[col])
    return result

lista = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original\n{}".format(lista))
print("Extract 1st Column\n{}".format(extract_column(lista,0)))