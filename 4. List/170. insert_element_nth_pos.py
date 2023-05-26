# 170. Write a python program to oinsert an element in a given list after every nth position

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
c = 0
nth = 2
for i in range(len(lista)):
    if c == nth:
        lista.insert(i,'a')
        c = 0
    else:    
        c+=1

print(lista)