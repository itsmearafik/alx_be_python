
outer_count = 5

while outer_count > 0:
    # outer loop the number of times the inner loop runs 
    inner_count = 1
    while inner_count <= outer_count:
        # inner loop repeats for each outer loop iteration 
        print(inner_count, end=" ")
        inner_count += 1
    print() # move to a new line after each iteration
    outer_count -= 1

    # Printing multiplication table 
    for i in range(1, 11):
        # outer loop iterates through rows (multiplication factors)
        for j in range(1, 11):
            # inner loop iterates through columns (outer factors)
            product = i * j 
            print(f"{i} x {j} = {product}", end="\t") #Print with tabs for better formating
            print()

            # Printing a Right Triangle of Asterisks 
            rows = 5 

            for i in range(1, rows + 1):
                # outer loop controls the number of rows 
                for j in range(1, i + 1):
                    # inner loop prints asterisks for each row
                    print("*", end="")
                print() #Move to a new line after each row of asterisks