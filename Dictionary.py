student={
         "name":{"samiksha","Diksha"},
         "age" : 21,
         "score" : 80,
         "rollno" :[1,2,3,4]
}

print(student)
print(type(student))

print(student["age"])
print(student["name"])
print(student["score"])

print(student.keys())
print(student.values())

student.pop("age")
print(student)

student.get()

new=student.copy()
print("Copied student dictionary is:",new)
print("Copied student dictionary is:",*new)

student_list=student.setdefault("age",20)
print("Updated age is:",student_list)


