#!/usr/bin/env python3

def main():
    # Prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Multiply the two numbers
        result = num1 * num2

        # Determine if the result is positive, negative, or zero
        if result > 0:
            print("The result of the multiplication is positive.")
        elif result < 0:
            print("The result of the multiplication is negative.")
        else:
            print("The result of the multiplication is zero.")

        # Display the result of the multiplication
        print(f"The result of multiplying {num1} and {num2} is: {result}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

