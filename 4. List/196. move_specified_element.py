# 196. Wrte apython program to move a specified element in a ggiven list

l = ['red', 'green', 'white', 'black', 'orange']

item = "green"

a = l.index(item)
l.append(l.pop(a))
print(l)