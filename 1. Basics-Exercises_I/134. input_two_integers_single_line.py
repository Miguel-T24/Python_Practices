# 134. Write a python program to input two integers on a single line

# Way 1 
str1 , str2 = input("Enter 1: "), input("Enter 2: ")

print(str1)
print(str2)

# way 2
x, y = map(str, input().split())
print(x)
print(y)