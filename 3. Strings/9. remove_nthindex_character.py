# 9. Write a python program to rmeove the nth index character from a nonempty string

def remove_nth(string, n):
    string = list(string)
    string.pop(n)
    return "".join(string)

print(remove_nth("Python" , 0) )
print(remove_nth("Python" , 3) )
