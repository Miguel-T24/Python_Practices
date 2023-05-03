# 70. Write a python program to find items starting with a specific character from a list

def start_with(lista, start):
    return list(filter(lambda x:x[0]==start,lista))

lista = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

print("Items  start with 'a' from the said list: \n{} ".format(start_with(lista,'a')))
print("Items  start with 'd' from the said list: \n{} ".format(start_with(lista,'d')))
print("Items  start with 'w' from the said list: \n{} ".format(start_with(lista,'w')))
