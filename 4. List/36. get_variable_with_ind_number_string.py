# 36. Write a python program to get a variable with an identification number or string

x = 100
print(format(id(x),'x'))
print("{}".format(id(x)))
s = "w3resource"
print(format(id(s),'x'))
print("{}".format(id(s)))