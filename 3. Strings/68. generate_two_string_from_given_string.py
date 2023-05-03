# 68. Write a python proram to generate two string from a given string. for the first string, use the characters that iccur only once, and for the second, use the characters that occur multiple times in the said string

from collections import Counter  
def generateStrings(input): 
     str_char_ctr = Counter(input) 
     part1 = [ key for (key,count) in str_char_ctr.items() if count==1] 
     part2 = [ key for (key,count) in str_char_ctr.items() if count>1] 
     part1.sort() 
     part2.sort()
     return part1,part2
input = "aabbcceffgh"
s1, s2 = generateStrings(input)
print(''.join(s1))   
print(''.join(s2))