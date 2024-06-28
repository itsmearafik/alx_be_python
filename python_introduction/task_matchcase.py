# Match Case statements allows you to handle multiple conditionsand corresponding code blocks

# requesting for user input (asking for the day of the week)
day = input("Enter a day of the week (Monday - sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednessday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":
        print("Weekend vibes!")
    case _:
        print("Invalid day entered. ") 

# using the match case statement to match against data types 

value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer: ", value)
    case str():
        print("You entered a string: ", value)
    case _:
        print("Invalid datatype.")

