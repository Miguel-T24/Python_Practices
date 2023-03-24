# 148. Write a pthon fucntion to find the maximum and miniun numbers from a sequence of number

def find(num):
    num = list(str(num))

    for i in range(len(num)):
        for j in range(i + 1,len(num)):
            if (num[i] > num[j]):
                num[i], num[j] = num[j] , num[i]
    
    return num[-1] , num[0]

maxi , mini = find(321)

print("Maximo : {} Minimo : {}".format(maxi,mini))
