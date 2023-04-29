# 42. Write a python program to filter a dictionary based on values

dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print("Original: {}".format(dic))
result = dict(filter(lambda x:x[1] > 170,dic.items()))
print("Dict greater than 170: {}".format(result))