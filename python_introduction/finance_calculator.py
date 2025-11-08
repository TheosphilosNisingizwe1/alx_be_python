monthly_income = float(input("Enter your monthly income. "))
monthly_expenses = float(input("Enter your total monthly expenses. "))
monthly savings = monthly_expenses - monthly_income
projected annual savings = ((monthly savings * 12) + (monthly savings * 12 * 0.05))
print(f"Your monthly savings are ${monthly savings})
print("Your projected savings for one year, with interest is {projected annual savings}.")