'''
for loops are used for iterating over items in a sequence list 
such as (list,tuple,string) etc.
Use cases:
    processing elements in a list, traversing a string, iterating over tuples.
'''

# iterating over lists 
fruits= ["apples", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# iterating over tuples 

colors = ("red", "green", "blue")

for color in colors:
    print(color)

# looping through characters 
message = "Hello, World"

for character in message:
    print(character)

# iterating over ranges
for number in range(1, 6):
    print(number)
