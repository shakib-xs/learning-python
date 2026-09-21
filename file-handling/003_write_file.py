# Python Write File
#
# The "w" mode opens a file for writing.
# If the file does not exist, Python creates it.
# Existing content is replaced.
#
# Syntax:
# file = open("filename", "w")
# file.write("data")
# file.close()


file = open("data.txt", "w")

file.write("Python File Handling")
file.write("\nWriting data to a file.")

file.close()

print("Data written successfully.")
