# 53. Write a python program to find the length of a dictionary of values

def len_of_values(dic):
    return dict(map(lambda x:(x[1],len(x[1])),dic.items()))

dic = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

print("Original: {}".format(dic))
print("Length: {}".format(len_of_values(dic)))

