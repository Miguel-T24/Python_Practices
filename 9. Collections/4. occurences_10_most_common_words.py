# 4. Write a python program to find the occurrence sof the 10 most common word in a given text

from collections import Counter
import re

text = """
The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects.
"""

word = re.findall('\w+',text)

print(Counter(word).most_common(10))