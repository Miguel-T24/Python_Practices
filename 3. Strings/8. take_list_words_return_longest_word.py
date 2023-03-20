# 8. write a python function that takes a list of word and return the longest word and the length of the longest one

def longest(string):
    string  = string.split(" ")
    maxi = 0
    word_max = ""

    for i in string:
        maxi = (maxi ,len(i))[len(i) > maxi]
        word_max = (word_max , i)[len(i) >= maxi]
    
    return word_max , maxi

word , maxi = longest("php exercises backend")

print("The word {} len {}".format(word, maxi))
