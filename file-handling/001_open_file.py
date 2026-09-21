# Python Open File
#
# The open() function is used to open a file.
#
# Syntax:
# open("filename", "mode")
#
# Common modes:
# "r" -> Read
# "w" -> Write
# "a" -> Append
# "x" -> Create


file = open("data.txt", "w")
file.write("Hello, Python!")
file.close()

print("File created successfully.")
