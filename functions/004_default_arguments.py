# Python Keyword Arguments

"""
 Keyword arguments are arguments passed using
 the parameter name.
"""

# Syntax:
# function_name(parameter=value)


# Using keyword arguments
def information(name, age):
    print("Name:", name)
    print("Age:", age)
information(name="Shakib", age=17)


#  Keyword arguments can be passed in a different order
information(age=17, name="Shakib")


# 3. Mixing positional and keyword arguments
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student("John", age=20, course="Python")