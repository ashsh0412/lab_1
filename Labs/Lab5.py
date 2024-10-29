def hex_char_decode(digit):
    pass


def hex_string_decode(hex):
    result = []
    if hex.startswith("0x"):
        hex = hex.lstrip("0x")
    list_hex = list(hex)
    reversed_list = list(reversed(list_hex))
    for i in range(0, len(list_hex)):
        try:
            int_value = int(reversed_list[i])
            value = int_value * (16**i)
            result.append(value)
        except ValueError:
            string_value = reversed_list[i].upper()
            if string_value == "A":
                value = 10 * (16**i)
                result.append(value)
            if string_value == "B":
                value = 11 * (16**i)
                result.append(value)
            if string_value == "C":
                value = 12 * (16**i)
                result.append(value)
            if string_value == "D":
                value = 13 * (16**i)
                result.append(value)
            if string_value == "E":
                value = 14 * (16**i)
                result.append(value)
            if string_value == "F":
                value = 15 * (16**i)
                result.append(value)

    print(f"Result: {sum(result)}\n")
    menu()


def binary_string_decode(binary):
    result = []
    if binary.startswith("0b"):
        binary = binary.lstrip("0b")
    list_binary = list(binary)

    for i in range(0, len(list_binary)):
        reversed_list = reversed(list_binary)
        int_list = list(map(int, reversed_list))
        value = int_list[i] * (2**i)
        result.append(value)
    print(f"Result: {sum(result)}\n")
    menu()


def binary_to_hex(binary):
    if binary.startswith("0B"):
        binary = binary.replace("0B", "")
    list_binary = list(reversed(binary))
    n = 4
    sliced_list = [
        list_binary[i * n : (i + 1) * n] for i in range((len(list_binary) - 1 + n) // n)
    ]
    result = []
    for i in range(len(sliced_list)):
        seperate_list = list((sliced_list[i]))
        int_list = list(map(int, seperate_list))
        try:
            a = int_list[0] * 1
            b = int_list[1] * 2
            c = int_list[2] * 4
            d = int_list[3] * 8
        except IndexError:
            a = int_list[0] * 1 if len(int_list) > 0 else 0
            b = int_list[1] * 2 if len(int_list) > 1 else 0
            c = int_list[2] * 4 if len(int_list) > 2 else 0
            d = int_list[3] * 8 if len(int_list) > 3 else 0
        hex_value = a + b + c + d
        if hex_value == 10:
            hex_value = "A"
        elif hex_value == 11:
            hex_value = "B"
        elif hex_value == 12:
            hex_value = "C"
        elif hex_value == 13:
            hex_value = "D"
        elif hex_value == 14:
            hex_value = "E"
        elif hex_value == 15:
            hex_value = "F"
        else:
            hex_value
        result.append(hex_value)
    result = "".join(str(item) for item in result)
    print(f"Result: {result[::-1]}\n")
    menu()


def check_option(option_num):
    if option_num == 1:
        numeric_string1 = input("Please enter the numeric string to convert: ")
        hex_string_decode(numeric_string1)
    elif option_num == 2:
        numeric_string2 = input("Please enter the numeric string to convert: ")
        binary_string_decode(numeric_string2)
    elif option_num == 3:
        binary = input("Please enter the numeric string to convert: ")
        binary_to_hex(binary)
    elif option_num == 4:
        print("Goodbye!")
        pass


def menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    option_num = int(input("Please enter an option: "))
    check_option(option_num)


menu()
