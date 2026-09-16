# Python Scope
#
# Scope determines where a variable can be accessed.
#
# Main types:
# 1. Local Scope
# 2. Global Scope
#
# Syntax:
# variable = value          # Global variable
#
# def function():
#     variable = value      # Local variable


#   Global variable
message = "Global variable"


def show_message():
    print(message)
show_message()


#   Local variable
def display():
    text = "Local variable"
    print(text)
display()


#  Global and local variables
number = 100


def show_number():
    number = 50
    print("Local:", number)
show_number()

print("Global:", number) 