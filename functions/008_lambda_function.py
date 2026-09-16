# Python Lambda Function

"""
A lambda function is a small anonymous function.
It can have any number of arguments but only one expression.
"""

# Syntax:
# lambda arguments: expression


#   Simple lambda function
square = lambda number: number * number
print(square(5))


#   Lambda with two arguments
add = lambda a, b: a + b
print(add(10, 20))


#   Lambda with three arguments
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))


#   Lambda with a condition
check = lambda number: "Even" if number % 2 == 0 else "Odd"
print(check(10))
print(check(7))