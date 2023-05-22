# 91. Write a python program to find a list with maximun and minimum lengths

def max_min_len(lista):
    result = tuple(map(lambda x : (len(x), x),lista))
    return (max(result,key=lambda x:x[0]),min(result,key=lambda x:x[0]))

print("Max: {} - Min: {}".format(*max_min_len([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])))
print("Max: {} - Min: {}".format(*max_min_len([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]])))