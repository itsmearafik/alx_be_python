""" 
Objective: Writing a unit test for a this `Simple Calculator` class that supports
addition, substraction, multiplication and division operations.
"""
class SimpleCalculator:
    #Addition operation
    def add(self, a, b):
        # return the addition of a and b 
        return a + b 
    
    # Subtraction operation 
    def subtract(self, a, b):
        # return the difference of a and b
        return a - b 
    
    # Multiplication of a and b 
    def multiply(self, a,b):
        # return the multiplication of a and b 
        return a * b 
    
    # Division of a and b 
    def divide(self, a, b):
        # return the division of a by b. Return none if b is zero 
        if b == 0:
            return None 
        else:
            return a / b 
        