# Python Range Function

""" The range() function generates a sequence of numbers.  """

# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)


#   range(stop)
for number in range(5):
    print(number)


#   range(start, stop)
for number in range(1, 6):
    print(number)


#   range(start, stop, step)
for number in range(1, 10, 2):
    print(number)


#   Counting backwards
for number in range(10, 0, -1):
    print(number)