# Python Arbitrary Arguments

"""
Arbitrary arguments allow a function to accept
an unknown number of arguments.
"""

# *args  -> Multiple positional arguments
# **kwargs -> Multiple keyword arguments
#
# Syntax:
# def function_name(*args):
#     statement
# 
# def function_name(**kwargs):
#     statement


#   Using *args
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)

#   Looping through *args
def show_numbers(*args):
    for number in args:
        print(number)

show_numbers(1, 2, 3, 4, 5)


#   Using **kwargs
def information(**kwargs):
    print(kwargs)


information(name="Nabil", age=28, city="Dhaka")

#   Looping through **kwargs
def show_information(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_information(name="Robin", age=12, city="Dhaka")