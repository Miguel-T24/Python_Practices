# 19. Write a python program to find all anagrams of a string in a given list of string using lambda

from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)