# Python Continue Statement

""" 
The continue statement skips the current iteration
and moves to the next iteration. 
"""

# Syntax:
# for variable in sequence:
#     if condition:
#         continue


# Skip the number 5
for number in range(1, 11):
    if number == 5:
        continue

    print(number)