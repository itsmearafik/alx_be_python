"""
Objective: A diivision calculator that handles errors like division
by error and non-numeric inpust using command line arguments.
"""

def safe_divide(numerator, denominator):
    try:
        # converting inputs to float 
        num = float(numerator)
        denom = float(denominator)

        # division operation
        result = num / denom
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    return f"The result of the division is {result:.1f}"