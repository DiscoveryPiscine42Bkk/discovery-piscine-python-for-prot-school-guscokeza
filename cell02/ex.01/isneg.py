#!/usr/bin/env python3

def main():
    # Prompt the user to enter a number
    try:
        number = float(input("Enter a number: "))

        # Check if the number is negative, positive, or zero
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
