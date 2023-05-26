# 173. Write a python program to merge some list items in a given list using the index values

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def merge_el(lista,f,t):
    return lista[:f] + ["".join(list(map(lambda x:lista[x],list(range(f,t)))))] + lista[t:]

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(merge_el(lista,2,4))
print(merge_el(lista,3,7))