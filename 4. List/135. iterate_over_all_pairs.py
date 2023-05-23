# 135, Write a ptyhon program to iterate over all pairs of consecutive items in a igven list

list1 = [1, 1, 2, 3, 3, 4, 4, 5]

result1 = [(list1[i-1],list1[i]) for i in range(8) if i!=0]
print(result1)


result2 = list(map(lambda x:(list1[x-1],list1[x]),list(range(1,len(list1)))))
print(result2)

print(result1 == result2)