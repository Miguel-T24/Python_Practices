# 10. Wrote a python program that iterates the integers from 1 to 50. for multiples of three print "FIZZ" instead of the number and for multiples of five print "BUZZ". For numer that are multiples of htree and five, print"FIZZBUZZ".

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
