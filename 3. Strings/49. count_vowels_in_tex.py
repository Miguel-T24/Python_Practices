# 49. Write a python program to count and display vowels in text

def count_vowels(string):
    result = list(filter(lambda x:x.lower() in "aeiou",string))
    return len(result), result

print(count_vowels('w3resource'))