import sys
from heifer_generator import get_cows


def list_cows(cows):
    print("Cows available:")
    for cow in cows:
        print(cow.name, end=" ")


def find_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            return cow
    return None


def main():
    cows = get_cows()

    if len(sys.argv) == 1:
        print("Usage: python cowsay.py [-l] [-n COW] MESSAGE")
        return

    if sys.argv[1] == "-l":
        list_cows(cows)
        return

    if sys.argv[1] == "-n":
        if len(sys.argv) < 4:
            print("Usage: python cowsay.py -n COW MESSAGE")
            return

        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)

        if cow is None:
            print(f"Could not find {cow_name} cow!")
            return

    else:
        message = " ".join(sys.argv[1:])
        cow = find_cow("heifer", cows)

    print(message)
    print(cow.image)


if __name__ == "__main__":
    main()
