# 42. Write a ptyhon program to count repeated characters in a string

string = 'thequickbrownfoxjumpsoverthelazydog'
set_string = "".join(set(string))
times = 0
for i in set_string:
    times = string.count(i)
    if(times > 1):
        print("{} appearance {} times".format(i, times))