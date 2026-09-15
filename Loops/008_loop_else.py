# Python Loop Else

"""
The else block after a loop executes when the loop
finishes normally without using break.
"""

# Syntax:
# for variable in sequence:
#     statement
# else:
#     statement


#   For loop with else
for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully")


#   While loop with else
number = 1

while number <= 3:
    print(number)
    number += 1
else:
    print("While loop completed")
