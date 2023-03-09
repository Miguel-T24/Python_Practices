# 51. Write a python program to determine the profiling to python programs


import cProfile

def suma():
    print(1+2)
cProfile.run('suma()')