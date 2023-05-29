# 230. Write a python program to find the indexes of all elements in the given lists that satisfy the provided testing function

def find_index(l,fn):
    return list(filter(fn,range(len(l))))

l = [1,2,3,4]
print(find_index(l,lambda x:l[x]%2==1))