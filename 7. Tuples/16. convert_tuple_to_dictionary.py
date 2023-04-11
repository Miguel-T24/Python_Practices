# 16. Write a python program to convert a tuple to a dictionary

tuplex = ((2,"w") ,(3,"r"))

dict1 = dict((x,y) for x ,y in tuplex)

print(dict1)