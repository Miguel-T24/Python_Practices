# 35. Write a python program to sort counter by value

dic = {'Math':81, 'Physics':83, 'Chemistry':87}
items = dic.items() 

result = sorted(items,key=lambda x:x[1], reverse=True)

print(result)
print(dict(result))