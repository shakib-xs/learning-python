# Python Read File
#
# The "r" mode opens a file for reading.
#
# Syntax:
# file = open("filename", "r")
# content = file.read()
# file.close()


file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
