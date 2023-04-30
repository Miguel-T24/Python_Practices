# 43. Write a python prohgram to conbvert more than one lists to a nested dictionary

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]

def nested_dictionary(d1,d2,d3):
    return list(map(lambda x,y,z:{x:{y:z}}, d1,d2,d3))

print(nested_dictionary(student_id, student_name, student_grade))