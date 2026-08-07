def calculate_tax(income):
    tax = 0
    details = []

    brackets = [
        (150000, 0.00),
        (300000, 0.05),
        (500000, 0.10),
        (750000, 0.15),
        (1000000, 0.20),
        (2000000, 0.25),
        (5000000, 0.30),
        (float("inf"), 0.35)
    ]

    lower = 0

    for upper, rate in brackets:
        if income > lower:
            taxable = min(income, upper) - lower
            tax_amount = taxable * rate
            tax += tax_amount

            details.append((lower + 1 if lower != 0 else 0,
                            min(income, upper),
                            rate,
                            tax_amount))

        lower = upper

        if income <= upper:
            break

    net_income = income - tax
    effective_rate = (tax / income) * 100 if income > 0 else 0

    return tax, net_income, effective_rate, details


def show_result(income):
    tax, net_income, effective_rate, details = calculate_tax(income)

    print("\nรายละเอียดภาษี")

    for start, end, rate, amount in details:
        print(f"{start:,.0f} - {end:,.0f} ({rate*100:.0f}%) = {amount:,.2f} บาท")

    print("-" * 40)
    print(f"ภาษีรวม               : {tax:,.2f} บาท")
    print(f"รายได้หลังหักภาษี      : {net_income:,.2f} บาท")
    print(f"Effective Tax Rate : {effective_rate:.2f}%")



def main():
    income = float(input("กรอกรายได้สุทธิ (บาท): "))
    show_result(income)


main()