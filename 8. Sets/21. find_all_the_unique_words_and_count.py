# 21. Write a python program to find all the unique words and count the frequency of occurrence from a given list of string. Use python ser data type

from collections import Counter

words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
words1 = set(words)

print("Original: {}".format(words))
print("Unique Words: {}".format(words1))
for i in words1:
    print("The \'{}\' appears {} times".format(i,words.count(i)))
    