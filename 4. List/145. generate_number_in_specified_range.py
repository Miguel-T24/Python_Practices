# 145. Write a pythjon program to generate a number in specified rangge except for some specific numbers

from random import choice

def generate(except_n, ran):
    result = tuple(filter(lambda x:x not in except_n, list(range(ran[0],ran[1]+1))))
    return choice(result)
print(generate((2,9,10),(1,10)))
print(generate((-5,0,4,3,2),(-5,5)))


