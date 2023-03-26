# 9. Write a python program t get the fibonacci series between 0 and 50

before = 0
current = 1
temp = 0

while(True):
    temp = current
    current = before + current
    before = temp
    if(current < 50):
        print(current, end=" ")
    else:
        break
print()