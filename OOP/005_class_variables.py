# Python Class Variables
#
# A class variable is shared by all objects of a class.
#
# Syntax:
# class ClassName:
#     class_variable = value


class Student:
    school = "Python Academy"

    def __init__(self, name):
        self.name = name


student1 = Student("John")
student2 = Student("Alex")

print(student1.name, student1.school)
print(student2.name, student2.school)
