# 18. Write a python program to find the median among three given numbers

a = 25
b = 15 
c = 35

l = [a,b,c]

median = list(filter(lambda x:x!= max(l) or x!=min(l),l))[0]
print(median)

median = next(filter(lambda x:x!=max(l) or x!=min(l),l))
print(median)