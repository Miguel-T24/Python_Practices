# 15. Write a python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separeted sequence after sorting them alphabetically

def hyphen_separated(string):
    string = string.split("-")
    string = sorted(string)

    return "-".join(string)

print(hyphen_separated("green-red-yellow-black-white"))