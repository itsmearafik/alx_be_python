'''
Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.
'''

# Prompt the user to enter the size of the pattern 
size = int(input("Enter the size of the pattern: "))

# Ensure the user entered a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # initialize the row counter
    row = 0

    # use a while loop to iterate through each row 
    while row < size:
        # use a for loop to print asterisks in each row 
        for col in range(size):
            print("*", end="")
            # Print a new line character to move to the next row 
            print()
            row += 1

            