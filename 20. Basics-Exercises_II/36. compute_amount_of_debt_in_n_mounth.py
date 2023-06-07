# 36. Write a python programt om compute the amount of debt in n months. Each month, the loan adds 5% interest to the 100000 debt and rounds to the nearest 1000 above.

def round_n(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
     
def compute_debt(n):
    if n==0: return 100000
    return int(round_n(compute_debt(n-1)*1.05))

print("Input number of months:")
result = compute_debt(int(input()))
print("Amount of debt: ","$"+str(result).strip())