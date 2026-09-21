# Python Decorator Returning Values
#
# A decorator can return the value produced
# by the decorated function.
#
# Syntax:
# def decorator(function):
#     def wrapper():
#         result = function()
#         return result
#     return wrapper


def decorator(function):
    def wrapper():
        result = function()
        return result

    return wrapper


@decorator
def add():
    return 10 + 20


result = add()

print(result)
