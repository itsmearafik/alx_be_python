'''
Functions are reusable blocks of code that perform specific tasks.
'''

# A simple function to greet the user (function structure)
def greet(name):
    # print a greeting message 
    print(f"Hello, {name}")
greet("arafik")

# Lambda functions are one-line expressions or anonymous functions 
addition = lambda x, y: x + y 
result = addition(5, 3)
print(result)

# default(*args)
# function definition with default value 
def greeting(name="World"):
    # print a welcome message 
    print(f"Hello, {name}!")

greeting()
greeting("arafik")


# Local vs Global scopes 
# `global` Use the global keyword to modify a global variable from within a function

count = 0
def increment_global():
    global count
    count += 1
increment_global()
print(count)

# `nonlocal` Use the nonlocal keyword to modify a variable from an enclosing function within a nested function. 

def outer_function():
    x = 10 # var in enclosing function 

    def inner_function():
        nonlocal x # using `nonlocal` to modify x from the enclosing function
        x += 5 # modifying the value of x 
    
    inner_function()
    print("Modified value of x from inner function: ", x)

outer_function()

# function to find the area of a rectangle 
def area_rectangle(length, width):
    area = length * width
    return f"Area of the rectangle of length: {length} and width: {width} is {area}"

print(area_rectangle(3,5))

# Function to check if even or odd 
def even_odd(num):
    if num / 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd.")

even_odd(3)