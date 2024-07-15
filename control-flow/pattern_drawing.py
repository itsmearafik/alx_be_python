# Utilize while loops & nested for loops to draw a text-based pattern 

# pattern_size = int(input("Enter the size of the pattern: "))

drawing = 0

# while drawing != pattern_size:
#     for x in range(1,pattern_size):
#         print("*", end="")

# cast the user input to int 

# iterate using while loop, to check number of rows

# use for loop to print symbol in a row 
rows = "*"
pattern_size = int(input("Enter the size of the pattern:"))

for i in range(pattern_size):
    for j in range(pattern_size):
        if j <= i:
            print(rows, end=' ')
        else:
            print(rows, end=' ')
    print()