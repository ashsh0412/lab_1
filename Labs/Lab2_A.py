a = float(input("Side length 1: "))
b = float(input("Side length 2: "))
c = float(input("Side length 3: "))

if a == b == c:
    print("This is an equilateral triangle!")
elif a != b != c:
    print("This is a scalene triangle!")
else:
    print("This is an isosceles triangle!")
