# 31. Write a python program that computes the greatest common divisor of two positive integer

def gcd(num1,num2):
    def div(n):
        common = []
        for i in range(1 , n + 1):
            if(n % i == 0):
                common.append(i)
        return common
    
    return max(list(set(div(6)).intersection(div(8))))


print(gcd(6,8))
