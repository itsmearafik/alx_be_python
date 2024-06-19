# Calculating monthly and future savings
# 

monthly_income = input("Enter your monthly income: ") 
expenses = input("Enter your total monthly expenses: ")
rate = 0.05

monthly_savings = int(monthly_income) - int(expenses)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

