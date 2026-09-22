# Python Regex Search
#
# re.search() searches for a pattern anywhere in a string.
#
# Syntax:
# re.search(pattern, string)


import re

text = "Python is a programming language."

result = re.search(r"programming", text)

if result:
    print("Match found:", result.group())
else:
    print("No match found")
