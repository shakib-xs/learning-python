# Python Regex Substitute
#
# re.sub() replaces matched text with new text.
#
# Syntax:
# re.sub(pattern, replacement, string)


import re

text = "I like Java."

result = re.sub(r"Java", "Python", text)

print(result)
