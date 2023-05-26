# 168. Write a python program to display vertically each element of a given lits, list of lists

def vertically(lista):
    for a,b,c in zip(*lista):
        print(a,b,c)

vertically([[1, 2, 5], [4, 5, 8], [7, 3, 6]] )