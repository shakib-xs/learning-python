# Python Swapping Variables


# Swapping two variables
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# Swapping using a temporary variable
x = 5
y = 15

temp = x
x = y
y = temp

print(x)
print(y)