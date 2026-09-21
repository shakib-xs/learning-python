# Python Close File
#
# The close() method closes an opened file.
# It is important to close a file after using it.
#
# Syntax:
# file.close()


file = open("data.txt", "w")

file.write("Python")

file.close()

print("File closed successfully.")
