# Python Return Statement

"""
# The return statement sends a value back from a function.
"""

# Syntax:
# def function_name():
#     return value
#
# result = function_name()


#   Returning a value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)


#   Returning a calculation
def square(number):
    return number * number
result = square(5)
print(result)


#  Using returned value in another calculation
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result + 10)