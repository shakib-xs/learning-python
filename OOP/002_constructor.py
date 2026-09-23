# Python Constructor
#
# __init__() is a special method that runs
# automatically when an object is created.
#
# Syntax:
# class ClassName:
#     def __init__(self, parameters):
#         self.variable = value


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("John", 20)

print(student.name)
print(student.age)
