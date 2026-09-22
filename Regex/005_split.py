# Python Regex Split
#
# re.split() splits a string using a regular expression.
#
# Syntax:
# re.split(pattern, string)


import re

text = "Python,Java,C++"

result = re.split(r",", text)

print(result)
