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