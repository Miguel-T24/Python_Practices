# 21. Write a python program to count the most and least common characters in a given string

import collections

string = "hello world"

print(string)

count = collections.Counter(string).most_common()
print(count)
most = count[0][1]
least = count[-1][1]

print(most)
print(least)

most = tuple(filter(lambda x:x[1] == most,count))
least = tuple(filter(lambda x:x[1] == least,count))
print("Most common: {}".format(*most))
print("least common: {}".format(*least))
