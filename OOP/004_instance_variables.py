# Python Instance Variables
#
# Instance variables belong to individual objects.
# They are usually created using self.
#
# Syntax:
# self.variable = value


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("John", 20)
person2 = Person("Alex", 25)

print(person1.name, person1.age)
print(person2.name, person2.age)
