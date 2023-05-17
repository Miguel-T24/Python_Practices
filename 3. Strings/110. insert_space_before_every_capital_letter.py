# 110. Write a python program to insert space before every capital letter appears in a given word

def test(string):
    return "".join(map(lambda x:(x," "+x)[x.isupper()],string)).lstrip()

print(test("PythonExercises"))
print(test("Python"))
print(test("PythonExercisesPracticeSolution"))