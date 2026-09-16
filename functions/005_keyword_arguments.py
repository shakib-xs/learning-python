# Python Keyword Arguments

"""
Keyword arguments are arguments passed using 
the parameter name.
"""

# Syntax:
# function_name(parameter=value)


#   Using keyword arguments
def information(name, age):
    print("Name:", name)
    print("Age:", age)

information(name="Oriyo", age=22)

information(age=14, name="Shakib")  # Keyword arguments can be passed in a different order


#   Mixing positional and keyword arguments
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Shakib", age=18, course="Python")