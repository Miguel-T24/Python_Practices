# 15. Write a pythonn function to create an html stringn with tags around the word(s)

def add_tags(tag,string):
    return "<{}>{}<{}/>".format(tag,string,tag)

print(add_tags('i','Python'))
print(add_tags('b','Tutorial'))