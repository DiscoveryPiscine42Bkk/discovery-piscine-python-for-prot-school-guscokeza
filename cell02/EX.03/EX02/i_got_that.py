#!/usr/bin/env python3

def main():
    # Start a while loop that continues until the user enters "STOP"
    while True:
        # Accept user input
        user_input = input("Enter something (type 'STOP' to exit): ")

        # Check if the user entered "STOP"
        if user_input == "STOP":
            print("Stopping the loop.")
            break
        else:
            # Respond to the user input
            print(f"I got that: {user_input}")

if __name__ == "__main__":
    main()
