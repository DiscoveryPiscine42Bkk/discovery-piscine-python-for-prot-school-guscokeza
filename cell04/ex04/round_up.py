#!/usr/bin/env python3
import math

# Ask the user to input a number
user_input = input("Enter a number: ")

# Try to convert the input to a float and round it up
try:
    number = float(user_input)
    rounded_number = math.ceil(number)  # Round up the number
    print(f"The number {number} rounded up is: {rounded_number}")
except ValueError:
    print("That's not a valid number.")
