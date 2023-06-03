# 6. Write a python program hat prints logn text converts it to list, and prints all the words and the frequency of each word

string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule.'''

s = string_words.split()
s_set=sorted(set(s), key= s.index)
l=[]
print("{:<20} {}".format("Word","Times"))

for i in s_set:
    l.append((i,s.count(i)))

for i in l:
    print("{:<20} {}".format(*i))