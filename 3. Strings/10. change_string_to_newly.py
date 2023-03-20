# 10. Qrite a python program to change a given string to a newly string where the first and last chars have been exchanged

def change_first_last(string):
    return string[-1] + string[1:len(string) - 1] + string[0]

print(change_first_last("Python"))
