# Python Function Parameters

"""
# Parameters are variables defined inside the function definition.
# Arguments are the actual values passed to the function.
"""

# Syntax:
# def function_name(parameter):
#     statement
#
# function_name(argument)


#  Function with one parameter
def greet(name):
    print("Hello", name)
greet("Python")


#   Function with two parameters
def add(a, b):
    print(a + b)
add(10, 20)


#   Function with multiple parameters
def information(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

information("Shakib", 17, "Dhaka")