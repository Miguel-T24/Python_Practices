# 113. Write a python program that return a string sorted alphabetically by the first characters of a given string of words

def sorted_alpha(string):
    string = string.split(" ")
    return " ".join(sorted(string , key=lambda x:x[0]))

print(sorted_alpha("Red Green Black White Pink"))
print(sorted_alpha("Calculate the sum of two said numbers given as strings."))
print(sorted_alpha("The quick brown fox jumps over the lazy dog."))