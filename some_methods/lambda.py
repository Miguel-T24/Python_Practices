# lambda

print((lambda x:x*x)(2)) # 4
print((lambda x,y:x + y)(7,3)) # 10
print((lambda x , y = 10: x + y)(1)) # 11

# Lambda With Map
nums = [4,5,6,9]
print(list(map(lambda x:x*x , nums)))

#  lambda with filter
print(list(filter(lambda x:x<5 , nums)))