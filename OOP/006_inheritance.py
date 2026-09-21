# Python Inheritance
#
# Inheritance allows one class to use
# properties and methods of another class.
#
# Syntax:
# class ChildClass(ParentClass):
#     statement


class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()
