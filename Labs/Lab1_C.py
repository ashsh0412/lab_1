def dateCalculator():
    year1 = int(input("Enter the year for date 1: "))
    month1 = int(input("Enter the month for date 1: "))
    day1 = int(input("Enter the day for date 1: "))
    year2 = int(input("Enter the year for date 2: "))
    month2 = int(input("Enter the month for date 2: "))
    day2 = int(input("Enter the day for date 2: "))

    if year1 and month1 and day1 and year2 and month2 and day2 < 0:
        print("these are should be greater than 0")
        dateCalculator()
    elif month1 and month2 > 12:
        print("Month should be lesser than 13")
        dateCalculator()
    elif day1 and day2 > 30:
        print("Days should be lesser than 31")
        dateCalculator()
    else:
        a = year1 * 360 + month1 * 30 + day1
        b = year2 * 360 + month2 * 30 + day2
        c = b - a
        if c < 0:
            c = -c
        print(
            f"The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {c} days!"
        )


dateCalculator()
