# Python Append File
#
# The "a" mode adds new data to the end of a file.
# Existing content is preserved.
#
# Syntax:
# file = open("filename", "a")
# file.write("data")
# file.close()


file = open("data.txt", "a")

file.write("\nNew data added.")

file.close()

print("Data appended successfully.")
