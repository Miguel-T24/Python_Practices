# 157. Write a python program to interleave list of varying lenghts

l1 = [2, 4, 7, 0, 5, 8]
l2 = [2, 5, 8]
l3 = [0, 1]
l4 = [3, 3, -1, 7]

len_max = max(len(l1),len(l2), len(l3), len(l4))

if len(l1)!=len_max:
    for i in range(len_max - len(l1)):
        l1.append(None)
if len(l2)!=len_max:
    for i in range(len_max - len(l2)):
        l2.append(None)
if len(l3)!=len_max:
    for i in range(len_max - len(l3)):
        l3.append(None)
if len(l4)!=len_max:
    for i in range(len_max - len(l4)):
        l4.append(None)
        
result = []
for i in range(len_max):
    result.append(l1[i])
    result.append(l2[i])
    result.append(l3[i])
    result.append(l4[i])

result = list(filter(lambda x:x!=None,result))
print(result)