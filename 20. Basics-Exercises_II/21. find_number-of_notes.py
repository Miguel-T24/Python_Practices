# 21. Write a python program to find the number of notes (samples of notes 10,20,50,100,200,500) against an amount.

# range - number of notes (n): n(1<=n<=1 000 000)

from itertools import combinations_with_replacement,chain
l = [500,200,100,50,20,10]

comb = combinations_with_replacement(l,1)
all_comb = []

for i in range(1,len(l)+1):
    all_comb.append(list(combinations_with_replacement(l,i)))

all_comb = list(chain(*all_comb))

r = next(filter(lambda x:sum(x)==1000,all_comb),None)
print(r)
print(len(r))