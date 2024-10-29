income = float(input("Enter your total income this year: "))

if 0 <= income <= 11000:
    owed_taxes = income * 0.1
    print(f"You owe ${owed_taxes} this year.")

elif 11001 <= income <= 44725:
    owed_taxes = (income - 11000) * 0.12
    print(f"You owe ${146894.50} this year.")

elif 44726 <= income <= 95375:
    print(f"You owe ${146894.50} this year.")

elif 95376 <= income <= 182100:
    owed_taxes = (income - 95375) * 0.24
    print(f"You owe ${146894.50} this year.")

elif 182101 <= income <= 231250:
    owed_taxes = (income - 182100) * 0.32
    print(f"You owe ${146894.50} this year.")

elif 231251 <= income <= 578125:
    owed_taxes = (income - 231250) * 0.35
    print(f"You owe ${146894.50:.2f} this year.")

elif 578126 <= income:
    owed_taxes = (income - 578125) * 0.37
    print(f"You owe ${330332.00:.2f} this year.")
