# 203. Write a python program to join adjacent members o a given list

l = ['1', '2', '3', '4', '5', '6', '7', '8']
# way 1
r = list(map(lambda x:l[x]+l[x+1], range(0,len(l),2)))
print(r)
