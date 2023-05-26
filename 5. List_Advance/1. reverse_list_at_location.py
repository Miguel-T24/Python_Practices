# 1. Write a python function to reverse a list at a specific location

def revese_specific_position(lista,s,e):
    return lista[:s]+list(reversed(lista[s:e+1]))+lista[e+1:]

lista  = [10,20,30,40,50,60,70,80]
print(lista)
print(revese_specific_position(lista,2,4))

print()
print(lista)
print(revese_specific_position(lista,6,7))

print()
print(lista)
print(revese_specific_position(lista,0,7))