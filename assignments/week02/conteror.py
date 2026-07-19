"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used

"""

exchange_rate = 35.5  

print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    thb = float(input("Enter amount in THB: "))
    usd = thb / exchange_rate
    print(f"\nCalculation: {thb:.2f} ÷ {exchange_rate} = {usd:.2f} USD")
    print(f"Result: {usd:.2f} USD")

elif choice == "2":
    usd = float(input("Enter amount in USD: "))
    thb = usd * exchange_rate
    print(f"\nCalculation: {usd:.2f} * {exchange_rate} = {thb:.2f} THB")
    print(f"Result: {thb:.2f} THB")

else:
    print("Invalid choice. Please run the program again.")