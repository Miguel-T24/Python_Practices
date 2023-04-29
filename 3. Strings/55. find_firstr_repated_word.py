# 55. Write a ptyhon program to find the first repeated word in a given string

def first_word_repeted(string):
    string = string.split(" ")
    for i in string:
        if(string.count(i) > 1):
            return i
    return None

print(first_word_repeted("ab ca bc ab"))
print(first_word_repeted("ab ca bc ab ca ab bc"))
print(first_word_repeted("ab ca bc ca ab bc"))
print(first_word_repeted("ab ca bc"))
