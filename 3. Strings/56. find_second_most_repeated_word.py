# 56. Write a python program to find the second most repeared word in a given string

def second_most_repeated(string):
    string = string.split(" ")
    dic = {}
    for i in string:
        if(string.count(i)>1):
            dic[i] = string.count(i)
    return sorted(dic.items(), key=lambda x:x[1], reverse=True)[1]

string = """
"Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."
"""
print(second_most_repeated(string))