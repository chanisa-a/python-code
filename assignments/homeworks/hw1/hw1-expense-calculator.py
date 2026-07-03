"""
Personal Finance Calculator
Student: [Chanisa Phanjumpee]
Date: [26/7/2568]
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("User's Monthly_income in THB: "))
rent_cost = float(input("Monthly rent: "))
food_budget = int(input("Monthly food budget in THB: "))
transportation_cost = float(input("Monthly transportation expense: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to invest: "))

fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_savings = remaining_income - emergency_fund - investment_amount
expense_ratio = (total_expenses / monthly_income) * 100

print("")
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {fixed_expenses:.2f} THB")
print(f"Variable Expenses: {variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")
print("")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")

 

