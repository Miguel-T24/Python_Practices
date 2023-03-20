# 117. write a python program to prove that two string variables of the same value point to the same memory location

str1 = "Python"
str2 = "Python"

print("Memory Location: {}".format(hex(id(str1))))
print("Memory Location: {}".format(hex(id(str2))))
