# Python Pass Statement

"""
# The pass statement does nothing.
# It is used as a placeholder when a statement is required
# but no code needs to be executed.
"""

# Syntax:
# if condition:
#     pass
# 
# or
# 
# for variable in sequence:
#     pass


#   Pass inside a loop
for number in range(5):
    if number == 2:
        pass

    print(number)


#   Empty loop using pass
for number in range(3):
    pass