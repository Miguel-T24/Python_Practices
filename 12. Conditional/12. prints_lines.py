# 12. Write a python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all chararacter in lower case)


lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)