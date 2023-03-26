# 4. Write a python program to construct the following pattern, using a nested for loop

active = 0
for i in range(0,5):
    for j in range(0, i+1):
        print("*", end="")
    print("")

for i in range(5,0,-1):
    for j in range(0, i-1):
        print("*", end="")
    print("")
