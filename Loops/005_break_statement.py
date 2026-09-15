# Python Break Statement

""" 
The break statement is used to stop a loop immediately. 
"""

# Syntax:
# for variable in sequence:
#     if condition:
#         break


# Stop the loop when number becomes 5
for number in range(1, 11):
    if number == 5:
        break

    print(number)
