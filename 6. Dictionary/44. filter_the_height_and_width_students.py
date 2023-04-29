# 44. Write a python program to filter the heoght and width of studnets, which are stored in a dictionary

dic  ={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

print("Original: {}".format(dic))

# height > 6ft
# weight > 70kg

result = dict(filter(lambda x:x[1][0] > 6 and x[1][1]>=70, dic.items()))

print("Result: {}".format(result))