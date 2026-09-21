# Python Regular Expressions - Basics
#
# Regular expressions (Regex) are used to search,
# match, and manipulate text using patterns.
#
# Syntax:
# import re
# re.function(pattern, text)


import re

text = "Python is easy to learn."

pattern = r"Python"

result = re.search(pattern, text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
