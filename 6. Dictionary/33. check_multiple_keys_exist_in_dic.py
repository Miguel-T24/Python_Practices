# 33. Write a python program to check if multiple keys exist in a dictionary

dic = {1:'b',2:"b"}

print(dic.keys() >= {1,2})
print(dic.keys() >= {1,"Hola"})