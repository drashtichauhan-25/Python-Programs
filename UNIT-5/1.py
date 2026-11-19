# Syntax Error example
# print("Hello"

# Name Error
try:
    print(x)
except NameError:
    print("Name Error occurred")

# Zero Division Error
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Value Error
try:
    num = int("Hello")
except ValueError:
    print("Invalid value")
