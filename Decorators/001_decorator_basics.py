# Python Decorator Basics
#
# A decorator is a function that modifies
# or extends the behavior of another function.
#
# Syntax:
# def decorator(function):
#     def wrapper():
#         statement
#         function()
#     return wrapper


def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello, Python!")


greet()
