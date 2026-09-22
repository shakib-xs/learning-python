# Python Regex Email Validation
#
# Regular expressions can be used to check
# whether text follows an email-like pattern.
#
# Syntax:
# re.match(pattern, string)


import re

email = "example@gmail.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.match(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")
