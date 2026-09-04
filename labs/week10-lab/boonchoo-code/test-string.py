print("\n=== READING AND CONVERTING ===")
# Note: Using input() instead of raw_input() for Python 3
name = input("Enter your name: ")
print(f"Hello {name}")

# Converting string to number
apple = input("Enter a number: ")
try:
    x = int(apple) - 10
    print(f"Result: {x}")
except ValueError:
    print("Please enter a valid number!")

###################################################

