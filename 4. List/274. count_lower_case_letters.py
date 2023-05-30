# 274. Write a Python program to count the lowercase letters in a given list of words

def count_lower(l):
    c = 0
    for i in l:
        for j in i:
            if(j.islower()):
                c+=1
    return c  

print(["Red", "Green", "Blue", "White"])
print(count_lower(["Red", "Green", "Blue", "White"]))