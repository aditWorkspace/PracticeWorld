students = {"Jeff": 13, "Bob": 12, "Marc":23}
print (students["Jeff"])
students ["Jeff"] = 14
print (students ["Jeff"])
del students["Jeff"]
print (students["Bob"])
students.clear()
print (students)
del students
students1 = {"Jeff": 13, "Bob": 12, "Marc":23}
print(len(students1))
print(students1.keys())
print(students1.keys)
#Jeff, Bob, and Marc are our keys for the dictionary
print (students1.values())
print (students1.values)
#Their ages are our values for the dictionary....... SOMETIMES Dictionaries are not ordered....so they can be switched every time you print
students2 = {"Jff": 183, "Bo": 2, "arc":73}
students2.update(students1)
print(students2)