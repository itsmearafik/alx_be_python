# create a single priority task for the day using python

# Asking for user inputs 
# store user input task description as => task_variable
task_variable = input("Enter your task: ")

# Ask for priority level (high, medium,low) as => priority_variable 
priority = input("Priority (high/medium/low): ")

# Ask if its time bound (Yes/No) => time_bound_variable
time_bound = input("Is it time-bound? (yes/no): ")

# Provide a customized reminder based on the priority and time sensitivity
reminder = ""

# Use match case to handle inputs based on priorities 
match priority:
    case "high":
        reminder = f"{task_variable} is a high priority task."
    case "medium":
        reminder = f"{task_variable} is a medium priority task."
    case "low":
        reminder = f"{task_variable} is a low priority task."
    case _:
        reminder = f"{task_variable} has an unspecified priority level."

# Use if conditionals to modify the reminder if the task is time bound 
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the customized reminder 
print("Reminder: ", reminder)