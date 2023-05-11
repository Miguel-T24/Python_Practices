# 58. Write a python program thath takes a string with some words. for two consecutive words in the said string, check whether the first words ends with a vowel and the nextword begins with a vowel. if the program meets the condition, return true, otherwise false. Only one space is allowed between the words

from re import search, IGNORECASE

def some_words(string):
    return bool(search("\w*[aeiou]{1}\s{1}[aeiou]{1}", string, IGNORECASE))

print(some_words("These exercises can be used for practice."))
print(some_words("Following exercises should be removed for practice."))
print(some_words("I use these stories in my classroom."))