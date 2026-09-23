# Python Polymorphism
#
# Polymorphism means the same method name
# can behave differently for different objects.
#
# Syntax:
# class ClassName:
#     def method_name(self):
#         statement


class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
