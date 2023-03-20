# 106. Write a python program to divide a path by extension separator

for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))