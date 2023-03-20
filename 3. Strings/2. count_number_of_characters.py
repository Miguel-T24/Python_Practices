# 2. Write a python program to count the number of characters (character frecuency) in string

def calculate(string):
    dic = {}
    count = 1
    string = list(string)
    for i in range(0, len(string) - 1):
        for j in range(i + 1, len(string)):
            if(string[i] == string[j]):
                count += 1
                string[j] = 0
        
        if(string[i] != 0): dic[string[i]] = count 
        count = 1
    if(string[-1] != 0): dic[string[-1]] = 1
    return dic


print(calculate("google.com"))

