#!/usr/bin/env python3

def main():
    try:
        # Accept user input and convert to a number
        num = int(input("Enter a number: "))

        # If the input number is greater than 25, display an error message
        if num > 25:
            print("Error")
        else:
            # Loop from the input number to 25
            for i in range(num, 26):
                print(i)
                
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
