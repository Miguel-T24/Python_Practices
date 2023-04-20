# 31. Write a python program to print the following numbers up to 2 decimal places with a sign

def sign_two_dec(number):
    if(not isinstance(number,float)):
        return "Invalid Value"
    else:
        number = str(number)
        numsign = ""
        for i in range(len(number)):
            if(number[i]=="."):
                for j in range(i+1,i+3):
                    numsign += number[j]
                return "+"+numsign

print(sign_two_dec(3.1415))


x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y));