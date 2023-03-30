# 4. Write a python program to create a liist contaninig the power of said number in bases raised to the corrresponding number in the indes using map.

base_num = [x for x in range(10,101,10)]
index = [x for x in range(1,11)]

print("base numebrs adb index: ")
print(base_num)
print(index)

result = list(map(lambda x , y : pow(x,y) , base_num,index))
print(result)

# other way

result = list(map(pow, base_num,index))
print(result)

