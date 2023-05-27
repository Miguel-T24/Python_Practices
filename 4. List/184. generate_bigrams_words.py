# 184. Write a python porgram to generate bigrams of words from a given lists of string

l = ['Sum all the items in a list', 'Find the second smallest number in a list']
l = " ".join(l)
print(l)

l = l.split(" ")
print(l)

result = list(map(lambda x:(l[x],l[x+1]),list(range(len(l)-1))))
print(result)