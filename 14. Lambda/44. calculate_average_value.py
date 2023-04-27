# 44. Write a python program to calculate the average value of the numebrs in a given tuple of tuples using lambda

def average_tuple(tuplee):
    tuple_list = list(tuplee)
    return tuple(map(lambda x:"{:.3f}".format(sum(x)/len(x)), tuple_list))

tuple1= ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print(average_tuple(tuple1))