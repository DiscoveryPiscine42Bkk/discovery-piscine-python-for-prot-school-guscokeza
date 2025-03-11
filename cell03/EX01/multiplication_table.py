#!/usr/bin/env python3

def main():
    try:
        # Accept user input and convert to a number
        num = int(input("Enter a number for the multiplication table: "))

        # Display the multiplication table for the input number
        print(f"Multiplication table for {num}:")
        for i in range(1, 11):
            result = num * i
            print(f"{num} x {i} = {result}")
            
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
