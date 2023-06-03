# 19. Write a python program that finds the value of n when degrees of number 2 are writte squentially on a line with out spaves between them

def ndegrees(num):
  ans = True
  n, tempn, i = 2, 2, 2
  while ans:
    if str(tempn) in num:
      i += 1
      tempn = pow(n, i)
    else:
      ans = False
  return i-1;
print(ndegrees("2481632"))
print(ndegrees("248163264"))