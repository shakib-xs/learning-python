# Python Nested Loop

''' A nested loop means using one loop inside another loop.  '''

# Syntax:
# for variable in sequence:
#     for variable in sequence:
#         statement

#   Nested for loop
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)


#   Multiplication table pattern
for number in range(1, 4):
    for multiplier in range(1, 4):
        print(number * multiplier)
