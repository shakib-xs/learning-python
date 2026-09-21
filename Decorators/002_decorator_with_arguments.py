# Python Decorator with Arguments
#
# A decorator can work with functions
# that accept arguments.
#
# Syntax:
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         statement
#         function(*args, **kwargs)
#     return wrapper


def decorator(function):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = function(*args, **kwargs)
        print("Function is finished")
        return result

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Python")
