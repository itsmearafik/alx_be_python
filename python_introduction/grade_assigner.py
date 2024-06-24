# This program takes the student score as input, it then uses
# a chain of if statements to check for specific score ranges and assigns the corresponding letter grade.

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is: ", grade)