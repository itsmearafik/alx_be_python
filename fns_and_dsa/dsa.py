'''
Data Structures in Python
Lists: ordered, mutable collections of items enclosed in []. can hold different data types and duplicates.
Tuples: just like `Lists` but immutable and enclosed in ().
Sets: unordered collections of unique elements enclosed in curly braces {}.
Dictionaries: unordered collections of key-value pairs enclosed in curly braces {}. Keys are unique & immutable, while values can be of any data type. 
'''
# Using list indexing to access eleements in a list `List[]`
fruit_list = ["apple", "banana", "cashew", "melon", "orange"]
print(f"Using list indexing {fruit_list[1]} ")

# slicing: creating a sub list from a list using slicing `List[start:stop:step]`
print(f"Using list slicing {fruit_list[1:1:2]} ")

# Appending / Adding elements to a list 
fruit_list.append("mango")
print(f"The new fruit list after appending/adding: {fruit_list}")

# Removing an element from a list 
fruit_list.remove("melon")
print(f"The new fruit list after removing melon: {fruit_list}")

# Dictionaries examples using a book list 
book_list = {"Ama Aidoo": "in the chest of a woman", "Aggrey":"One woman Many nations"}
print(book_list.keys())
print(book_list.values())
