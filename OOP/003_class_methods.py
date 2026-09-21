# Python Class Methods
#
# A method is a function defined inside a class.
#
# Syntax:
# class ClassName:
#     def method_name(self):
#         statement


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
