# 19. Write a python program to get a newly*generated string from given string where "Is" has been added to the front. Return the string unchanged if the given string alreade begins with "Is"

string = input("Enter string: ")

if string[:2] == "Is":
    print(string)
else:
    print("Is"+string)