# 23. Write a python program to find the shortest distance form a specified character in a given stirng. Return the shortest distances through a list and use an itertools component to solve the  problem


import itertools as it

def char_shortest_distancer(str1, char1):
    result = [len(str1)] * len(str1)
    prev_char = -len(str1)
    for i in it.chain(range(len(str1)),reversed(range(len(str1)))):
        if str1[i] == char1:
            prev_char = i
        result[i] = min(result[i], abs(i-prev_char))
    return result

str1 = "w3resource"
chr1='r'
print("Original string:",str1,": Specified character:",chr1)
print(char_shortest_distancer(str1,chr1))