# Python Regex Findall
#
# re.findall() returns all non-overlapping matches.
#
# Syntax:
# re.findall(pattern, string)


import re

text = "Python is easy. Python is powerful."

matches = re.findall(r"Python", text)

print("Matches:", matches)
print("Count:", len(matches))
