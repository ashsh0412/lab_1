from console_gfx import display_image, load_file, test_image, test_rainbow

def to_hex_string(data):
    return ''.join(f"{x:x}" for x in data)

def count_runs(flat_data):
    count = 0
    i = 0
    while i < len(flat_data):
        run_length = 1
        while i + run_length < len(flat_data) and flat_data[i] == flat_data[i + run_length] and run_length < 15:
            run_length += 1
        count += 1
        i += run_length
    return count

def encode_rle(flat_data):
    rle = []
    i = 0
    while i < len(flat_data):
        run_length = 1
        while i + run_length < len(flat_data) and flat_data[i] == flat_data[i + run_length] and run_length < 15:
            run_length += 1
        rle.append(run_length)
        rle.append(flat_data[i])
        i += run_length
    return rle

def get_decoded_length(rle_data):
    return sum(rle_data[i] for i in range(0, len(rle_data), 2))

def decode_rle(rle_data):
    decoded = []
    for i in range(0, len(rle_data), 2):
        run_length = rle_data[i]
        value = rle_data[i + 1]
        decoded.extend([value] * run_length)
    return decoded

def string_to_data(data_string):
    result = []
    for i in data_string:
        if i.isdigit(): 
            result.append(int(i))
        else: 
            result.append(int(i, 16))
    return result 

def to_rle_string(rle_data):
    return ':'.join(f"{rle_data[i]}{rle_data[i + 1]:X}" for i in range(0, len(rle_data), 2))

def string_to_rle(rle_string):
    parts = rle_string.split(':')
    rle_data = []
    for part in parts:
        run_length = int(part[:-1])
        value = int(part[-1], 16)
        rle_data.extend([run_length, value])
    return rle_data

def display_menu():
    print("Welcome to the RLE image encoder!")
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

def main():
    image_data = None
    display_menu()
    
    while True:
        option = int(input("Select a Menu Option: "))
        
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = load_file(file_name)
            print("File loaded.")
        elif option == 2:
            image_data = test_image
            print("Test image data loaded.")
        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))
            print("RLE data decoded.")
        elif option == 4:
            hex_string = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(hex_string))
            print("RLE hex data decoded.")
        elif option == 5:
            hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_string)
            print("Flat hex data loaded.")
        elif option == 6:
            if image_data:
                display_image(image_data)
            else:
                print("No image data to display.")
        elif option == 7:
            if image_data:
                rle_data = encode_rle(image_data)
                print("RLE representation:", to_rle_string(rle_data))
            else:
                print("No image data to encode.")
        elif option == 8:
            if image_data:
                rle_data = encode_rle(image_data)
                print("RLE hex values:", to_hex_string(rle_data))
            else:
                print("No image data to encode.")
        elif option == 9:
            if image_data:
                print("Flat hex values:", to_hex_string(image_data))
            else:
                print("No image data to display.")
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()



