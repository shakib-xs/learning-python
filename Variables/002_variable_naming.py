# Python Variable Naming Rules

# Rules:
# => Variable name must start with a letter (a-z, A-Z) or underscore (_).
# => Variable name cannot start with a number.
# => Variable name can contain letters, numbers, and underscores.
# => Variable names are case-sensitive.
# => Spaces are not allowed in variable names.
# => Python keywords cannot be used as variable names.
# => Use descriptive and meaningful names.
# => Use snake_case for multiple words.

# Rule 1: Start with a letter or underscore
name = "Shakib"
_name = "Shakib"


# Rule 2: Cannot start with a number
# 1name = "Shakib"       # Invalid


# Rule 3: Can contain letters, numbers, and underscores
student1 = "Shakib"
student_1 = "Shakib"


# Rule 4: Variable names are case-sensitive
name = "Shadman"
Name = "Shakib"

print(name)
print(Name)


# Rule 5: Spaces are not allowed
# student name = "Shakib"    # Invalid

# Use underscore instead
student_name = "Shakib"


# Rule 6: Python keywords cannot be used
# class = "CST"               # Invalid
# if = 10                     # Invalid


# Rule 7: Use descriptive and meaningful names
age = 18
student_name = "Shakib"
student_age = 18


# Rule 8: Use snake_case for multiple words
first_name = "Shadman"
last_name = "Shakib"
student_id = 101


# Valid Variable Names
my_name = "Shadman"
age = 18
student2 = "Fahim"
_student = "Fahad"


# Invalid Variable Names
# 2student = "Nirob"
# my-name = "Shadman"
# my name = "Shakib"
# class = "CST"