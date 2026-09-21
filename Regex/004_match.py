# Python Regex Match
#
# re.match() checks whether a pattern matches
# at the beginning of a string.
#
# Syntax:
# re.match(pattern, string)


import re

text = "Python is powerful."

result = re.match(r"Python", text)

if result:
    print("Match found:", result.group())
else:
    print("No match at the beginning")
