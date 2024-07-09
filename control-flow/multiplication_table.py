# Use the `for` loop to generate and print the multiplicaiton table for a given number 

number = int(input("Enter a number to see its multiplication table: "))

# operator = 10
for ops in range(1,11):
    print(f"{number} * {ops} = {number * ops}")