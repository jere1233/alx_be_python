 
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")

