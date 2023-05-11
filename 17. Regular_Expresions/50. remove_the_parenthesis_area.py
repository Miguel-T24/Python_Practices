# 50. Wriyte a python program to rmeove the parentesis area in a string

from re import sub

lista  = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

for i in lista:
    print(sub("\(.+\)","",i))
