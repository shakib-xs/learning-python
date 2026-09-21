# Python With Statement
#
# The with statement automatically closes the file
# after the block of code is completed.
#
# Syntax:
# with open("filename", "mode") as file:
#     statement


with open("data.txt", "w") as file:
    file.write("Python With Statement")


with open("data.txt", "r") as file:
    content = file.read()

print(content)
