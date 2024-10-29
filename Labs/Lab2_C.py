a = input("Enter the unit you are converting from: ")
b = input("Enter the unit you are converting to: ")

if a == "Fahrenheit":
    c = float(input("Enter the temperature in Fahrenheit: "))
    if b == "Celcius":
        result = (c - 32) * 5 / 9
        result = round(result, 1)
        print(f"That is {result} degrees Celsius.")
    elif b == "Kelvin":
        result = (c - 32) / 1.8 + 273.15
        result = round(result, 1)
        print(f"That is {result} degrees Kelvin.")
    else:
        print(f"That is {c} degrees Fahrenheit.")
elif a == "Celsius":
    c = float(input("Enter the temperature in Celsius: "))
    if b == "Fahrenheit":
        result = c * 9 / 5 + 32
        result = round(result, 1)
        print(f"That is {result} degrees Fahrenheit.")
    elif b == "Kelvin":
        result = c + 273.15
        result = round(result, 1)
        print(f"That is {result} degrees Kelvin.")
    else:
        print(f"That is {c} degrees Celsius.")
# kelvin
elif a == "Kelvin":
    c = float(input("Enter the temperature in Kelvin: "))
    if b == "Celsius":
        result = c - 273.15
        result = round(result, 1)
        print(f"That is {result} degrees Kelvin.")
    elif b == "Fahrenheit":
        result = 1.8 * (c - 273.15) + 32
        result = round(result, 1)
        print(f"That is {result} degrees Fahrenheit.")
    else:
        print(f"That is {c} degrees Kelvin.")
