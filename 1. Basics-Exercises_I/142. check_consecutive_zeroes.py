# 142 Write a python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones same length in a given string. Return True / False

def check_zeroes_consecutive(num):
    num = list(num)
    countz = 0
    counto = 0
    active = 0

    zeros = []
    ones = []

    for x in num:
        if x == "0":
            zeros.append(x)
        if x == "1":
            ones.append(x)
    if(len(zeros) != len(ones)):
        return False

    for i in num:
        if (i == "0" and active == 0):
            countz += 1
        elif (i == "1"):
            counto +=1
            active = 1
        elif(i == "0" and active == 1):
            if(countz != counto):
                return False
            countz = 1
            counto = 0
            active = 0
    
    return True

print(check_zeroes_consecutive("01010101"))
print(check_zeroes_consecutive("00"))
print(check_zeroes_consecutive("000111000111"))