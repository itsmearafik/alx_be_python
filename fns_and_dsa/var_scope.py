# Python uses the `LEGB` rule for lookup.
"""
L (local): var within a function or block
E (enclosing): within nested functions.
G (global): var outside all functions but accessible within the program.
B (built-in): functions and var that are part of pythons core functionality
"""

count = 10 # global variable 

def outer_function():
    count = 5 # local variable within outer function

    def inner_function():
        count = 2 # local variable within inner function
        print(f"Inner function: {count}") # Accesses local count (2)
    
    inner_function()
    print(f"Outer function: {count}") # Accesses local count (5)

print(f"Global scope: {count}")  # Accesses global count (10)

outer_function()