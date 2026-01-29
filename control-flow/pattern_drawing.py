# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control the number of rows
while row < size:
    # Use a nested for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    row += 1
