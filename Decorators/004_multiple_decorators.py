# Python Multiple Decorators
#
# Multiple decorators can be applied to one function.
#
# Syntax:
# @decorator_one
# @decorator_two
# def function():
#     statement


def first_decorator(function):
    def wrapper():
        print("First decorator")
        function()

    return wrapper


def second_decorator(function):
    def wrapper():
        print("Second decorator")
        function()

    return wrapper


@first_decorator
@second_decorator
def greet():
    print("Hello, Python!")


greet()
