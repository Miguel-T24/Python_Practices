# 30. Write a python program to get the top three items in a shop

data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

data = data.items()
data = sorted(data,key=lambda x:x[1], reverse=True)
print(data)
print(dict(data))

for i in range(0,3):
    print("Key: {} - Value: {}".format(data[i][0],data[i][1]))
    
