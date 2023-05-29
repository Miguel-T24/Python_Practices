# 235. Write a ptyhon program to find the index of the last element int the given lust that satisfies the provided testing function

def find_last_index(l,fn):
    return len(l) - 1 - next(filter(fn,range(len(l))))


l = [1, 2, 3, 4]

print(find_last_index(l,lambda x:x%2 ==1))