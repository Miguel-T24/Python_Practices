# 267. write a python program to get cumulative sum of the elemnts

def cumulative_sum(l):
    result = []
    for i in range(len(l)):
        if(i==0):
            result.append(l[i])
        else:
            result.append(result[i-1] + l[i])
    return result

print([1, 2, 3, 4])
print(cumulative_sum([1, 2, 3, 4]))

print([-1, -2, -3, 4])
print(cumulative_sum([-1, -2, -3, 4]))