# 66. Write a python program to check if specific key and value exist in a dictionary

list_dic = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

def test(dictt, key, value):
   if any(sub[key] == value for sub in dictt):
       return True
   return False

students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]


print("\nOriginal dictionary:")
print(students)
print("\nCheck if a specific Key and a value exist in the said dictionary:")
print(test(students,'student_id', 1))
print(test(students,'name', 'Brian Howell'))
print(test(students,'class', 'VII'))
print(test(students,'class', 'I'))
print(test(students,'name', 'Brian Howelll'))
print(test(students,'student_id', 11))