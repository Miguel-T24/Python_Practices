# 4. Write a python program to get a string from a given string where all occurences of its firts char have been changed to '$' except the firs char itself.

def change_char_occurance(string):
    string = list(string)
    for i in range(1,len(string)):
        if(string[i] == string[0]):string[i] = '$'
    return "".join(string)

print(change_char_occurance("restart"))

