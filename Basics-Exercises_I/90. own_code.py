# 90. Write a python program to create a copy of its own source code

def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("90. own_code.py", "z.py")
        with open('90. own_code.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')