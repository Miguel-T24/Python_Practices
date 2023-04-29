# 60. Write a python program to capitalize the first and last letter of each word in a given string

def capitalize_first_last(string):
    string = string.strip().split(" ")
    for i in range(len(string)):
        temp = list(string[i])
        temp[0] = temp[0].upper()
        temp[-1] = temp[-1].upper()
        string[i] = "".join(temp)
    return " ".join(string)

print(capitalize_first_last("hola mundo como estan"))