# create a single priority task for the day using python

# Asking for user inputs 
# store user input task description as => task_variable
# Ask for priority level (high, medium,low) as => priority_variable 
# Ask if its time bound (Yes/No) => time_bound_variable

task_variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process task based on priority and time sensitivity

match time_bound:
    case time_bound if ("yes" in time_bound):
        # if time_bound == "yes":
        print(f"Reminder: '{task_variable}' is a {priority} priority task that requires immidiate attention today!")
    case time_bound if (time_bound == "no"):
        print(f"Reminder: '{task_variable}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Please enter the correct response. check sentence for example")

