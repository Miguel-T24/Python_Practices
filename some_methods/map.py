# Map(func, iter)

def addition(n):
    return n + n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result))

result = map(lambda x:x+x,numbers)
print(list(result))

print("Add two list")
numbers1 = [1,2,3,4]
numbers2 = [1,2,3,4]
result = map(lambda x,y : x + y , numbers1,numbers2)
print(list(result))

l = ['sat', 'bat', 'cat', 'mat']
result = map(list,l)
print(list(result))

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num

numbers = [1,2,3,4,5]
result = map(double_even, numbers)
print(list(result))

result = map(lambda x:(x,x*2)[x%2==0], numbers)
print(list(result))
