# 4. Write a python program to reverse a string

def reverse_string(string):
    for i in range(len(string) -1 , -1,-1):
        print(string[i],end="")
    print()
reverse_string("Hola")

print("Other way")

print("Hola"[-1::-1])
