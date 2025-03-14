#!/usr/bin/env python3

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if division by zero is attempted
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Display the results
print(f"The result of {num1} + {num2} is: {addition}")
print(f"The result of {num1} - {num2} is: {subtraction}")
print(f"The result of {num1} * {num2} is: {multiplication}")
print(f"The result of {num1} / {num2} is: {division}")
