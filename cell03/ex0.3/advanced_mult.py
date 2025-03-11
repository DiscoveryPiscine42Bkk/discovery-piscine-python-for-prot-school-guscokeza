num = int(input())
    # Loop through numbers 1 to 10 to display each multiplication table
for num in range(1, 11):
        print(f"Multiplication Table for {num}")
        print("-" * 25)
        
        # Nested loop to generate and display each multiplication row for current number
        for i in range(1, 11):
            result = num * i
            print(f"{num} x {i} = {result}")
        
        # Add a separator between tables
        print("\n" + "=" * 25 + "\n")


