""" 
Objective: Writing a script that performs specified operations with dates and times using the python `datetime` module.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formated_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formated_future_date}")
    return future_date 

def main():
    current_date = display_current_datetime()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()