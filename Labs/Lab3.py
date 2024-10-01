import math

result = []
num_of_cal = 0

def format_result(value):
    if isinstance(value, float):
        return f"{value:.2f}".rstrip('0').rstrip('.') if not value.is_integer() else f"{value:.1f}"
    else:
        return str(value)

def check_input(input_value, x, y):
    global num_of_cal
    
    if input_value == 1:
        anw = addition(x, y)
    elif input_value == 2:
        anw = substraction(x, y)
    elif input_value == 3:
        anw = multiplication(x, y)
    elif input_value == 4:
        if y == 0:
            print("Error: invalid input!\n")
            return
        anw = division(x, y)
    elif input_value == 5:
        anw = exponential(x, y)
    elif input_value == 6:
        if x <= 0 or y <= 0 or x == 1:
            print("Error: invalid input!\n")
            return
        anw = logarithm(x, y)
    elif input_value == 7:
        if not result:
            print("Error: No calculations yet to average!")
            menu_selection()
            return
        anw = average()
        print(f"Sum of calculations: {format_result(anw[0])}")
        print(f"Number of calculations: {format_result(num_of_cal)}")
        print(f"Average of calculations: {format_result(anw[1])}\n")
        menu_selection()
        return
    else:
        print("Error: Invalid selection!\n")
        return

    result.append(anw)
    num_of_cal += 1
    print(f"Current Result: {format_result(anw)}\n")
    start_calculation()

def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def exponential(x, y):
    return math.pow(x, y)

def logarithm(x, y):
    return math.log(y, x)  # x is the base, y is the argument

def average():
    if result:
        total_sum = sum(result)
        count = len(result)
        return total_sum, total_sum / count
    return 0, 0

def menu_selection():
    global result
    RESULT = sum(result) if result else 0
    try:
        input_value = int(input("Enter Menu Selection: "))
        
        if input_value == 0:
            print("Thanks for using this calculator. Goodbye!")
            return
        
        elif input_value < 0 or input_value > 7:
            print("Error: Invalid selection!\n")
            menu_selection()
            return
        
        if input_value in [1, 2, 3, 4, 5, 6]:
            try:
                x = input("Enter first operand: ")
                if x == "RESULT":
                    x = RESULT
                else:
                    x = float(x)
                y = input("Enter second operand: ")
                if y == "RESULT":
                    y = RESULT
                else:
                    y = float(y)
            except ValueError:
                print("Error: Invalid input!")
                menu_selection()
                return
            
            check_input(input_value, x, y)
        
        elif input_value == 7:
            check_input(input_value, 0, 0)  # Dummy values for x and y

    except ValueError:
        print("Invalid input. Please enter a number.")
        menu_selection()
    except EOFError:
        pass

def start_calculation():
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average\n")
    
    menu_selection()  

print("Current Result: 0.0\n")
start_calculation()