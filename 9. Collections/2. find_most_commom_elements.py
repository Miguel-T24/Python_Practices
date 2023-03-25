# 2. Write a python program to find the most common elements and their counts in a specified text

from collections import Counter

s = 'lkseropewdssafsdfafkpwe'

print("Original text : {}".format(s))
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))