# 229. Write a python program to find the index of the first element in the given lists that satisfies the provided testing function

def find_index(l,fn):
    return list(filter(fn,l))

l = [1,2,3,4]

print(find_index(l,lambda x:x%2==0))