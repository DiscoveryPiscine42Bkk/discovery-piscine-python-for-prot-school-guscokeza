#!/usr/bin/env python3

# Ask the user to input a number
user_input = input("Enter a number: ")

# Check if the input is a valid float
try:
    number = float(user_input)
    if '.' in user_input:
        print(f"The number {user_input} is a decimal (floating-point number).")
    else:
        print(f"The number {user_input} is an integer, not a decimal.")
except ValueError:
    print("That's not a valid number.")
