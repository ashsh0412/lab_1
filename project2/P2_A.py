from console_gfx import display_image, load_file, test_image, test_rainbow


def menu():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    display_image(test_rainbow)
    print("\n\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")


def starting():
    menu()
    option = int(input("Select a Menu Option: "))
    check_option(option)


def to_hex_string(data):
    new_list = []
    n = len(data)
    for i in range(0, n):
        if 0 <= data[i] <= 9:
            new_list.append(str(data[i]))
        elif data[i] == 10:
            new_list.append("A")
        elif data[i] == 11:
            new_list.append("B")
        elif data[i] == 12:
            new_list.append("C")
        elif data[i] == 13:
            new_list.append("D")
        elif data[i] == 14:
            new_list.append("E")
        elif data[i] == 15:
            new_list.append("F")

    hex_string = "".join(new_list)
    print(hex_string)


def check_option(option):
    if option == 0:
        pass
    elif option == 1:
        file_name = input("Enter name of file to load: ")
        loaded_file = load_file(file_name)
        print(loaded_file)
    elif option == 2:
        display_image(test_image)


starting()
