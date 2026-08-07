prices = []

print("Enter prices of 6 items:")

for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)


budget = int(input("\nEnter total budget: "))
total_spent = 0
bought_items = []
print()

for i in range(6):
    price = prices[i]

    if total_spent + price <= budget:
        print(f"Item {i + 1} = {price} -> buy")

        total_spent += price
        bought_items.append(price)

        print(f"Current total = {total_spent}")
    else:
        print(f"Item {i + 1} = {price} -> cannot buy")
        print(f"Current total = {total_spent}")

    print()


remaining_budget = budget - total_spent

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {remaining_budget}")
