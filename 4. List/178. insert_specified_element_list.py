# 178. Write a python program to insert a specified element in a given list after every nth elemetns

lista = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
c = 0
el = 20

for i in range(len(lista)):
    if(c==4):
        lista.insert(i,el)
        c=0
    else:
        c+=1

print(lista)