def rountTotal():
    price = float(input("Enter the price of the item: "))
    taxPercent = float(input("Enter the sales tax percentage: "))
    total = price + price*taxPercent/100
    print(f"Your total is ${total:.2f}")

rountTotal()