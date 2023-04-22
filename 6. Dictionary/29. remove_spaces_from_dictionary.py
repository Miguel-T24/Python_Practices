# 29. Write a python program to remove spaces from dictiornary keys

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original Dict: {}".format(student_list))
student_list = student_list.items()
student_list = dict(map(lambda x:[x[0].replace(" ",""), x[1]],student_list))
print("New Dict: {}".format(student_list))
