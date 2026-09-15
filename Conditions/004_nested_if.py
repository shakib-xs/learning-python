# Python Nested If Statement

# Syntax:
# if condition:
#     if condition:
#         statement
#     else:
#         statement
# else:
#     statement


number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not a positive number")