# 56. write a python program to convert string to list

import ast
color = "['Red', 'Green', 'White']"
print(ast.literal_eval(color))