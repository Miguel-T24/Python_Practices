# 27. Write a python program to calculate the averange value of the numbers in a given tuuple of tuples

def avg_tuples(tup):
    return list(map(lambda x:sum(x) / len(x),tup))

tupla1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

print("Tupla 1: {}".format(tupla1))
print("Averange: {}".format(avg_tuples(tupla1)))

tupla2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print("Tupla 1: {}".format(tupla2))
print("Averange: {}".format(avg_tuples(tupla2)))
